# Architecture

RM520N Carrier connects an RM520N-GL M.2 modem to a PCIe Ethernet controller and provides a separate management controller that can recover modem power without depending on the modem's operating system.

```text
Regulated 48 V passive input ── input/filter ── 12 V converter ─┐
                                                            ├── system rails
Regulated 12 V auxiliary input (J2) ── protected input ────────┘
                                                               │
                         ┌─────────────────────────────────────┤
                         │                                     │
                    always-on rail                    modem buck + eFuse
                         │                                     │
                    ESP32-S3FN8                         RM520N-GL M.2
                         │                                     │
                 switched radio rail                  PCIe ── RTL8125BG
                         │                                     │
                 E22-900MM22S LoRa                       magnetics ── RJ45

ESP32-S3 ── isolated control/qualification ── modem reset and power controls
ESP32-S3 USB host / external USB-C ── ownership mux ── modem USB management
Physical nano-SIM / soldered eUICC ── modem SIM interfaces
```

The control isolation shown here prevents backfeed between powered and unpowered domains; it does not provide galvanic isolation from the input supply. Auxiliary DC, USB, coax, and mounting interfaces share system ground.

## Main parts and interfaces

| Reference | Part or interface | Role |
| --- | --- | --- |
| J1 | Stewart SS-7188S-A-NF RJ45 | Ethernet cable and passive power input |
| J2 | JST B2B-XH-A(LF)(SN) | 12 V auxiliary input; pin 1 positive, pin 2 ground |
| J3 | ATTEND 123A-42B02 M.2 socket | RM520N-GL power and data connection |
| U1 | MP4583GQVE-Z | Main 48 V to 12 V converter |
| U3 | MP2329GG-P | Modem regulator; nominal unprotected output about 4.056 V |
| U10 | RTL8125BG-CG | PCIe to 2.5 GbE controller |
| U40 | H2414QR | Separate Ethernet magnetics |
| J4 | GCT SIM8066-6-1-14-01-A | Back-face, edge-accessible nano-SIM |
| U8 | ST4SI3M004600HFW | Experimental ST4SIM-300M eUICC population |
| U800 | ESP32-S3FN8 | Always-on management controller and USB full-speed host |
| U801 | E22-900MM22S | SPI LoRa radio for an intended US 915 MHz network |
| U840 | NCA9536DQJ | Status-only I²C observer at address 0x41 |

The temperature sensor uses I²C address 0x48. Bus failures or stale readings must be reported as unknown; status telemetry must not bypass the hardware power-good or recovery controls. Current telemetry is coarse until calibrated.

## Power and recovery

Revision A uses regulated 48 V ±5% **passive, nonisolated SELV power** or regulated 12 V ±5% at J2. It has no IEEE PoE detection or classification. Use a compatible injector with the documented pinout; do not assume an arbitrary Ethernet power source is suitable.

The management rail is independent of the switched modem rail. Turning off the modem preserves the controller and radio supply path, while total input loss turns off all domains. There is no battery ride-through.

A healthy blank or reset controller allows power-good-qualified hardware modem autostart; the radio defaults off and internal USB ownership is disabled. An absent physical joint-enable driver leaves the modem enables low. These are different hardware states.

Firmware power recovery must hold both the buck and eFuse enables low for at least five seconds **and** confirm the modem output has fallen below 100 mV before restarting. The dwell restarts after a controller reset. Radio recovery requires at least 350 ms off and a measured rail below 100 mV. These operational delays are not implemented by blank-controller hardware autostart. The full limits are in [POWER_TARGETS_AND_RECOVERY.txt](../manufacturing/rev-a/requirements/POWER_TARGETS_AND_RECOVERY.txt).

## Management software

No controller firmware or OOB network implementation is included. Intended functions are bounded status queries, telemetry, modem reset, and power cycling over an authenticated LoRa link. Commands need identifiers, acknowledgements, replay protection, retry limits, and reset logs. A remote radio station and a network plan are also required.

Internal USB AT access and simultaneous PCIe Ethernet operation need validation with the exact RM520N-GL firmware. The M.2 connection does not assume a debug UART. SSH or a shell console over LoRa requires a separately verified modem service and transport; it is not established by this hardware design.

The eUICC population is experimental. Physical SIM selection, eUICC provisioning, modem support, and the selected operator must be verified together on a first article.
