# LED Chain Board
## Brainstorming
- [ ] 3 outputs for chaining and splitting chain.
- [ ] 2 Knöpfe für interface
    - [ ] fals notwendig poti for einzelregelung
- [ ] Programmierinterface 6 pol am rand der platine
- [ ] 2-4 Channel möglichkeit ?
- [ ] 4 Bohrungen am Besten WESA ?
- [ ] optionale heatsinks
- [ ] 2 stecker für nur 48 V versorgung and daisy chaining
- [ ] Temperatursensor
- [ ]

## Komponentenliste
### LED
#### White
LED: https://www.digikey.de/product-detail/de/luminus-devices-inc/MP-3030-1100-56-95/1214-1348-1-ND/5731661
30 per boaard -> ~1800 Lumen at ~15W
With 2 x 15 LEDs + 20 Ohm resistor at 0.5 W loss each

or :
https://www.samsung.com/led/lighting/mid-power-leds/3030-leds/lm301z-plus/
LED 5700K: https://www.digikey.de/product-detail/de/samsung-semiconductor-inc/SPMWH3326MP7WAQ3S0/1510-SPMWH3326MP7WAQ3S0CT-ND/11697647
LED 3000K: https://www.digikey.de/product-detail/de/samsung-semiconductor-inc/SPMWH3326MP7WAV3S0/1510-SPMWH3326MP7WAV3S0DKR-ND/11697667
2.75 V 65mA 16 in reihe
each:
    4 x https://www.digikey.de/de/products/detail/stackpole-electronics-inc/RMCF1206JT82R0/1753887

-> 32 LEDs per board

#### Color
https://www.digikey.de/de/products/detail/american-bright-optoelectronics-corporation/BL-HJXGXBX32N/9678120
https://www.digikey.de/de/products/detail/inolux/IN-P55TATRGB/7604873

G&B: each 2x150 Ohm https://www.digikey.de/de/products/detail/te-connectivity-passive-product/CRGCQ1206F150R/8576402
R: 8x150 of the G&B ones
    or + LED https://www.digikey.de/de/products/detail/rohm-semiconductor/SML-D12U1WT86/5843853
    and 2x150 + 1x https://www.digikey.de/de/products/detail/stackpole-electronics-inc/RNCP1206FTD20R0/2240306

### AT Tiny
https://www.digikey.de/product-detail/de/microchip-technology/ATTINY841-SSUR/ATTINY841-SSURCT-ND/4437442
Seltsam: https://www.digikey.de/product-detail/de/microchip-technology/ATTINY1605-SSNR/ATTINY1604-SSNRCT-ND/10270383
13 IOs

### Stecker
https://www.digikey.de/product-detail/de/phoenix-contact/1778781/277-2317-1-ND/2625587
Backup: https://www.digikey.de/product-detail/de/harting/14110213002002/1195-3634-1-ND/4834962

Strom:
https://www.digikey.de/product-detail/de/te-connectivity-amp-connectors/2305910-2/A126307-ND/7561708
https://www.digikey.de/product-detail/de/te-connectivity-amp-connectors/2305909-2/A126305CT-ND/7561706

### Programmer
https://www.digikey.com/en/products/detail/te-connectivity-amp-connectors/166086-6/5264359
https://www.digikey.de/de/products/detail/kyocera-avx/009159006551906/4490440

### Spannungsregler
https://www.digikey.de/product-detail/en/monolithic-power-systems-inc/MP4573GN-Z/1589-1680-1-ND/9433446
Vout = 5V
Vin = 48V
Ipeak = 10mA
L = 47 mH
https://www.digikey.de/de/products/detail/taiyo-yuden/NRS6045T470MMGK/2665994

### MOSFET
https://www.digikey.de/product-detail/de/infineon-technologies/BSS671S2LH6327XTSA1/BSS670S2LH6327XTSA1DKR-ND/3196841
Favorite: https://www.digikey.de/product-detail/de/diodes-incorporated/DMN11H220L-7/DMN10H220L-7DICT-ND/4794804

### RS 486 Transceiver
https://www.digikey.de/product-detail/en/analog-devices-inc/ADM484MGMGeach:0MGþ=ARZ/ADM483ARZ-ND/1007307


### Netzteil
https://www.reichelt.de/tischnetzteil-280-w-48-v-5-84-a-mw-gst280a48-p171085.html?&nbc=1
https://www.reichelt.de/netzteile-festspannung-c4950.html?ACTION=2&GROUPID=4950&SEARCH=%2A&START=0&OFFSET=16&nbc=1&SID=96cf37ff842aa7a2495d23bd0364113894efbe5d78afa5c3dbda3


### kondensatoren für 48V
100V: https://www.digikey.de/product-detail/de/nichicon/UUX2A100MNL1GS/493-6279-1-ND/3438792
63V: https://www.digikey.de/product-detail/de/united-chemi-con/EMVE630ADA100MF55G/565-2264-1-ND/757425


### 0 Ohm Brücke
https://www.digikey.de/de/products/detail/yageo/RC0603FR-130RL/12756394
https://www.digikey.de/de/products/detail/yageo/AC0603FR-070RL/2827812
https://www.digikey.de/de/products/detail/stackpole-electronics-inc/RMCF1206ZT0R00/1756906


## Kostenrechnung
### DIP-Schalter
0.886€ for 8 positions https://www.digikey.de/product-detail/de/cui-devices/DS04-254-2-08BK-SMT-TR/2223-DS04-254-2-08BK-SMT-CT-ND/11312442

### 2 Taster auf dem board
0.30€ = 0.15€ x 2
https://www.digikey.de/product-detail/de/c-k/PTS636-SK50-SMTR-LFS/CKN12315-1-ND/10071750
https://www.digikey.de/product-detail/de/c-k/PTS645SL43SMTR92-LFS/CKN10880CT-ND/7645250
https://www.digikey.de/product-detail/de/c-k/PTS-647-SM38-SMTR2-LFS/PTS647SM38SMTR2LFSCT-ND/9649870


### Boardverbindung
Kupflungstecker: 0.76 pC https://www.digikey.de/product-detail/de/kyocera-avx/009159008061916/478-8660-ND/4009961
    leider nur 3A

Symmetrich auf platine: 1.58 = 2x0.79 https://www.digikey.de/product-detail/de/te-connectivity-amp-connectors/1971567-2/A104071CT-ND/3043635
    leider nur 3A
Symmetrich auf platine: 1.18 = 2x0.58 https://www.digikey.de/product-detail/de/assmann-wsw-components/ABTB-400-04-SR1/AE11577CT-ND/9616167
    6A
Symmetrich auf platine: 1.24 = 2x0.62 https://www.digikey.de/product-detail/de/amphenol-icc-fci/10120045-401LF/609-5015-1-ND/5731726
    5A
