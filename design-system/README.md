# SALVATOR ORBIS design system

The house style every SALVATOR ORBIS website, preview and app is built from.
Forge, Bestie and any future build agent must read this file before designing anything.

## Status (19 Oct 2026)

**Choosing a direction.** Three direction boards, each built on De Desmond Mag Wheel and Tyres' real details:

| Board | Link | Idea |
|---|---|---|
| A · Retail Counter | https://salvator-demos.mastermavusana.workers.dev/design-directions/a-retail-counter/ | Looks like a real SA tyre retailer (reference: tyre-shop.co.za). Navy + yellow, Roboto, hero tyre finder, product tiles, bottom app bar. |
| B · Signwriter | https://salvator-demos.mastermavusana.workers.dev/design-directions/b-signwriter/ | Hand-painted shop-sign look. Flat red/yellow/blue, Passion One, phone number as hero, painted price board. |
| C · Pit Lane | https://salvator-demos.mastermavusana.workers.dev/design-directions/c-pit-lane/ | Premium motorsport. Graphite + one signal colour, Saira Condensed, angled buttons, spec rows, quote configurator. |

Index of all three: https://salvator-demos.mastermavusana.workers.dev/design-directions/

Once Vusumuzi picks (or mixes) a direction, this folder gets:

- `kit.css`: the shared tokens and components every preview links to
- `components.md`: the approved sections (header, hero, tyre finder, services, size guide, reviews, visit, offer strip, mobile bar) with copy-paste HTML
- `forge-design-skill.md`: the step-by-step rules Forge follows

Until then, new previews keep the current rules in Forge's task prompt, and must avoid everything in the banned list below.

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
