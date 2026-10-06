from pathlib import Path
import html, json

ROOT = Path(__file__).resolve().parent
SOURCE = json.loads((ROOT / 'sources/products-2026-09-28.json').read_text())
FONT = 'Montserrat,Arial,sans-serif'
GREEN, MINT, INK = '#188348', '#E5FCEF', '#104C3E'
CREAM, RUST = '#FFF5E7', '#C75C36'
UTM = '?utm_source=omnisend&utm_medium=email&utm_campaign=skilsas_20261006_kurybos_popiete'
CATEGORY = 'https://www.skilsas.lt/lavinamosios-priemones/spalvinimui-ir-kurybai'
PUBLIC = 'https://raw.githubusercontent.com/elaiskai/skilsas-email-assets/505f12dee10d10b12289b3254c3c8a660cbd82c2/campaigns/2026-10-06/kurybos-popiete/'
SUBJECT = 'Kai lauke lyja, namuose kuriam 🎨'
PREHEADER = '8 kūrybos idėjos rudens popietei: piešti, spalvinti ir eksperimentuoti.'

PRODUCTS = [
    ('led-holder', 'LED PIEŠIMO LENTA', 'Su markerių laikikliu', '43 × 26 cm lenta, 5 markeriai ir 9 šviesos režimai.'),
    ('led', 'LED PIEŠIMO LENTA', 'Šviečianti lenta', '35 × 26 cm lenta, ant kurios piešiniai nušvinta spalvomis.'),
    ('draw', 'LIETUVIŠKAI ĮGARSINTA', '„Mokausi piešti“', '100 dvipusių kortelių su piešimo žingsniais ir garsais.'),
    ('crayons', '24 SPALVOS · NUO 3 M.', 'Šilkinės kreidelės', 'Išsukamos, ryškios ir lengvai nuplaunamos kreidelės.'),
    ('roll', 'DIDELIS FORMATAS · NUO 3 M.', '„Gyvūnų pasaulis“', 'Spalvinimo rulonas kūrybai vienam arba kartu.'),
    ('dino', 'AKVARELĖ · NUO 5 M.', '„Dinozaurai“', '26 piešiniai, integruota paletė ir 2 teptukai.'),
    ('marble', '12 SPALVŲ · NUO 6 M.', 'Marmuravimo rinkinys', 'Raštai kuriami ant vandens ir perkeliami ant popieriaus.'),
    ('windows', 'LANGŲ DEKORACIJOS · NUO 6 M.', '„Kosmoso pasaulis“', '12 vitražinių formelių, 10 dažų ir 12 siurbtukų.'),
]

STARTERS = [
    ('Išsirinkite priemonę', 'Lenta, kreidelės ar akvarelė.'),
    ('Sugalvokite temą', 'Rudens lapas, lapė ar kosmosas.'),
    ('Palikite vietos netikėtumui', 'Tegul spalvas šiandien renkasi vaikas.'),
]


def esc(value): return html.escape(str(value), quote=True)
def product_url(key): return SOURCE[key]['offers']['url'] + UTM
def price(key):
    value = SOURCE[key]['offers']['price']
    return (str(int(value)) if value == int(value) else f'{value:.2f}'.replace('.', ',')) + ' €'
def table(body, extra=''):
    return f'<table role="presentation" cellpadding="0" cellspacing="0" border="0" {extra}>{body}</table>'
def row(body, style='', extra=''):
    return f'<tr><td {extra} style="{style}">{body}</td></tr>\n'
def p(text, margin='0 0 16px', size=17, color=INK, cls=''):
    return f'<p class="{cls}" style="margin:{margin};font-family:{FONT};font-size:{size}px;line-height:{round(size*1.5)}px;color:{color};">{text}</p>'
def eyebrow(text, color=GREEN):
    return f'<p style="margin:0 0 10px;font-family:{FONT};font-size:11px;line-height:17px;letter-spacing:1px;font-weight:700;color:{color};">{text}</p>'
def heading(text, color=INK):
    return f'<h2 style="margin:0 0 12px;font-family:{FONT};font-size:28px;line-height:35px;color:{color};font-weight:700;">{text}</h2>'
def button(text, href, inverse=False):
    bg, fg = (MINT, INK) if inverse else (GREEN, '#FFFFFF')
    return table(row(f'<a href="{esc(href)}" style="display:inline-block;padding:14px 20px;border:1px solid {bg};border-radius:28px;font-family:{FONT};font-size:15px;line-height:22px;font-weight:700;text-decoration:none;color:{fg};">{text}&nbsp; →</a>', f'background-color:{bg};border-radius:28px;mso-padding-alt:14px 20px;', f'align="center" bgcolor="{bg}"'))
def section(label, title, subtitle=''):
    return row(eyebrow(label)+heading(title)+(p(subtitle, '0', 16) if subtitle else ''), 'padding:26px 24px 18px;')
def card(product):
    key, label, title, desc = product
    href = esc(product_url(key))
    image = f'<a href="{href}"><img src="assets/products/{key}.jpg" width="124" height="124" alt="{esc(SOURCE[key]["name"])}" style="display:block;width:124px;max-width:100%;height:auto;border:0;border-radius:12px;"></a>'
    title_html = eyebrow(label) + f'<h3 style="margin:0;font-family:{FONT};font-size:20px;line-height:26px;font-weight:700;color:{INK};">{title}</h3>'
    cta = f'<a href="{href}" style="display:inline-block;padding:10px 9px;background-color:{GREEN};border:1px solid {GREEN};border-radius:22px;font-family:{FONT};font-size:13px;line-height:20px;font-weight:700;text-decoration:none;color:#FFFFFF;white-space:nowrap;">Apžiūrėti&nbsp;→</a>'
    purchase = f'<p style="margin:0 0 14px;font-family:{FONT};font-size:25px;line-height:34px;font-weight:700;color:{INK};white-space:nowrap;">{price(key).replace(" ", "&nbsp;")}</p>' + cta
    visual = table(f'<tr><td width="132" valign="middle" style="width:132px;padding:0;">{image}</td><td valign="middle" align="right" style="padding:0;">{purchase}</td></tr>', 'width="100%" style="width:100%;table-layout:fixed;"')
    content = row(title_html, 'padding:16px 16px 12px;vertical-align:top;', 'height="86" class="product-title-cell"')
    content += row(visual, 'padding:0 16px;')
    content += row(p(desc, '0', 16, cls='product-description'), 'padding:14px 15px 18px;vertical-align:top;', 'height="72" class="product-desc-cell"')
    return table(content, 'class="product-card" width="100%" bgcolor="#FFFFFF" style="width:100%;background-color:#FFFFFF;border:1px solid #C7E5D4;border-radius:20px;table-layout:fixed;"')
def grid(products):
    columns = []
    for index, product in enumerate(products):
        if index % 2 == 0:
            columns.append('<!--[if mso]><table role="presentation" width="576" cellpadding="0" cellspacing="0" border="0"><tr><![endif]-->')
        columns.append('<!--[if mso]><td width="288" valign="top"><![endif]--><div class="product-column" style="display:inline-block;vertical-align:top;width:100%;max-width:288px;text-align:left;">' + table(row(card(product), 'padding:0 6px 12px;'), 'width="100%" style="width:100%;table-layout:fixed;"') + '</div><!--[if mso]></td><![endif]-->')
        if index % 2 == 1 or index == len(products) - 1:
            columns.append('<!--[if mso]></tr></table><![endif]-->')
    return row(''.join(columns), 'padding:0 12px;font-size:0;line-height:0;', 'align="center"')
def feature(label, title, body, bg='#D4EFDE', dark=False):
    color = MINT if dark else INK
    content = eyebrow(label, color) + heading(title, color) + body
    return row(table(row(content, 'padding:24px;'), f'width="100%" bgcolor="{bg}" style="width:100%;background-color:{bg};border-radius:22px;table-layout:fixed;"'), 'padding:14px 18px 16px;')


parts = []
parts.append(row(f'<a href="{esc("https://www.skilsas.lt/" + UTM)}"><img src="assets/brand/logo.png" width="112" height="65" alt="SKILSAS" style="display:block;width:112px;height:auto;border:0;"></a>', 'padding:24px 24px 20px;', 'align="center"'))
parts.append(row(eyebrow('RUDENS KŪRYBOS POPIETĖ') + f'<h1 class="hero-title" style="margin:0 0 16px;font-family:{FONT};font-size:33px;line-height:40px;font-weight:700;letter-spacing:-1px;color:{INK};">Kai lauke lyja,<br>namuose kuriam.</h1>' + p('8 idėjos spalvotai popietei be ekranų.', '0', 18), 'padding:4px 20px 24px;', 'align="center"'))
parts.append(row(f'<a href="{esc(product_url("led-holder"))}"><img src="assets/campaign/hero.jpg" width="564" height="564" alt="SKILSAS LED piešimo lenta su šviečiančiu lapės piešiniu rudeniškame kūrybos kampelyje" style="display:block;width:100%;height:auto;border:1px solid #BCDCCB;border-radius:24px;box-sizing:border-box;"></a>', 'padding:0 18px;font-size:0;line-height:0;'))
parts.append(row(eyebrow('PIEŠINIAI, KURIE NUŠVINTA') + heading('LED lenta su<br>markerių laikikliu') + p('5 markeriai, 9 šviesos režimai ir vieta kiekvienai naujai idėjai.', '0 0 14px', 16) + f'<p style="margin:0 0 18px;font-family:{FONT};font-size:30px;line-height:38px;font-weight:700;color:{INK};">{price("led-holder")}</p>' + button('Apžiūrėti LED lentą', product_url('led-holder')), 'padding:24px 24px 32px;', 'align="center"'))
parts.append(row(p('<strong>Labas!</strong>', '0 0 10px') + p('Kai už lango pilka, ant stalo gali atsirasti visas spalvotas pasaulis. Šiai popietei atrinkau priemones, kurios kviečia piešti, spalvinti ir išbandyti ką nors naujo.', '0'), 'padding:0 24px 8px;'))

starter_rows = ''
for index, (title, desc) in enumerate(STARTERS, 1):
    starter_rows += f'<tr><td width="38" valign="top" style="padding:0 0 15px;font-family:{FONT};font-size:26px;line-height:32px;font-weight:700;color:{RUST};">{index:02d}</td><td style="padding:0 0 15px 10px;">' + p(f'<strong>{title}</strong>', '0', 17) + p(desc, '0', 15) + '</td></tr>'
parts.append(feature('KŪRYBOS PRADŽIA', 'Trys maži žingsniai.', table(starter_rows, 'width="100%" style="table-layout:fixed;"'), CREAM))

parts.append(section('01 / ŠVIESA IR LINIJA', 'Nuo pirmo brūkšnio.', 'Pieškite, kopijuokite arba kurkite visai be taisyklių.'))
parts.append(grid(PRODUCTS[1:3]))
parts.append(section('02 / SPALVOS ANT POPIERIAUS', 'Daug vietos fantazijai.', 'Kreidelės, didelis rulonas ir akvarelė su dinozaurais.'))
parts.append(grid(PRODUCTS[3:6]))
parts.append(feature('PABANDYKITE KARTU', 'Tik trys spalvos.', p('Išsirinkite tris spalvas ir pabandykite visą piešinį sukurti tik jomis.', '0 0 18px', 16, MINT) + table(row(p('Kokią nuotaiką jos sukūrė?', '0', 18, MINT), 'padding:0 0 0 16px;border-left:3px solid #94DAB1;'), 'width="100%"'), INK, True))
parts.append(section('03 / MAŽI EKSPERIMENTAI', 'Kai spalvos nustebina.', 'Raštai ant vandens ir vitražinės dekoracijos langui.'))
parts.append(grid(PRODUCTS[6:]))
parts.append(feature('RYTOJAUS IDĖJA', 'Sukurkite mini parodą.', p('Išsirinkite tris šios savaitės darbelius, sugalvokite jiems pavadinimus ir surenkite parodą namuose.', '0', 16), '#FFE8D8'))
parts.append(row(p('Kūrybai nereikia tobulo rezultato. Užtenka smalsumo pradėti.') + p('Su meile,<br><strong>Ingrida</strong>', '0'), 'padding:4px 24px 30px;'))
parts.append(row(f'<h2 style="margin:0 0 22px;font-family:{FONT};font-size:28px;line-height:35px;font-weight:700;color:{MINT};">Ką šiandien<br>sukursite kartu?</h2>' + button('Atrasti kūrybos priemones', CATEGORY + UTM, True), f'padding:34px 22px;background-color:{INK};', f'align="center" bgcolor="{INK}"'))

footer = p(f'<a href="{esc("https://www.skilsas.lt/" + UTM)}" style="color:{MINT};text-decoration:none;">skilsas.lt</a>&nbsp; · &nbsp;<a href="https://www.facebook.com/skilsaslietuva" style="color:{MINT};text-decoration:none;">Facebook</a>&nbsp; · &nbsp;<a href="https://www.instagram.com/skilsas.lt/" style="color:{MINT};text-decoration:none;">Instagram</a>', '0 0 16px', 13, MINT)
footer += p('MB SKILSAS<br>S. Stanevičiaus g. 61, LT-07114 Vilnius', '0 0 12px', 11, '#C6DCD3')
footer += p('Šį laišką gavote, nes užsisakėte SKILSAS naujienas.', '0 0 12px', 11, '#C6DCD3')
footer += p('<a href="https://www.skilsas.lt/privatumo-politika" style="color:#C6DCD3;">Privatumas</a>&nbsp; · &nbsp;<a href="[[preference_link]]" style="color:#C6DCD3;">Keisti nuostatas</a>&nbsp; · &nbsp;<a href="[[unsubscribe_link]]" style="color:#C6DCD3;">Atsisakyti naujienų</a>', '0', 11, '#C6DCD3')
parts.append(row(table(row(footer, 'padding-top:22px;border-top:1px solid #477769;', 'align="center"'), 'width="100%"'), f'padding:0 22px 30px;background-color:{INK};', f'align="center" bgcolor="{INK}"'))

content = table(''.join(parts), 'class="wrap" width="600" bgcolor="#E5FCEF" style="width:100%;max-width:600px;table-layout:fixed;background-color:#E5FCEF;"')
doc = '''<!doctype html>
<html lang="lt" xmlns:o="urn:schemas-microsoft-com:office:office">
<head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="x-apple-disable-message-reformatting"><meta name="format-detection" content="telephone=no,address=no,email=no,date=no"><meta name="color-scheme" content="light"><title>Kai lauke lyja, namuose kuriam.</title>
<!--[if mso]><noscript><xml><o:OfficeDocumentSettings><o:PixelsPerInch>96</o:PixelsPerInch></o:OfficeDocumentSettings></xml></noscript><![endif]-->
<style>
@font-face{font-family:Montserrat;font-weight:400;src:url('assets/brand/Montserrat-Regular.ttf') format('truetype');}
@font-face{font-family:Montserrat;font-weight:700;src:url('assets/brand/Montserrat-Bold.ttf') format('truetype');}
body{margin:0!important;padding:0!important;-webkit-text-size-adjust:100%;-ms-text-size-adjust:100%;}
table{border-spacing:0;mso-table-lspace:0pt;mso-table-rspace:0pt;}
img{border:0;outline:none;text-decoration:none;-ms-interpolation-mode:bicubic;}
a[x-apple-data-detectors]{color:inherit!important;text-decoration:none!important;}
@media screen and (min-width:481px){.hero-title{font-size:46px!important;line-height:52px!important;}}
@media screen and (max-width:599px){.product-column{max-width:100%!important;}.product-title-cell,.product-desc-cell{height:auto!important;}}
</style>
<!--[if mso]><style>body,table,td,p,a,h1,h2,h3{font-family:Arial,sans-serif!important;}</style><![endif]-->
</head><body style="margin:0;padding:0;background-color:#EDF3ED;">
'''
doc += f'<div style="display:none;font-size:1px;line-height:1px;max-height:0;max-width:0;opacity:0;overflow:hidden;mso-hide:all;">{PREHEADER}</div>'
doc += table(row('<!--[if mso]><table role="presentation" width="600" cellpadding="0" cellspacing="0" border="0"><tr><td><![endif]-->' + content + '<!--[if mso]></td></tr></table><![endif]-->', '', 'align="center"'), 'width="100%" bgcolor="#EDF3ED"') + '</body></html>\n'

(ROOT / 'preview.html').write_text(doc)
(ROOT / 'newsletter.html').write_text(doc.replace('src="assets/', f'src="{PUBLIC}assets/').replace("url('assets/", f"url('{PUBLIC}assets/"))

text = [f'TEMA: {SUBJECT}', f'PREHEADER: {PREHEADER}', '', 'Kai lauke lyja, namuose kuriam.', '8 idėjos spalvotai popietei be ekranų.', '', 'Labas!', 'Kai už lango pilka, ant stalo gali atsirasti visas spalvotas pasaulis. Šiai popietei atrinkau priemones, kurios kviečia piešti, spalvinti ir išbandyti ką nors naujo.', '', 'KŪRYBOS PRADŽIA – Trys maži žingsniai.']
for index, (title, desc) in enumerate(STARTERS, 1):
    text.append(f'{index}. {title}: {desc}')
text.extend(['', '01 / ŠVIESA IR LINIJA – Nuo pirmo brūkšnio.', 'Pieškite, kopijuokite arba kurkite visai be taisyklių.', ''])
for index, (key, label, title, desc) in enumerate(PRODUCTS):
    if index == 3:
        text.extend(['02 / SPALVOS ANT POPIERIAUS – Daug vietos fantazijai.', 'Kreidelės, didelis rulonas ir akvarelė su dinozaurais.', ''])
    if index == 6:
        text.extend(['PABANDYKITE KARTU – Tik trys spalvos.', 'Išsirinkite tris spalvas ir pabandykite visą piešinį sukurti tik jomis.', 'Kokią nuotaiką jos sukūrė?', '', '03 / MAŽI EKSPERIMENTAI – Kai spalvos nustebina.', 'Raštai ant vandens ir vitražinės dekoracijos langui.', ''])
    text.extend([f'{label} | {title} – {price(key)}', desc, product_url(key), ''])
text.extend(['RYTOJAUS IDĖJA – Sukurkite mini parodą.', 'Išsirinkite tris šios savaitės darbelius, sugalvokite jiems pavadinimus ir surenkite parodą namuose.', '', 'Kūrybai nereikia tobulo rezultato. Užtenka smalsumo pradėti.', '', 'Su meile,', 'Ingrida', '', 'Atrasti kūrybos priemones:', CATEGORY + UTM, '', 'MB SKILSAS | S. Stanevičiaus g. 61, LT-07114 Vilnius', 'Šį laišką gavote, nes užsisakėte SKILSAS naujienas.', 'Privatumas: https://www.skilsas.lt/privatumo-politika', 'Keisti nuostatas: [[preference_link]]', 'Atsisakyti naujienų: [[unsubscribe_link]]'])
(ROOT / 'newsletter.txt').write_text('\n'.join(text) + '\n')

subjects = '''# SKILSAS · 10.06 · Temos ir preheaderiai

**Rekomenduojama tema:** Kai lauke lyja, namuose kuriam 🎨

**Preheaderis:** 8 kūrybos idėjos rudens popietei: piešti, spalvinti ir eksperimentuoti.

| Variantas | Subject line | Preheader |
| --- | --- | --- |
| A · sezonas | Kai lauke lyja, namuose kuriam 🎨 | 8 kūrybos idėjos rudens popietei: piešti, spalvinti ir eksperimentuoti. |
| B · smalsumas | O jeigu šiandien lapė nušvistų? ✨ | LED piešimo lentos, kreidelės ir spalvingi eksperimentai. |
| C · emocija | Mažos rankos. Didelės idėjos. | Priemonės kūrybos popietei, kurioje taisykles kuria vaikas. |
| D · atranka | 8 idėjos spalvotai rudens popietei | Nuo pirmo brūkšnio iki raštų ant vandens. |
| E · bendras laikas | Šiandien kuriame kartu 🎨 | Išsirinkite priemonę, tris spalvas ir pradėkite. |

A/B bandymui siūlomi A ir B su tuo pačiu A preheaderiu.
'''
(ROOT / 'subject-lines.md').write_text(subjects)

print(json.dumps({'products': len(PRODUCTS), 'html_bytes': len(doc.encode()), 'subject': SUBJECT}, ensure_ascii=False))
