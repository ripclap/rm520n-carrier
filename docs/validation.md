# Validation status

**Rev A is a first-prototype hardware release.** It is suitable for submission to a fabricator and assembler that accepts its job-specific requirements. It is not a tested production design.

## Release checks

The Rev A package completed native schematic/PCB checks, circuit-to-layout comparison, routing and return-path review, power and thermal calculations, and comparison of the exported artwork, drills, BOM, and placements with the native design. The native board has zero unrouted connections and no ERC or DRC errors. Two DRC warnings have individual dispositions in the [requirement set](../manufacturing/rev-a/requirements/warning-dispositions1248.json).

The public repository contains that electrical design with portable local assets. A simplified, drawing-based RTL8125 body replaces its presentation model; the copper, pads, vias, zones, and circuit remain unchanged. Fresh [DRC](../manufacturing/rev-a/verification/drc.json) and [ERC](../manufacturing/rev-a/verification/erc.json) reports cover the public files. The root [manifest](../manifest.json) records public-release checksums. Warning dispositions apply to the exact documented geometry and do not grant a general clearance waiver.

To check the release files:

```sh
python3 tools/verify_release.py
```

To make a separate export from the native source, install KiCad 10 and place `kicad-cli` on `PATH`, then run:

```sh
python3 tools/export.py --output build
```

Use `--kicad-cli /path/to/kicad-cli` to specify the executable explicitly. Keep new exports separate from the tagged manufacturing files until their checks and requirements have been reviewed.

| Area | State at Rev A |
| --- | --- |
| Editable schematic, PCB, rules, and local assets | Published |
| Complete routed layout and manufacturing exports | Published |
| CAD, numerical, and export review | Completed; public-file DRC/ERC and checksum records are published |
| Supplier acceptance of stack, drill, fill/cap, cover, stencil, and finished metal | Pending |
| Measured power, startup, load-step, fault, and thermal behavior | Pending first article |
| RM520N-GL firmware, PCIe Ethernet, USB AT management, and reset behavior | Pending first article |
| Physical SIM, eUICC provisioning, antenna, and enclosure fit | Pending first article |
| Management firmware, authenticated LoRa commands, and remote network | Not included |
| EMC/RF or product certification | No certification claimed |

## Operating targets and conditions

The modem supply targets 3 A continuous at 0–40 °C under the released voltage, efficiency, thermal, copper, and input RMS conditions. Sustained 4 A qualification begins at ambient no greater than 20 °C. Higher ambient operation needs measured requalification. These are acceptance targets, not demonstrated output ratings.

Normal modem voltage must remain 3.135–4.4 V and ripple below 100 mV peak-to-peak. The recoverable overvoltage gate is below 4.7 V peak including uncertainty and no more than 100 mV post-threshold rise; it does not guarantee arbitrary fault duration or repetition. A failed hardware gate must be corrected before a modem is installed.

The passive 48 V input has no IEEE negotiation and no galvanically isolated power stage. Input source, cable/injector pinout, finished copper, actual winding imbalance, input RMS, and cooling are part of qualification. Firmware timing cannot substitute for power protection or supplier process acceptance.

## Required evidence before a larger lot

- Supplier CAM/assembly acceptance and finished-process inspection records.
- First-article voltage/current waveforms, measured efficiencies, temperatures, and fault/recovery results at the intended operating limits.
- Data-interface and modem-firmware results, including simultaneous USB management and PCIe Ethernet where intended.
- SIM/eUICC, radio/network, mechanical, and enclosure results for the actual supplied parts.
- A recorded disposition for every failed acceptance gate and a fixed source revision for any corrected build.

Use [FIRST_ARTICLE_TEST.txt](../manufacturing/rev-a/requirements/FIRST_ARTICLE_TEST.txt) as the acceptance procedure and [bring-up](bring-up.md) as its overview. Publish measured results with their exact board and firmware revision rather than replacing pending items with assumptions.
