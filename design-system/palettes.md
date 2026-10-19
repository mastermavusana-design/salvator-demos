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
