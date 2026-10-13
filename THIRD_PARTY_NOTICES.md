# Third-party libraries

## KiCad libraries

The following collections contain files from the KiCad library contributors,
including project modifications to component placement, courtyards and lands:

- `hardware/rev-a/lib/resolved/`
- Stock-derived footprints in `hardware/rev-a/lib/carrier.pretty/`
- `hardware/rev-a/stock-3dmodels/`
- Corresponding stock models copied into `hardware/assembly-preview/models/`

The library collections are distributed under **CC-BY-SA-4.0 with the KiCad
design exception**, except where an individual model retains a different
notice. The design exception permits a separate license for electronic designs
using those libraries and their generated design files. Library copies remain
subject to their own notices.

The upstream license and complete CC-BY-SA text are included in
`LICENSES/KiCad-libraries-exception.md` and `LICENSES/CC-BY-SA-4.0.txt`.
Individual author notices in STEP files have been retained.

Sources:

- [KiCad library licensing](https://www.kicad.org/libraries/license/)
- [KiCad footprints](https://gitlab.com/kicad/libraries/kicad-footprints)
- [KiCad 3D models](https://gitlab.com/kicad/libraries/kicad-packages3D)

## Older diode models

`hardware/rev-a/stock-3dmodels/Diode_SMD.3dshapes/D_SMB.step` and
`D_SMC.step`, and their copies in the assembly preview, retain **GPL-3.0-or-later
with the KiCad design exception** as specified in their original headers.
The GPL text is included in `LICENSES/GPL-3.0-or-later.txt`. Preserve their
original headers and exception when redistributing these models.

## Project component definitions and viewing models

Project-specific symbols and land patterns use component pin assignments and
package drawings linked from the component properties and BOM. The U10 package
illustration consists of functional outline and orientation primitives; its
electrical land pattern, thermal vias and paste definition are project-specific.
Supplier datasheets and reference-board archives are linked where relevant and
are not redistributed here.

The RTL8125 viewing mesh is a project-created rectangular package body. Other
project viewing meshes are drawing-based envelopes or assembly illustrations.
They are licensed with the hardware and do not establish mechanical tolerance
or supplier qualification. See the component drawings and fabrication contract
for dimensional acceptance.

Component and manufacturer names identify the selected parts. No rights in
third-party trademarks or component firmware are granted by the project license.
