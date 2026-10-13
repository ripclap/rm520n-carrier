RM520N Carrier Rev A — manufacturing schedules

Use the fabrication, assembly and requirements folders for the same tagged
revision together. manifest.json and SHA256SUMS identify the published files.
The native board is hardware/rev-a/carrier.kicad_pcb. The public PCB changes
only an illustrative 3D model reference from the engineering submission;
all circuit, copper, pad, via, zone, rule and placement data are unchanged.

FABRICATION_AND_ASSEMBLY.txt and FAB_CURRENT_HOLE_COVER_REQUIREMENTS1248.txt
are the written process requirements. Their machine schedules are:
- FAB_ALL1161_HOLE_SITE_SCHEDULE1243.csv: all drilled holes and slots
- factory-site-schedule1248.json: per-site drill/land/wall/cover limits
- mask-cover-owner1248.json: mask/paste ownership at each via
- seven-raw-tool-rebind1248.json: seven special raw-tool diagnostics
- U4_VIN_FACTORY_COUPLED_REQUIREMENTS1190.txt: coupled drill recipe
- warning-dispositions1248.json: the two native DRC warning dispositions

Numeric suffixes identify schedule revisions, not alternative board choices.
No Type VI override is active. Supporting calculation names prefixed with
local-reference are descriptive review labels, not external file dependencies.
PCB_sha256 identifies the public native board; ancestral source hashes are
background traceability, not a selection of an older board for fabrication.
The mask/paste file bindings identify the actual published fabrication files.

Filled/capped vias, continuous cover, local copper wall, finished annulus,
underbody seating, impedance and drilling tolerance require supplier CAM and
process acceptance. Nominal CAD checks do not establish fabricated dimensions.
Use FIRST_ARTICLE_TEST.txt and POWER_TARGETS_AND_RECOVERY.txt before fitting
the modem or assigning an operating rating. Failures require corrective work.
