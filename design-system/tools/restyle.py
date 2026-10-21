#!/usr/bin/env python3
"""Turn each shop's Style A preview into Style D and Style E versions (same content, new look),
restore first versions from git history, and build a client style picker per shop.
Run from the repo root."""
import re, html, subprocess, json, os, urllib.parse

src = open(os.path.join(os.path.dirname(os.path.abspath(__file__)), 'build_styles_de.py')).read().split('# ---------------- values')[0]
exec(src)  # brings CSS_D, CSS_E, HERO_D_ART, HERO_E_ART, tyre_mark, ICON_*, PH

SHOPS = [
 # slug, first-version commit, D palette, E palette
 ('de-desmond-mag-wheel-and-tyres', '61da236', 'D2', 'E2'),
 ('karims-tyre-wheel-and-balance', '61da236', 'D3', 'E3'),
 ('synclaire-used-tyres-repairs', '61da236', 'D4', 'E4'),
 ('chris-kwifor-and-sons-tyre-center', '6ae1790', 'D5', 'E5'),
 ('jf-tyres', '6ae1790', 'D6', 'E6'),
 ('sc-auto-fitment-second-hand-tyres-and-wheels-repair', '6ae1790', 'D7', 'E7'),
]
PAL = {
 'D2': ('Lime / amber', dict(glow='#B8F22E', glow2='#FFC23A', base='#0C100B', base2='#161C14')),
 'D3': ('Ice blue / red', dict(glow='#6EC8FF', glow2='#FF5A5F', base='#0A0D14', base2='#141A26')),
 'D4': ('Violet / cyan', dict(glow='#C2A1FF', glow2='#3FE0D0', base='#0E0B14', base2='#1A1524')),
 'D5': ('Gold / white', dict(glow='#FFD24A', glow2='#F2F2F2', base='#0F0E0B', base2='#1B1913')),
 'D6': ('Teal / pink', dict(glow='#2EE6C5', glow2='#FF7FC0', base='#0A1112', base2='#131D1F')),
 'D7': ('Red / amber', dict(glow='#FF6B6B', glow2='#FFB547', base='#120B0B', base2='#1F1414')),
 'E2': ('Sea / sand', dict(s1='#3CCFC4', s2='#D3F5F1', s3='#FFE3A3', deep='#0B3B3A', deep2='#146B66')),
 'E3': ('Evening / coral', dict(s1='#FFB089', s2='#FFE3D1', s3='#FFD27A', deep='#4A1D2E', deep2='#7A2E4A')),
 'E4': ('Highveld green', dict(s1='#8EDBAA', s2='#E3F6E9', s3='#FCE5A6', deep='#12382A', deep2='#1F6B4A')),
 'E5': ('Storm / gold', dict(s1='#8FB3D9', s2='#E1ECF7', s3='#F7D27E', deep='#1E2A3A', deep2='#34506F')),
 'E6': ('Lavender dusk', dict(s1='#A99BEA', s2='#ECE8FB', s3='#FFD9A8', deep='#2A1F5C', deep2='#4B3A99')),
 'E7': ('Desert / clay', dict(s1='#F2B66B', s2='#FCEBD4', s3='#FFD3B0', deep='#4A2A10', deep2='#7A4A1F')),
}
WHATSAPP_VUSI = '27721005611'

def pal_css(key):
    n, p = PAL[key]
    if key.startswith('D'):
        return f":root{{--glow:{p['glow']};--glow-2:{p['glow2']};--base:{p['base']};--base-2:{p['base2']}}}"
    return f":root{{--sky-1:{p['s1']};--sky-2:{p['s2']};--sky-3:{p['s3']};--deep:{p['deep']};--deep-2:{p['deep2']}}}"

def grab(pat, s, flags=re.S):
    m = re.search(pat, s, flags)
    if not m: raise ValueError('missing: ' + pat[:60])
    return m

def restyle(a, style, palkey):
    css = CSS_D if style == 'D' else CSS_E
    fonts = ('family=Saira:ital,wght@1,700;1,800&family=Roboto:wght@400;500;700' if style == 'D'
             else 'family=Montserrat:wght@700;800&family=Roboto:wght@400;500;700')
    theme = PAL[palkey][1].get('base') or PAL[palkey][1].get('s1')
    brand = grab(r'<a class="brand"[^>]*><i>[^<]*</i><span><b>(.*?)</b><small>(.*?)</small></span></a>', a)
    short, small = brand.group(1), brand.group(2)
    hlinks = grab(r'<div class="hlinks">.*?</div>\n</div></header>', a).group(0)
    hlinks = hlinks[:-len('\n</div></header>')]
    board = grab(r'<div class="board">.*?</div>', a).group(0)
    util = grab(r'<div class="util">.*?</div></div>', a).group(0).replace(' style="color:#fff;font-weight:700"', '')
    hero = grab(r'<div class="hero">.*?</form>\n  </div>\n</div>', a)
    h = hero.group(0)
    h1 = grab(r'<h1>(.*?)</h1>', h).group(1)
    tag = re.sub(r'<[^>]+>', '', h1).strip().rstrip('.')
    sub = grab(r'<p class="sub">.*?</p>', h).group(0)
    ticks = grab(r'<ul class="ticks">.*?</ul>', h).group(0)
    form = grab(r'<form class="finder".*?</form>', h).group(0)
    if style == 'E': form = form.replace('Find my tyre size', 'Find your tyre')
    else: form = form.replace('Find my tyre size', 'Find my tyre')
    rule = '<span class="rule"></span>' if style == 'D' else ''
    art = HERO_D_ART if style == 'D' else HERO_E_ART
    new_hero = f'''<div class="hero">
  {art}
  <div class="w">
    <div>
      <div class="lock">{tyre_mark('lk')}<div>{rule}<h1>{short}</h1><span class="tag">{tag}</span></div></div>
      {sub}
      {ticks}
    </div>
    {form}
  </div>
</div>'''
    header = f'''<header><div class="w">
  <a class="brand" href="#top">{tyre_mark('mk')}<span><b>{short}</b><small>{small}</small></span></a>
  <nav class="mainnav" aria-label="Sections"><a href="#top" aria-current="page">Home</a><a href="#prices">Tyre prices</a><a href="#services">Services</a><a href="#size">Tyre sizes</a><a href="#visit">Find us</a></nav>
  {hlinks.strip()}
</div></header>'''
    if style == 'D':
        band_photo, band_alt, band_text = 'offroad', '4x4 on a rocky mountain track at sunset', 'Gravel, potholes, <em>long trips.</em> Tyres for every road.'
    else:
        band_photo, band_alt, band_text = 'highway', 'Car wheel on a coastal road', 'Smooth, quiet, <em>safe.</em> Every kilometre.'
    band = (f'\n<div class="band"><img loading="lazy" src="{PH}{band_photo}-1376.jpg" srcset="{PH}{band_photo}-800.jpg 800w, {PH}{band_photo}-1376.jpg 1376w" sizes="100vw" alt="{band_alt} (stock image)">'
            f'<div class="w"><p class="bandtx">{band_text}</p><a class="bandbtn" href="#finder">Find my size</a></div><small class="credit">Stock image · your photo here</small></div>\n')
    # assemble
    title = grab(r'<title>(.*?)</title>', a).group(1)
    body_start = a.index('<body>') + len('<body>')
    main_start = a.index('<main id="top">')
    rest = a[main_start:]
    rest = rest.replace(h, new_hero, 1)
    sv = rest.index('<section id="services">'); end = rest.index('</div></section>', sv) + len('</div></section>')
    rest = rest[:end] + band + rest[end:]
    rest = re.sub(r'<section class="sys">.*?</section>\n?', '', rest, flags=re.S)
    rest = rest.replace('Some photos: Unsplash/Pexels</span>', 'Some photos: Unsplash/Pexels and SALVATOR ORBIS stock images</span>')
    extra = '\n.tiles+.tiles{margin-top:14px}\n' + pal_css(palkey)
    head = f'''<!doctype html>
<html lang="en-ZA">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{title} · Style {style}</title>
<meta name="robots" content="noindex, nofollow">
<meta name="theme-color" content="{theme}">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?{fonts}&display=swap">
<style>
{css}{extra}
</style>
</head>
<body>
'''
    out = head + board + '\n' + util + '\n' + header + '\n\n' + rest
    return out, short, title

def picker(slug, name, short, area, wa, options):
    cards = ''
    for o in options:
        msg = urllib.parse.quote(f"Hi Vusumuzi, it's {name}. I like the {o['label']} look for my website.")
        cards += f'''
  <article class="opt">
    <div class="thumb"><iframe loading="lazy" tabindex="-1" aria-hidden="true" title="{html.escape(o['label'])}" src="{o['href']}"></iframe><a href="{o['href']}" target="_blank" rel="noopener" aria-label="View {html.escape(o['label'])}"></a></div>
    <div class="tx"><h2>{html.escape(o['label'])}</h2><p>{html.escape(o['desc'])}</p>
      <div class="acts"><a class="view" href="{o['href']}" target="_blank" rel="noopener">View full site</a><a class="pick" href="https://wa.me/{WHATSAPP_VUSI}?text={msg}" target="_blank" rel="noopener">I like this one</a></div>
    </div>
  </article>'''
    return f'''<!doctype html>
<html lang="en-ZA">
<head>
<meta charset="utf-8">
<meta name="viewport" content="width=device-width,initial-scale=1">
<title>{html.escape(short)} · pick your website style</title>
<meta name="robots" content="noindex, nofollow">
<link rel="preconnect" href="https://fonts.googleapis.com">
<link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
<link rel="stylesheet" href="https://fonts.googleapis.com/css2?family=Roboto+Condensed:wght@700;800&family=Roboto:wght@400;500;700&display=swap">
<style>
*{{box-sizing:border-box}}
body{{margin:0;background:#F3F4F6;color:#16191F;font:400 17px/1.5 Roboto,Arial,sans-serif}}
.w{{max-width:1200px;margin:0 auto;padding:0 16px}}
header{{background:#111;color:#F2F2F2;padding:22px 0}}
h1{{font:800 clamp(26px,4vw,38px)/1.1 "Roboto Condensed",Arial,sans-serif;margin:0 0 6px;text-transform:uppercase}}
header p{{margin:0;color:#D6D6D6;max-width:60ch}}
main{{padding:22px 0 40px}}
.grid{{display:grid;grid-template-columns:repeat(auto-fill,minmax(320px,1fr));gap:16px}}
.opt{{background:#fff;border:1px solid #D9DEE6;border-radius:4px;overflow:hidden;display:flex;flex-direction:column}}
.thumb{{position:relative;aspect-ratio:9/12;overflow:hidden;background:#E6E9EE;border-bottom:1px solid #D9DEE6}}
.thumb iframe{{position:absolute;left:0;top:0;width:390px;height:520px;border:0;transform-origin:0 0;pointer-events:none}}
.thumb a{{position:absolute;inset:0}}
.tx{{padding:14px 16px 16px;display:flex;flex-direction:column;gap:6px;flex:1}}
.tx h2{{font:800 22px/1.1 "Roboto Condensed",Arial,sans-serif;margin:0;text-transform:uppercase}}
.tx p{{margin:0;color:#4A515E;font-size:16px}}
.acts{{margin-top:auto;padding-top:8px;display:flex;gap:8px;flex-wrap:wrap}}
.acts a{{flex:1;min-height:48px;display:inline-flex;align-items:center;justify-content:center;border-radius:4px;font-weight:700;text-decoration:none;font-size:16px;padding:0 12px}}
.view{{border:2px solid #16191F;color:#16191F}}
.pick{{background:#0B7A3E;color:#fff}}
footer{{color:#4A515E;font-size:15px;padding-bottom:40px}}
footer a{{color:#16191F;font-weight:700}}
</style>
</head>
<body>
<header><div class="w"><h1>{html.escape(short)}: pick your website style</h1><p>Here is your shop's website in {len(options)} different looks. Same content and the same WhatsApp tyre finder in each, only the style changes. Tap "View full site" to try one on your phone, then "I like this one" to tell Vusumuzi which you want.</p></div></header>
<main class="w"><div class="grid">{cards}
</div></main>
<footer class="w">These are previews designed for {html.escape(name)} by SALVATOR ORBIS. Nothing here is live yet. Questions? Vusumuzi Nhlapo · <a href="tel:+27721005611">072 100 5611</a> · <a href="https://wa.me/{WHATSAPP_VUSI}">WhatsApp</a></footer>
<script>
(function(){{function fit(){{document.querySelectorAll('.thumb').forEach(function(t){{t.querySelector('iframe').style.transform='scale('+(t.clientWidth/390)+')';}});}}window.addEventListener('resize',fit);fit();}})();
</script>
</body>
</html>
'''

import sys
if len(sys.argv) >= 4:
    # usage: python3 design-system/tools/restyle.py <slug> <D palette e.g. D2> <E palette e.g. E3> [first-version commit]
    SHOPS = [(sys.argv[1], sys.argv[4] if len(sys.argv) > 4 else None, sys.argv[2], sys.argv[3])]
review_items = []
for slug, first, dk, ek in SHOPS:
    a = open(f'{slug}/index.html').read()
    a_pal = None
    for k in ['d', 'e']:
        key = dk if k == 'd' else ek
        out, short, title = restyle(a, k.upper(), key)
        os.makedirs(f'{slug}/style-{k}', exist_ok=True)
        open(f'{slug}/style-{k}/index.html', 'w').write(out)
    if first:
        os.makedirs(f'{slug}/v1', exist_ok=True)
        v1 = subprocess.check_output(['git', 'show', f'{first}:{slug}/index.html']).decode()
        open(f'{slug}/v1/index.html', 'w').write(v1)
    name = html.unescape(re.search(r'<title>(.*?) · ', a).group(1))
    area = html.unescape(re.search(r'<title>.*? · (.*?)</title>', a).group(1))
    wa = re.search(r'wa\.me/(\d+)', a).group(1)
    opts = [
        dict(label='Classic shop', href='../', desc='Clean and practical, like the big tyre retailers. Price list and tyre finder up front.'),
        dict(label='Neon night', href='../style-d/', desc='Dark and bold, with glowing tyre tracks. Stands out at night and on social media.'),
        dict(label='Open sky', href='../style-e/', desc='Bright and friendly, blue sky into sunrise, with rounded buttons.'),
    ]
    if os.path.exists(f'{slug}/v1/index.html'):
        opts.append(dict(label='Made-for-you', href='../v1/', desc='The first design we made just for your shop, with its own layout and colours.'))
    os.makedirs(f'{slug}/choose', exist_ok=True)
    open(f'{slug}/choose/index.html', 'w').write(picker(slug, name, html.unescape(short), area, wa, opts))
    review_items.append(dict(slug=slug, name=name, area=area, d=dk, e=ek))
print(json.dumps(review_items))
print('done', len(review_items))
