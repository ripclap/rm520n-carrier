# Contributing

After a reviewed change, refresh the file inventory with
`python3 tools/update_manifest.py --revision rev-a` and check it with
`python3 tools/verify_release.py`. A new hardware revision needs a new folder,
manufacturing package, revision label and tag; retain the released Rev A files.

Design review, measured test reports, sourcing corrections, and hardware changes are welcome. Start with an issue for a circuit, stack, connector, or power-stage change so its effects can be reviewed before layout work.

## Design source

Edit the native project in `hardware/rev-a/` using KiCad 10. Keep symbols, footprints, and model references portable. The PCB in `hardware/assembly-preview/` is for presentation only.

Do not mix manufacturing files from different revisions. A change to copper, components, pad geometry, stack, rules, or assembly requirements needs updated exports and validation records. Model or documentation changes should identify whether they affect the electrical or manufacturing design.

## Submitting a change

- Explain the problem, affected references or nets, and resulting behavior.
- For a substitute part, include the exact MPN and manufacturer documentation. Compare electrical limits, pinout, land pattern, height, supply status, and temperature behavior.
- State which checks were run and attach relevant results. Separate CAD checks, calculations, supplier process acceptance, and measurements on an assembled board.
- Include schematics or layout views where they help review. Avoid unrelated formatting, library updates, or export changes in the same pull request.
- Preserve the independent management supply and hardware recovery path when changing modem controls.

New copper or circuit changes must pass ERC and DRC, retain zero unrouted connections, and preserve or explicitly revise the impedance and fabrication requirements. Existing warning dispositions apply only to their documented geometry.

## Hardware test reports

Include PCB revision, assembly substitutions, modem firmware, input source and cable, instrument/fixture details, ambient temperature, cooling, and measured waveforms. Follow [bring-up](docs/bring-up.md) and report failed acceptance limits as well as passing results.

Remove credentials, subscriber identifiers, SIM profiles, private network details, and other sensitive data from reports. Do not attach an entire modem backup when a bounded log or measurement is sufficient.

## Licensing

Contributions must be material you have the right to publish and must use the license applicable to the file being changed. Preserve third-party notices and record the origin and license of any new library or asset. See [LICENSE](LICENSE) and [LICENSES/](LICENSES/).
