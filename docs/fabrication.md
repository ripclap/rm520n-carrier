# Fabrication and assembly

Rev A is a conditional first-prototype package. Obtain job-specific CAM and assembly acceptance before ordering. The supplier must review the complete [requirement set](../manufacturing/rev-a/requirements/), including the per-site hole schedule and coupled drill requirements.

## Order package

Send these folders together from the same revision:

- [fabrication/](../manufacturing/rev-a/fabrication/): six-layer Gerbers, separate PTH/NPTH drills, maps, IPC-D-356 netlist, and net-name map.
- [assembly/](../manufacturing/rev-a/assembly/): fitted BOM, SMT placements, four manual through-hole placements, assembly exclusions, and front/back drawings.
- [requirements/](../manufacturing/rev-a/requirements/): stack, finished-metal, drill/fill/cap/cover, stencil, power, and first-article contracts.

The [native KiCad project](../hardware/rev-a/carrier.kicad_pro) is the editable authority. The assembly-preview PCB and rendered images must not be used as fabrication artwork.

## Board and stack

The board is 110 × 96 mm, six copper layers, nominal 1.6 mm, ENIG, with lead-free assembly. The selected construction is JLC06161H-3313. Nominal dielectrics are 0.0994 / 0.5500 / 0.1088 / 0.5500 / 0.0994 mm from front to back, with the exact material and layer table in [FABRICATION_AND_ASSEMBLY.txt](../manufacturing/rev-a/requirements/FABRICATION_AND_ASSEMBLY.txt).

Front high-speed routes reference In1; back routes reference In4. Impedance targets are USB 90 Ω differential, PCIe/REFCLK 85 Ω differential, MDI/cable 100 Ω differential, and LoRa 50 Ω. Request coupons and a stack/etch calculation, with nominal target tolerance ±10%. A supplier's proposed stack or artwork compensation must be reviewed for spacing, return continuity, power paths, and launches.

Power qualification requires finished outer copper at least 30 µm, In2 and In3 each at least 15.2 µm, In1 ground copper at least 12 µm, and a **local** finished via-wall minimum of 20 µm. Maximum full barrel span is 1.76 mm. A plating average does not establish the local wall minimum.

## Drills, caps, and cover

There are 1,124 through vias: 158 filled/capped Type VII and 966 ordinary. The complete 1,161-hole schedule also includes mechanical holes and four exposed-pad thermal PTHs. It includes 81 nominal 150 µm via drills, with individual finished-bore limits. Require no breakout and at least 50 µm finished copper annulus on all six copper layers.

Filled/capped sites require void-controlled nonconductive fill and planar copper caps on both faces, with maximum cap protrusion 10 µm. Ordinary sites require qualified bilateral mask cover, with maximum local peak 25 µm. Preserve specified terminal mask/paste apertures; do not add paste openings to vias. Parts over these sites have additional underside-clearance and terminal-interface requirements.

The two U4 VIN vias have a coupled raw-drill diameter, position, web, wall, and annulus recipe. Review [U4_VIN_FACTORY_COUPLED_REQUIREMENTS1190.txt](../manufacturing/rev-a/requirements/U4_VIN_FACTORY_COUPLED_REQUIREMENTS1190.txt) explicitly. Generic drill tolerance is insufficient to establish compliance. Large-bore fallback cover alternatives are inactive and need a per-site engineering disposition if proposed.

## Assembly and sourcing

Fit all 423 purchased components: 419 SMT and four through-hole items **C725, J1, R727, and J2**. Include the fitted H1 Würth spacer. J800 is a service-pad pattern and is not a purchased connector.

H1 needs the specified segmented annular stencil deposit of at least 150 µm through a qualified **local** step or paste process; do not apply that thickness to fine-pitch ICs. Check seated card support height, the separately supplied M2×3 retention screw, head/washer clearance, protrusion, and torque. The primary torque ceiling is 0.2 N·m and may need to be lower for the actual module or hardware.

Exact MPNs govern the assembly. A substitution needs electrical, land-pattern, height, thermal, and lifecycle review. The BOM's E22-900MM22S allocation assumes JLCPCB Standard PCBA; another builder needs a separately confirmed source. The modem, enclosure, antennas/coax, retention hardware outside the fitted BOM, and eUICC provisioning are separate items.

The component pricing model is not a fabrication or assembled-board quote. Filled/capped processing, assembly setup, manual soldering, test, shipping, and other exclusions need supplier pricing.

## Receiving and qualification

Require inspection records for finished metal, actual bore, annulus, caps, cover, local stencil, and underbody clearances. Complete [first-article bring-up](bring-up.md) with the modem absent, then qualify modem interfaces and enclosure fit. Neither CAD clearance nor a generic supplier capability table replaces actual process acceptance and first-article measurements.
