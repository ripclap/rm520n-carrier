#!/usr/bin/env python3
# SPDX-License-Identifier: MIT
"""Refresh the release inventory after reviewed source/document changes."""
import argparse
import hashlib
import json
from pathlib import Path

ROOT = Path(__file__).resolve().parents[1]
EXCLUDED = {".git", "build", ".venv", "__pycache__"}


def payload_files():
    for path in sorted(ROOT.rglob("*")):
        if not path.is_file():
            continue
        relative = path.relative_to(ROOT)
        if any(part in EXCLUDED or part.endswith("-backups") for part in relative.parts):
            continue
        if path.name in {"manifest.json", "SHA256SUMS", ".DS_Store"} or path.suffix in {".pyc", ".kicad_prl", ".lck", ".bak"}:
            continue
        if path.is_symlink():
            raise SystemExit(f"Resolve the symlink before packaging: {relative}")
        yield path


def main():
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--revision", default="rev-a")
    args = parser.parse_args()
    files = {}
    for path in payload_files():
        data = path.read_bytes()
        files[path.relative_to(ROOT).as_posix()] = {"bytes": len(data), "sha256": hashlib.sha256(data).hexdigest()}
    manifest = {
        "project": "RM520N Carrier",
        "revision": args.revision,
        "status": "first-prototype; supplier CAM acceptance and hardware commissioning pending",
        "source": "hardware/rev-a/carrier.kicad_pro",
        "verification": "manufacturing/rev-a/verification/",
        "files": files,
    }
    (ROOT / "manifest.json").write_text(json.dumps(manifest, indent=2) + "\n")
    checksums = {name: item["sha256"] for name, item in files.items()}
    checksums["manifest.json"] = hashlib.sha256((ROOT / "manifest.json").read_bytes()).hexdigest()
    (ROOT / "SHA256SUMS").write_text("".join(f"{digest}  {name}\n" for name, digest in sorted(checksums.items())))
    print(f"Inventoried {len(files)} files. Review the diff and run verify_release.py before tagging.")


if __name__ == "__main__":
    main()
