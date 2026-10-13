# First-article bring-up

Use this checklist to plan the bench work. [FIRST_ARTICLE_TEST.txt](../manufacturing/rev-a/requirements/FIRST_ARTICLE_TEST.txt) contains the acceptance procedure and exact limits. No assembled-board results have been published for Rev A.

## 1. Inspect the assembly

Compare the revision, fitted MPNs, and placements with the release BOM and drawings. Review the supplier's actual drill, plating, annulus, cap, cover, and stencil records. Inspect both board faces and X-ray the exposed-pad and filled/capped interfaces. Check the M.2 spacer, card seating, retention hardware, and SIM access through the intended case opening.

Keep the modem and antennas unfitted during initial power, load, and fault tests.

## 2. Test each power input

Begin with a current-limited regulated source, USB disconnected. Test 12 V ±5% at J2 and the specified 48 V ±5% passive injector separately. J2 pin 1 is positive and pin 2 is ground. Confirm actual input voltage and polarity before connection; use rated 3 A auxiliary wiring.

Verify TP1/V12, TP2/V3V7, TP3/V3V3, TP4/V0V95, the always-on rail, and the switched radio rail. Capture startup and input transfer. Check reverse blocking and verify that external USB VBUS cannot power the modem or management rails unexpectedly.

At the board, the auxiliary input must remain at least 11.4 V. The passive path requires loaded FILTER at least 41.562266501 V and unloaded startup at least 41.977840535 V. Lower-voltage diagnostic calculations do not relax these installation limits.

## 3. Qualify the modem rail with a dummy load

Use an instrumented load in place of the modem. Test input extremes, cold and hot startup, and load steps after actual protected power-good qualification.

| Measurement | Acceptance scope |
| --- | --- |
| Normal modem connector voltage | 3.135–4.4 V, including measurement uncertainty |
| Normal ripple | Less than 100 mV peak-to-peak |
| Continuous target | 3 A at 0–40 °C, with the required measured efficiency and thermal path |
| Initial sustained 4 A test | Ambient at or below 20 °C; requalify before using higher ambient |
| Passive input RMS | At most 0.80 A aggregate and conservatively for each injection leg; include ripple, bursts, and imbalance |
| Main converter efficiency | At least 90% in the declared load case |
| Modem converter efficiency | At least 88% in the declared load case |
| Always-on and each Ethernet converter efficiency | At least 82% for each stage in its declared load case |
| Main thermal path | At most 32 °C/W; junction at most 125 °C |
| Component and winding case temperature | At most 70 °C under the released engineering conditions |

Use calibrated measurements at the modem connector, short probe grounds or differential probing, and the actual cooling arrangement. The 4 A current case has little input RMS margin; average current alone does not pass it. Record winding imbalance and powered Ethernet temperature as well as converter temperatures.

## 4. Test protection and recovery

With the modem absent, use a qualified current-limited fault fixture. Test protected output shorts and direct regulator shorts as separate cases. Record current, timing, fault energy, overvoltage cutoff, latch/rearm, input removal, and backfeed.

An overvoltage fault must remain below 4.7 V peak including uncertainty, with post-threshold rise no greater than 100 mV. This is a commissioning gate, not permission for normal operation above 4.4 V. A failed limit requires a hardware change before fitting the modem.

Confirm R221 and R779 are both fitted as 1 kΩ regulator bleeds. Measure decay on the regulator and protected output. Verify that modem power-off leaves management available and that USB, service, and status interfaces cannot backfeed an off domain.

Verify blank-controller and reset defaults, hardware power-good timing, and watchdog recovery. Firmware recovery must hold both modem enables low for at least five seconds and confirm output below 100 mV; restart the dwell after controller reset. Radio recovery must hold RUN low for at least 350 ms and confirm its rail below 100 mV. Manual FULL_CARD_POWER_OFF requests require at least one second; the separate hardware release qualification is at least 180 ms after valid protected output.

## 5. Install the modem and test interfaces

After the previous gates pass, install the exact production RM520N-GL and record its firmware. Verify startup and reset timing, 2.5 GbE negotiation and sustained traffic, all four cable pairs, DC imbalance, and behavior during modem transmit bursts. Inspect impedance coupon results and test the manufactured high-speed interfaces.

Exercise USB-C attach/unplug, both ownership selections, powered-off states, and power-good isolation before internal USB host testing. Verify the intended AT endpoints while PCIe Ethernet is active. Record physical SIM insertion, detect and selection, eUICC provisioning, telemetry calibration, and failure behavior on the status bus.

## 6. Qualify radio and enclosure

Configure the E22-900MM22S for the intended US 915 MHz network. Test SPI/control timing, radio reset, link behavior, recovery commands, and the actual antenna and enclosure. Verify the final network and RF deployment requirements. Test authentication, replay rejection, bounded retries, and reset logs in the management firmware.

Keep a first-article record containing hardware and firmware revisions, substitutions, fixtures, supply conditions, temperatures, waveforms, measurements, and the disposition of every failed gate. Complete it before ordering a larger lot.
