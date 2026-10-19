# SALVATOR ORBIS design system

The house style every SALVATOR ORBIS website, preview and app is built from.
Forge, Bestie and any future build agent must read this file before designing anything.

## Status: Style A "Retail Counter" chosen (19 Oct 2026)

Vusumuzi picked **Style A · Retail Counter** (reference: tyre-shop.co.za). All new previews, websites and app screens use it.

| File | What it is |
|---|---|
| `forge-design-skill.md` | The rules and build steps. Read this first. |
| `style-a/template.html` | Master page with `{{PLACEHOLDERS}}`, copy per shop |
| `stock-photos.md` | Approved tyre and wheel stock photos |
| `palettes.md` | Colour palettes: same layout for every shop, but never the same colours twice |
| Live example | https://salvator-demos.mastermavusana.workers.dev/design-directions/a-retail-counter/ |

The other two boards (B · Signwriter, C · Pit Lane) stay in `design-directions/` for reference only: https://salvator-demos.mastermavusana.workers.dev/design-directions/

## Why this exists

Vusumuzi doesn't want the sites to look "built by Claude". The giveaway patterns are listed below. They are banned in all new work.

## Banned patterns (the "Claude look")

- Fonts: Fraunces, Bricolage Grotesque, Space Grotesk, Inter, DM Sans, Sora, Manrope, Plus Jakarta Sans, Instrument Serif, Bodoni Moda, Playfair Display. Use only the fonts the chosen direction names.
- Small UPPERCASE labels with wide letter-spacing above headings ("eyebrows").
- Pill-shaped buttons and chips (`border-radius: 999px`) unless the chosen direction says so.
- Cream / beige / "paper" page backgrounds (#FAF4EA, #F4EFE8, #FBF8F3 and similar).
- Soft floating cards with big rounded corners and blurry drop shadows.
- Offset "sticker" shadows and tilted sticker labels as decoration.
- The section header pattern of a big heading on the left and a grey paragraph on the right.
- Gradient text, glassmorphism, glowing blobs, emoji used as icons.
- Generic hero copy ("Elevate your…", "Experience the…", "Where X meets Y").
- Every section the same width and rhythm. Vary density the way real shop sites do.

## Rules that stay, whatever the direction

- Mobile first; phone, WhatsApp and directions reachable with one thumb on every screen.
- Body text 17px or more; muted text no lighter than #4A403D on light, no darker than #E2D6CA on dark; check contrast before pushing.
- Only published facts; `R[ — ]`, `[your brands]`, `[confirm]` for unknowns; never invented reviews, prices, brands, awards or staff.
- Stock photos are labelled as stock; never AI images, never other businesses' photos or chain signage.
- Previews carry the preview ribbon and `noindex, nofollow`.
- Each shop gets its own colours (taken from its real sign or listing photos) inside the chosen direction's structure.
