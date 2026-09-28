from pathlib import Path
import html, json

ROOT = Path(__file__).resolve().parent
SOURCE = json.loads((ROOT / 'sources/products-2026-09-28.json').read_text())
FONT = 'Montserrat,Arial,sans-serif'
GREEN, MINT, INK = '#188348', '#E5FCEF', '#104C3E'
UTM = '?utm_source=omnisend&utm_medium=email&utm_campaign=skilsas_mazos_rankos_dideles_idejos'
PUBLIC = 'https://raw.githubusercontent.com/elaiskai/skilsas-email-assets/555185a195bfeafd7ec59875550651f667c7c3c4/campaigns/2026-09-28/mazos-rankos-dideles-idejos/'
SUBJECT = 'Mažos rankos. Didelės idėjos. 🎨'
PREHEADER = '8 idėjos kūrybos popietei: nuo šviečiančių piešinių iki spalvų ant vandens.'
PRODUCTS = [
    ('led-holder', 'SKILSAS', 'LED lenta su markerių laikikliu', 'Šviečianti piešimo lenta, kurioje markeriai turi savo vietą.'),
    ('led', 'SKILSAS', 'LED piešimo lenta', 'Skaidrus piešimo paviršius, kuriame spalvotos linijos nušvinta.'),
    ('draw', 'SKILSAS · LIETUVIŠKAI', '„Mokausi piešti“', '100 dvipusių kortelių su piešimo žingsniais ir lietuvišku įgarsinimu.'),
    ('crayons', 'TOOKYLAND · NUO 3 M.', '24 spalvų kreidelės', 'Išsukamos šilkinės kreidelės – spalvinti minkštai ir ryškiai.'),
    ('roll', 'TOOKYLAND · NUO 3 M.', '„Gyvūnų pasaulis“', 'Didelis spalvinimo rulonas, kurį smagu ištiesti ir spalvinti kartu.'),
    ('dino', 'TOOKYLAND · NUO 5 M.', 'Akvarelė „Dinozaurai“', '26 piešiniai su spalvų palete puslapyje. Tereikia vandens.'),
    ('marble', 'TOOKYLAND · NUO 6 M.', 'Marmuravimo rinkinys', '12 spalvų raštams ant vandens kurti ir perkelti ant popieriaus.'),
    ('windows', 'TOOKYLAND · NUO 6 M.', '„Kosmoso pasaulis“', '12 vitražinių formelių spalvinti ir papuošti langą.'),
]

def esc(s): return html.escape(str(s), quote=True)
def url(key): return SOURCE[key]['offers']['url'] + UTM
def price(key):
    v = SOURCE[key]['offers']['price']
    return (str(int(v)) if v == int(v) else f'{v:.2f}'.replace('.', ',')) + ' €'
def table(body, extra=''):
    return f'<table role="presentation" cellpadding="0" cellspacing="0" border="0" {extra}>{body}</table>'
def row(body, style='', extra=''):
    return f'<tr><td {extra} style="{style}">{body}</td></tr>\n'
def p(text, margin='0 0 16px', size=17, color=INK, cls=''):
    return f'<p class="{cls}" style="margin:{margin};font-family:{FONT};font-size:{size}px;line-height:{round(size*1.5)}px;color:{color};">{text}</p>'
def eyebrow(text):
    return f'<p style="margin:0 0 10px;font-family:{FONT};font-size:11px;line-height:17px;letter-spacing:1px;font-weight:700;color:{GREEN};">{text}</p>'
def heading(text):
    return f'<h2 style="margin:0 0 12px;font-family:{FONT};font-size:28px;line-height:35px;color:{INK};font-weight:700;">{text}</h2>'
def button(text, href, inverse=False):
    bg, fg = (MINT, INK) if inverse else (GREEN, '#FFFFFF')
    return table(row(f'<a href="{esc(href)}" style="display:inline-block;padding:14px 20px;border:1px solid {bg};border-radius:28px;font-family:{FONT};font-size:15px;line-height:22px;font-weight:700;text-decoration:none;color:{fg};">{text}&nbsp; →</a>', f'background-color:{bg};border-radius:28px;mso-padding-alt:14px 20px;', f'align="center" bgcolor="{bg}"'))
def section(label, title):
    return row(eyebrow(label)+heading(title), 'padding:20px 24px 20px;')
def card(product):
    key, label, title, desc = product
    a = esc(url(key))
    image = f'<a href="{a}"><img src="assets/products/{key}.jpg" width="92" height="92" alt="{esc(SOURCE[key]["name"])}" style="display:block;width:92px;max-width:100%;height:auto;border:0;border-radius:12px;"></a>'
    title_html = f'<p style="margin:0 0 6px;font-family:{FONT};font-size:10px;line-height:15px;letter-spacing:0.35px;font-weight:700;color:{GREEN};">{label}</p><h3 style="margin:0;font-family:{FONT};font-size:18px;line-height:24px;font-weight:700;color:{INK};">{title}</h3>'
    top = table(f'<tr><td width="108" valign="middle" style="width:108px;padding:0;">{image}</td><td valign="middle" style="padding:0;text-align:left;word-break:normal;">{title_html}</td></tr>', 'width="100%" style="width:100%;table-layout:fixed;"')
    desc_html = p(desc, '14px 0 16px',16,cls='product-description')
    cta = f'<a href="{a}" style="display:inline-block;padding:10px 14px;background-color:{GREEN};border:1px solid {GREEN};border-radius:22px;font-family:{FONT};font-size:14px;line-height:20px;font-weight:700;text-decoration:none;color:#FFFFFF;white-space:nowrap;">Apžiūrėti&nbsp;→</a>'
    bottom = table(f'<tr><td width="40%" valign="middle" style="padding:0;font-family:{FONT};font-size:23px;line-height:30px;font-weight:700;color:{INK};white-space:nowrap;">{price(key).replace(" ", "&nbsp;")}</td><td width="60%" align="right" valign="middle" style="padding:0;">{cta}</td></tr>', 'width="100%" style="width:100%;table-layout:fixed;"')
    return row(table(row(top+desc_html+bottom,'padding:20px;'),'class="product-card" width="100%" bgcolor="#FFFFFF" style="width:100%;background-color:#FFFFFF;border-radius:22px;table-layout:fixed;"'),'padding:0 18px 16px;')

parts=[]
parts.append(row(f'<a href="{esc("https://www.skilsas.lt/"+UTM)}"><img src="assets/brand/logo.png" width="112" height="65" alt="SKILSAS" style="display:block;width:112px;height:auto;border:0;"></a>','padding:24px 24px 20px;','align="center"'))
parts.append(row(eyebrow('ŠIANDIEN KURIAME KARTU')+f'<h1 class="hero-title" style="margin:0 0 16px;font-family:{FONT};font-size:34px;line-height:41px;font-weight:700;letter-spacing:-1px;color:{INK};">Mažos rankos.<br>Didelės idėjos.</h1>'+p('O jeigu šiandien saulė būtų žalia?','0',18),'padding:4px 20px 24px;','align="center"'))
parts.append(row(f'<a href="{esc(url("led-holder"))}"><img src="assets/campaign/hero.jpg" width="564" height="564" alt="SKILSAS LED piešimo lenta su markerių laikikliu ir spalvotu dinozauro piešiniu" style="display:block;width:100%;height:auto;border:1px solid #BCDCCB;border-radius:24px;box-sizing:border-box;"></a>','padding:0 18px;font-size:0;line-height:0;'))
parts.append(row(eyebrow('PIEŠINIAI, KURIE NUŠVINTA')+heading('LED lenta su<br>markerių laikikliu')+p('Spalvotos linijos šviečia, o markeriai laukia savo vietose.','0 0 14px',16)+f'<p style="margin:0 0 18px;font-family:{FONT};font-size:30px;line-height:38px;font-weight:700;color:{INK};">{price("led-holder")}</p>'+button('Apžiūrėti LED lentą',url('led-holder')),'padding:24px 24px 32px;','align="center"'))
parts.append(row(p('<strong>Labas!</strong>')+p('Piešiniui nebūtina būti panašiam į tikrą pasaulį. Jame gali gyventi violetinis dinozauras, žalia saulė ir namas iki debesų.')+p('Atrinkau 8 priemones tokioms idėjoms: piešti, spalvinti ir išbandyti ką nors naujo. Tegul šiandien spalvas renkasi vaikas.','0'),'padding:0 24px 20px;'))
parts.append(section('01 / PIEŠTI SAVO PASAULĮ','Nuo pirmos linijos.'))
parts.extend(card(x) for x in PRODUCTS[1:3])
parts.append(section('02 / PRIPILDYTI SPALVŲ','Ant lapo telpa tiek daug.'))
parts.extend(card(x) for x in PRODUCTS[3:6])
parts.append(section('03 / IŠBANDYTI KĄ NORS NAUJO','O dabar – mažas eksperimentas.'))
parts.extend(card(x) for x in PRODUCTS[6:])
idea=eyebrow('MAŽA IDĖJA ŠIAI POPIETEI')+p('<strong>Nupieškite gyvūną, kurio dar niekas nematė.</strong> Tada kartu sugalvokite jo vardą ir tai, ką jis labiausiai mėgsta.','0',16)
parts.append(row(table(row(idea,'padding:24px;'),'width="100%" bgcolor="#D4EFDE" style="background-color:#D4EFDE;border-radius:20px;table-layout:fixed;"'),'padding:8px 18px 24px;'))
parts.append(row(p('Smagiausia dalis? Pamatyti, ką vaikas sugalvos pats.')+p('Su meile,<br><strong>Ingrida</strong>','0'),'padding:0 24px 30px;'))
parts.append(row(f'<h2 style="margin:0 0 22px;font-family:{FONT};font-size:28px;line-height:35px;font-weight:700;color:{MINT};">Ką šiandien<br>sukursite kartu?</h2>'+button('Daugiau kūrybos idėjų','https://www.skilsas.lt/lavinamosios-priemones/spalvinimui-ir-kurybai'+UTM,True),f'padding:34px 22px;background-color:{INK};',f'align="center" bgcolor="{INK}"'))
footer=p(f'<a href="{esc("https://www.skilsas.lt/"+UTM)}" style="color:{MINT};text-decoration:none;">skilsas.lt</a>&nbsp; · &nbsp;<a href="https://www.facebook.com/skilsaslietuva" style="color:{MINT};text-decoration:none;">Facebook</a>&nbsp; · &nbsp;<a href="https://www.instagram.com/skilsas.lt/" style="color:{MINT};text-decoration:none;">Instagram</a>','0 0 16px',13,MINT)
footer+=p('MB SKILSAS<br>S. Stanevičiaus g. 61, LT-07114 Vilnius','0 0 12px',11,'#C6DCD3')+p('Šį laišką gavote, nes užsisakėte SKILSAS naujienas.','0 0 12px',11,'#C6DCD3')
footer+=p('<a href="https://www.skilsas.lt/privatumo-politika" style="color:#C6DCD3;">Privatumas</a>&nbsp; · &nbsp;<a href="[[preference_link]]" style="color:#C6DCD3;">Keisti nuostatas</a>&nbsp; · &nbsp;<a href="[[unsubscribe_link]]" style="color:#C6DCD3;">Atsisakyti naujienų</a>','0',11,'#C6DCD3')
parts.append(row(table(row(footer,'padding-top:22px;border-top:1px solid #477769;','align="center"'),'width="100%"'),f'padding:0 22px 30px;background-color:{INK};',f'align="center" bgcolor="{INK}"'))
content=table(''.join(parts),'class="wrap" width="600" bgcolor="#E5FCEF" style="width:100%;max-width:600px;table-layout:fixed;background-color:#E5FCEF;"')
doc='''<!doctype html>
<html lang="lt" xmlns:o="urn:schemas-microsoft-com:office:office">
<head><meta charset="UTF-8"><meta name="viewport" content="width=device-width,initial-scale=1"><meta name="x-apple-disable-message-reformatting"><meta name="format-detection" content="telephone=no,address=no,email=no,date=no"><meta name="color-scheme" content="light"><title>Mažos rankos. Didelės idėjos.</title>
<!--[if mso]><noscript><xml><o:OfficeDocumentSettings><o:PixelsPerInch>96</o:PixelsPerInch></o:OfficeDocumentSettings></xml></noscript><![endif]-->
<style>
@font-face{font-family:Montserrat;font-weight:400;src:url('assets/brand/Montserrat-Regular.ttf') format('truetype');}
@font-face{font-family:Montserrat;font-weight:700;src:url('assets/brand/Montserrat-Bold.ttf') format('truetype');}
body{margin:0!important;padding:0!important;-webkit-text-size-adjust:100%;-ms-text-size-adjust:100%;}
table{border-spacing:0;mso-table-lspace:0pt;mso-table-rspace:0pt;}
img{border:0;outline:none;text-decoration:none;-ms-interpolation-mode:bicubic;}
a[x-apple-data-detectors]{color:inherit!important;text-decoration:none!important;}
@media screen and (min-width:481px){.hero-title{font-size:46px!important;line-height:52px!important;}}
</style>
<!--[if mso]><style>body,table,td,p,a,h1,h2,h3{font-family:Arial,sans-serif!important;}</style><![endif]-->
</head><body style="margin:0;padding:0;background-color:#EDF3ED;">
'''
doc+=f'<div style="display:none;font-size:1px;line-height:1px;max-height:0;max-width:0;opacity:0;overflow:hidden;mso-hide:all;">{PREHEADER}</div>'
doc+=table(row('<!--[if mso]><table role="presentation" width="600" cellpadding="0" cellspacing="0" border="0"><tr><td><![endif]-->'+content+'<!--[if mso]></td></tr></table><![endif]-->','','align="center"'),'width="100%" bgcolor="#EDF3ED"')+'</body></html>\n'
(ROOT/'preview.html').write_text(doc)
(ROOT/'newsletter.html').write_text(doc.replace('src="assets/',f'src="{PUBLIC}assets/').replace("url('assets/",f"url('{PUBLIC}assets/"))
text=[f'TEMA: {SUBJECT}',f'PREHEADER: {PREHEADER}','','Mažos rankos. Didelės idėjos.','O jeigu šiandien saulė būtų žalia?','','Labas!','Piešiniui nebūtina būti panašiam į tikrą pasaulį. Jame gali gyventi violetinis dinozauras, žalia saulė ir namas iki debesų.','Atrinkau 8 priemones tokioms idėjoms: piešti, spalvinti ir išbandyti ką nors naujo. Tegul šiandien spalvas renkasi vaikas.','']
for key,label,title,desc in PRODUCTS: text.extend([f'{label} | {title} – {price(key)}',desc,url(key),''])
text.extend(['Maža idėja šiai popietei:','Nupieškite gyvūną, kurio dar niekas nematė. Tada kartu sugalvokite jo vardą ir tai, ką jis labiausiai mėgsta.','','Smagiausia dalis? Pamatyti, ką vaikas sugalvos pats.','','Su meile,','Ingrida','','Daugiau kūrybos idėjų:','https://www.skilsas.lt/lavinamosios-priemones/spalvinimui-ir-kurybai'+UTM,'','MB SKILSAS | S. Stanevičiaus g. 61, LT-07114 Vilnius','Šį laišką gavote, nes užsisakėte SKILSAS naujienas.','Privatumas: https://www.skilsas.lt/privatumo-politika','Keisti nuostatas: [[preference_link]]','Atsisakyti naujienų: [[unsubscribe_link]]'])
(ROOT/'newsletter.txt').write_text('\n'.join(text)+'\n')
(ROOT/'subject-lines.md').write_text('''# Temos ir preheaderiai

**Rekomenduojama tema:** Mažos rankos. Didelės idėjos. 🎨

**Preheaderis:** 8 idėjos kūrybos popietei: nuo šviečiančių piešinių iki spalvų ant vandens.

| Variantas | Subject line | Preheader |
| --- | --- | --- |
| A · emocija | Mažos rankos. Didelės idėjos. 🎨 | 8 idėjos kūrybos popietei: nuo šviečiančių piešinių iki spalvų ant vandens. |
| B · smalsumas | O jeigu šiandien saulė būtų žalia? | Piešimo lentos, kreidelės ir kūrybiniai rinkiniai mažųjų fantazijai. |
| C · produktas | Piešiniai, kurie nušvinta ✨ | Atraskite SKILSAS LED lentas ir dar daugiau priemonių kūrybai. |
| D · atranka | 8 idėjos mažųjų kūrybos popietei | Nuo pirmos linijos iki spalvingo eksperimento – išsirinkite savo. |
| E · bendras laikas | Šiandien kuriame kartu 🎨 | Ištieskite spalvinimo ruloną, atsiverskite akvarelę ar įjunkite LED lentą. |

A/B bandymui siūlomi A ir B su tuo pačiu A preheaderiu, kad skirtųsi tik tema. Siuntimo data dar neparinkta.
''')
print(json.dumps({'products':len(PRODUCTS),'html_bytes':len(doc.encode()),'subject':SUBJECT},ensure_ascii=False))
