#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Run KiCad 10 checks and export fresh review files without overwriting the release."""
import argparse
import json
from pathlib import Path
import shutil
import subprocess

ROOT = Path(__file__).resolve().parents[1]


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--kicad-cli", default=shutil.which("kicad-cli"))
    parser.add_argument("--output", type=Path, default=ROOT / "build")
    parser.add_argument("--check-only", action="store_true")
    args = parser.parse_args()
    if not args.kicad_cli:
        parser.error("Put kicad-cli on PATH or specify --kicad-cli.")
    output = args.output.resolve()
    protected = [ROOT, ROOT / "manufacturing", ROOT / "hardware", ROOT / "docs", ROOT / "LICENSES", ROOT / "tools", ROOT / ".github"]
    if output in protected or any(parent in output.parents for parent in protected[1:]):
        parser.error("Use a separate output directory; released source and manufacturing files are protected.")
    output.mkdir(parents=True, exist_ok=True)
    board = "hardware/rev-a/carrier.kicad_pcb"
    schematic = "hardware/rev-a/carrier.kicad_sch"
    version = subprocess.check_output([args.kicad_cli, "--version"], text=True).strip()
    if not version.startswith("10."):
        parser.error("This revision requires KiCad 10.")

    def run(*command):
        subprocess.run([args.kicad_cli, *map(str, command)], cwd=ROOT, check=True)

    run("sch", "erc", "--format", "json", "--severity-all", "-o", output / "erc.json", schematic)
    run("pcb", "drc", "--schematic-parity", "--format", "json", "--severity-all", "-o", output / "drc.json", board)
    drc = json.loads((output / "drc.json").read_text())
    erc = json.loads((output / "erc.json").read_text())
    if any(v["severity"] == "error" for v in drc["violations"]) or drc["unconnected_items"] or drc["schematic_parity"] or any(s["violations"] for s in erc["sheets"]):
        raise SystemExit("Native checks failed. Inspect the reports before exporting.")
    print(f"KiCad {version}: no ERC/DRC errors or connectivity/parity failures; {len(drc['violations'])} DRC warnings.")
    if args.check_only:
        return
    fabrication = output / "fabrication"
    fabrication.mkdir(exist_ok=True)
    layers = "F.Cu,In1.Cu,In2.Cu,In3.Cu,In4.Cu,B.Cu,F.Mask,B.Mask,F.Paste,B.Paste,F.Silkscreen,B.Silkscreen,Edge.Cuts"
    run("pcb", "export", "gerbers", "--layers", layers, "--subtract-soldermask", "--check-zones", "-o", str(fabrication) + "/", board)
    run("pcb", "export", "drill", "--excellon-separate-th", "--generate-map", "--generate-report", "--report-path", fabrication / "carrier-drill.rpt", "-o", str(fabrication) + "/", board)
    run("pcb", "export", "ipcd356", "-o", fabrication / "carrier.ipc", board)
    run("pcb", "export", "pos", "--format", "csv", "--units", "mm", "--side", "both", "-o", output / "native-placement.csv", board)
    run("sch", "export", "netlist", "--format", "kicadxml", "-o", output / "carrier-netlist.xml", schematic)
    run("sch", "export", "pdf", "--exclude-pdf-metadata", "--exclude-pdf-property-popups", "-o", output / "schematic.pdf", schematic)
    print("Exports written to", output)
    print("Raw native placement includes mechanical/unpurchased features. Reconcile with the fitted BOM before assembly.")
    print("A design change also requires updated BOM, process schedules, impedance and first-article review.")


if __name__ == "__main__":
    main()
