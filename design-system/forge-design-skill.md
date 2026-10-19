# Forge design rules: Style A "Retail Counter"

Chosen by Vusumuzi on 19 Oct 2026. Every new SALVATOR ORBIS preview, website and app screen is built in Style A unless he says otherwise. Older previews stay as they are.

Reference look: tyre-shop.co.za (a real South African tyre retailer). The site should feel like a real shop, not a designed portfolio.

## Files

- `design-system/style-a/template.html`: the master page. Copy it to `<slug>/index.html` and fill it in.
- Live example: https://salvator-demos.mastermavusana.workers.dev/design-directions/a-retail-counter/ (De Desmond Mag Wheel and Tyres)
- `design-system/stock-photos.md`: approved tyre and wheel stock photos.
- `design-system/README.md`: banned "Claude look" patterns and the rules that never change.

## Build steps

1. Copy `style-a/template.html` to `<slug>/index.html`. Keep it one self-contained file.
2. Replace every `{{PLACEHOLDER}}` (name, short name, monogram, tagline, phone, tel, wa, street, suburb, city/postcode, place ID, rating, reviews, URL-encoded name/address). Search for `{{` before pushing; none may remain.
3. Rewrite the copy that came from De Desmond to this shop's real facts: hero headline, the three ticks, the value strip, the service tiles, the FAQ answers, the hours table and footer line. The template's "Open 24 hours / Any hour" lines are De Desmond's; remove them unless the shop's listing says 24 hours.
4. Colours: change only the `:root` tokens. `--navy` becomes the shop's main sign colour (dark enough for white text, contrast at least 4.5:1) and `--yellow` its highlight colour (dark text on it, at least 4.5:1). Keep `--green` for WhatsApp. If the shop has no clear colours, keep navy and yellow.
5. Photos: the shop's own photos first; then `stock-photos.md`. Hero = a wide tyre/warehouse photo; tiles = tyres, mags, workshop. Caption stock "Your photo here".
6. Prices: fill the `priceData` JSON block (see Prices below). Never invent prices.
7. Services: only what the listing supports; anything else gets the `confirm` tag.
8. Check: 390px and 1280px widths with no sideways scroll, contrast of any new colour pair, no `{{`, no banned patterns from the README, `noindex` meta present.

## Fonts and shapes (do not change)

- Roboto Condensed 700–800 for headings (section titles uppercase), Roboto 400/500/700 for text. No other fonts.
- Corners 4px maximum (2px on small tags). No pill buttons, no rounded floating cards, no soft shadows except the tyre finder panel.
- No small uppercase letter-spaced labels above headings. Section titles sit left with an action link on the right.
- Mobile: the bottom bar (Home · Find size · Call · WhatsApp) is always present.

## Section order

Utility bar → header (monogram, name, Call, WhatsApp) → category nav → hero with tyre finder → value strip → services tiles → tyre prices → brands we fit → how to read your tyre size → buying help FAQ → visit (hours, rating, map) → offer strip (packages from settings/campaign) → footer → mobile bottom bar.

Sections can be dropped when a shop has nothing for them (e.g. no mags), never reordered into a "creative" layout.

## Prices

All prices live in one JSON block in the page (`<script type="application/json" id="priceData">`): `updated` date, and `items` of `{size, type: "New"|"Second-hand", brand, price}`. The list, filters and WhatsApp "Order" buttons are built from it automatically.

- Preview stage: example common sizes with `"price": null` (shows `R[ — ]`) and `[Brand]`, plus the note that these are examples.
- Live site: the shop's real price list. Prices per tyre, VAT included, with the "updated" date shown. Sizes they don't list fall back to the WhatsApp quote finder.
- Updating: the owner WhatsApps a photo of the price list or new prices to Vusumuzi; the JSON is updated and pushed (target: same day). Tyre Pro clients can later get a Google Sheet they edit themselves that the site reads.
- Displayed prices must be honoured, so stale prices are removed rather than left up.

## For apps (Tyre Pro booking and later)

Same tokens, fonts and shapes. Forms use full-width 48px+ controls with labels above, dropdowns for fixed choices, a sticky full-width green action button, and a bottom bar for main navigation.
