# Style A palettes: every sample gets its own colours

Vusumuzi's rule (19 Oct 2026): **no two website samples share the same colours.** Style A keeps the same layout, fonts and shapes for every shop; only the palette changes.

All palettes below are contrast-checked: white text on `--main` and `--main-2` at least 5.8:1, dark text (#1A1D23) on `--hi` at least 7:1, `--hi` on `--main` at least 5:1, `--main` on `--tint` at least 6.5:1.

| # | Name | --main | --main-2 | --hi | --tint | Used by |
|---|---|---|---|---|---|---|
| 0 | Navy / yellow | #0A2A5E | #123A7A | #FFD200 | #F1F3F6 | De Desmond Style A example only. Never reuse. |
| 1 | Oxblood / amber | #7A1F2B | #94283A | #F2A900 | #F6F1F1 | Do not use: Vusumuzi didn't like it (19 Oct 2026) |
| 2 | Forest / lime | #1F5130 | #256B3D | #C5E04A | #F0F5F0 | Karims (19 Oct 2026) |
| 3 | Charcoal / orange | #2B2F36 | #3A3F48 | #FF8A1F | #F2F2F3 | De Desmond (19 Oct 2026) |
| 4 | Petrol / sand | #0F4C5C | #14637A | #F4C95D | #EEF4F5 | Chris Kwifor & Sons (19 Oct 2026; replaced oxblood, which Vusumuzi didn't like) |
| 5 | Purple / gold | #3D2A6B | #4E3787 | #E8B931 | #F3F1F8 | |
| 6 | Brick / butter | #9A3412 | #B23E17 | #FFD66B | #F8F1EE | Synclaire (19 Oct 2026) |
| 7 | Cobalt / sky | #1D3F94 | #2550B8 | #7FD1FF | #EFF3FB | SC Auto Fitment (19 Oct 2026) |
| 8 | Pine / coral | #22433D | #2D5A52 | #FF9E7A | #EFF4F3 | |
| 9 | Black / red | #151515 | #2A2A2A | #FF6B57 | #F2F2F2 | JF Tyres (19 Oct 2026) |
| 10 | Plum / pink | #5B1A3A | #74234B | #F7A8C4 | #F7F0F3 | |
| 11 | Olive / mustard | #3F4A12 | #55631A | #E9C84A | #F3F4EC | |

## How to pick

1. Read the hub `mocks` collection: every mock records `palette` (the name above, or `custom:<main>/<hi>`).
2. If the shop's own sign or listing photos show clear brand colours, build a custom palette from them, as long as it isn't the same as or close to one already used. Check the four contrast pairs above (white on main ≥ 4.5, ink on hi ≥ 4.5, hi on main ≥ 3, main on tint ≥ 4.5) and save it as `custom:<main>/<hi>`.
3. Otherwise take the lowest-numbered palette that no mock has used yet.
4. When all 11 are used, start again from the palette used longest ago, but never the same palette as the previous 5 mocks, and never for two shops on the same street or route stop.
5. Paste the four values into the `:root` block of the page and write the palette name into the mock record (`palette`) and the "Used by" column here.

`--green` (#0B7A3E, WhatsApp) never changes.

## Style D · Neon Night palettes

Tokens: `--glow` (main signal), `--glow-2` (second signal), `--base` (page), `--base-2` (panels). Both glows must reach at least 4.5:1 on `--base` (these all reach 6:1 or more); text stays white/#C3CDD6.

| # | Name | --glow | --glow-2 | --base | --base-2 | Used by |
|---|---|---|---|---|---|---|
| D1 | Cyan / orange | #22E3F0 | #FF8A2A | #0B0E12 | #151A21 | Style D sample (De Desmond board) only |
| D2 | Lime / amber | #B8F22E | #FFC23A | #0C100B | #161C14 | De Desmond style-d (21 Oct 2026) |
| D3 | Ice blue / red | #6EC8FF | #FF5A5F | #0A0D14 | #141A26 | Karims style-d (21 Oct 2026) |
| D4 | Violet / cyan | #C2A1FF | #3FE0D0 | #0E0B14 | #1A1524 | Synclaire style-d (21 Oct 2026) |
| D5 | Gold / white | #FFD24A | #F2F2F2 | #0F0E0B | #1B1913 | Chris Kwifor style-d (21 Oct 2026) |
| D6 | Teal / pink | #2EE6C5 | #FF7FC0 | #0A1112 | #131D1F | JF Tyres style-d (21 Oct 2026) |
| D7 | Red / amber | #FF6B6B | #FFB547 | #120B0B | #1F1414 | SC Auto Fitment style-d (21 Oct 2026) |

## Style E · Open Sky palettes

Tokens: `--sky-1` (top of hero), `--sky-2` (middle), `--sky-3` (bottom/sunrise), `--deep` (headings, buttons), `--deep-2` (links). `--deep` must reach 4.5:1 on `--sky-1` and 7:1 on white.

| # | Name | --sky-1 | --sky-2 | --sky-3 | --deep | --deep-2 | Used by |
|---|---|---|---|---|---|---|---|
| E1 | Blue sky / sunrise | #1CC2EE | #BFEFFB | #FBC98E | #0D2A52 | #1B4A8A | Style E sample (De Desmond board) only |
| E2 | Sea / sand | #3CCFC4 | #D3F5F1 | #FFE3A3 | #0B3B3A | #146B66 | De Desmond style-e (21 Oct 2026) |
| E3 | Evening / coral | #FFB089 | #FFE3D1 | #FFD27A | #4A1D2E | #7A2E4A | Karims style-e (21 Oct 2026) |
| E4 | Highveld green | #8EDBAA | #E3F6E9 | #FCE5A6 | #12382A | #1F6B4A | Synclaire style-e (21 Oct 2026) |
| E5 | Storm / gold | #8FB3D9 | #E1ECF7 | #F7D27E | #1E2A3A | #34506F | Chris Kwifor style-e (21 Oct 2026) |
| E6 | Lavender dusk | #A99BEA | #ECE8FB | #FFD9A8 | #2A1F5C | #4B3A99 | JF Tyres style-e (21 Oct 2026) |
| E7 | Desert / clay | #F2B66B | #FCEBD4 | #FFD3B0 | #4A2A10 | #7A4A1F | SC Auto Fitment style-e (21 Oct 2026) |

Same rule as Style A: no two samples share a palette; record it on the mock as e.g. `D2 lime-amber`. Check the contrast pairs before pushing a new palette.
