#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Check the published file inventory, local models and native check reports."""
import hashlib
import json
from pathlib import Path
import re
import sys

ROOT = Path(__file__).resolve().parents[1]


def main():
    manifest = json.loads((ROOT / "manifest.json").read_text())
    errors = []
    for name, expected in manifest["files"].items():
        path = ROOT / name
        if not path.is_file():
            errors.append(f"Missing: {name}")
            continue
        data = path.read_bytes()
        if len(data) != expected["bytes"] or hashlib.sha256(data).hexdigest() != expected["sha256"]:
            errors.append(f"Changed: {name}")
    for path in [ROOT / "hardware/rev-a/carrier.kicad_pcb",
                 ROOT / "hardware/assembly-preview/assembly-preview.kicad_pcb"]:
        for model in set(re.findall(r'\(model\s+"([^"]+)"', path.read_text())):
            local = path.parent / model.replace("${KIPRJMOD}/", "")
            if not local.is_file():
                errors.append(f"Missing model: {model}")
    reports = ROOT / "manufacturing/rev-a/verification"
    drc = json.loads((reports / "drc.json").read_text())
    erc = json.loads((reports / "erc.json").read_text())
    if drc["unconnected_items"] or drc["schematic_parity"]:
        errors.append("Native DRC has connectivity or schematic parity failures")
    violations = drc["violations"]
    expected_warnings = {"track_dangling", "copper_sliver"}
    if len(violations) != 2 or any(v["severity"] != "warning" for v in violations) or {v["type"] for v in violations} != expected_warnings:
        errors.append("DRC differs from the two documented Rev A warnings")
    if any(s["violations"] for s in erc["sheets"]):
        errors.append("Native ERC has violations")
    if errors:
        print("\n".join(errors), file=sys.stderr)
        return 1
    print(f"Verified {len(manifest['files'])} files; local models resolve; saved DRC/ERC reports match Rev A.")
    print("This verifies the release contents. Use export.py --check-only to run KiCad checks again.")
    return 0


if __name__ == "__main__":
    raise SystemExit(main())
