#!/usr/bin/env python3
"""Generate 13 new blog articles × 4 languages for mexvisapro.com"""
import os, json

BASE = "/home/olek/immigration-site"
WA = "529987583392"

CSS = """
    :root{--gold:#f0a500;--dark:#0b1120;--navy:#1a2744;--bg:#f7f8fc}
    *{margin:0;padding:0;box-sizing:border-box}
    html{scroll-behavior:smooth}
    body{font-family:Inter,system-ui,sans-serif;color:#1e1e2d;background:#fff;overflow-x:hidden}
    .nav-bar{background:#fff;border-bottom:1px solid #eee;padding:.7rem 0;position:sticky;top:0;z-index:100;box-shadow:0 1px 8px rgba(0,0,0,.04)}
    .nav-bar .brand{font-weight:800;font-size:1.25rem;color:var(--dark);text-decoration:none}
    .nav-bar .brand span{color:var(--gold)}
    .nav-links a{color:#555;text-decoration:none;font-size:.85rem;font-weight:500}
    .nav-links a:hover{color:var(--gold)}
    .nav-wa{background:var(--gold);color:#fff!important;padding:.4rem .9rem;border-radius:8px;font-weight:600;font-size:.8rem}
    .lang-btns{display:flex;gap:2px}
    .lang-btn{display:inline-block;padding:3px 8px;border-radius:4px;font-size:.7rem;font-weight:700;color:#888;background:#f0f0f0;text-decoration:none;transition:all .2s}
    .lang-btn:hover,.lang-btn.active{color:#fff;background:var(--gold)}
    .nav-wa:hover{background:#d4940a;color:#fff!important}
    .article-hero{padding:4rem 0 2.5rem;background:linear-gradient(135deg,var(--dark) 0%,var(--navy) 60%,#0d3b66 100%);position:relative;overflow:hidden}
    .article-hero::before{content:"";position:absolute;top:-40%;right:-15%;width:500px;height:500px;background:radial-gradient(circle,rgba(240,165,0,.1) 0%,transparent 70%);border-radius:50%}
    .article-hero *{position:relative;z-index:1}
    .article-hero .crumb{font-size:.8rem;margin-bottom:.8rem}
    .article-hero .crumb a{color:var(--gold);text-decoration:none}
    .article-hero .crumb span{color:rgba(255,255,255,.4)}
    .article-hero h1{font-size:2.2rem;font-weight:900;color:#fff;line-height:1.25;max-width:720px}
    .article-hero .lead-text{color:rgba(255,255,255,.65);font-size:1rem;max-width:600px;margin-top:.7rem;line-height:1.6}
    .article-meta{font-size:.8rem;color:rgba(255,255,255,.45);margin-top:1rem;display:flex;gap:1.2rem;flex-wrap:wrap}
    .article-body{max-width:760px;margin:0 auto;padding:2.5rem 1.2rem 3rem}
    .article-body h2{font-size:1.45rem;font-weight:800;color:#1e1e2d;margin:2.5rem 0 .8rem;padding-top:1.5rem;border-top:2px solid #f0f0f0}
    .article-body h3{font-size:1.1rem;font-weight:700;color:var(--dark);margin:1.5rem 0 .6rem;padding-left:.8rem;border-left:3px solid var(--gold)}
    .article-body p{font-size:1rem;line-height:1.8;color:#444;margin-bottom:1.2rem}
    .article-body ul,.article-body ol{margin:1rem 0 1.5rem 1.5rem;color:#444}
    .article-body li{margin-bottom:.5rem;line-height:1.7;font-size:.95rem}
    .article-body strong{color:#1e1e2d}
    .article-body a{color:var(--gold);text-decoration:underline}
    .article-body a:hover{color:#d4940a}
    .info-box{background:#fff8e6;border-left:4px solid var(--gold);padding:1.2rem 1.4rem;border-radius:0 12px 12px 0;margin:1.5rem 0}
    .info-box p{margin:0;font-size:.92rem;color:#555;line-height:1.6}
    .info-box strong{color:#1e1e2d}
    .cta-box{background:linear-gradient(135deg,var(--dark),var(--navy));border-radius:16px;padding:2.5rem;text-align:center;margin:2.5rem 0}
    .cta-box h3{color:#fff;font-size:1.3rem;margin-bottom:.4rem;font-weight:800}
    .cta-box p{color:rgba(255,255,255,.65);margin-bottom:1.2rem;font-size:.9rem}
    .btn-gold{background:linear-gradient(135deg,var(--gold),#d4940a);color:#fff;font-weight:700;border:none;padding:.7rem 1.6rem;border-radius:10px;font-size:.95rem;text-decoration:none;display:inline-block;box-shadow:0 4px 15px rgba(240,165,0,.35)}
    .btn-gold:hover{color:#fff;transform:translateY(-2px);box-shadow:0 6px 20px rgba(240,165,0,.45)}
    footer{background:var(--dark);padding:2rem 0;text-align:center;color:rgba(255,255,255,.45);font-size:.8rem}
    footer a{color:var(--gold);text-decoration:none}
    @media(max-width:768px){.article-hero h1{font-size:1.7rem}.article-hero{padding:3rem 0 2rem}.article-body{padding:2rem 1rem}}
    .mobile-toggle{display:none;background:none;border:none;color:var(--dark);font-size:1.5rem;cursor:pointer;padding:4px}
    .mobile-menu{display:none}@media(max-width:767.98px){.mobile-toggle{display:block}.nav-links .desk-link,.nav-links .lang-btns{display:none!important}.mobile-menu{display:none;position:fixed;top:0;left:0;right:0;bottom:0;background:rgba(11,17,32,.97);z-index:200;flex-direction:column;align-items:center;justify-content:center;gap:1.5rem}.mobile-menu.open{display:flex}.mobile-menu a{color:#fff;font-size:1.2rem;text-decoration:none;font-weight:600}.mobile-menu a:hover{color:var(--gold)}.mobile-menu .close-btn{position:absolute;top:1rem;right:1.5rem;background:none;border:none;color:#fff;font-size:2rem;cursor:pointer}.mobile-menu .lang-row{display:flex;gap:6px}}
"""

LANG_LABELS = {
    'en': {'home':'Home','services':'Services','blog':'Blog','partners':'Partners','consult':'Consult Free','date':'June 6, 2026','min':'min read','team':'MexVisa Pro Team','related':'Related Articles','wa_text':'Hi! Free consultation please'},
    'es': {'home':'Inicio','services':'Servicios','blog':'Blog','partners':'Socios','consult':'Consulta Gratis','date':'6 junio, 2026','min':'min de lectura','team':'Equipo MexVisa Pro','related':'Artículos Relacionados','wa_text':'Hola! Consulta gratis por favor'},
    'ru': {'home':'Главная','services':'Услуги','blog':'Блог','partners':'Партнёры','consult':'Бесплатно','date':'6 июня, 2026','min':'мин чтения','team':'Команда MexVisa Pro','related':'Похожие статьи','wa_text':'Привет! Бесплатная консультация'},
    'zh': {'home':'首页','services':'服务','blog':'博客','partners':'合作伙伴','consult':'免费咨询','date':'2026年6月6日','min':'分钟阅读','team':'MexVisa Pro团队','related':'相关文章','wa_text':'你好！免费咨询'},
}

LANG_PREFIXES = {'en':'','es':'/es','ru':'/ru','zh':'/zh'}
LANG_BLOG = {'en':'/blog','es':'/es/blog','ru':'/ru/blog','zh':'/zh/blog'}

def html(lang, slug, d):
    lbl = LANG_LABELS[lang]
    pfx = LANG_PREFIXES[lang]
    blog_pfx = LANG_BLOG[lang]
    slugs = d['slugs']
    sl = slugs[lang]
    en_sl = slugs['en']

    hreflang = '\n'.join(
        [f'  <link rel="alternate" hreflang="{lg}" href="https://mexvisapro.com{LANG_BLOG[lg]}/{slugs[lg]}/">' for lg in ['en','es','ru','zh']] +
        [f'  <link rel="alternate" hreflang="x-default" href="https://mexvisapro.com/blog/{en_sl}/">']
    )

    faq_schema = json.dumps({"@context":"https://schema.org","@type":"FAQPage","mainEntity":[
        {"@type":"Question","name":q,"acceptedAnswer":{"@type":"Answer","text":a}}
        for q,a in d['faq'][lang]
    ]}, ensure_ascii=False)

    mobile_menu_home = f'{pfx}/' if pfx else '/'
    mobile_home_link = f'/en/' if lang == 'en' else f'{pfx}/'

    nav_links = f'''
      <a href="{mobile_home_link}" class="d-none d-md-inline">{lbl['home']}</a>
      <a href="{pfx}/#services" class="d-none d-md-inline">{lbl['services']}</a>
      <a href="{blog_pfx}/" style="color:var(--gold);font-weight:700">{lbl['blog']}</a>
      <a href="{pfx}/partners/" class="d-none d-md-inline" style="color:#f0a500;font-weight:700"><i class="bi bi-people-fill me-1"></i>{lbl['partners']}</a>
      <div class="lang-btns d-none d-md-flex gap-1">
        <a href="/blog/{en_sl}/" class="lang-btn{"" if lang!="en" else " active"}">EN</a>
        <a href="/es/blog/{slugs["es"]}/" class="lang-btn{"" if lang!="es" else " active"}">ES</a>
        <a href="/ru/blog/{slugs["ru"]}/" class="lang-btn{"" if lang!="ru" else " active"}">RU</a>
        <a href="/zh/blog/{slugs["zh"]}/" class="lang-btn{"" if lang!="zh" else " active"}">ZH</a>
      </div>
      <button class="mobile-toggle" onclick="document.getElementById('mobileMenu').classList.add('open')" aria-label="Menu"><i class="bi bi-list"></i></button>
      <a href="https://wa.me/{WA}?text={lbl['wa_text'].replace(' ','%20')}" target="_blank" rel="noopener" class="nav-wa"><i class="bi bi-whatsapp me-1"></i>{lbl['consult']}</a>'''

    related_links = '\n'.join([f'    <li><a href="{LANG_BLOG[lang]}/{r}/">{t}</a></li>' for r,t in d.get('related',{}).get(lang,[])])

    return f'''<!DOCTYPE html>
<html lang="{lang}">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-Content-Type-Options" content="nosniff">
  <meta http-equiv="X-Frame-Options" content="DENY">
  <title>{d['title'][lang]}</title>
  <meta name="description" content="{d['desc'][lang]}">
  <meta name="author" content="MexVisa Pro">
  <meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1">
  <meta name="theme-color" content="#f0a500">
  <link rel="icon" href="/favicon.ico" sizes="32x32">
  <link rel="icon" type="image/png" sizes="192x192" href="/assets/img/icon-192.png">
  <link rel="apple-touch-icon" href="/assets/img/apple-touch-icon.png">
  <link rel="canonical" href="https://mexvisapro.com{blog_pfx}/{sl}/">
  {hreflang}
  <meta property="og:title" content="{d['title'][lang]}">
  <meta property="og:description" content="{d['desc'][lang]}">
  <meta property="og:type" content="article">
  <meta property="og:url" content="https://mexvisapro.com{blog_pfx}/{sl}/">
  <meta property="og:site_name" content="MexVisa Pro">
  <meta property="og:image" content="https://mexvisapro.com/assets/img/og-image.png">
  <meta property="article:published_time" content="2026-06-06T00:00:00-05:00">
  <meta property="article:modified_time" content="2026-06-06T00:00:00-05:00">
  <meta name="twitter:card" content="summary_large_image">
  <meta name="twitter:title" content="{d['title'][lang]}">
  <meta name="twitter:description" content="{d['desc'][lang]}">
  <script type="application/ld+json">
  {{"@context":"https://schema.org","@type":"Article","headline":"{d['h1'][lang]}","url":"https://mexvisapro.com{blog_pfx}/{sl}/","datePublished":"2026-06-06","dateModified":"2026-06-06","author":{{"@type":"Organization","name":"MexVisa Pro","url":"https://mexvisapro.com"}},"publisher":{{"@type":"Organization","name":"MexVisa Pro","logo":{{"@type":"ImageObject","url":"https://mexvisapro.com/assets/img/icon-512.png"}}}},"inLanguage":"{lang}","timeRequired":"PT8M"}}
  </script>
  <script type="application/ld+json">
  {{"@context":"https://schema.org","@type":"BreadcrumbList","itemListElement":[{{"@type":"ListItem","position":1,"name":"{lbl['home']}","item":"https://mexvisapro.com{pfx}/"}},{{"@type":"ListItem","position":2,"name":"{lbl['blog']}","item":"https://mexvisapro.com{blog_pfx}/"}},{{"@type":"ListItem","position":3,"name":"{d['breadcrumb'][lang]}","item":"https://mexvisapro.com{blog_pfx}/{sl}/"}}]}}
  </script>
  <script type="application/ld+json">
  {faq_schema}
  </script>
  <link rel="preconnect" href="https://cdn.jsdelivr.net" crossorigin>
  <link rel="preconnect" href="https://fonts.googleapis.com" crossorigin>
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <style>{CSS}</style>
  <link href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" rel="stylesheet">
  <link rel="preload" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css" as="style" onload="this.onload=null;this.rel='stylesheet'">
  <noscript><link href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css" rel="stylesheet"></noscript>
  <link href="https://fonts.googleapis.com/css2?family=Inter:wght@400;500;600;700;800;900&display=swap" rel="stylesheet">
</head>
<body>
<nav class="nav-bar">
  <div class="container d-flex align-items-center justify-content-between">
    <a class="brand" href="{pfx}/"><i class="bi bi-globe-americas me-2"></i>MexVisa<span>Pro</span></a>
    <div class="nav-links d-flex align-items-center gap-3">{nav_links}
    </div>
  </div>
</nav>
<section class="article-hero">
  <div class="container">
    <div class="crumb"><a href="{pfx}/">{lbl['home']}</a> <span>›</span> <a href="{blog_pfx}/">{lbl['blog']}</a> <span>›</span> <span style="color:rgba(255,255,255,.6)">{d['breadcrumb'][lang]}</span></div>
    <h1>{d['h1'][lang]}</h1>
    <p class="lead-text">{d['lead'][lang]}</p>
    <div class="article-meta"><i class="bi bi-calendar3 me-1"></i>{lbl['date']} · <i class="bi bi-clock ms-2 me-1"></i>8 {lbl['min']} · <i class="bi bi-person ms-2 me-1"></i>{lbl['team']}</div>
  </div>
</section>
<article class="article-body">
{d['body'][lang]}
  <h2>{lbl['related']}</h2>
  <ul>
{related_links}
  </ul>
</article>
<footer>
  <div class="container">
    <p><a href="{pfx}/"><i class="bi bi-globe-americas me-1"></i>MexVisa<strong>Pro</strong></a> — Immigration Services in Riviera Maya · Since 2009</p>
    <p style="margin-top:.3rem">© 2026 MexVisa Pro · <a href="/privacy/" style="color:rgba(255,255,255,.35)">Privacy</a> · <a href="/terms/" style="color:rgba(255,255,255,.35)">Terms</a></p>
  </div>
</footer>
<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" defer></script>
<div id="mobileMenu" class="mobile-menu">
  <button class="close-btn" onclick="document.getElementById('mobileMenu').classList.remove('open')" aria-label="Close"><i class="bi bi-x-lg"></i></button>
  <a href="{mobile_home_link}" onclick="document.getElementById('mobileMenu').classList.remove('open')">{lbl['home']}</a>
  <a href="{blog_pfx}/">{lbl['blog']}</a>
  <a href="{pfx}/partners/" style="color:var(--gold)">{lbl['partners']}</a>
  <a href="https://wa.me/{WA}?text={lbl['wa_text'].replace(' ','%20')}" target="_blank" rel="noopener" class="nav-wa"><i class="bi bi-whatsapp me-1"></i>{lbl['consult']}</a>
  <div class="lang-row">
    <a href="/blog/{en_sl}/" class="lang-btn{"" if lang!="en" else ' style="color:#fff;background:var(--gold)"'}">EN</a>
    <a href="/es/blog/{slugs["es"]}/" class="lang-btn{"" if lang!="es" else ' style="color:#fff;background:var(--gold)"'}">ES</a>
    <a href="/ru/blog/{slugs["ru"]}/" class="lang-btn{"" if lang!="ru" else ' style="color:#fff;background:var(--gold)"'}">RU</a>
    <a href="/zh/blog/{slugs["zh"]}/" class="lang-btn{"" if lang!="zh" else ' style="color:#fff;background:var(--gold)"'}">ZH</a>
  </div>
</div>
</body>
</html>'''

def write(lang, slug, d):
    pfx = '' if lang == 'en' else f'/{lang}'
    path = f'{BASE}{pfx}/blog/{slug}'
    os.makedirs(path, exist_ok=True)
    with open(f'{path}/index.html', 'w') as f:
        f.write(html(lang, slug, d))
    print(f'  wrote {pfx}/blog/{slug}/')

# ─── ARTICLE DATA ────────────────────────────────────────────────────────────

CTA = {
    'en': lambda topic: f'''  <div class="cta-box">
    <h3>Need Help With {topic}?</h3>
    <p>Our Riviera Maya experts guide you through every step. Response in under 30 minutes.</p>
    <a href="https://wa.me/{WA}?text=Hi!%20I%20need%20help%20with%20{topic.replace(" ","%20")}" class="btn-gold" target="_blank" rel="noopener"><i class="bi bi-whatsapp me-2"></i>Free Consultation</a>
  </div>''',
    'es': lambda topic: f'''  <div class="cta-box">
    <h3>¿Necesitas ayuda con {topic}?</h3>
    <p>Nuestros expertos en Riviera Maya te guían en cada paso. Respuesta en menos de 30 minutos.</p>
    <a href="https://wa.me/{WA}?text=Hola!%20Necesito%20ayuda%20con%20{topic.replace(" ","%20")}" class="btn-gold" target="_blank" rel="noopener"><i class="bi bi-whatsapp me-2"></i>Consulta Gratuita</a>
  </div>''',
    'ru': lambda topic: f'''  <div class="cta-box">
    <h3>Нужна помощь?</h3>
    <p>Наши эксперты в Ривьера-Майя ответят в течение 30 минут.</p>
    <a href="https://wa.me/{WA}?text=Здравствуйте!%20Нужна%20консультация" class="btn-gold" target="_blank" rel="noopener"><i class="bi bi-whatsapp me-2"></i>Бесплатная консультация</a>
  </div>''',
    'zh': lambda topic: f'''  <div class="cta-box">
    <h3>需要帮助？</h3>
    <p>我们的Riviera Maya专家团队30分钟内回复您。</p>
    <a href="https://wa.me/{WA}?text=你好！需要免费咨询" class="btn-gold" target="_blank" rel="noopener"><i class="bi bi-whatsapp me-2"></i>免费咨询</a>
  </div>''',
}

IB = lambda txt: f'  <div class="info-box"><p>{txt}</p></div>'

ARTICLES = {}

# ── 1. IMSS ──────────────────────────────────────────────────────────────────
ARTICLES['imss-health-insurance-foreigners-mexico'] = {
    'slugs': {'en':'imss-health-insurance-foreigners-mexico','es':'imss-seguro-salud-extranjeros-mexico','ru':'imss-meditsinskaya-strakhovka-meksika','zh':'imss-yiliao-baoxian-waiguoren-moxige'},
    'title': {
        'en':'IMSS Health Insurance for Foreigners in Mexico 2026 | MexVisa Pro',
        'es':'IMSS para Extranjeros en México 2026 | Seguro Médico | MexVisa Pro',
        'ru':'IMSS Медицинская Страховка для Иностранцев в Мексике 2026 | MexVisa Pro',
        'zh':'墨西哥IMSS医疗保险外国人指南2026 | MexVisa Pro',
    },
    'desc': {
        'en':'How foreigners with Mexican residency can enroll in IMSS public health insurance in 2026. Cost, coverage, enrollment steps, and comparison with private insurance.',
        'es':'Cómo los extranjeros con residencia mexicana pueden inscribirse al IMSS en 2026. Costo, cobertura, pasos de inscripción y comparación con seguro privado.',
        'ru':'Как иностранцы с мексиканским видом на жительство могут застраховаться в IMSS в 2026 году. Стоимость, покрытие, шаги регистрации.',
        'zh':'2026年持墨西哥居留权的外国人如何加入IMSS公共医疗保险。费用、覆盖范围、注册步骤与私人保险比较。',
    },
    'h1': {
        'en':'IMSS Health Insurance for Foreigners in Mexico: Complete 2026 Guide',
        'es':'IMSS para Extranjeros en México: Guía Completa 2026',
        'ru':'IMSS для Иностранцев в Мексике: Полное Руководство 2026',
        'zh':'墨西哥IMSS医疗保险外国人完整指南2026',
    },
    'lead': {
        'en':'Mexican residents — including foreigners — can enroll in IMSS, Mexico\'s public health system, for as little as $500/year. Here\'s how to do it in 2026.',
        'es':'Los residentes en México, incluidos los extranjeros, pueden inscribirse al IMSS por tan solo $500 USD al año. Aquí te explicamos cómo hacerlo en 2026.',
        'ru':'Резиденты Мексики, включая иностранцев, могут вступить в систему IMSS примерно за $500 в год. Подробное руководство на 2026 год.',
        'zh':'在墨西哥的居民（包括外国人）每年只需约500美元即可加入IMSS。以下是2026年的详细步骤。',
    },
    'breadcrumb': {'en':'IMSS for Foreigners','es':'IMSS para Extranjeros','ru':'IMSS для Иностранцев','zh':'IMSS外国人医保'},
    'faq': {
        'en':[
            ('Can foreigners join IMSS in Mexico?','Yes. Any foreigner holding a valid Mexican Temporary or Permanent Resident card can voluntarily enroll in IMSS. Tourist visa holders are not eligible.'),
            ('How much does IMSS cost for foreigners in Mexico?','In 2026, voluntary IMSS enrollment for foreigners costs approximately $500–$600 USD per year, paid annually. The exact amount is based on the current UMA value set by the government.'),
            ('What does IMSS cover for foreign residents?','IMSS covers doctor visits, specialist consultations, surgeries, hospitalization, prescription drugs, maternity care, emergency care, and preventive health programs — the same coverage as Mexican citizens.'),
        ],
        'es':[
            ('¿Pueden los extranjeros inscribirse al IMSS en México?','Sí. Cualquier extranjero con tarjeta de Residente Temporal o Permanente vigente puede inscribirse voluntariamente al IMSS. Los titulares de visa de turista no son elegibles.'),
            ('¿Cuánto cuesta el IMSS para extranjeros en México?','En 2026, la inscripción voluntaria al IMSS para extranjeros cuesta aproximadamente $500–$600 USD al año. El monto exacto se basa en el valor de la UMA vigente.'),
            ('¿Qué cubre el IMSS para residentes extranjeros?','El IMSS cubre consultas médicas, especialistas, cirugías, hospitalización, medicamentos, atención de maternidad, urgencias y programas preventivos — la misma cobertura que para ciudadanos mexicanos.'),
        ],
        'ru':[
            ('Могут ли иностранцы вступить в IMSS в Мексике?','Да. Любой иностранец с действующей картой временного или постоянного резидента Мексики может добровольно вступить в IMSS. Обладатели туристической визы не имеют права на это.'),
            ('Сколько стоит IMSS для иностранцев в Мексике?','В 2026 году добровольное членство в IMSS обходится примерно в $500–$600 USD в год.'),
            ('Что покрывает IMSS для иностранных резидентов?','IMSS покрывает визиты к врачам, консультации специалистов, операции, госпитализацию, лекарства, скорую помощь — такое же покрытие, как для мексиканских граждан.'),
        ],
        'zh':[
            ('外国人可以在墨西哥加入IMSS吗？','可以。任何持有有效墨西哥临时或永久居留卡的外国人都可以自愿加入IMSS。持旅游签证者不符合条件。'),
            ('外国人在墨西哥加入IMSS需要多少钱？','2026年，外国人自愿加入IMSS每年费用约为500-600美元，按年缴纳。'),
            ('IMSS为外国居民提供哪些医疗覆盖？','IMSS涵盖就医、专科会诊、手术、住院、处方药、急诊护理等——与墨西哥公民享受相同的保障。'),
        ],
    },
    'body': {
        'en': f'''  <p>One of the biggest advantages of getting Mexican residency is access to <strong>IMSS</strong> (Instituto Mexicano del Seguro Social) — Mexico's public healthcare system. With a valid Resident card, foreigners can enroll voluntarily for around <strong>$500 USD/year</strong> and receive the same coverage as Mexican citizens.</p>
{IB('<strong><i class="bi bi-lightbulb me-2"></i>Key fact:</strong> IMSS is only available to foreigners holding Temporary or Permanent Residency cards. Tourist visa holders cannot enroll.')}
  <h2>What Is IMSS?</h2>
  <p>IMSS is Mexico's largest public health insurance system, covering over 70 million Mexicans. It operates hospitals, clinics, and specialist centers nationwide. In the Riviera Maya, IMSS has major facilities in <strong>Cancún, Playa del Carmen, and Chetumal</strong>.</p>
  <p>For foreigners on residency visas, voluntary enrollment (Incorporación Voluntaria) gives full access to all IMSS services for a flat annual fee.</p>
  <h2>Who Can Enroll?</h2>
  <ul>
    <li><strong>Temporary Residents (Residente Temporal)</strong> — eligible from the moment you receive your card</li>
    <li><strong>Permanent Residents (Residente Permanente)</strong> — eligible immediately</li>
    <li><strong>Spouse and dependent children</strong> — can be added as beneficiaries at a reduced additional cost</li>
  </ul>
  <p>Tourist visa holders, digital nomads without residency, and overstay visitors <strong>cannot enroll</strong>.</p>
  <h2>Cost in 2026</h2>
  <p>The annual fee is calculated as a multiple of the <strong>UMA</strong> (Unidad de Medida y Actualización), Mexico's official reference unit. In 2026:</p>
  <ul>
    <li><strong>Primary member:</strong> ~$500–$600 USD/year (paid in MXN at current rate)</li>
    <li><strong>Spouse:</strong> ~50% of primary fee</li>
    <li><strong>Children under 16:</strong> included at a small additional fee</li>
  </ul>
{IB('<strong><i class="bi bi-info-circle me-2"></i>Payment:</strong> The annual IMSS fee is paid in full at the start of each year. Some IMSS offices accept installment payments — ask your local subdelegación.')}
  <h2>What IMSS Covers</h2>
  <ul>
    <li>General practitioner and specialist consultations</li>
    <li>Diagnostic tests (blood work, X-rays, ultrasounds, MRI)</li>
    <li>Surgeries and hospital stays</li>
    <li>Prescription medications (IMSS formulary)</li>
    <li>Maternity and obstetric care</li>
    <li>Emergency care (24/7)</li>
    <li>Dental care (basic)</li>
    <li>Mental health services</li>
    <li>Preventive programs (cancer screening, diabetes, hypertension)</li>
  </ul>
  <h2>How to Enroll in IMSS — Step by Step</h2>
  <h3>Step 1: Gather Your Documents</h3>
  <ul>
    <li>Valid Mexican Residency card (Residente Temporal or Permanente)</li>
    <li>Passport (original + copy)</li>
    <li>CURP (Mexican national ID number for foreigners — MexVisa Pro can help you get this)</li>
    <li>RFC (if you have one)</li>
    <li>Proof of address in Mexico (utility bill or lease agreement)</li>
    <li>Recent passport photo</li>
  </ul>
  <h3>Step 2: Visit Your Local IMSS Subdelegación</h3>
  <p>Go to the IMSS office (Subdelegación) nearest to your address. In Playa del Carmen, the IMSS subdelegación is on Av. 30. In Cancún, it's in the Ciudad del Carmen zone. Bring all original documents and copies.</p>
  <h3>Step 3: Complete the Voluntary Enrollment Form</h3>
  <p>Request the <strong>Incorporación Voluntaria al Régimen Obligatorio</strong> form. Staff will verify your documents and assign you a <strong>NSS</strong> (Número de Seguridad Social) — your IMSS membership number.</p>
  <h3>Step 4: Pay the Annual Fee</h3>
  <p>Pay the annual premium. You'll receive your IMSS credential card. Coverage begins immediately.</p>
  <h3>Step 5: Register Your Doctor and Clinic</h3>
  <p>IMSS assigns you to a <strong>Unidad de Medicina Familiar (UMF)</strong> near your address — your primary care clinic. All specialist referrals, tests, and hospitalizations go through this clinic.</p>
  <h2>IMSS vs Private Health Insurance</h2>
  <ul>
    <li><strong>IMSS pros:</strong> Very cheap (~$500/year), comprehensive coverage, no copays for most services</li>
    <li><strong>IMSS cons:</strong> Wait times can be long, clinic assigned by address, less flexibility in choosing doctors</li>
    <li><strong>Private pros:</strong> Immediate access, English-speaking doctors in tourist areas, faster appointments</li>
    <li><strong>Private cons:</strong> $100–$500/month for full coverage, out-of-pocket costs for non-covered services</li>
  </ul>
  <p>Many expats carry <strong>both</strong> — IMSS for major procedures and hospitalizations, private for day-to-day doctor visits and emergencies where speed matters.</p>
{CTA['en']("IMSS enrollment")}''',
        'es': f'''  <p>Una de las mayores ventajas de obtener la residencia mexicana es el acceso al <strong>IMSS</strong> (Instituto Mexicano del Seguro Social). Con una tarjeta de residente vigente, los extranjeros pueden inscribirse voluntariamente por aproximadamente <strong>$500 USD al año</strong> y recibir la misma cobertura que los ciudadanos mexicanos.</p>
{IB('<strong><i class="bi bi-lightbulb me-2"></i>Importante:</strong> El IMSS solo está disponible para extranjeros con tarjeta de Residente Temporal o Permanente. Los titulares de visa de turista no pueden inscribirse.')}
  <h2>¿Qué es el IMSS?</h2>
  <p>El IMSS es el sistema de salud pública más grande de México, con cobertura para más de 70 millones de mexicanos. Opera hospitales, clínicas y centros especializados en todo el país. En la Riviera Maya tiene instalaciones en <strong>Cancún, Playa del Carmen y Chetumal</strong>.</p>
  <h2>¿Quién Puede Inscribirse?</h2>
  <ul>
    <li><strong>Residentes Temporales</strong> — elegibles desde que reciben su tarjeta</li>
    <li><strong>Residentes Permanentes</strong> — elegibles de inmediato</li>
    <li><strong>Cónyuge e hijos dependientes</strong> — pueden agregarse como beneficiarios</li>
  </ul>
  <h2>Costo en 2026</h2>
  <ul>
    <li><strong>Titular:</strong> ~$500–$600 USD/año (pagado en MXN)</li>
    <li><strong>Cónyuge:</strong> ~50% de la cuota del titular</li>
    <li><strong>Hijos menores de 16 años:</strong> cuota adicional mínima</li>
  </ul>
  <h2>¿Qué Cubre el IMSS?</h2>
  <ul>
    <li>Consultas de medicina general y especialidades</li>
    <li>Estudios diagnósticos (análisis, rayos X, ultrasonidos, resonancias)</li>
    <li>Cirugías y hospitalización</li>
    <li>Medicamentos (formulario IMSS)</li>
    <li>Atención de maternidad</li>
    <li>Urgencias 24/7</li>
    <li>Servicios dentales básicos y salud mental</li>
    <li>Programas preventivos (detección de cáncer, diabetes, hipertensión)</li>
  </ul>
  <h2>Cómo Inscribirse al IMSS — Paso a Paso</h2>
  <h3>Documentos Necesarios</h3>
  <ul>
    <li>Tarjeta de residencia mexicana vigente</li>
    <li>Pasaporte (original y copia)</li>
    <li>CURP (MexVisa Pro puede ayudarte a obtenerlo)</li>
    <li>Comprobante de domicilio en México</li>
    <li>Foto tamaño pasaporte</li>
  </ul>
  <h3>Proceso en la Subdelegación</h3>
  <p>Visita la Subdelegación del IMSS más cercana a tu domicilio. En Playa del Carmen está en Av. 30. En Cancún, en la zona de Ciudad del Carmen. Solicita el formulario de <strong>Incorporación Voluntaria al Régimen Obligatorio</strong>. Te asignarán un NSS y recibirás tu credencial IMSS.</p>
  <h2>IMSS vs Seguro Privado</h2>
  <ul>
    <li><strong>IMSS ventajas:</strong> Muy económico (~$500/año), cobertura completa, sin copagos para la mayoría de servicios</li>
    <li><strong>IMSS desventajas:</strong> Tiempos de espera, clínica asignada por domicilio</li>
    <li><strong>Privado ventajas:</strong> Acceso inmediato, médicos angloparlantes, citas rápidas</li>
    <li><strong>Privado desventajas:</strong> $100–$500/mes para cobertura completa</li>
  </ul>
  <p>Muchos expatriados tienen <strong>ambos</strong> — IMSS para cirugías y hospitalización, privado para consultas cotidianas.</p>
{CTA['es']("inscripción al IMSS")}''',
        'ru': f'''  <p>Одно из главных преимуществ мексиканского вида на жительство — доступ к <strong>IMSS</strong> (Instituto Mexicano del Seguro Social), государственной системе здравоохранения Мексики. При наличии карты резидента иностранцы могут вступить добровольно примерно за <strong>$500 USD в год</strong>.</p>
{IB('<strong>Важно:</strong> IMSS доступен только для иностранцев с картой временного или постоянного резидента Мексики.')}
  <h2>Что такое IMSS?</h2>
  <p>IMSS — крупнейшая система медицинского страхования Мексики, охватывающая более 70 миллионов человек. В Ривьера-Майя крупные учреждения IMSS расположены в <strong>Канкуне, Плая-дель-Кармен и Четумале</strong>.</p>
  <h2>Кто может вступить?</h2>
  <ul>
    <li><strong>Временные резиденты</strong> — с момента получения карты</li>
    <li><strong>Постоянные резиденты</strong> — немедленно</li>
    <li><strong>Супруг(а) и дети-иждивенцы</strong> — как бенефициары</li>
  </ul>
  <h2>Стоимость в 2026 году</h2>
  <ul>
    <li><strong>Основной участник:</strong> ~$500–$600 USD/год</li>
    <li><strong>Супруг(а):</strong> ~50% от основного взноса</li>
    <li><strong>Дети до 16 лет:</strong> небольшой дополнительный взнос</li>
  </ul>
  <h2>Что покрывает IMSS?</h2>
  <ul>
    <li>Приём терапевта и специалистов</li>
    <li>Анализы, рентген, УЗИ, МРТ</li>
    <li>Операции и госпитализация</li>
    <li>Рецептурные препараты</li>
    <li>Помощь при беременности и родах</li>
    <li>Скорая помощь 24/7</li>
    <li>Стоматология (базовая)</li>
  </ul>
  <h2>Как вступить в IMSS — пошагово</h2>
  <h3>Необходимые документы</h3>
  <ul>
    <li>Действующая карта резидента Мексики</li>
    <li>Паспорт (оригинал и копия)</li>
    <li>CURP (мексиканский налоговый номер для иностранцев)</li>
    <li>Подтверждение адреса в Мексике</li>
    <li>Фото на документы</li>
  </ul>
  <h3>Процедура в субделегации IMSS</h3>
  <p>Посетите ближайшую субделегацию IMSS. Запросите форму <strong>Incorporación Voluntaria al Régimen Obligatorio</strong>. Вам присвоят номер социального страхования (NSS) и выдадут удостоверение IMSS.</p>
  <h2>IMSS vs Частная страховка</h2>
  <ul>
    <li><strong>IMSS плюсы:</strong> Очень дёшево (~$500/год), полное покрытие</li>
    <li><strong>IMSS минусы:</strong> Время ожидания может быть длительным</li>
    <li><strong>Частная страховка плюсы:</strong> Немедленный доступ, врачи говорят по-русски/по-английски</li>
    <li><strong>Частная страховка минусы:</strong> $100–$500/месяц</li>
  </ul>
{CTA['ru']("IMSS")}''',
        'zh': f'''  <p>获得墨西哥居留权的最大优势之一是可以加入<strong>IMSS</strong>（墨西哥社会保障局）——墨西哥的公共医疗体系。持有有效居留卡的外国人每年只需约<strong>500美元</strong>即可自愿加入，享受与墨西哥公民相同的医疗保障。</p>
{IB('<strong>重要提示：</strong>IMSS仅对持有临时或永久居留卡的外国人开放。持旅游签证者不符合条件。')}
  <h2>什么是IMSS？</h2>
  <p>IMSS是墨西哥最大的公共医疗保险系统，覆盖7000多万人。在Riviera Maya地区，IMSS在<strong>坎昆、普拉亚德尔卡门和切图马尔</strong>设有主要医疗机构。</p>
  <h2>谁可以加入？</h2>
  <ul>
    <li><strong>临时居民（Residente Temporal）</strong>——收到居留卡后即可申请</li>
    <li><strong>永久居民（Residente Permanente）</strong>——立即可申请</li>
    <li><strong>配偶和未成年子女</strong>——可作为受益人添加</li>
  </ul>
  <h2>2026年费用</h2>
  <ul>
    <li><strong>主要成员：</strong>约500-600美元/年</li>
    <li><strong>配偶：</strong>约为主要费用的50%</li>
    <li><strong>16岁以下子女：</strong>少量附加费用</li>
  </ul>
  <h2>IMSS覆盖范围</h2>
  <ul>
    <li>全科医生和专科会诊</li>
    <li>诊断检查（血检、X光、超声波、核磁共振）</li>
    <li>手术和住院治疗</li>
    <li>处方药（IMSS药品目录）</li>
    <li>产科护理</li>
    <li>24/7急诊</li>
    <li>基础牙科和心理健康服务</li>
  </ul>
  <h2>如何加入IMSS——详细步骤</h2>
  <h3>所需文件</h3>
  <ul>
    <li>有效的墨西哥居留卡</li>
    <li>护照（原件和复印件）</li>
    <li>CURP（MexVisa Pro可协助办理）</li>
    <li>墨西哥地址证明</li>
    <li>证件照</li>
  </ul>
  <h3>在IMSS分局的办理流程</h3>
  <p>前往离您最近的IMSS分局（Subdelegación）。在普拉亚德尔卡门，分局位于30大道。申请<strong>自愿加入强制制度</strong>表格。工作人员将验证您的文件，分配社会保险号码（NSS）并发放IMSS证件卡。</p>
  <h2>IMSS与私人医疗保险对比</h2>
  <ul>
    <li><strong>IMSS优点：</strong>费用极低（约500美元/年），综合覆盖，大多数服务无需自付</li>
    <li><strong>IMSS缺点：</strong>候诊时间可能较长，医生由系统分配</li>
    <li><strong>私人保险优点：</strong>立即就医，医生可能会说英语，预约更灵活</li>
    <li><strong>私人保险缺点：</strong>每月100-500美元</li>
  </ul>
{CTA['zh']("IMSS加入")}''',
    },
    'related': {
        'en':[('mexico-temporary-residency-guide','Mexico Temporary Residency Guide 2026'),('curp-foreigners-mexico','CURP for Foreigners in Mexico'),('rfc-registration-mexico-expats','RFC Registration for Expats in Mexico')],
        'es':[('guia-residencia-temporal-mexico','Guía de Residencia Temporal México 2026'),('curp-extranjeros-mexico','CURP para Extranjeros en México'),('rfc-registro-extranjeros-mexico','RFC para Extranjeros en México')],
        'ru':[('vremennoe-rezidentstvo-meksika','Временное резидентство в Мексике 2026'),('curp-dlya-inostrantsev-meksika','CURP для иностранцев в Мексике'),('rfc-registratsiya-meksika','RFC регистрация в Мексике')],
        'zh':[('墨西哥临时居留指南2026','mexico-temporary-residency-guide'),('curp-waiguoren-moxige','墨西哥CURP外国人申请'),('rfc-zhuche-waiguoren','墨西哥RFC注册')],
    },
}

# ── 2. CURP ──────────────────────────────────────────────────────────────────
ARTICLES['curp-foreigners-mexico'] = {
    'slugs': {'en':'curp-foreigners-mexico','es':'curp-extranjeros-mexico','ru':'curp-dlya-inostrantsev-meksika','zh':'curp-waiguoren-moxige'},
    'title': {
        'en':'CURP for Foreigners in Mexico 2026: How to Get It | MexVisa Pro',
        'es':'CURP para Extranjeros en México 2026: Cómo Obtenerlo | MexVisa Pro',
        'ru':'CURP для Иностранцев в Мексике 2026: Как Получить | MexVisa Pro',
        'zh':'墨西哥外国人CURP申请指南2026 | MexVisa Pro',
    },
    'desc': {
        'en':'How to get a CURP number in Mexico as a foreigner in 2026. Required for IMSS, RFC, school enrollment, and banking. Step-by-step guide for residents.',
        'es':'Cómo obtener el CURP en México como extranjero en 2026. Necesario para IMSS, RFC, escuelas y banca. Guía paso a paso para residentes.',
        'ru':'Как получить CURP в Мексике как иностранцу в 2026 году. Необходим для IMSS, RFC, школ и банков. Пошаговое руководство.',
        'zh':'2026年外国人在墨西哥如何申请CURP号码。IMSS、RFC、学校入学和银行开户均需要。居民分步指南。',
    },
    'h1': {
        'en':'CURP for Foreigners in Mexico: Step-by-Step Guide 2026',
        'es':'CURP para Extranjeros en México: Guía Paso a Paso 2026',
        'ru':'CURP для Иностранцев в Мексике: Пошаговое Руководство 2026',
        'zh':'墨西哥外国人CURP申请：2026年分步指南',
    },
    'lead': {
        'en':'The CURP is Mexico\'s personal ID code. Every foreign resident needs one — for IMSS enrollment, RFC registration, school, and banking. Here\'s how to get yours.',
        'es':'El CURP es el código de identidad personal de México. Todo residente extranjero lo necesita — para el IMSS, RFC, escuelas y banca. Aquí te explicamos cómo obtenerlo.',
        'ru':'CURP — личный идентификационный код Мексики. Каждому иностранному резиденту он необходим для IMSS, RFC, школ и банков.',
        'zh':'CURP是墨西哥的个人身份识别码。每位外国居民都需要它——用于IMSS、RFC、学校和银行。',
    },
    'breadcrumb': {'en':'CURP for Foreigners','es':'CURP para Extranjeros','ru':'CURP для Иностранцев','zh':'外国人CURP'},
    'faq': {
        'en':[
            ('What is a CURP in Mexico?','CURP stands for Clave Única de Registro de Población — Mexico\'s unique population registry code. It is an 18-character alphanumeric code assigned to every person living legally in Mexico, including foreigners with residency.'),
            ('Can foreigners get a CURP in Mexico?','Yes. Any foreigner with a valid Temporary or Permanent Resident card is entitled to a CURP. It is free and required for many official procedures including IMSS, RFC, school enrollment, and notarial documents.'),
            ('How long does it take to get a CURP as a foreigner?','If you apply online through the RENAPO portal with your INM registration number, the CURP can be generated instantly. In-person at a RENAPO or INM office, same-day processing is standard.'),
        ],
        'es':[
            ('¿Qué es el CURP en México?','El CURP (Clave Única de Registro de Población) es el código de identidad único de México. Es un código alfanumérico de 18 caracteres asignado a toda persona que vive legalmente en México, incluidos los extranjeros con residencia.'),
            ('¿Pueden los extranjeros obtener un CURP en México?','Sí. Todo extranjero con tarjeta de Residente Temporal o Permanente vigente tiene derecho a obtener un CURP. Es gratuito y necesario para muchos trámites oficiales.'),
            ('¿Cuánto tarda obtener el CURP como extranjero?','Si solicitas en línea a través del portal RENAPO con tu número de registro INM, el CURP puede generarse al instante. En persona, el trámite es el mismo día.'),
        ],
        'ru':[
            ('Что такое CURP в Мексике?','CURP — уникальный идентификационный код населения Мексики. Это 18-символьный буквенно-цифровой код, присваиваемый каждому человеку, законно проживающему в Мексике.'),
            ('Могут ли иностранцы получить CURP в Мексике?','Да. Любой иностранец с действующей картой временного или постоянного резидента имеет право на CURP. Это бесплатно и необходимо для многих официальных процедур.'),
            ('Сколько времени занимает получение CURP для иностранца?','При онлайн-заявке через портал RENAPO с номером регистрации INM CURP может быть сгенерирован мгновенно.'),
        ],
        'zh':[
            ('什么是墨西哥CURP？','CURP是墨西哥独特的人口注册码（Clave Única de Registro de Población）。这是一个18位字母数字组合代码，分配给每个在墨西哥合法居住的人，包括持有居留权的外国人。'),
            ('外国人可以在墨西哥申请CURP吗？','可以。任何持有有效临时或永久居留卡的外国人都有权获得CURP。免费申请，且许多官方手续都需要它。'),
            ('外国人申请CURP需要多长时间？','通过RENAPO门户网站在线申请（使用您的INM注册号），CURP可以即时生成。'),
        ],
    },
    'body': {
        'en': f'''  <p>The <strong>CURP</strong> (Clave Única de Registro de Población) is Mexico's national ID code — an 18-character number that identifies every person living legally in Mexico. As a foreign resident, you'll need it for almost everything: IMSS enrollment, RFC tax registration, school enrollment, bank accounts, and notarial acts.</p>
{IB('<strong>Good news:</strong> Getting a CURP as a foreigner is free and fast — often same-day if you apply online.')}
  <h2>Who Needs a CURP?</h2>
  <p>All foreigners with a valid Mexican Temporary or Permanent Resident card are entitled to — and usually need — a CURP. Tourist visa holders are not assigned a CURP through standard channels.</p>
  <p>You'll need your CURP for:</p>
  <ul>
    <li>Enrolling in IMSS (public health insurance)</li>
    <li>Getting your RFC (tax registration number)</li>
    <li>Enrolling children in Mexican public or private schools</li>
    <li>Opening bank accounts (some banks require it)</li>
    <li>Signing notarial documents and property transactions</li>
    <li>Obtaining a Mexican driver's license</li>
    <li>Receiving Mexican government services</li>
  </ul>
  <h2>How to Get Your CURP — Option 1: Online (Fastest)</h2>
  <h3>Through the RENAPO Portal</h3>
  <p>Go to <strong>gob.mx/curp</strong> and select the option for foreigners. You'll need:</p>
  <ul>
    <li>Your INM registration number (from your Residency card)</li>
    <li>Full name as it appears in your passport</li>
    <li>Date and country of birth</li>
    <li>Gender</li>
  </ul>
  <p>If your INM record is active in the system, your CURP is generated immediately and can be downloaded as a PDF.</p>
  <h2>How to Get Your CURP — Option 2: In Person</h2>
  <h3>At an INM Office</h3>
  <p>When you register at INM after entering Mexico, the officer typically generates your CURP automatically. Check your INM paperwork — it may already be there.</p>
  <h3>At a RENAPO Office or DIF</h3>
  <p>Bring your Residency card, passport, and proof of address. The CURP is issued free of charge and usually same-day.</p>
  <h2>Understanding Your CURP Code</h2>
  <p>The CURP has 18 characters structured as:</p>
  <ul>
    <li><strong>Characters 1–4:</strong> Letters from your last name and first name</li>
    <li><strong>Characters 5–10:</strong> Date of birth (YYMMDD)</li>
    <li><strong>Character 11:</strong> Gender (H/M)</li>
    <li><strong>Characters 12–13:</strong> State of birth (or XX for foreigners)</li>
    <li><strong>Characters 14–16:</strong> Consonants from your name</li>
    <li><strong>Character 17:</strong> Century indicator</li>
    <li><strong>Character 18:</strong> Check digit</li>
  </ul>
{IB('<strong><i class="bi bi-info-circle me-2"></i>Foreigners:</strong> Your state code will be "NE" (Nacido en el Extranjero — born abroad). This is normal and correct.')}
  <h2>CURP vs RFC — What\'s the Difference?</h2>
  <ul>
    <li><strong>CURP:</strong> General personal ID for all residents. Free, no expiry. Required for social services, education, healthcare.</li>
    <li><strong>RFC:</strong> Tax registration number. Required if you earn income in Mexico, sign contracts, open business accounts. Separate process through SAT.</li>
  </ul>
  <p>Most expats need both. The CURP is usually obtained first — it's then used in the RFC registration process.</p>
  <h2>What If My CURP Has Errors?</h2>
  <p>If your CURP contains incorrect data (wrong name spelling, wrong birthdate), you must go to a RENAPO office in person with your original passport and residency card to request a correction. MexVisa Pro can assist with CURP corrections.</p>
{CTA['en']("your CURP")}''',
        'es': f'''  <p>El <strong>CURP</strong> (Clave Única de Registro de Población) es el código de identidad nacional de México — un número de 18 caracteres que identifica a toda persona que vive legalmente en el país. Como residente extranjero, lo necesitarás para casi todo: IMSS, RFC, escuelas, cuentas bancarias y actos notariales.</p>
{IB('<strong>Buenas noticias:</strong> Obtener el CURP como extranjero es gratuito y rápido — a menudo el mismo día si solicitas en línea.')}
  <h2>¿Quién Necesita el CURP?</h2>
  <p>Todos los extranjeros con tarjeta de Residente Temporal o Permanente vigente tienen derecho y normalmente necesitan un CURP. Lo necesitarás para:</p>
  <ul>
    <li>Inscribirte al IMSS (seguro médico público)</li>
    <li>Obtener tu RFC (registro tributario)</li>
    <li>Inscribir a tus hijos en escuelas mexicanas</li>
    <li>Abrir cuentas bancarias</li>
    <li>Firmar documentos notariales y transacciones inmobiliarias</li>
    <li>Obtener licencia de conducir mexicana</li>
  </ul>
  <h2>Cómo Obtener tu CURP — Opción 1: En Línea (Más Rápido)</h2>
  <p>Accede a <strong>gob.mx/curp</strong> y selecciona la opción para extranjeros. Necesitarás:</p>
  <ul>
    <li>Tu número de registro INM (de tu tarjeta de residencia)</li>
    <li>Nombre completo tal como aparece en tu pasaporte</li>
    <li>Fecha y país de nacimiento</li>
  </ul>
  <p>Si tu registro en el INM está activo en el sistema, el CURP se genera al instante y se puede descargar en PDF.</p>
  <h2>Cómo Obtener tu CURP — Opción 2: En Persona</h2>
  <p>Cuando te registras en el INM después de ingresar a México, el funcionario normalmente genera tu CURP automáticamente. Revisa tu documentación del INM — puede que ya esté incluido. También puedes ir a una oficina RENAPO o DIF con tu tarjeta de residencia, pasaporte y comprobante de domicilio.</p>
  <h2>CURP vs RFC — ¿Cuál es la Diferencia?</h2>
  <ul>
    <li><strong>CURP:</strong> Identificación personal general. Gratuito, sin vencimiento. Para servicios sociales, educación, salud.</li>
    <li><strong>RFC:</strong> Registro tributario. Necesario si generas ingresos en México o firmas contratos. Trámite separado ante el SAT.</li>
  </ul>
  <p>La mayoría de los expatriados necesitan ambos. El CURP se obtiene primero y luego se utiliza en el proceso de registro del RFC.</p>
{CTA['es']("tu CURP")}''',
        'ru': f'''  <p><strong>CURP</strong> (Clave Única de Registro de Población) — национальный идентификационный код Мексики. Как иностранный резидент, он вам понадобится практически для всего: IMSS, RFC, школы, банковские счета и нотариальные документы.</p>
{IB('<strong>Хорошая новость:</strong> Получить CURP как иностранцу — бесплатно и быстро, часто в тот же день.')}
  <h2>Кому нужен CURP?</h2>
  <p>Все иностранцы с действующей картой временного или постоянного резидента Мексики имеют право на CURP. Он нужен для:</p>
  <ul>
    <li>Вступления в IMSS</li>
    <li>Получения RFC (налогового номера)</li>
    <li>Записи детей в мексиканские школы</li>
    <li>Открытия банковских счетов</li>
    <li>Подписания нотариальных документов</li>
    <li>Получения мексиканских водительских прав</li>
  </ul>
  <h2>Как получить CURP — Онлайн (Быстрее)</h2>
  <p>Зайдите на <strong>gob.mx/curp</strong> и выберите опцию для иностранцев. Понадобятся: номер регистрации INM, полное имя как в паспорте, дата и страна рождения. Если ваша запись в INM активна, CURP генерируется мгновенно.</p>
  <h2>Как получить CURP — Лично</h2>
  <p>При регистрации в INM после въезда в Мексику CURP обычно генерируется автоматически. Также можно обратиться в офис RENAPO или DIF с картой резидента, паспортом и подтверждением адреса.</p>
  <h2>CURP vs RFC — в чём разница?</h2>
  <ul>
    <li><strong>CURP:</strong> Общий личный ID. Бесплатно, бессрочно. Для здравоохранения, образования, соцуслуг.</li>
    <li><strong>RFC:</strong> Налоговый номер. Нужен для получения дохода в Мексике. Отдельная процедура через SAT.</li>
  </ul>
{CTA['ru']("CURP")}''',
        'zh': f'''  <p><strong>CURP</strong>（人口登记唯一密钥）是墨西哥的国家身份识别码——一个18位字符，标识每个在墨西哥合法居住的人。作为外国居民，您几乎需要它做所有事情：IMSS、RFC、学校、银行账户和公证文件。</p>
{IB('<strong>好消息：</strong>作为外国人获取CURP是免费且快速的——在线申请通常当天即可完成。')}
  <h2>谁需要CURP？</h2>
  <p>所有持有有效墨西哥临时或永久居留卡的外国人都有权获得CURP。您需要它用于：</p>
  <ul>
    <li>加入IMSS（公共医疗保险）</li>
    <li>获取RFC（税务登记号）</li>
    <li>子女就读墨西哥学校</li>
    <li>开设银行账户</li>
    <li>签署公证文件和房产交易</li>
    <li>办理墨西哥驾照</li>
  </ul>
  <h2>如何获取CURP——方式一：在线（最快）</h2>
  <p>访问<strong>gob.mx/curp</strong>并选择外国人选项。您需要：INM注册号（来自居留卡）、护照上的全名、出生日期和国家。如果您的INM记录在系统中处于活跃状态，CURP可以立即生成并以PDF格式下载。</p>
  <h2>如何获取CURP——方式二：亲自前往</h2>
  <p>在入境墨西哥后在INM注册时，工作人员通常会自动生成您的CURP。查看您的INM文件——可能已经包含在内。也可携带居留卡、护照和地址证明前往RENAPO或DIF办公室办理。</p>
  <h2>CURP与RFC的区别</h2>
  <ul>
    <li><strong>CURP：</strong>通用个人ID，免费、永久有效。用于社会服务、教育、医疗。</li>
    <li><strong>RFC：</strong>税务登记号。在墨西哥有收入或签订合同时需要。通过SAT单独办理。</li>
  </ul>
{CTA['zh']("申请CURP")}''',
    },
    'related': {
        'en':[('imss-health-insurance-foreigners-mexico','IMSS Health Insurance for Foreigners'),('rfc-registration-mexico-expats','RFC Registration for Expats'),('mexico-temporary-residency-guide','Mexico Temporary Residency Guide')],
        'es':[('imss-seguro-salud-extranjeros-mexico','IMSS para Extranjeros en México'),('rfc-registro-extranjeros-mexico','RFC para Extranjeros en México'),('guia-residencia-temporal-mexico','Guía de Residencia Temporal México')],
        'ru':[('imss-meditsinskaya-strakhovka-meksika','IMSS для иностранцев'),('rfc-registratsiya-meksika','RFC регистрация в Мексике'),('vremennoe-rezidentstvo-meksika','Временное резидентство Мексика')],
        'zh':[('imss-yiliao-baoxian-waiguoren-moxige','IMSS外国人医疗保险'),('rfc-zhuche-waiguoren','RFC注册'),('mexico-temporary-residency-guide','墨西哥临时居留指南')],
    },
}

# ── 3. TOURIST VISA EXTENSION / OVERSTAY ────────────────────────────────────
ARTICLES['mexico-tourist-visa-extension'] = {
    'slugs': {'en':'mexico-tourist-visa-extension','es':'extension-visa-turista-mexico','ru':'prodlenie-turisticheskoy-vizy-meksika','zh':'moxige-lvyou-qianzheng-yanqi'},
    'title': {
        'en':'Mexico Tourist Visa Extension 2026: Can You Stay Longer? | MexVisa Pro',
        'es':'Extensión de Visa Turista México 2026: ¿Puedes Quedarte Más Tiempo? | MexVisa Pro',
        'ru':'Продление Туристической Визы в Мексике 2026 | MexVisa Pro',
        'zh':'墨西哥旅游签证延期2026：能住更长时间吗？| MexVisa Pro',
    },
    'desc': {
        'en':'Can you extend your Mexico tourist visa beyond 180 days in 2026? Official rules on FMM extension, overstay consequences, border runs, and legal alternatives for staying longer.',
        'es':'¿Puedes extender tu visa de turista en México más allá de 180 días en 2026? Reglas oficiales sobre extensión de FMM, consecuencias del overstay y alternativas legales.',
        'ru':'Можно ли продлить туристическую визу в Мексике более 180 дней в 2026 году? Официальные правила, последствия просрочки и законные альтернативы.',
        'zh':'2026年能否将墨西哥旅游签证延长至180天以上？FMM延期的官方规定、逾期后果、边境出境及合法替代方案。',
    },
    'h1': {
        'en':'Mexico Tourist Visa Extension 2026: Rules, Options & Consequences',
        'es':'Extensión de Visa Turista México 2026: Reglas, Opciones y Consecuencias',
        'ru':'Продление Туристической Визы Мексики 2026: Правила и Последствия',
        'zh':'墨西哥旅游签证延期2026：规定、选项与后果',
    },
    'lead': {
        'en':'Mexico grants up to 180 days to tourists — but what if you want to stay longer? Here are the official rules, what happens if you overstay, and how to make your stay legal.',
        'es':'México otorga hasta 180 días a los turistas, pero ¿qué pasa si quieres quedarte más tiempo? Aquí están las reglas oficiales, consecuencias del overstay y cómo hacer tu estancia legal.',
        'ru':'Мексика предоставляет туристам до 180 дней — но что если вы хотите остаться дольше? Официальные правила, последствия просрочки и законные способы остаться.',
        'zh':'墨西哥给予游客最多180天——但如果您想住更长时间呢？以下是官方规定、逾期后果以及如何使您的居留合法化。',
    },
    'breadcrumb': {'en':'Tourist Visa Extension','es':'Extensión Visa Turista','ru':'Продление Туристической Визы','zh':'旅游签证延期'},
    'faq': {
        'en':[
            ('Can I extend my Mexico tourist visa?','Mexico does not allow FMM tourist permits to be extended beyond the initial grant (up to 180 days). There is no official extension process. To stay legally, you must either leave Mexico before expiry and re-enter, or apply for a residency visa.'),
            ('What happens if I overstay my Mexico tourist visa?','Overstaying your FMM permit results in a fine when you exit Mexico (approximately $30–$50 USD per excess day). Repeated overstays can lead to denial of entry at the border. You are not automatically deported for a first-time overstay.'),
            ('Can I do a border run to reset my Mexico tourist stay?','Yes, you can leave Mexico and re-enter to get a new FMM permit. However, immigration officers at the border have discretion to grant fewer than 180 days — or deny entry — if they see a pattern of repeated short stays.'),
        ],
        'es':[
            ('¿Puedo extender mi visa turista de México?','México no permite extender la forma migratoria FMM más allá del período inicial (hasta 180 días). No existe un proceso oficial de extensión. Para permanecer legalmente, debes salir de México antes de que venza o solicitar una visa de residencia.'),
            ('¿Qué pasa si me paso del tiempo permitido en México?','Superar el tiempo permitido de tu FMM resulta en una multa al salir (~$30–$50 USD por día de exceso). Los overstays repetidos pueden llevar a la negación de entrada en la frontera.'),
            ('¿Puedo hacer una salida fronteriza para renovar mi estancia turística?','Sí, puedes salir y volver a entrar para obtener una nueva forma FMM. Sin embargo, los agentes de migración tienen discreción para otorgar menos de 180 días si detectan un patrón de entradas repetidas cortas.'),
        ],
        'ru':[
            ('Можно ли продлить туристическую визу в Мексике?','Мексика не позволяет продлевать разрешение FMM сверх первоначального срока (до 180 дней). Официального процесса продления нет. Чтобы остаться законно, нужно либо покинуть Мексику до истечения срока, либо подать заявку на вид на жительство.'),
            ('Что будет, если я просрочу туристическую визу в Мексике?','За превышение срока действия FMM при выезде начисляется штраф (~$30–$50 USD за каждый лишний день). Повторные просрочки могут привести к отказу во въезде.'),
            ('Можно ли выехать из Мексики и сразу вернуться, чтобы обновить туристический статус?','Да, вы можете выехать и вернуться для получения нового разрешения FMM. Однако пограничники вправе выдать менее 180 дней или отказать во въезде при многократных коротких визитах.'),
        ],
        'zh':[
            ('我可以延长墨西哥旅游签证吗？','墨西哥不允许将FMM旅游许可延长至初始批准期限（最多180天）之外。没有官方延期流程。要合法继续居住，您必须在到期前离开墨西哥后重新入境，或申请居留签证。'),
            ('如果我在墨西哥逾期居留会怎样？','逾期居住FMM许可在出境时会产生罚款（每超出一天约30-50美元）。多次逾期可能导致边境拒绝入境。'),
            ('我可以出境再入境来重置墨西哥旅游居留时间吗？','可以，您可以离开墨西哥后重新入境获得新的FMM许可。但如果移民官员发现频繁短暂停留的规律，可能会给予少于180天的居留时间，甚至拒绝入境。'),
        ],
    },
    'body': {
        'en': f'''  <p>When you enter Mexico as a tourist, immigration stamps your passport with an <strong>FMM</strong> (Forma Migratoria Múltiple) granting up to 180 days. Many visitors assume they can simply extend this — they cannot. Mexico has no tourist visa extension mechanism. Here's what you actually can do.</p>
{IB('<strong><i class="bi bi-exclamation-triangle me-2"></i>Critical:</strong> The 180-day limit is set by the immigration officer at the port of entry — they can grant fewer. Always check the number stamped on your entry.')}
  <h2>Can You Extend a Mexico Tourist Visa?</h2>
  <p>No. Mexico does not have an extension process for the FMM tourist permit. Once issued, the number of days cannot be increased. The only legal options for staying longer are:</p>
  <ul>
    <li><strong>Leave and re-enter</strong> (border run) — get a new FMM on re-entry</li>
    <li><strong>Apply for residency</strong> — convert to a legal resident status</li>
  </ul>
  <h2>The Border Run Option</h2>
  <p>Leaving Mexico briefly — to Belize, Guatemala, the US, or any destination — and re-entering resets your tourist clock. Many long-term visitors do this every 180 days.</p>
  <h3>Risks of Border Runs</h3>
  <ul>
    <li><strong>Officer discretion:</strong> Border agents can grant fewer than 180 days if your passport shows repeated Mexico entries. Some receive 90 or even 30 days.</li>
    <li><strong>Pattern detection:</strong> If you've done 3+ consecutive border runs, officers may question your intent and require proof you don't live in Mexico permanently.</li>
    <li><strong>Entry denial:</strong> In rare cases, travelers with long border-run histories are denied entry.</li>
    <li><strong>No rights:</strong> As a tourist, you can't open a bank account, access IMSS, or build toward residency.</li>
  </ul>
  <h2>What Happens If You Overstay?</h2>
  <p>If you stay past your FMM expiry date:</p>
  <ul>
    <li><strong>Fine at exit:</strong> Approximately $30–$50 USD per excess day, paid at the airport or border crossing</li>
    <li><strong>No immediate deportation</strong> for first-time overstays</li>
    <li><strong>Record with INM:</strong> Overstays are logged and can complicate future residency applications</li>
    <li><strong>Potential entry ban:</strong> Repeated or very long overstays (months) can result in denial of future entry</li>
  </ul>
{IB('<strong><i class="bi bi-lightbulb me-2"></i>Tip:</strong> If you realize you\'ve overstayed, exit Mexico as soon as possible and pay the fine. Do not wait hoping it won\'t be noticed — it always is.')}
  <h2>The Better Solution: Mexican Residency</h2>
  <p>If you want to live in Mexico longer than 6 months per year, the right move is getting <strong>Temporary Residency</strong>. It gives you:</p>
  <ul>
    <li>Legal status to live in Mexico indefinitely (renewable annually)</li>
    <li>Right to open a Mexican bank account</li>
    <li>Access to IMSS public healthcare</li>
    <li>Mexican ID card (Residente Temporal card)</li>
    <li>Path to Permanent Residency after 4 years</li>
  </ul>
  <p>Requirements: approximately <strong>$4,400 USD/month</strong> in income or <strong>$72,000 USD</strong> in savings. MexVisa Pro processes your residency in 4 days through the Riviera Maya INM offices.</p>
  <h2>Digital Nomads: The Gray Area</h2>
  <p>If you work remotely for a foreign company while in Mexico as a tourist, you're technically in a gray area. You won't be arrested, but:</p>
  <ul>
    <li>After <strong>183 days in a calendar year</strong>, you become a Mexican tax resident and must register with SAT</li>
    <li>You cannot legally bill Mexican clients on a tourist visa</li>
    <li>You have no right to remain if asked to leave</li>
  </ul>
{CTA['en']("Mexico residency instead of border runs")}''',
        'es': f'''  <p>Al ingresar a México como turista, migración sella tu pasaporte con una <strong>FMM</strong> (Forma Migratoria Múltiple) que otorga hasta 180 días. Muchos visitantes asumen que pueden extender este plazo — no pueden. México no tiene mecanismo de extensión de visa turista.</p>
{IB('<strong><i class="bi bi-exclamation-triangle me-2"></i>Crítico:</strong> El límite de 180 días lo establece el agente de migración en el punto de entrada — pueden otorgar menos. Siempre revisa el número estampado en tu ingreso.')}
  <h2>¿Puedes Extender la Visa Turista de México?</h2>
  <p>No. México no tiene un proceso de extensión para la forma FMM. Las únicas opciones legales para quedarse más tiempo son:</p>
  <ul>
    <li><strong>Salir y reingresar</strong> (salida fronteriza) — obtener una nueva FMM al reingresar</li>
    <li><strong>Solicitar residencia</strong> — convertirte en residente legal</li>
  </ul>
  <h2>La Opción de Salida Fronteriza</h2>
  <p>Salir brevemente a Belice, Guatemala, EE.UU. u otro destino y reingresar reinicia tu reloj turístico. Sin embargo, hay riesgos:</p>
  <ul>
    <li><strong>Discreción del agente:</strong> Pueden otorgar menos de 180 días si tu pasaporte muestra entradas repetidas a México.</li>
    <li><strong>Detección de patrones:</strong> Si has hecho 3+ salidas fronterizas consecutivas, el agente puede cuestionarte.</li>
    <li><strong>Sin derechos:</strong> Como turista, no puedes abrir cuenta bancaria, acceder al IMSS ni construir hacia la residencia.</li>
  </ul>
  <h2>¿Qué Pasa si te Pasas del Tiempo Permitido?</h2>
  <ul>
    <li><strong>Multa al salir:</strong> Aproximadamente $30–$50 USD por día de exceso</li>
    <li><strong>Registro en el INM:</strong> Los overstays quedan registrados y pueden complicar futuras solicitudes de residencia</li>
    <li><strong>Posible prohibición de entrada</strong> en casos repetidos o muy prolongados</li>
  </ul>
  <h2>La Mejor Solución: Residencia Mexicana</h2>
  <p>Si quieres vivir en México más de 6 meses al año, lo correcto es obtener <strong>Residencia Temporal</strong>. Te da estatus legal indefinido, cuenta bancaria, IMSS, identificación y camino hacia la residencia permanente. Requisitos: ~<strong>$4,400 USD/mes</strong> o <strong>$72,000 USD</strong> en ahorros.</p>
{CTA['es']("residencia mexicana")}''',
        'ru': f'''  <p>При въезде в Мексику как турист иммиграционная служба ставит в паспорт разрешение <strong>FMM</strong> на срок до 180 дней. Продлить этот срок нельзя — официального механизма продления туристической визы не существует.</p>
{IB('<strong>Важно:</strong> 180-дневный лимит устанавливает пограничный офицер при въезде — он может дать и меньше. Всегда проверяйте штамп.')}
  <h2>Можно ли продлить туристическую визу в Мексике?</h2>
  <p>Нет. Единственные законные варианты для более длительного пребывания:</p>
  <ul>
    <li><strong>Выехать и вернуться</strong> (пограничная поездка) — получить новое FMM при въезде</li>
    <li><strong>Подать заявку на вид на жительство</strong></li>
  </ul>
  <h2>Пограничные поездки</h2>
  <p>Кратковременный выезд в Белиз, Гватемалу, США или другую страну и возвращение обнуляют туристический счётчик. Риски:</p>
  <ul>
    <li>Офицеры могут выдать менее 180 дней при частых повторных въездах</li>
    <li>В редких случаях — отказ во въезде</li>
    <li>Без прав: нет банковского счёта, IMSS, пути к резидентству</li>
  </ul>
  <h2>Последствия просрочки</h2>
  <ul>
    <li>Штраф при выезде: ~$30–$50 USD за каждый лишний день</li>
    <li>Запись в INM, осложняющая будущие заявки на резидентство</li>
    <li>При многократных или длительных просрочках — запрет на въезд</li>
  </ul>
  <h2>Лучшее решение: Мексиканское резидентство</h2>
  <p>Если вы хотите жить в Мексике более 6 месяцев в год, правильным шагом является получение <strong>временного вида на жительство</strong>. Требования: ~<strong>$4,400 USD/мес</strong> или <strong>$72,000 USD</strong> на счёту.</p>
{CTA['ru']("мексиканское резидентство")}''',
        'zh': f'''  <p>进入墨西哥作为游客时，移民局会在护照上盖章一个<strong>FMM</strong>（多重移民表格），最长授予180天居留。很多访客以为可以延期——实际上不行。墨西哥没有旅游签证延期机制。</p>
{IB('<strong>重要：</strong>180天限制由入境口岸的移民官员决定——他们可能给予更少天数。始终检查入境章上的日期。')}
  <h2>能延长墨西哥旅游签证吗？</h2>
  <p>不能。合法延长居留的唯一选项：</p>
  <ul>
    <li><strong>出境后重新入境</strong>（边境出行）——重新获得FMM许可</li>
    <li><strong>申请居留签证</strong>——成为合法居民</li>
  </ul>
  <h2>边境出行选项</h2>
  <p>短暂离开墨西哥（前往伯利兹、危地马拉、美国等）后重新入境可以重置旅游居留时间。风险：</p>
  <ul>
    <li>如护照显示频繁入境，移民官员可能给予少于180天</li>
    <li>极少情况下可能被拒绝入境</li>
    <li>旅游身份无法开设银行账户、访问IMSS或建立居留路径</li>
  </ul>
  <h2>逾期后果</h2>
  <ul>
    <li>出境时罚款：每超一天约30-50美元</li>
    <li>INM记录，可能影响未来居留申请</li>
    <li>多次或长期逾期可能导致未来被拒绝入境</li>
  </ul>
  <h2>更好的解决方案：墨西哥居留权</h2>
  <p>如果您希望每年在墨西哥居住超过6个月，正确做法是申请<strong>临时居留</strong>。要求：约<strong>4,400美元/月</strong>收入或<strong>72,000美元</strong>存款。</p>
{CTA['zh']("墨西哥居留权")}''',
    },
    'related': {
        'en':[('mexico-temporary-residency-guide','Mexico Temporary Residency Guide 2026'),('mexico-border-run-visa-run','Mexico Border Run Guide'),('digital-nomad-visa-mexico','Digital Nomad Visa Mexico')],
        'es':[('guia-residencia-temporal-mexico','Guía de Residencia Temporal México'),('salida-fronteriza-mexico','Salida Fronteriza México'),('digital-nomad-visa-mexico','Visa Nómada Digital México')],
        'ru':[('vremennoe-rezidentstvo-meksika','Временное резидентство Мексика'),('pogranichnyy-vyyezd-meksika','Пограничная поездка Мексика'),('tsifrovoy-nomad-viza-meksika','Виза для цифровых кочевников')],
        'zh':[('mexico-temporary-residency-guide','墨西哥临时居留指南'),('moxige-bianjing-chuxing','墨西哥边境出行指南'),('digital-nomad-visa-mexico','数字游民签证')],
    },
}

ARTICLES['family-reunification-visa-mexico'] = {
    'slugs':{'en':'family-reunification-visa-mexico','es':'visa-reunion-familiar-mexico','ru':'viza-dlya-semi-meksika','zh':'jiating-tuanju-qianzheng-moxige'},
    'title':{
        'en':'Family Reunification Visa Mexico 2026: Bring Your Family Legally',
        'es':'Visa Reunificación Familiar México 2026: Reúne a Tu Familia Legalmente',
        'ru':'Виза для воссоединения семьи в Мексике 2026',
        'zh':'墨西哥家庭团聚签证2026：合法接亲属来墨',
    },
    'desc':{
        'en':'Family reunification visa Mexico 2026 — how to bring spouse, children or parents to Mexico legally. INM process, documents, costs. Free consultation.',
        'es':'Visa reunificación familiar México 2026 — cómo traer cónyuge, hijos o padres legalmente. Proceso INM, documentos, costos. Consulta gratis.',
        'ru':'Виза для воссоединения семьи в Мексике 2026 — как привезти супруга, детей или родителей. Процесс INM, документы, стоимость.',
        'zh':'2026年墨西哥家庭团聚签证——如何合法接配偶、子女或父母来墨。INM流程、材料、费用。免费咨询。',
    },
    'h1':{
        'en':'Family Reunification Visa Mexico: <em>Bring Your Loved Ones</em>',
        'es':'Visa Reunificación Familiar México: <em>Reúne a Tu Familia</em>',
        'ru':'Виза для воссоединения семьи в Мексике: <em>Привезите близких</em>',
        'zh':'墨西哥家庭团聚签证：<em>让家人合法团聚</em>',
    },
    'lead':{
        'en':'If you hold Mexican residency or citizenship, you can sponsor your spouse, children under 18, or dependent parents for legal residency in Mexico.',
        'es':'Si tienes residencia o ciudadanía mexicana, puedes patrocinar a tu cónyuge, hijos menores de 18 años o padres dependientes para la residencia en México.',
        'ru':'Если у вас есть мексиканское резидентство или гражданство, вы можете спонсировать супруга, детей до 18 лет или родителей-иждивенцев.',
        'zh':'持有墨西哥居留权或国籍者，可为配偶、18岁以下子女或受抚养父母申办合法居留。',
    },
    'breadcrumb':{'en':'Family Reunification','es':'Reunificación Familiar','ru':'Воссоединение семьи','zh':'家庭团聚'},
    'faq':{
        'en':[
            ('Who qualifies as a family member for reunification?','Spouse (married or common-law), biological or adopted children under 18, and economically dependent parents of a Mexican resident or citizen.'),
            ('How long does the family reunification process take?','Typically 4–8 weeks from document submission to approved residency card. Processing at the consulate abroad takes 2–4 weeks.'),
            ('Does the sponsor need to be a Mexican citizen?','No. A temporary or permanent resident can sponsor immediate family members through INM.'),
            ('What income must the sponsor prove?','The sponsor must show sufficient income to support the family — generally $1,500–$2,500 USD/month depending on family size.'),
        ],
        'es':[
            ('¿Quién califica como familiar para la reunificación?','Cónyuge (casado o unión libre), hijos biológicos o adoptados menores de 18 años, y padres económicamente dependientes de un residente o ciudadano mexicano.'),
            ('¿Cuánto tiempo tarda el proceso de reunificación familiar?','Típicamente 4–8 semanas desde la presentación de documentos hasta la tarjeta de residencia aprobada.'),
            ('¿El patrocinador debe ser ciudadano mexicano?','No. Un residente temporal o permanente puede patrocinar a familiares directos a través del INM.'),
            ('¿Qué ingresos debe demostrar el patrocinador?','El patrocinador debe mostrar ingresos suficientes — generalmente $1,500–$2,500 USD/mes según el tamaño de la familia.'),
        ],
        'ru':[
            ('Кто считается членом семьи для воссоединения?','Супруг(а), дети до 18 лет и экономически зависимые родители мексиканского резидента или гражданина.'),
            ('Сколько занимает процесс воссоединения?','Обычно 4–8 недель от подачи документов до получения карты резидента.'),
            ('Должен ли спонсор быть гражданином Мексики?','Нет. Временный или постоянный резидент может спонсировать ближайших родственников.'),
            ('Какой доход должен подтвердить спонсор?','Достаточный для содержания семьи — как правило $1,500–$2,500 USD/месяц.'),
        ],
        'zh':[
            ('哪些亲属符合家庭团聚条件？','配偶（已婚或同居）、18岁以下亲生或收养子女，以及经济依赖墨西哥居民或公民的父母。'),
            ('家庭团聚流程需要多长时间？','从提交材料到获批居留卡通常需要4–8周。'),
            ('担保人必须是墨西哥公民吗？','不需要。临时或永久居民可通过INM为直系亲属担保。'),
            ('担保人需证明多少收入？','需证明足以养家的收入——通常为每月1,500–2,500美元。'),
        ],
    },
    'body':{
        'en':"""
<h2>Two Pathways for Family Reunification</h2>
<p>Mexico offers two main legal routes for family members of residents and citizens:</p>
<h3>1. Temporary Residency by Family Unity</h3>
<p>The most common route. If you hold <strong>temporary or permanent residency</strong>, your spouse, children under 18, and dependent parents can apply for temporary residency under the "family unity" category at a Mexican consulate in your home country.</p>
<h3>2. Direct Permanent Residency</h3>
<p>If you are a <strong>Mexican citizen</strong>, your foreign spouse and children can apply directly for permanent residency — skipping the temporary residency stage entirely.</p>

<h2>Required Documents</h2>
<ul>
  <li>Valid passport of the applicant</li>
  <li>Proof of family relationship (marriage certificate, birth certificate — apostilled)</li>
  <li>Copy of sponsor's Mexican residency card or passport</li>
  <li>Sponsor's proof of income (bank statements, payslips)</li>
  <li>Completed INM application form</li>
  <li>Recent passport-sized photos</li>
  <li>Payment of consular fee (~$36 USD)</li>
</ul>

<h2>Step-by-Step Process</h2>
<ol>
  <li><strong>Apostille documents</strong> in the country of origin</li>
  <li><strong>Book consulate appointment</strong> at the nearest Mexican embassy</li>
  <li><strong>Submit application</strong> and pay fee</li>
  <li><strong>Receive visa</strong> (sticker in passport, valid 180 days)</li>
  <li><strong>Enter Mexico</strong> and register with INM within 30 days</li>
  <li><strong>Receive residency card</strong> (CURP + residency card issued)</li>
</ol>

<div class="info-box"><p><strong>Important:</strong> All foreign documents must be apostilled and officially translated into Spanish by a certified translator (perito traductor).</p></div>

<h2>Costs</h2>
<p>Consular fee: ~<strong>$36 USD</strong> per person. INM registration in Mexico: ~<strong>$200–$300 USD</strong>. Translation and apostille per document: ~<strong>$50–$120 USD</strong>.</p>

<h2>Common Mistakes to Avoid</h2>
<ul>
  <li>Submitting documents without apostille — they will be rejected</li>
  <li>Waiting too long after arrival — you must register within 30 days</li>
  <li>Applying as a tourist and hoping to change status in-country (not possible for this category)</li>
</ul>
""",
        'es':"""
<h2>Dos Vías para la Reunificación Familiar</h2>
<p>México ofrece dos rutas legales principales para los familiares de residentes y ciudadanos:</p>
<h3>1. Residencia Temporal por Unidad Familiar</h3>
<p>La vía más común. Si tienes <strong>residencia temporal o permanente</strong>, tu cónyuge, hijos menores de 18 años y padres dependientes pueden solicitar residencia temporal bajo la categoría "unidad familiar" en un consulado mexicano en su país de origen.</p>
<h3>2. Residencia Permanente Directa</h3>
<p>Si eres <strong>ciudadano mexicano</strong>, tu cónyuge e hijos extranjeros pueden solicitar directamente la residencia permanente, saltándose la etapa de residencia temporal.</p>

<h2>Documentos Requeridos</h2>
<ul>
  <li>Pasaporte vigente del solicitante</li>
  <li>Prueba de relación familiar (acta de matrimonio, acta de nacimiento — apostillada)</li>
  <li>Copia de la tarjeta de residencia mexicana o pasaporte del patrocinador</li>
  <li>Comprobante de ingresos del patrocinador (estados de cuenta, recibos de sueldo)</li>
  <li>Formulario de solicitud INM completado</li>
  <li>Fotos de pasaporte recientes</li>
  <li>Pago de cuota consular (~$36 USD)</li>
</ul>

<h2>Proceso Paso a Paso</h2>
<ol>
  <li><strong>Apostillar documentos</strong> en el país de origen</li>
  <li><strong>Reservar cita consular</strong> en la embajada mexicana más cercana</li>
  <li><strong>Presentar solicitud</strong> y pagar cuota</li>
  <li><strong>Recibir visa</strong> (sello en pasaporte, válida 180 días)</li>
  <li><strong>Ingresar a México</strong> y registrarse en el INM en 30 días</li>
  <li><strong>Recibir tarjeta de residencia</strong> (CURP + tarjeta de residente)</li>
</ol>

<div class="info-box"><p><strong>Importante:</strong> Todos los documentos extranjeros deben apostillarse y traducirse oficialmente al español por un perito traductor certificado.</p></div>

<h2>Costos</h2>
<p>Cuota consular: ~<strong>$36 USD</strong> por persona. Registro INM en México: ~<strong>$200–$300 USD</strong>. Traducción y apostilla por documento: ~<strong>$50–$120 USD</strong>.</p>

<h2>Errores Comunes a Evitar</h2>
<ul>
  <li>Presentar documentos sin apostilla — serán rechazados</li>
  <li>Esperar demasiado tras la llegada — debes registrarte en 30 días</li>
  <li>Ingresar como turista esperando cambiar estatus en el país (no es posible para esta categoría)</li>
</ul>
""",
        'ru':"""
<h2>Два способа воссоединения семьи</h2>
<p>Мексика предлагает два основных законных пути для членов семей резидентов и граждан:</p>
<h3>1. Временное резидентство по семейному единству</h3>
<p>Самый распространённый вариант. Если у вас есть <strong>временное или постоянное резидентство</strong>, ваш супруг(а), дети до 18 лет и зависимые родители могут подать заявку на временное резидентство по категории «семейное единство» в мексиканском консульстве.</p>
<h3>2. Прямое постоянное резидентство</h3>
<p>Если вы <strong>гражданин Мексики</strong>, ваш иностранный супруг(а) и дети могут сразу подать на постоянное резидентство, минуя этап временного.</p>

<h2>Необходимые документы</h2>
<ul>
  <li>Действующий паспорт заявителя</li>
  <li>Подтверждение родства (свидетельство о браке, о рождении — с апостилем)</li>
  <li>Копия карты резидента или паспорта спонсора</li>
  <li>Подтверждение дохода спонсора (выписки со счёта, расчётные листки)</li>
  <li>Заполненная форма заявки INM</li>
  <li>Фотографии паспортного формата</li>
  <li>Оплата консульского сбора (~$36 USD)</li>
</ul>

<h2>Пошаговый процесс</h2>
<ol>
  <li><strong>Апостилировать документы</strong> в стране происхождения</li>
  <li><strong>Записаться на приём в консульство</strong></li>
  <li><strong>Подать заявку</strong> и оплатить сбор</li>
  <li><strong>Получить визу</strong> (штамп в паспорте, действительна 180 дней)</li>
  <li><strong>Въехать в Мексику</strong> и зарегистрироваться в INM в течение 30 дней</li>
  <li><strong>Получить карту резидента</strong> (CURP + карта резидента)</li>
</ol>

<div class="info-box"><p><strong>Важно:</strong> Все иностранные документы должны иметь апостиль и быть официально переведены на испанский язык сертифицированным переводчиком.</p></div>

<h2>Стоимость</h2>
<p>Консульский сбор: ~<strong>$36 USD</strong> с человека. Регистрация в INM: ~<strong>$200–$300 USD</strong>. Перевод и апостиль за документ: ~<strong>$50–$120 USD</strong>.</p>

<h2>Типичные ошибки</h2>
<ul>
  <li>Подача документов без апостиля — они будут отклонены</li>
  <li>Промедление после въезда — регистрация обязательна в течение 30 дней</li>
  <li>Въезд по туристической визе в надежде изменить статус внутри страны (для этой категории невозможно)</li>
</ul>
""",
        'zh':"""
<h2>家庭团聚的两条途径</h2>
<p>墨西哥为居民和公民的家属提供两条主要合法途径：</p>
<h3>1. 家庭统一类临时居留</h3>
<p>最常见的方式。持有<strong>临时或永久居留权</strong>者，其配偶、18岁以下子女及受抚养父母可在墨西哥驻外使领馆以"家庭统一"类别申请临时居留。</p>
<h3>2. 直接永久居留</h3>
<p>若您是<strong>墨西哥公民</strong>，其外籍配偶和子女可直接申请永久居留，无需经过临时居留阶段。</p>

<h2>所需材料</h2>
<ul>
  <li>申请人有效护照</li>
  <li>亲属关系证明（结婚证、出生证明——需加盖海牙认证/公证书）</li>
  <li>担保人墨西哥居留卡或护照复印件</li>
  <li>担保人收入证明（银行流水、工资单）</li>
  <li>已填写的INM申请表</li>
  <li>近期护照尺寸照片</li>
  <li>领事费（约36美元）</li>
</ul>

<h2>办理步骤</h2>
<ol>
  <li><strong>在原籍国办理文件认证</strong></li>
  <li><strong>预约最近的墨西哥使领馆</strong></li>
  <li><strong>提交申请</strong>并缴费</li>
  <li><strong>获得签证</strong>（护照贴纸，有效期180天）</li>
  <li><strong>入境墨西哥后30天内</strong>向INM登记</li>
  <li><strong>领取居留卡</strong>（含CURP编号）</li>
</ol>

<div class="info-box"><p><strong>注意：</strong>所有外国文件须经认证，并由认证译员翻译成西班牙语。</p></div>

<h2>费用</h2>
<p>领事费：每人约<strong>36美元</strong>。INM注册费：约<strong>200–300美元</strong>。每份文件翻译及认证：约<strong>50–120美元</strong>。</p>

<h2>常见错误</h2>
<ul>
  <li>未经认证提交文件——将被拒绝</li>
  <li>入境后拖延登记——必须在30天内完成</li>
  <li>以旅游签证入境后试图在墨境内变更身份（此类别不可行）</li>
</ul>
""",
    },
    'related':{
        'en':[('apostille-documents-mexico-immigration','Apostille Documents for Mexico'),('curp-foreigners-mexico','CURP for Foreigners'),('mexico-temporary-residency-guide','Temporary Residency Guide')],
        'es':[('apostilla-documentos-mexico-inmigracion','Apostilla para México'),('curp-extranjeros-mexico','CURP para Extranjeros'),('guia-residencia-temporal-mexico','Residencia Temporal')],
        'ru':[('apostil-dokumenty-meksika','Апостиль для Мексики'),('curp-dlya-inostrantsev-meksika','CURP для иностранцев'),('vremennoe-rezidentstvo-meksika','Временное резидентство')],
        'zh':[('gongzheng-wenjian-moxige-yimin','墨西哥文件认证'),('curp-waiguoren-moxige','外国人CURP'),('mexico-temporary-residency-guide','临时居留指南')],
    },
}

ARTICLES['rfc-registration-mexico-expats'] = {
    'slugs':{'en':'rfc-registration-mexico-expats','es':'rfc-registro-extranjeros-mexico','ru':'rfc-registratsiya-meksika','zh':'rfc-zhuche-waiguoren'},
    'title':{
        'en':'RFC Registration Mexico for Expats 2026: Tax ID Guide',
        'es':'RFC para Extranjeros en México 2026: Guía Completa de Registro',
        'ru':'Регистрация RFC в Мексике для иностранцев 2026',
        'zh':'2026年外国人在墨西哥注册RFC完整指南',
    },
    'desc':{
        'en':'RFC registration Mexico for expats 2026 — how to get your Mexican tax ID (RFC), required documents, SAT online process, and why you need it.',
        'es':'RFC para extranjeros en México 2026 — cómo obtener tu RFC, documentos necesarios, proceso en el SAT y por qué lo necesitas.',
        'ru':'RFC в Мексике для иностранцев 2026 — как получить мексиканский налоговый ID, документы, процесс в SAT.',
        'zh':'2026年外国人墨西哥RFC注册——如何获取税务ID、所需材料、SAT在线流程及必要性。',
    },
    'h1':{
        'en':'RFC Registration Mexico: <em>Your Tax ID as an Expat</em>',
        'es':'RFC para Extranjeros en México: <em>Tu ID Fiscal como Expatriado</em>',
        'ru':'RFC в Мексике: <em>Налоговый ID для иностранцев</em>',
        'zh':'墨西哥RFC注册：<em>外国人税务身份证</em>',
    },
    'lead':{
        'en':'The RFC (Registro Federal de Contribuyentes) is Mexico\'s tax identification number. As an expat, you need it to open bank accounts, sign contracts, invoice clients, and comply with SAT tax obligations.',
        'es':'El RFC (Registro Federal de Contribuyentes) es el número de identificación fiscal de México. Como expatriado, lo necesitas para abrir cuentas bancarias, firmar contratos, facturar y cumplir con el SAT.',
        'ru':'RFC — это налоговый идентификатор Мексики. Как иностранцу, он нужен для открытия банковских счетов, подписания договоров, выставления счетов и соблюдения налоговых требований SAT.',
        'zh':'RFC（联邦纳税人登记号）是墨西哥的税务识别号。作为外籍人士，开银行账户、签合同、开具发票及履行SAT税务义务均需要它。',
    },
    'breadcrumb':{'en':'RFC Registration','es':'Registro RFC','ru':'Регистрация RFC','zh':'RFC注册'},
    'faq':{
        'en':[
            ('Do all foreigners need an RFC in Mexico?','You need RFC if you are a tax resident (183+ days/year), earn income in Mexico, open a business, or need to issue formal invoices (facturas).'),
            ('Can I get RFC without permanent residency?','Yes. Temporary residents can register for RFC at the SAT office with their residency card and CURP.'),
            ('How long does RFC registration take?','Same-day at a SAT office with appointment. Online registration takes 1–3 business days.'),
            ('Is RFC the same as CURP?','No. CURP is a population registry number (identity). RFC is the tax ID used for fiscal purposes.'),
        ],
        'es':[
            ('¿Todos los extranjeros necesitan RFC en México?','Necesitas RFC si eres residente fiscal (183+ días/año), generas ingresos en México, tienes un negocio o necesitas emitir facturas.'),
            ('¿Puedo obtener RFC sin residencia permanente?','Sí. Los residentes temporales pueden registrarse en el SAT con su tarjeta de residencia y CURP.'),
            ('¿Cuánto tiempo tarda el registro de RFC?','El mismo día en una oficina SAT con cita. El registro en línea tarda 1–3 días hábiles.'),
            ('¿RFC es lo mismo que CURP?','No. El CURP es el número de registro de población (identidad). El RFC es el ID fiscal para propósitos fiscales.'),
        ],
        'ru':[
            ('Все ли иностранцы нуждаются в RFC в Мексике?','RFC нужен налоговым резидентам (183+ дней/год), получателям доходов в Мексике, владельцам бизнеса или тем, кто выставляет счета.'),
            ('Можно ли получить RFC без постоянного резидентства?','Да. Временные резиденты могут зарегистрироваться в SAT, имея карту резидента и CURP.'),
            ('Сколько занимает регистрация RFC?','В офисе SAT с записью — в тот же день. Онлайн-регистрация: 1–3 рабочих дня.'),
            ('RFC и CURP — одно и то же?','Нет. CURP — это номер реестра населения. RFC — налоговый идентификатор.'),
        ],
        'zh':[
            ('所有外国人在墨西哥都需要RFC吗？','若您是税务居民（每年183天以上）、在墨有收入、经营企业或需开具发票，则需要RFC。'),
            ('没有永久居留权可以申请RFC吗？','可以。临时居民持居留卡和CURP即可在SAT办公室注册。'),
            ('注册RFC需要多长时间？','预约后当天在SAT办理即可。在线注册需1–3个工作日。'),
            ('RFC和CURP一样吗？','不同。CURP是人口登记号（身份标识），RFC是用于税务目的的税务ID。'),
        ],
    },
    'body':{
        'en':"""
<h2>Who Needs RFC in Mexico?</h2>
<p>RFC is mandatory if you:</p>
<ul>
  <li>Stay in Mexico <strong>183+ days per calendar year</strong> (tax resident)</li>
  <li>Earn income from Mexican clients or employers</li>
  <li>Own or operate a business in Mexico</li>
  <li>Need to issue official invoices (facturas digitales)</li>
  <li>Want to open certain bank accounts or sign formal contracts</li>
</ul>
<div class="info-box"><p><strong>Note:</strong> Even if you work remotely for a foreign company, you may still become a Mexican tax resident after 183 days and need RFC to comply with SAT.</p></div>

<h2>Required Documents</h2>
<ul>
  <li>Valid passport (original + copy)</li>
  <li>Mexican residency card (temporary or permanent)</li>
  <li>CURP number (obtain this first if you don't have it)</li>
  <li>Proof of address in Mexico (utility bill, lease agreement)</li>
  <li>Completed SAT pre-registration form (from sat.gob.mx)</li>
</ul>

<h2>How to Register RFC</h2>
<h3>Option 1: SAT Office (Recommended)</h3>
<ol>
  <li>Pre-register at <strong>sat.gob.mx</strong> to get a confirmation number</li>
  <li>Book an appointment at your nearest SAT office</li>
  <li>Bring all documents to the appointment</li>
  <li>Receive your RFC on the same day</li>
</ol>
<h3>Option 2: Online via SAT Portal</h3>
<p>Available for those with an active e.firma (digital signature). If you don't have e.firma yet, start with the in-person process.</p>

<h2>RFC Format</h2>
<p>For individuals (personas físicas), RFC is a 13-character code: <strong>4 letters + 6 digits (birthdate) + 3 alphanumeric characters</strong>. Example: MAGO850312XY3</p>

<h2>After Getting RFC</h2>
<ul>
  <li>Register your tax regime (régimen fiscal) — most expats use "Régimen de actividades empresariales y profesionales" or "Plataformas tecnológicas"</li>
  <li>Obtain your <strong>e.firma</strong> (digital certificate) for filing returns online</li>
  <li>Set up <strong>Buzon Tributario</strong> (electronic mailbox) for official SAT communications</li>
  <li>File monthly/annual tax declarations as required</li>
</ul>

<h2>Tax Rates for Foreign Residents</h2>
<p>Mexico uses a progressive tax system for individuals: from <strong>1.92% up to 35%</strong> depending on annual income. Most expats earning $30,000–$80,000 USD/year fall in the 25–30% bracket. Tax treaties with 60+ countries prevent double taxation.</p>
""",
        'es':"""
<h2>¿Quién Necesita RFC en México?</h2>
<p>El RFC es obligatorio si:</p>
<ul>
  <li>Permaneces en México <strong>183+ días por año calendario</strong> (residente fiscal)</li>
  <li>Generas ingresos de clientes o empleadores mexicanos</li>
  <li>Tienes o diriges un negocio en México</li>
  <li>Necesitas emitir facturas digitales oficiales</li>
  <li>Quieres abrir ciertas cuentas bancarias o firmar contratos formales</li>
</ul>
<div class="info-box"><p><strong>Nota:</strong> Aunque trabajes remotamente para una empresa extranjera, puedes convertirte en residente fiscal mexicano después de 183 días y necesitar RFC para cumplir con el SAT.</p></div>

<h2>Documentos Requeridos</h2>
<ul>
  <li>Pasaporte vigente (original + copia)</li>
  <li>Tarjeta de residencia mexicana (temporal o permanente)</li>
  <li>Número de CURP</li>
  <li>Comprobante de domicilio en México (recibo de servicios, contrato de arrendamiento)</li>
  <li>Formulario de pre-registro del SAT completado (de sat.gob.mx)</li>
</ul>

<h2>Cómo Registrar tu RFC</h2>
<h3>Opción 1: Oficina SAT (Recomendado)</h3>
<ol>
  <li>Pre-regístrate en <strong>sat.gob.mx</strong> para obtener número de confirmación</li>
  <li>Agenda cita en la oficina SAT más cercana</li>
  <li>Lleva todos los documentos a tu cita</li>
  <li>Recibe tu RFC el mismo día</li>
</ol>
<h3>Opción 2: Portal SAT en Línea</h3>
<p>Disponible para quienes tienen e.firma activa. Si aún no tienes e.firma, comienza con el proceso presencial.</p>

<h2>Formato del RFC</h2>
<p>Para personas físicas, el RFC tiene 13 caracteres: <strong>4 letras + 6 dígitos (fecha de nacimiento) + 3 caracteres alfanuméricos</strong>. Ejemplo: MAGO850312XY3</p>

<h2>Después de Obtener tu RFC</h2>
<ul>
  <li>Registra tu régimen fiscal — la mayoría de expatriados usa "Régimen de actividades empresariales y profesionales" o "Plataformas tecnológicas"</li>
  <li>Obtén tu <strong>e.firma</strong> para presentar declaraciones en línea</li>
  <li>Configura tu <strong>Buzón Tributario</strong> para comunicaciones oficiales del SAT</li>
  <li>Presenta declaraciones mensuales/anuales según corresponda</li>
</ul>

<h2>Tasas Impositivas para Residentes Extranjeros</h2>
<p>México usa un sistema progresivo: desde <strong>1.92% hasta 35%</strong> según ingresos anuales. La mayoría de expatriados con ingresos de $30,000–$80,000 USD/año caen en el tramo del 25–30%. Los tratados fiscales con más de 60 países evitan la doble tributación.</p>
""",
        'ru':"""
<h2>Кому нужен RFC в Мексике?</h2>
<p>RFC обязателен, если вы:</p>
<ul>
  <li>Находитесь в Мексике <strong>183+ дней в год</strong> (налоговый резидент)</li>
  <li>Получаете доход от мексиканских клиентов или работодателей</li>
  <li>Владеете или управляете бизнесом в Мексике</li>
  <li>Должны выставлять официальные счета (facturas digitales)</li>
  <li>Хотите открыть банковский счёт или подписать формальный договор</li>
</ul>
<div class="info-box"><p><strong>Примечание:</strong> Даже работая удалённо на иностранную компанию, после 183 дней вы становитесь налоговым резидентом Мексики и обязаны получить RFC.</p></div>

<h2>Необходимые документы</h2>
<ul>
  <li>Действующий паспорт (оригинал + копия)</li>
  <li>Карта резидента Мексики (временного или постоянного)</li>
  <li>Номер CURP</li>
  <li>Подтверждение адреса в Мексике (квитанция за коммунальные услуги, договор аренды)</li>
  <li>Заполненная форма предварительной регистрации SAT (с sat.gob.mx)</li>
</ul>

<h2>Как зарегистрировать RFC</h2>
<h3>Вариант 1: Офис SAT (рекомендуется)</h3>
<ol>
  <li>Пройдите предварительную регистрацию на <strong>sat.gob.mx</strong></li>
  <li>Запишитесь на приём в ближайший офис SAT</li>
  <li>Принесите все документы</li>
  <li>Получите RFC в тот же день</li>
</ol>
<h3>Вариант 2: Онлайн через портал SAT</h3>
<p>Доступно для тех, у кого есть активная e.firma. Если её нет — начните с личного визита.</p>

<h2>Формат RFC</h2>
<p>Для физических лиц RFC состоит из 13 символов: <strong>4 буквы + 6 цифр (дата рождения) + 3 буквенно-цифровых символа</strong>. Пример: MAGO850312XY3</p>

<h2>После получения RFC</h2>
<ul>
  <li>Зарегистрируйте налоговый режим — большинство экспатов выбирают "Régimen de actividades empresariales y profesionales"</li>
  <li>Получите <strong>e.firma</strong> (цифровой сертификат) для подачи деклараций онлайн</li>
  <li>Настройте <strong>Buzón Tributario</strong> для официальных уведомлений SAT</li>
  <li>Подавайте ежемесячные/годовые декларации по мере необходимости</li>
</ul>

<h2>Налоговые ставки для иностранных резидентов</h2>
<p>Мексика использует прогрессивную систему: от <strong>1,92% до 35%</strong> в зависимости от годового дохода. Большинство экспатов с доходом $30,000–$80,000 USD/год платят 25–30%. Налоговые соглашения с 60+ странами исключают двойное налогообложение.</p>
""",
        'zh':"""
<h2>谁需要在墨西哥注册RFC？</h2>
<p>如果您符合以下情况，则需要RFC：</p>
<ul>
  <li>每年在墨西哥居住<strong>183天以上</strong>（税务居民）</li>
  <li>从墨西哥客户或雇主处获取收入</li>
  <li>在墨西哥拥有或经营企业</li>
  <li>需要开具正式发票（facturas digitales）</li>
  <li>希望开设某些银行账户或签署正式合同</li>
</ul>
<div class="info-box"><p><strong>注意：</strong>即使您为外国公司远程工作，在墨停留超183天后仍可能成为税务居民，需注册RFC以遵守SAT规定。</p></div>

<h2>所需材料</h2>
<ul>
  <li>有效护照（原件及复印件）</li>
  <li>墨西哥居留卡（临时或永久）</li>
  <li>CURP号码</li>
  <li>墨西哥住址证明（水电账单、租房合同）</li>
  <li>已填写的SAT预注册表（来自sat.gob.mx）</li>
</ul>

<h2>如何注册RFC</h2>
<h3>方式一：SAT办公室（推荐）</h3>
<ol>
  <li>在<strong>sat.gob.mx</strong>预注册，获取确认号</li>
  <li>预约最近的SAT办公室</li>
  <li>携带所有材料前往</li>
  <li>当天领取RFC</li>
</ol>
<h3>方式二：SAT在线门户</h3>
<p>适用于已有e.firma（数字签名）的人员。若尚无e.firma，请先到场办理。</p>

<h2>RFC格式</h2>
<p>个人RFC为13位字符：<strong>4个字母 + 6位数字（出生日期）+ 3位字母数字</strong>。示例：MAGO850312XY3</p>

<h2>获得RFC后</h2>
<ul>
  <li>注册税务制度——大多数外籍人士选择"Régimen de actividades empresariales y profesionales"</li>
  <li>获取<strong>e.firma</strong>（数字证书）以便在线申报</li>
  <li>设置<strong>Buzón Tributario</strong>接收SAT官方通知</li>
  <li>按要求提交月度/年度税务申报</li>
</ul>

<h2>外国居民税率</h2>
<p>墨西哥实行累进税制：从<strong>1.92%到35%</strong>不等。年收入3万–8万美元的外籍人士通常适用25–30%税率。与60多个国家的税收协定可避免双重征税。</p>
""",
    },
    'related':{
        'en':[('curp-foreigners-mexico','CURP for Foreigners'),('imss-health-insurance-foreigners-mexico','IMSS Health Insurance'),('digital-nomad-visa-mexico','Digital Nomad Visa Mexico')],
        'es':[('curp-extranjeros-mexico','CURP para Extranjeros'),('imss-seguro-salud-extranjeros-mexico','IMSS Seguro de Salud'),('digital-nomad-visa-mexico','Visa Nómada Digital')],
        'ru':[('curp-dlya-inostrantsev-meksika','CURP для иностранцев'),('imss-meditsinskaya-strakhovka-meksika','Страховка IMSS'),('tsifrovoy-nomad-viza-meksika','Виза цифрового кочевника')],
        'zh':[('curp-waiguoren-moxige','外国人CURP'),('imss-yiliao-baoxian-waiguoren-moxige','IMSS医疗保险'),('digital-nomad-visa-mexico','数字游民签证')],
    },
}

ARTICLES['residency-cancun-mexico'] = {
    'slugs':{'en':'residency-cancun-mexico','es':'residencia-cancun-mexico','ru':'rezidentstvo-kankun-meksika','zh':'kankunju-liu-moxige'},
    'title':{
        'en':'Residency in Cancún Mexico 2026: Complete Expat Guide',
        'es':'Residencia en Cancún México 2026: Guía Completa para Expatriados',
        'ru':'Резидентство в Канкуне, Мексика 2026: Полное руководство',
        'zh':'2026年坎昆墨西哥居留完整外籍指南',
    },
    'desc':{
        'en':'How to get residency in Cancún Mexico 2026 — INM office, costs, best neighborhoods, and expat lifestyle. Free immigration consultation.',
        'es':'Cómo obtener residencia en Cancún México 2026 — oficina INM, costos, mejores colonias y vida de expatriado. Consulta gratuita.',
        'ru':'Как получить резидентство в Канкуне 2026 — офис INM, расходы, районы для жизни, опыт экспатов.',
        'zh':'如何在坎昆获得墨西哥居留权2026——INM办公室、费用、最佳社区及外籍生活。',
    },
    'h1':{
        'en':'Residency in Cancún Mexico: <em>Your Caribbean Life Awaits</em>',
        'es':'Residencia en Cancún México: <em>Tu Vida en el Caribe te Espera</em>',
        'ru':'Резидентство в Канкуне: <em>Жизнь на Карибах ждёт вас</em>',
        'zh':'坎昆居留权：<em>加勒比海生活等待您</em>',
    },
    'lead':{
        'en':'Cancún offers the largest urban infrastructure on Mexico\'s Caribbean coast, with a major international airport, world-class hospitals, and a thriving expat community — making it one of the top relocation destinations.',
        'es':'Cancún ofrece la mayor infraestructura urbana en la costa caribeña de México, con un gran aeropuerto internacional, hospitales de clase mundial y una próspera comunidad de expatriados.',
        'ru':'Канкун предлагает крупнейшую городскую инфраструктуру на карибском побережье Мексики: международный аэропорт, больницы мирового класса и активное сообщество экспатов.',
        'zh':'坎昆拥有墨西哥加勒比海岸最完善的城市基础设施——国际机场、世界级医院和繁荣的外籍社区，是顶级移居目的地之一。',
    },
    'breadcrumb':{'en':'Residency Cancún','es':'Residencia Cancún','ru':'Резидентство Канкун','zh':'坎昆居留'},
    'faq':{
        'en':[
            ('Where is the INM office in Cancún?','The main INM Cancún office is at Av. Nader 1, Centro, Cancún, Q. Roo. Open Mon–Fri 9am–1pm. Appointment required.'),
            ('How much does it cost to live in Cancún as an expat?','A comfortable lifestyle runs $1,500–$2,500 USD/month for a couple, including rent, food, transport, and health insurance.'),
            ('Which neighborhoods are best for expats in Cancún?','Puerto Cancún, Zona Hotelera (hotel zone), and El Centro are popular. Puerto Cancún is gated community style with marinas.'),
            ('Is Cancún safe for expats?','The hotel zone and residential areas are generally safe. Like any large city, stay aware in downtown areas at night.'),
        ],
        'es':[
            ('¿Dónde está la oficina INM en Cancún?','La oficina principal del INM Cancún está en Av. Nader 1, Centro. Abierta lun–vie 9am–1pm. Se requiere cita.'),
            ('¿Cuánto cuesta vivir en Cancún como expatriado?','Un estilo de vida cómodo cuesta $1,500–$2,500 USD/mes para una pareja, incluyendo renta, comida, transporte y seguro médico.'),
            ('¿Qué colonias son mejores para expatriados en Cancún?','Puerto Cancún, Zona Hotelera y El Centro son populares. Puerto Cancún es estilo comunidad cerrada con marinas.'),
            ('¿Es seguro Cancún para expatriados?','La zona hotelera y las áreas residenciales son generalmente seguras. Como cualquier ciudad grande, mantente alerta en el centro por las noches.'),
        ],
        'ru':[
            ('Где находится офис INM в Канкуне?','Главный офис INM Канкун находится по адресу: Av. Nader 1, Centro, Cancún, Q. Roo. Пн–Пт 9:00–13:00. Требуется запись.'),
            ('Сколько стоит жизнь в Канкуне для экспата?','Комфортный образ жизни для пары: $1,500–$2,500 USD/месяц, включая аренду, питание, транспорт и медицинскую страховку.'),
            ('Какие районы лучше для экспатов в Канкуне?','Puerto Cancún, Zona Hotelera и El Centro. Puerto Cancún — закрытые жилые комплексы с марина.'),
            ('Безопасен ли Канкун для экспатов?','Туристическая зона и жилые районы в целом безопасны. Как в любом крупном городе, ночью в центре сохраняйте бдительность.'),
        ],
        'zh':[
            ('坎昆的INM办公室在哪里？','坎昆INM主办公室位于Av. Nader 1, Centro, Cancún, Q. Roo。周一至周五9:00–13:00开放，需提前预约。'),
            ('外籍人士在坎昆的生活费用是多少？','一对夫妇舒适生活每月约需1,500–2,500美元，包括租金、餐饮、交通和医疗保险。'),
            ('坎昆哪些社区最适合外籍人士？','Puerto Cancún、酒店区（Zona Hotelera）和市中心（El Centro）较受欢迎。Puerto Cancún为封闭式社区，带有游艇码头。'),
            ('坎昆对外籍人士安全吗？','酒店区和住宅区总体安全。如同任何大城市，夜晚在市中心需保持警惕。'),
        ],
    },
    'body':{
        'en':"""
<h2>Why Choose Cancún for Residency?</h2>
<p>Cancún is the commercial and transportation hub of the Yucatán Peninsula, offering advantages that smaller towns can't match:</p>
<ul>
  <li><strong>International airport</strong> — direct flights to 60+ cities in the Americas and Europe</li>
  <li><strong>Medical infrastructure</strong> — Hospiten, Amerimed, Galenia hospitals with English-speaking staff</li>
  <li><strong>Schools</strong> — international schools offering IB and US curriculum</li>
  <li><strong>Banking</strong> — all major Mexican and international banks represented</li>
  <li><strong>Cost advantage</strong> — 20–30% lower cost of living than Tulum or Playa del Carmen for similar quality</li>
</ul>

<h2>INM Process in Cancún</h2>
<p>The Cancún INM office handles residency applications for Quintana Roo state. The process is the same as nationally:</p>
<ol>
  <li>Obtain visa from Mexican consulate abroad (unless already in Mexico on tourist entry)</li>
  <li>Book INM appointment at Av. Nader 1</li>
  <li>Submit biometrics and documents</li>
  <li>Receive temporary or permanent residency card in 4–8 weeks</li>
</ol>
<div class="info-box"><p><strong>Tip:</strong> Appointments at the Cancún INM fill up quickly. Book 2–3 weeks in advance at gob.mx/inm.</p></div>

<h2>Neighborhoods for Expats</h2>
<h3>Puerto Cancún</h3>
<p>Premium gated community north of the hotel zone. Marina, golf course, luxury condos. Monthly rents: $1,200–$3,000 USD.</p>
<h3>Zona Hotelera (Hotel Zone)</h3>
<p>The strip along the Caribbean lagoon. Condos with beach access, walking distance to restaurants and entertainment. Rents: $900–$2,500 USD/month.</p>
<h3>Supermanzanas (SM) – Downtown</h3>
<p>Where locals live. More affordable ($400–$900 USD/month), authentic Mexican neighborhoods, near government services and SAT office.</p>

<h2>Cost of Living Breakdown</h2>
<ul>
  <li>1BR condo rental: $500–$1,200 USD/month</li>
  <li>Groceries for 2: $300–$500 USD/month</li>
  <li>Utilities (electricity high in summer due to AC): $80–$200 USD/month</li>
  <li>IMSS voluntary health insurance: ~$100 USD/month</li>
  <li>Transport (car or Uber): $100–$200 USD/month</li>
</ul>

<h2>Practical Tips for New Residents</h2>
<ul>
  <li>Open a <strong>BBVA or HSBC</strong> account — both have English-speaking staff in Cancún</li>
  <li>Get CFE (electricity) in your name early — the bill is needed for RFC and various registrations</li>
  <li>Join <strong>Facebook groups</strong> like "Expats in Cancún" for housing, recommendations and community</li>
  <li>Hurricane season is June–November — invest in a good weather app and know your evacuation routes</li>
</ul>
""",
        'es':"""
<h2>¿Por Qué Elegir Cancún para Residir?</h2>
<p>Cancún es el hub comercial y de transporte de la Península de Yucatán, ofreciendo ventajas que las ciudades más pequeñas no pueden igualar:</p>
<ul>
  <li><strong>Aeropuerto internacional</strong> — vuelos directos a 60+ ciudades en América y Europa</li>
  <li><strong>Infraestructura médica</strong> — hospitales Hospiten, Amerimed, Galenia con personal anglohablante</li>
  <li><strong>Colegios</strong> — escuelas internacionales con currículos IB y estadounidense</li>
  <li><strong>Banca</strong> — todos los principales bancos mexicanos e internacionales</li>
  <li><strong>Ventaja de costo</strong> — 20–30% menor costo de vida que Tulum o Playa del Carmen para calidad similar</li>
</ul>

<h2>Proceso INM en Cancún</h2>
<p>La oficina INM de Cancún maneja solicitudes de residencia para el estado de Quintana Roo:</p>
<ol>
  <li>Obtén visa en el consulado mexicano en el extranjero</li>
  <li>Agenda cita en INM, Av. Nader 1</li>
  <li>Presenta biometría y documentos</li>
  <li>Recibe tarjeta de residencia en 4–8 semanas</li>
</ol>
<div class="info-box"><p><strong>Consejo:</strong> Las citas en el INM de Cancún se llenan rápido. Reserva con 2–3 semanas de anticipación en gob.mx/inm.</p></div>

<h2>Colonias para Expatriados</h2>
<h3>Puerto Cancún</h3>
<p>Comunidad cerrada premium al norte de la zona hotelera. Marina, campo de golf, condominios de lujo. Rentas mensuales: $1,200–$3,000 USD.</p>
<h3>Zona Hotelera</h3>
<p>El corredor junto a la laguna del Caribe. Condos con acceso a playa, a pie de restaurantes y entretenimiento. Rentas: $900–$2,500 USD/mes.</p>
<h3>Supermanzanas (SM) – Centro</h3>
<p>Donde viven los locales. Más asequible ($400–$900 USD/mes), auténticos vecindarios mexicanos, cerca de servicios gubernamentales y la oficina SAT.</p>

<h2>Desglose del Costo de Vida</h2>
<ul>
  <li>Renta de condo 1 hab: $500–$1,200 USD/mes</li>
  <li>Supermercado para 2: $300–$500 USD/mes</li>
  <li>Servicios (electricidad alta en verano por AC): $80–$200 USD/mes</li>
  <li>IMSS seguro de salud voluntario: ~$100 USD/mes</li>
  <li>Transporte (auto o Uber): $100–$200 USD/mes</li>
</ul>
""",
        'ru':"""
<h2>Почему выбрать Канкун для резидентства?</h2>
<p>Канкун — торговый и транспортный хаб полуострова Юкатан с преимуществами, недоступными в небольших городах:</p>
<ul>
  <li><strong>Международный аэропорт</strong> — прямые рейсы в 60+ городов Америки и Европы</li>
  <li><strong>Медицинская инфраструктура</strong> — больницы Hospiten, Amerimed, Galenia с англоязычным персоналом</li>
  <li><strong>Школы</strong> — международные школы с программами IB и по стандартам США</li>
  <li><strong>Банки</strong> — все крупные мексиканские и международные банки</li>
  <li><strong>Ценовое преимущество</strong> — стоимость жизни на 20–30% ниже, чем в Тулуме или Плайя-дель-Кармен</li>
</ul>

<h2>Процесс получения резидентства в Канкуне</h2>
<ol>
  <li>Получить визу в мексиканском консульстве за рубежом</li>
  <li>Записаться в INM по адресу Av. Nader 1</li>
  <li>Сдать биометрию и документы</li>
  <li>Получить карту резидента через 4–8 недель</li>
</ol>
<div class="info-box"><p><strong>Совет:</strong> Запись в INM Канкуна заполняется быстро. Бронируйте за 2–3 недели на gob.mx/inm.</p></div>

<h2>Районы для экспатов</h2>
<h3>Puerto Cancún</h3>
<p>Элитный закрытый жилой комплекс к северу от туристической зоны. Марина, поле для гольфа, люксовые апартаменты. Аренда: $1,200–$3,000 USD/месяц.</p>
<h3>Zona Hotelera (Туристическая зона)</h3>
<p>Полоса вдоль Карибской лагуны. Апартаменты с выходом к пляжу. Аренда: $900–$2,500 USD/месяц.</p>
<h3>Supermanzanas – Центр</h3>
<p>Районы для местных жителей. Дешевле ($400–$900 USD/месяц), рядом с государственными службами.</p>

<h2>Расходы на жизнь</h2>
<ul>
  <li>Аренда 1-комнатных апартаментов: $500–$1,200 USD/месяц</li>
  <li>Продукты для двоих: $300–$500 USD/месяц</li>
  <li>Коммунальные услуги (электричество летом высокое из-за кондиционеров): $80–$200 USD/месяц</li>
  <li>Добровольная страховка IMSS: ~$100 USD/месяц</li>
  <li>Транспорт (машина или Uber): $100–$200 USD/месяц</li>
</ul>
""",
        'zh':"""
<h2>为什么选择坎昆居住？</h2>
<p>坎昆是尤卡坦半岛的商业和交通枢纽，拥有小城市无法比拟的优势：</p>
<ul>
  <li><strong>国际机场</strong>——直飞美洲和欧洲60多个城市</li>
  <li><strong>医疗基础设施</strong>——Hospiten、Amerimed、Galenia医院，配备英语工作人员</li>
  <li><strong>学校</strong>——提供IB和美国课程的国际学校</li>
  <li><strong>银行</strong>——所有主要墨西哥及国际银行均有分支</li>
  <li><strong>成本优势</strong>——同等质量下，生活成本比图卢姆或卡门海滩低20–30%</li>
</ul>

<h2>坎昆INM办理流程</h2>
<ol>
  <li>在墨西哥驻外使领馆获取签证</li>
  <li>预约Av. Nader 1的INM办公室</li>
  <li>提交生物信息和材料</li>
  <li>4–8周内领取居留卡</li>
</ol>
<div class="info-box"><p><strong>提示：</strong>坎昆INM预约很快排满，请提前2–3周在gob.mx/inm预约。</p></div>

<h2>外籍人士社区</h2>
<h3>Puerto Cancún</h3>
<p>酒店区北部的高端封闭社区，带游艇码头和高尔夫球场。月租：1,200–3,000美元。</p>
<h3>酒店区（Zona Hotelera）</h3>
<p>沿加勒比湖的地带，海滩公寓步行可达餐厅和娱乐场所。月租：900–2,500美元。</p>
<h3>Supermanzanas（市中心）</h3>
<p>本地人聚居地，更实惠（400–900美元/月），靠近政府服务机构。</p>

<h2>生活费用明细</h2>
<ul>
  <li>一居室公寓租金：500–1,200美元/月</li>
  <li>两人餐饮：300–500美元/月</li>
  <li>公用事业（夏季空调导致电费较高）：80–200美元/月</li>
  <li>IMSS自愿医疗保险：约100美元/月</li>
  <li>交通（自驾或Uber）：100–200美元/月</li>
</ul>
""",
    },
    'related':{
        'en':[('residency-tulum-mexico','Residency in Tulum'),('inm-office-playa-del-carmen','INM Office Playa del Carmen'),('mexico-temporary-residency-guide','Temporary Residency Guide')],
        'es':[('residencia-tulum-mexico','Residencia en Tulum'),('oficina-inm-playa-del-carmen','Oficina INM Playa del Carmen'),('guia-residencia-temporal-mexico','Guía de Residencia Temporal')],
        'ru':[('rezidentstvo-tulum-meksika','Резидентство в Тулуме'),('ofis-inm-playa-del-karmen','Офис INM Плайя-дель-Кармен'),('vremennoe-rezidentstvo-meksika','Временное резидентство')],
        'zh':[('tulumju-liu-moxige','图卢姆居留'),('inm-bangongshi-playa-del-carmen','普拉亚德尔卡门INM办公室'),('mexico-temporary-residency-guide','临时居留指南')],
    },
}

ARTICLES['residency-tulum-mexico'] = {
    'slugs':{'en':'residency-tulum-mexico','es':'residencia-tulum-mexico','ru':'rezidentstvo-tulum-meksika','zh':'tulumju-liu-moxige'},
    'title':{
        'en':'Residency in Tulum Mexico 2026: Bohemian Paradise for Expats',
        'es':'Residencia en Tulum México 2026: Paraíso Bohemio para Expatriados',
        'ru':'Резидентство в Тулуме, Мексика 2026: Бохемский рай для экспатов',
        'zh':'2026年图卢姆墨西哥居留：外籍人士的波西米亚天堂',
    },
    'desc':{
        'en':'How to get residency in Tulum Mexico 2026 — INM process, best areas, costs, internet quality, and expat community tips.',
        'es':'Cómo obtener residencia en Tulum México 2026 — proceso INM, mejores zonas, costos, calidad de internet y consejos para expatriados.',
        'ru':'Как получить резидентство в Тулуме 2026 — процесс INM, лучшие районы, расходы, интернет и советы экспатов.',
        'zh':'如何在图卢姆获得墨西哥居留权2026——INM流程、最佳区域、费用、网络质量及外籍建议。',
    },
    'h1':{
        'en':'Residency in Tulum Mexico: <em>Live in the Jungle by the Sea</em>',
        'es':'Residencia en Tulum México: <em>Vive en la Selva Junto al Mar</em>',
        'ru':'Резидентство в Тулуме: <em>Жизнь в джунглях у моря</em>',
        'zh':'图卢姆居留：<em>在海边丛林中生活</em>',
    },
    'lead':{
        'en':'Tulum has evolved from a backpacker destination into a world-class wellness and digital nomad hub — now with a new international airport, improved infrastructure, and a growing permanent expat community.',
        'es':'Tulum ha evolucionado de destino mochilero a hub de bienestar y nómadas digitales de clase mundial — ahora con nuevo aeropuerto internacional e infraestructura mejorada.',
        'ru':'Тулум превратился из места для бэкпекеров в центр велнеса и цифровых кочевников мирового класса — с новым международным аэропортом и улучшенной инфраструктурой.',
        'zh':'图卢姆已从背包客胜地发展为世界级健康和数字游民中心——拥有新国际机场、完善基础设施和不断增长的外籍永久社区。',
    },
    'breadcrumb':{'en':'Residency Tulum','es':'Residencia Tulum','ru':'Резидентство Тулум','zh':'图卢姆居留'},
    'faq':{
        'en':[
            ('Where do I process residency if I live in Tulum?','Tulum has a small INM delegation. For full residency processing, many residents go to the Playa del Carmen or Cancún INM offices.'),
            ('Is internet reliable in Tulum?','The urban zone (Tulum Pueblo) has fiber optic available from Telmex/Megacable. The jungle hotel zone has slower, satellite-based connections.'),
            ('Is Tulum more expensive than Cancún?','Yes. Tulum costs 20–40% more for comparable housing due to its boutique/luxury positioning and lower supply of standard apartments.'),
            ('Is Tulum safe?','The tourist areas are generally safe. The new airport and highway infrastructure have improved security presence significantly since 2024.'),
        ],
        'es':[
            ('¿Dónde tramito la residencia si vivo en Tulum?','Tulum tiene una pequeña delegación INM. Para el trámite completo, muchos residentes van a las oficinas INM de Playa del Carmen o Cancún.'),
            ('¿Es confiable el internet en Tulum?','La zona urbana (Tulum Pueblo) tiene fibra óptica disponible de Telmex/Megacable. La zona hotelera de la selva tiene conexiones más lentas vía satélite.'),
            ('¿Es Tulum más caro que Cancún?','Sí. Tulum cuesta 20–40% más por vivienda comparable debido a su posicionamiento boutique/lujo.'),
            ('¿Es seguro Tulum?','Las áreas turísticas son generalmente seguras. El nuevo aeropuerto e infraestructura vial han mejorado significativamente la presencia de seguridad desde 2024.'),
        ],
        'ru':[
            ('Где оформлять резидентство, если я живу в Тулуме?','В Тулуме есть небольшое представительство INM. Для полного оформления многие резиденты едут в офисы INM в Плайя-дель-Кармен или Канкуне.'),
            ('Надёжен ли интернет в Тулуме?','В городской зоне (Tulum Pueblo) доступна оптоволоконная сеть от Telmex/Megacable. В отельной зоне джунглей — более медленное спутниковое соединение.'),
            ('Тулум дороже Канкуна?','Да, примерно на 20–40% дороже из-за позиционирования как бутик/люкс.'),
            ('Безопасен ли Тулум?','Туристические зоны в целом безопасны. Новый аэропорт и дорожная инфраструктура значительно улучшили ситуацию с безопасностью с 2024 года.'),
        ],
        'zh':[
            ('住在图卢姆，在哪里办理居留手续？','图卢姆有小型INM办事处，但完整办理通常需前往卡门海滩或坎昆的INM办公室。'),
            ('图卢姆的网络可靠吗？','城区（Tulum Pueblo）可使用Telmex/Megacable的光纤网络。丛林酒店区网络较慢，依赖卫星连接。'),
            ('图卢姆比坎昆贵吗？','是的，同类住房贵20–40%，因其精品/奢华定位和标准公寓供应较少。'),
            ('图卢姆安全吗？','旅游区总体安全。自2024年起，新机场和公路基础设施大幅改善了安全保障。'),
        ],
    },
    'body':{
        'en':"""
<h2>Two Zones of Tulum</h2>
<p>Understanding Tulum's geography is essential before choosing where to live:</p>
<h3>Tulum Pueblo (Urban Zone)</h3>
<p>The town itself, 3 km inland from the beach. More affordable, practical for daily life, has supermarkets, hardware stores, SAT office, and fiber internet. Most permanent expat residents live here.</p>
<h3>Tulum Hotel Zone (Selva Zone)</h3>
<p>The famous beachfront strip with boutique hotels, yoga studios, and jungle villas. Beautiful but expensive and less practical for permanent living — lower internet quality, higher prices, flood risk in rainy season.</p>

<h2>Cost of Living in Tulum</h2>
<ul>
  <li>1BR apartment (Pueblo): $700–$1,200 USD/month</li>
  <li>Jungle villa (hotel zone): $2,000–$5,000 USD/month</li>
  <li>Groceries for 2: $400–$600 USD/month (organic/health food premium)</li>
  <li>Eating out: $15–$40 USD per meal at mid-range restaurants</li>
  <li>Scooter rental: $150–$200 USD/month (most common transport)</li>
</ul>

<div class="info-box"><p><strong>Key fact:</strong> Tulum has fewer standard chain supermarkets — many expats do a monthly Costco or Walmart run to Playa del Carmen (45 min) or Cancún (1.5 hrs) for bulk goods.</p></div>

<h2>INM Registration for Tulum Residents</h2>
<p>The closest well-staffed INM office is in <strong>Playa del Carmen</strong> (45 min drive). The Tulum delegation can handle some paperwork but appointment availability is limited.</p>
<p>Process remains the same: obtain visa abroad → enter Mexico → register with INM within 30 days → receive residency card.</p>

<h2>Lifestyle and Community</h2>
<p>Tulum attracts:</p>
<ul>
  <li>Digital nomads and remote workers (good coworking spaces in Pueblo)</li>
  <li>Wellness entrepreneurs (yoga instructors, healers, retreat organizers)</li>
  <li>Artists, influencers, and creatives</li>
  <li>Investors in Riviera Maya real estate</li>
</ul>
<p>The expat Facebook group "Expats Tulum" has 15,000+ members and is the best resource for housing, recommendations, and community events.</p>

<h2>New Tulum International Airport (2024)</h2>
<p>The Felipe Carrillo Puerto International Airport opened in December 2023, with commercial flights from 2024. Offers direct routes to Mexico City, Monterrey, and growing international connections — eliminating the need to fly through Cancún for many destinations.</p>
""",
        'es':"""
<h2>Las Dos Zonas de Tulum</h2>
<p>Entender la geografía de Tulum es esencial antes de elegir dónde vivir:</p>
<h3>Tulum Pueblo (Zona Urbana)</h3>
<p>El pueblo en sí, a 3 km de la playa. Más asequible y práctico para la vida diaria: supermercados, ferreterías, oficina SAT e internet de fibra. Aquí vive la mayoría de los expatriados permanentes.</p>
<h3>Zona Hotelera de Tulum (Zona Selva)</h3>
<p>El famoso corredor frente al mar con hoteles boutique, estudios de yoga y villas en la selva. Hermoso pero caro y menos práctico para vivir permanentemente.</p>

<h2>Costo de Vida en Tulum</h2>
<ul>
  <li>Departamento 1 hab (Pueblo): $700–$1,200 USD/mes</li>
  <li>Villa en la selva (zona hotelera): $2,000–$5,000 USD/mes</li>
  <li>Supermercado para 2: $400–$600 USD/mes (prima por alimentos orgánicos/saludables)</li>
  <li>Comer fuera: $15–$40 USD por comida en restaurantes de gama media</li>
  <li>Renta de scooter: $150–$200 USD/mes (transporte más común)</li>
</ul>

<div class="info-box"><p><strong>Dato clave:</strong> Tulum tiene menos supermercados de cadena — muchos expatriados van mensualmente a Costco o Walmart en Playa del Carmen (45 min) o Cancún (1.5 hrs).</p></div>

<h2>Registro INM para Residentes de Tulum</h2>
<p>La oficina INM más cercana y con buen personal está en <strong>Playa del Carmen</strong> (45 min en auto). La delegación de Tulum puede manejar algunos trámites, pero la disponibilidad de citas es limitada.</p>
""",
        'ru':"""
<h2>Две зоны Тулума</h2>
<p>Понимание географии Тулума необходимо перед выбором места жительства:</p>
<h3>Tulum Pueblo (Городская зона)</h3>
<p>Сам город, в 3 км от пляжа. Доступнее и практичнее: супермаркеты, строительные магазины, офис SAT, оптический интернет. Здесь живёт большинство постоянных экспатов.</p>
<h3>Отельная зона Тулума (Зона сельвы)</h3>
<p>Знаменитый прибрежный коридор с бутик-отелями и виллами в джунглях. Красивый, но дорогой и менее практичный для постоянного проживания.</p>

<h2>Стоимость жизни в Тулуме</h2>
<ul>
  <li>1-комнатная квартира (Pueblo): $700–$1,200 USD/месяц</li>
  <li>Вилла в джунглях (отельная зона): $2,000–$5,000 USD/месяц</li>
  <li>Продукты для двоих: $400–$600 USD/месяц</li>
  <li>Питание в кафе: $15–$40 USD за обед в ресторане среднего класса</li>
  <li>Аренда скутера: $150–$200 USD/месяц (самый распространённый транспорт)</li>
</ul>

<div class="info-box"><p><strong>Важный факт:</strong> В Тулуме мало сетевых супермаркетов — многие экспаты ежемесячно ездят в Costco или Walmart в Плайя-дель-Кармен (45 мин) или Канкун (1,5 ч).</p></div>

<h2>Регистрация в INM для жителей Тулума</h2>
<p>Ближайший укомплектованный офис INM находится в <strong>Плайя-дель-Кармен</strong> (45 мин езды). Делегация Тулума может обработать часть документов, но запись ограничена.</p>
""",
        'zh':"""
<h2>图卢姆的两个区域</h2>
<p>选择居住地前，了解图卢姆的地理分布至关重要：</p>
<h3>Tulum Pueblo（城区）</h3>
<p>距海滩3公里的市区，更实惠实用：有超市、五金店、SAT办公室和光纤网络。大多数长期外籍居民住在这里。</p>
<h3>图卢姆酒店区（丛林区）</h3>
<p>著名的精品酒店、瑜伽工作室和丛林别墅沿线地带。美丽但昂贵，不太适合长期居住。</p>

<h2>图卢姆生活费用</h2>
<ul>
  <li>一居室公寓（Pueblo）：700–1,200美元/月</li>
  <li>丛林别墅（酒店区）：2,000–5,000美元/月</li>
  <li>两人餐饮：400–600美元/月（有机/健康食品溢价）</li>
  <li>外出就餐：中档餐厅每餐15–40美元</li>
  <li>摩托车租金：150–200美元/月（最常用交通方式）</li>
</ul>

<div class="info-box"><p><strong>关键信息：</strong>图卢姆连锁超市较少——许多外籍人士每月前往卡门海滩（45分钟）或坎昆（1.5小时）的Costco或Walmart采购。</p></div>

<h2>图卢姆居民的INM注册</h2>
<p>最近的完善INM办公室位于<strong>卡门海滩</strong>（驾车45分钟）。图卢姆办事处可处理部分手续，但预约名额有限。</p>
""",
    },
    'related':{
        'en':[('residency-cancun-mexico','Residency in Cancún'),('inm-office-playa-del-carmen','INM Office Playa del Carmen'),('digital-nomad-visa-mexico','Digital Nomad Visa Mexico')],
        'es':[('residencia-cancun-mexico','Residencia en Cancún'),('oficina-inm-playa-del-carmen','Oficina INM Playa del Carmen'),('digital-nomad-visa-mexico','Visa Nómada Digital')],
        'ru':[('rezidentstvo-kankun-meksika','Резидентство в Канкуне'),('ofis-inm-playa-del-karmen','Офис INM Плайя-дель-Кармен'),('tsifrovoy-nomad-viza-meksika','Виза цифрового кочевника')],
        'zh':[('kankunju-liu-moxige','坎昆居留'),('inm-bangongshi-playa-del-carmen','普拉亚德尔卡门INM'),('digital-nomad-visa-mexico','数字游民签证')],
    },
}

ARTICLES['inm-office-playa-del-carmen'] = {
    'slugs':{'en':'inm-office-playa-del-carmen','es':'oficina-inm-playa-del-carmen','ru':'ofis-inm-playa-del-karmen','zh':'inm-bangongshi-playa-del-carmen'},
    'title':{
        'en':'INM Office Playa del Carmen 2026: Complete Guide for Expats',
        'es':'Oficina INM Playa del Carmen 2026: Guía Completa para Expatriados',
        'ru':'Офис INM в Плайя-дель-Кармен 2026: Полное руководство',
        'zh':'2026年卡门海滩INM办公室完整指南',
    },
    'desc':{
        'en':'INM office Playa del Carmen — address, hours, how to book appointments, required documents, and tips for a smooth residency process in 2026.',
        'es':'Oficina INM Playa del Carmen — dirección, horarios, cómo agendar citas, documentos requeridos y consejos para un proceso de residencia sin problemas en 2026.',
        'ru':'Офис INM в Плайя-дель-Кармен — адрес, часы работы, запись, документы и советы для успешного оформления резидентства в 2026 году.',
        'zh':'卡门海滩INM办公室——地址、开放时间、预约方式、所需材料及2026年顺利办理居留的建议。',
    },
    'h1':{
        'en':'INM Office Playa del Carmen: <em>Everything You Need to Know</em>',
        'es':'Oficina INM Playa del Carmen: <em>Todo lo que Necesitas Saber</em>',
        'ru':'Офис INM в Плайя-дель-Кармен: <em>Всё что нужно знать</em>',
        'zh':'卡门海滩INM办公室：<em>您需要了解的一切</em>',
    },
    'lead':{
        'en':'The Playa del Carmen INM office is the primary immigration authority for residents of Playa del Carmen, Tulum, Akumal, and surrounding areas. Here\'s how to navigate it efficiently.',
        'es':'La oficina INM de Playa del Carmen es la autoridad migratoria principal para residentes de Playa del Carmen, Tulum, Akumal y áreas circundantes.',
        'ru':'Офис INM в Плайя-дель-Кармен — главный иммиграционный орган для жителей Плайя-дель-Кармен, Тулума, Акумаля и прилегающих районов.',
        'zh':'卡门海滩INM办公室是卡门海滩、图卢姆、阿库马尔及周边地区居民的主要移民管理机构。',
    },
    'breadcrumb':{'en':'INM Playa del Carmen','es':'INM Playa del Carmen','ru':'INM Плайя-дель-Кармен','zh':'卡门海滩INM'},
    'faq':{
        'en':[
            ('What is the address of INM Playa del Carmen?','INM Playa del Carmen is located at Calle 10 Norte esq. Av. 25, Playa del Carmen, Q. Roo. Near the ADO bus terminal.'),
            ('What are the INM Playa del Carmen office hours?','Monday to Friday, 9:00 AM – 1:00 PM. Appointments are mandatory — walk-ins are generally not accepted.'),
            ('How do I book an INM appointment online?','Go to gob.mx/inm → "Citas" → select "Quintana Roo" → "Playa del Carmen." Slots open 2–3 weeks in advance.'),
            ('Can I do my residency renewal at any INM office?','Generally yes, but it\'s recommended to use the office in your registered area of residence.'),
        ],
        'es':[
            ('¿Cuál es la dirección del INM Playa del Carmen?','El INM Playa del Carmen está ubicado en Calle 10 Norte esq. Av. 25, Playa del Carmen, Q. Roo. Cerca de la terminal ADO.'),
            ('¿Cuál es el horario de la oficina INM Playa del Carmen?','Lunes a viernes, 9:00 AM – 1:00 PM. Las citas son obligatorias — generalmente no se aceptan personas sin cita.'),
            ('¿Cómo agendo una cita INM en línea?','Ve a gob.mx/inm → "Citas" → selecciona "Quintana Roo" → "Playa del Carmen." Los lugares se abren con 2–3 semanas de anticipación.'),
            ('¿Puedo renovar mi residencia en cualquier oficina INM?','Generalmente sí, pero se recomienda usar la oficina de tu área de residencia registrada.'),
        ],
        'ru':[
            ('Какой адрес офиса INM в Плайя-дель-Кармен?','INM Плайя-дель-Кармен расположен по адресу: Calle 10 Norte esq. Av. 25, Playa del Carmen, Q. Roo. Рядом с автовокзалом ADO.'),
            ('Каков режим работы офиса INM в Плайя-дель-Кармен?','Понедельник–пятница, 9:00–13:00. Запись обязательна — без записи, как правило, не принимают.'),
            ('Как записаться на приём в INM онлайн?','На сайте gob.mx/inm → "Citas" → выберите "Quintana Roo" → "Playa del Carmen." Слоты открываются за 2–3 недели.'),
            ('Можно ли продлить резидентство в любом офисе INM?','В целом да, но рекомендуется обращаться в офис по месту регистрации.'),
        ],
        'zh':[
            ('卡门海滩INM办公室的地址是什么？','卡门海滩INM位于Calle 10 Norte esq. Av. 25, Playa del Carmen, Q. Roo。靠近ADO巴士总站。'),
            ('卡门海滩INM办公室的开放时间？','周一至周五，上午9:00–下午1:00。必须提前预约——通常不接受现场办理。'),
            ('如何在线预约INM？','访问gob.mx/inm → "Citas" → 选择"Quintana Roo" → "Playa del Carmen"。预约位置提前2–3周开放。'),
            ('可以在任何INM办公室办理居留续签吗？','一般可以，但建议在您注册居住地的办公室办理。'),
        ],
    },
    'body':{
        'en':"""
<h2>Office Details</h2>
<ul>
  <li><strong>Address:</strong> Calle 10 Norte esq. Av. 25, Playa del Carmen, Quintana Roo</li>
  <li><strong>Hours:</strong> Monday–Friday, 9:00 AM – 1:00 PM</li>
  <li><strong>Appointments:</strong> Required — book at gob.mx/inm</li>
  <li><strong>Phone:</strong> Check the official INM website for current numbers</li>
</ul>

<h2>How to Book Your Appointment</h2>
<ol>
  <li>Go to <strong>gob.mx/inm</strong></li>
  <li>Click "Citas para trámites migratorios"</li>
  <li>Select the type of procedure (residency application, renewal, card pickup, etc.)</li>
  <li>Choose "Quintana Roo" → "Playa del Carmen"</li>
  <li>Select available date and time</li>
  <li>Fill in personal details and confirm</li>
  <li>Save your confirmation number (required at the appointment)</li>
</ol>

<div class="info-box"><p><strong>Tip:</strong> Appointments release around midnight. Check the portal at 12:00–12:30 AM for the best chance of getting slots 2–3 weeks out.</p></div>

<h2>Documents to Bring</h2>
<h3>For New Residency Application</h3>
<ul>
  <li>Original passport + 2 copies of all pages</li>
  <li>Immigration visa (from the consulate abroad)</li>
  <li>Completed INM application form (FMM)</li>
  <li>2 passport-sized photos (white background)</li>
  <li>Proof of address (utility bill or lease)</li>
  <li>Payment receipt for immigration fees</li>
</ul>
<h3>For Residency Renewal</h3>
<ul>
  <li>Original passport + copies</li>
  <li>Current residency card (original)</li>
  <li>Proof of economic solvency (bank statements)</li>
  <li>Proof of address</li>
  <li>Application form</li>
</ul>

<h2>INM Fee Schedule 2026</h2>
<p>Immigration fees (derechos migratorios) are set annually by the Mexican government and paid at authorized banks before your appointment:</p>
<ul>
  <li>Temporary residency (1 year): ~$3,800 MXN (~$190 USD)</li>
  <li>Temporary residency (2 years): ~$7,000 MXN (~$350 USD)</li>
  <li>Permanent residency: ~$4,500 MXN (~$225 USD)</li>
  <li>Card replacement: ~$1,200 MXN (~$60 USD)</li>
</ul>

<h2>Common Issues and How to Avoid Them</h2>
<ul>
  <li><strong>Wrong document copies</strong> — bring copies of every passport page, not just the photo page</li>
  <li><strong>Photos not compliant</strong> — white background only, no glasses, recent</li>
  <li><strong>Missing bank payment</strong> — pay the INM fee at BBVA, Santander, or Banamex before arrival</li>
  <li><strong>Late arrival</strong> — arrive 15 minutes early; late appointments may be cancelled</li>
</ul>

<h2>After Your Appointment</h2>
<p>You'll receive a receipt and a date to return and pick up your residency card (typically 4–6 weeks later). Bring the same receipt and passport to the pickup appointment.</p>
""",
        'es':"""
<h2>Detalles de la Oficina</h2>
<ul>
  <li><strong>Dirección:</strong> Calle 10 Norte esq. Av. 25, Playa del Carmen, Quintana Roo</li>
  <li><strong>Horario:</strong> Lunes–Viernes, 9:00 AM – 1:00 PM</li>
  <li><strong>Citas:</strong> Obligatorias — agenda en gob.mx/inm</li>
</ul>

<h2>Cómo Agendar tu Cita</h2>
<ol>
  <li>Ve a <strong>gob.mx/inm</strong></li>
  <li>Clic en "Citas para trámites migratorios"</li>
  <li>Selecciona el tipo de trámite</li>
  <li>Elige "Quintana Roo" → "Playa del Carmen"</li>
  <li>Selecciona fecha y hora disponibles</li>
  <li>Completa datos personales y confirma</li>
  <li>Guarda tu número de confirmación</li>
</ol>

<div class="info-box"><p><strong>Consejo:</strong> Las citas se liberan alrededor de la medianoche. Revisa el portal a las 12:00–12:30 AM para mejores oportunidades con 2–3 semanas de anticipación.</p></div>

<h2>Documentos a Traer</h2>
<h3>Para Nueva Solicitud de Residencia</h3>
<ul>
  <li>Pasaporte original + 2 copias de todas las páginas</li>
  <li>Visa de inmigración (del consulado en el extranjero)</li>
  <li>Formulario INM completado (FMM)</li>
  <li>2 fotos tamaño pasaporte (fondo blanco)</li>
  <li>Comprobante de domicilio</li>
  <li>Recibo de pago de derechos migratorios</li>
</ul>

<h2>Cuotas INM 2026</h2>
<ul>
  <li>Residencia temporal (1 año): ~$3,800 MXN (~$190 USD)</li>
  <li>Residencia temporal (2 años): ~$7,000 MXN (~$350 USD)</li>
  <li>Residencia permanente: ~$4,500 MXN (~$225 USD)</li>
  <li>Reposición de tarjeta: ~$1,200 MXN (~$60 USD)</li>
</ul>

<h2>Errores Comunes y Cómo Evitarlos</h2>
<ul>
  <li><strong>Copias incorrectas</strong> — lleva copias de todas las páginas del pasaporte, no solo la foto</li>
  <li><strong>Fotos no conformes</strong> — fondo blanco obligatorio, sin lentes, recientes</li>
  <li><strong>Pago bancario faltante</strong> — paga antes de llegar en BBVA, Santander o Banamex</li>
  <li><strong>Llegada tarde</strong> — llega 15 minutos antes; las citas tardías pueden cancelarse</li>
</ul>
""",
        'ru':"""
<h2>Детали офиса</h2>
<ul>
  <li><strong>Адрес:</strong> Calle 10 Norte esq. Av. 25, Playa del Carmen, Quintana Roo</li>
  <li><strong>Часы работы:</strong> Пн–Пт, 9:00–13:00</li>
  <li><strong>Запись:</strong> Обязательна — на gob.mx/inm</li>
</ul>

<h2>Как записаться</h2>
<ol>
  <li>Перейдите на <strong>gob.mx/inm</strong></li>
  <li>Нажмите "Citas para trámites migratorios"</li>
  <li>Выберите тип процедуры</li>
  <li>Выберите "Quintana Roo" → "Playa del Carmen"</li>
  <li>Выберите дату и время</li>
  <li>Заполните личные данные и подтвердите</li>
  <li>Сохраните номер подтверждения</li>
</ol>

<div class="info-box"><p><strong>Совет:</strong> Слоты открываются около полуночи. Проверяйте портал в 00:00–00:30 для получения записи за 2–3 недели.</p></div>

<h2>Документы для визита</h2>
<h3>Первичная заявка на резидентство</h3>
<ul>
  <li>Оригинал паспорта + 2 копии всех страниц</li>
  <li>Иммиграционная виза (из консульства)</li>
  <li>Заполненная форма INM (FMM)</li>
  <li>2 фото формата паспорта (белый фон)</li>
  <li>Подтверждение адреса</li>
  <li>Квитанция об оплате иммиграционного сбора</li>
</ul>

<h2>Тарифы INM 2026</h2>
<ul>
  <li>Временное резидентство (1 год): ~$3,800 MXN (~$190 USD)</li>
  <li>Временное резидентство (2 года): ~$7,000 MXN (~$350 USD)</li>
  <li>Постоянное резидентство: ~$4,500 MXN (~$225 USD)</li>
  <li>Замена карты: ~$1,200 MXN (~$60 USD)</li>
</ul>
""",
        'zh':"""
<h2>办公室详情</h2>
<ul>
  <li><strong>地址：</strong>Calle 10 Norte esq. Av. 25, Playa del Carmen, Quintana Roo</li>
  <li><strong>开放时间：</strong>周一至周五，上午9:00–下午1:00</li>
  <li><strong>预约：</strong>必须——在gob.mx/inm预约</li>
</ul>

<h2>如何预约</h2>
<ol>
  <li>访问<strong>gob.mx/inm</strong></li>
  <li>点击"Citas para trámites migratorios"</li>
  <li>选择手续类型</li>
  <li>选择"Quintana Roo"→"Playa del Carmen"</li>
  <li>选择可用日期和时间</li>
  <li>填写个人信息并确认</li>
  <li>保存确认号码</li>
</ol>

<div class="info-box"><p><strong>提示：</strong>预约位置在午夜前后开放。建议在00:00–00:30查看门户网站，获取2–3周后的预约位置。</p></div>

<h2>携带材料</h2>
<h3>新居留申请</h3>
<ul>
  <li>护照原件及所有页面复印件（2份）</li>
  <li>移民签证（来自驻外使领馆）</li>
  <li>已填写的INM申请表（FMM）</li>
  <li>2张护照尺寸照片（白色背景）</li>
  <li>地址证明</li>
  <li>移民费用缴费收据</li>
</ul>

<h2>2026年INM费用</h2>
<ul>
  <li>临时居留（1年）：约3,800墨西哥比索（约190美元）</li>
  <li>临时居留（2年）：约7,000墨西哥比索（约350美元）</li>
  <li>永久居留：约4,500墨西哥比索（约225美元）</li>
  <li>补办居留卡：约1,200墨西哥比索（约60美元）</li>
</ul>
""",
    },
    'related':{
        'en':[('residency-cancun-mexico','Residency in Cancún'),('residency-tulum-mexico','Residency in Tulum'),('mexico-temporary-residency-guide','Temporary Residency Guide')],
        'es':[('residencia-cancun-mexico','Residencia en Cancún'),('residencia-tulum-mexico','Residencia en Tulum'),('guia-residencia-temporal-mexico','Guía de Residencia Temporal')],
        'ru':[('rezidentstvo-kankun-meksika','Резидентство в Канкуне'),('rezidentstvo-tulum-meksika','Резидентство в Тулуме'),('vremennoe-rezidentstvo-meksika','Временное резидентство')],
        'zh':[('kankunju-liu-moxige','坎昆居留'),('tulumju-liu-moxige','图卢姆居留'),('mexico-temporary-residency-guide','临时居留指南')],
    },
}

ARTICLES['mexico-vs-panama-vs-costa-rica-retirement'] = {
    'slugs':{'en':'mexico-vs-panama-vs-costa-rica-retirement','es':'jubilarse-mexico-vs-panama-vs-costa-rica','ru':'meksika-panama-kosta-rika-pensiya','zh':'moxige-panama-hasilajia-yanglaobijiao'},
    'title':{
        'en':'Mexico vs Panama vs Costa Rica Retirement 2026: Which Is Best?',
        'es':'Jubilarse en México vs Panamá vs Costa Rica 2026: ¿Cuál Es el Mejor?',
        'ru':'Мексика vs Панама vs Коста-Рика для пенсии 2026: Сравнение',
        'zh':'2026年墨西哥vs巴拿马vs哥斯达黎加退休对比：哪个最好？',
    },
    'desc':{
        'en':'Mexico vs Panama vs Costa Rica for retirement 2026 — cost of living, visa requirements, healthcare, safety, and climate compared side by side.',
        'es':'México vs Panamá vs Costa Rica para jubilarse 2026 — costo de vida, requisitos de visa, salud, seguridad y clima comparados.',
        'ru':'Мексика vs Панама vs Коста-Рика для пенсии 2026 — стоимость жизни, визовые требования, здравоохранение, безопасность и климат.',
        'zh':'2026年退休地点对比：墨西哥vs巴拿马vs哥斯达黎加——生活成本、签证要求、医疗、安全与气候全面比较。',
    },
    'h1':{
        'en':'Mexico vs Panama vs Costa Rica Retirement: <em>The Full Comparison</em>',
        'es':'Jubilarse en México vs Panamá vs Costa Rica: <em>La Comparación Completa</em>',
        'ru':'Мексика vs Панама vs Коста-Рика для пенсии: <em>Полное сравнение</em>',
        'zh':'墨西哥vs巴拿马vs哥斯达黎加退休：<em>全面对比</em>',
    },
    'lead':{
        'en':'Three of Latin America\'s top retirement destinations each offer distinct advantages. This comparison helps you decide which fits your lifestyle, budget, and priorities.',
        'es':'Tres de los principales destinos de jubilación de América Latina ofrecen ventajas distintas. Esta comparación te ayuda a decidir cuál se adapta a tu estilo de vida y presupuesto.',
        'ru':'Три ведущих направления для пенсии в Латинской Америке — у каждого свои преимущества. Это сравнение поможет выбрать подходящее.',
        'zh':'拉丁美洲三大退休目的地各有独特优势。本对比帮助您根据生活方式、预算和优先级做出选择。',
    },
    'breadcrumb':{'en':'Mexico vs Panama vs Costa Rica','es':'México vs Panamá vs Costa Rica','ru':'Мексика vs Панама vs Коста-Рика','zh':'三国退休对比'},
    'faq':{
        'en':[
            ('Which country is cheapest for retirement?','Mexico\'s Riviera Maya and Panama\'s interior offer the lowest costs. Costa Rica is the most expensive of the three.'),
            ('Which has the best healthcare?','All three have good private healthcare. Mexico\'s Riviera Maya hospitals (Cancún) are excellent and affordable. Panama City has the most internationally accredited hospitals.'),
            ('Which has the easiest retirement visa?','Panama\'s Pensionado visa is the most generous — it offers discounts on everything from restaurants to airlines. Mexico requires income proof but no age minimum.'),
            ('Which is safest?','Costa Rica consistently ranks as the safest. Mexico\'s tourist/expat zones are safe. Panama City is safe in expat areas; some rural areas less so.'),
        ],
        'es':[
            ('¿Qué país es más barato para jubilarse?','La Riviera Maya de México y el interior de Panamá ofrecen los costos más bajos. Costa Rica es el más caro de los tres.'),
            ('¿Cuál tiene mejor atención médica?','Los tres tienen buena atención médica privada. Los hospitales de Cancún son excelentes y accesibles. Ciudad de Panamá tiene los hospitales más acreditados internacionalmente.'),
            ('¿Cuál tiene la visa de jubilación más fácil?','La visa Pensionado de Panamá es la más generosa — ofrece descuentos en restaurantes, aerolíneas y más. México requiere prueba de ingresos pero sin mínimo de edad.'),
            ('¿Cuál es el más seguro?','Costa Rica se clasifica consistentemente como el más seguro. Las zonas turísticas de México son seguras. Ciudad de Panamá es segura en áreas de expatriados.'),
        ],
        'ru':[
            ('Какая страна самая дешёвая для пенсии?','Ривьера Майя в Мексике и внутренние районы Панамы предлагают самые низкие расходы. Коста-Рика самая дорогая из трёх.'),
            ('В какой стране лучше здравоохранение?','Во всех трёх есть хорошая частная медицина. Больницы в Канкуне отличны и доступны. Панама-Сити имеет наибольшее число международно аккредитованных больниц.'),
            ('Где проще пенсионная виза?','Панамская виза Pensionado самая щедрая — даёт скидки везде. В Мексике требуется подтверждение дохода, возрастного минимума нет.'),
            ('Где безопаснее?','Коста-Рика стабильно считается самой безопасной. Туристические зоны Мексики безопасны. Панама-Сити безопасна в экспат-районах.'),
        ],
        'zh':[
            ('哪个国家退休生活成本最低？','墨西哥里维埃拉玛雅和巴拿马内陆地区费用最低。哥斯达黎加是三国中最贵的。'),
            ('哪个国家医疗条件最好？','三国均有良好的私立医疗。坎昆医院优秀且实惠。巴拿马城拥有最多国际认证医院。'),
            ('哪个国家的退休签证最容易获得？','巴拿马的Pensionado签证最优惠——餐厅、航空公司等均有折扣。墨西哥需证明收入，无年龄下限。'),
            ('哪个国家最安全？','哥斯达黎加持续被评为最安全。墨西哥旅游/外籍区域安全。巴拿马城外籍社区区域安全。'),
        ],
    },
    'body':{
        'en':"""
<h2>Quick Comparison Table</h2>
<ul>
  <li><strong>Cost of living:</strong> Mexico ★★★★☆ | Panama ★★★★☆ | Costa Rica ★★★☆☆</li>
  <li><strong>Healthcare quality:</strong> Mexico ★★★★☆ | Panama ★★★★★ | Costa Rica ★★★★☆</li>
  <li><strong>Retirement visa ease:</strong> Mexico ★★★★☆ | Panama ★★★★★ | Costa Rica ★★★☆☆</li>
  <li><strong>Safety:</strong> Mexico ★★★☆☆ | Panama ★★★★☆ | Costa Rica ★★★★★</li>
  <li><strong>Climate:</strong> Mexico ★★★★★ | Panama ★★★★☆ | Costa Rica ★★★★☆</li>
  <li><strong>US flight access:</strong> Mexico ★★★★★ | Panama ★★★★☆ | Costa Rica ★★★★☆</li>
</ul>

<h2>Mexico (Riviera Maya)</h2>
<h3>Pros</h3>
<ul>
  <li>No specific retirement visa needed — qualify via income or asset proof</li>
  <li>Direct flights to 200+ US/Canada cities</li>
  <li>Caribbean beaches, diverse culture</li>
  <li>World-class private hospitals in Cancún</li>
  <li>Large English-speaking expat community</li>
</ul>
<h3>Cons</h3>
<ul>
  <li>Public healthcare (IMSS) quality varies — most expats pay private</li>
  <li>Hurricane risk June–November</li>
  <li>Some areas have higher crime than expat zones</li>
</ul>
<p><strong>Income requirement:</strong> ~$2,500 USD/month for temporary residency</p>
<p><strong>Monthly budget (comfortable):</strong> $1,800–$3,500 USD/month (couple)</p>

<h2>Panama</h2>
<h3>Pros</h3>
<ul>
  <li><strong>Pensionado visa</strong> — best retirement visa in Latin America with 20–50% discounts on flights, hotels, restaurants, hospitals</li>
  <li>No tax on foreign income</li>
  <li>USD currency — no exchange risk</li>
  <li>JCI-accredited hospitals in Panama City</li>
  <li>Modern infrastructure and banking</li>
</ul>
<h3>Cons</h3>
<ul>
  <li>Less cultural variety than Mexico</li>
  <li>Hot and humid year-round with heavy rainy season</li>
  <li>Less direct flight options from Europe</li>
</ul>
<p><strong>Income requirement:</strong> $1,000 USD/month pension or investment income</p>
<p><strong>Monthly budget:</strong> $2,000–$3,500 USD/month (couple, Panama City)</p>

<h2>Costa Rica</h2>
<h3>Pros</h3>
<ul>
  <li>Consistently ranked safest country in Central America</li>
  <li>Stable democracy, no military since 1948</li>
  <li>CAJA public health system (access with residency)</li>
  <li>Excellent biodiversity and outdoor lifestyle</li>
</ul>
<h3>Cons</h3>
<ul>
  <li>Most expensive of the three</li>
  <li>Rentista visa requires $2,500/month income</li>
  <li>Bureaucracy slower than Mexico or Panama</li>
  <li>Less beach variety — Pacific coast dominant</li>
</ul>
<p><strong>Income requirement:</strong> $2,500 USD/month (Rentista visa)</p>
<p><strong>Monthly budget:</strong> $2,500–$4,500 USD/month (couple)</p>

<div class="info-box"><p><strong>Bottom line:</strong> Mexico wins on location and US flight access. Panama wins on retirement visa benefits and no foreign income tax. Costa Rica wins on safety and political stability. For Riviera Maya lovers, Mexico is the clear choice.</p></div>
""",
        'es':"""
<h2>Tabla de Comparación Rápida</h2>
<ul>
  <li><strong>Costo de vida:</strong> México ★★★★☆ | Panamá ★★★★☆ | Costa Rica ★★★☆☆</li>
  <li><strong>Calidad de salud:</strong> México ★★★★☆ | Panamá ★★★★★ | Costa Rica ★★★★☆</li>
  <li><strong>Facilidad de visa:</strong> México ★★★★☆ | Panamá ★★★★★ | Costa Rica ★★★☆☆</li>
  <li><strong>Seguridad:</strong> México ★★★☆☆ | Panamá ★★★★☆ | Costa Rica ★★★★★</li>
  <li><strong>Clima:</strong> México ★★★★★ | Panamá ★★★★☆ | Costa Rica ★★★★☆</li>
  <li><strong>Acceso aéreo a EE.UU.:</strong> México ★★★★★ | Panamá ★★★★☆ | Costa Rica ★★★★☆</li>
</ul>

<h2>México (Riviera Maya)</h2>
<ul>
  <li>No se necesita visa específica de jubilación — calificas con prueba de ingresos</li>
  <li>Vuelos directos a 200+ ciudades en EE.UU./Canadá</li>
  <li>Playas caribeñas y cultura diversa</li>
  <li>Hospitales privados de primer nivel en Cancún</li>
  <li>Gran comunidad de expatriados anglohablantes</li>
</ul>
<p><strong>Requisito de ingresos:</strong> ~$2,500 USD/mes para residencia temporal</p>
<p><strong>Presupuesto mensual (cómodo):</strong> $1,800–$3,500 USD/mes (pareja)</p>

<h2>Panamá</h2>
<ul>
  <li><strong>Visa Pensionado</strong> — la mejor visa de jubilación de América Latina con 20–50% de descuento en vuelos, hoteles, restaurantes y hospitales</li>
  <li>Sin impuesto sobre ingresos extranjeros</li>
  <li>Moneda USD — sin riesgo cambiario</li>
  <li>Hospitales acreditados JCI en Ciudad de Panamá</li>
</ul>
<p><strong>Requisito de ingresos:</strong> $1,000 USD/mes de pensión o ingresos de inversión</p>
<p><strong>Presupuesto mensual:</strong> $2,000–$3,500 USD/mes (pareja)</p>

<h2>Costa Rica</h2>
<ul>
  <li>Clasificado consistentemente como el país más seguro de Centroamérica</li>
  <li>Democracia estable, sin ejército desde 1948</li>
  <li>Sistema de salud público CAJA (acceso con residencia)</li>
  <li>Excelente biodiversidad y estilo de vida al aire libre</li>
</ul>
<p><strong>Requisito de ingresos:</strong> $2,500 USD/mes (visa Rentista)</p>
<p><strong>Presupuesto mensual:</strong> $2,500–$4,500 USD/mes (pareja)</p>

<div class="info-box"><p><strong>Conclusión:</strong> México gana en ubicación y acceso a vuelos. Panamá gana en beneficios de visa de jubilación y sin impuesto a ingresos extranjeros. Costa Rica gana en seguridad y estabilidad política.</p></div>
""",
        'ru':"""
<h2>Быстрое сравнение</h2>
<ul>
  <li><strong>Стоимость жизни:</strong> Мексика ★★★★☆ | Панама ★★★★☆ | Коста-Рика ★★★☆☆</li>
  <li><strong>Здравоохранение:</strong> Мексика ★★★★☆ | Панама ★★★★★ | Коста-Рика ★★★★☆</li>
  <li><strong>Простота визы:</strong> Мексика ★★★★☆ | Панама ★★★★★ | Коста-Рика ★★★☆☆</li>
  <li><strong>Безопасность:</strong> Мексика ★★★☆☆ | Панама ★★★★☆ | Коста-Рика ★★★★★</li>
  <li><strong>Климат:</strong> Мексика ★★★★★ | Панама ★★★★☆ | Коста-Рика ★★★★☆</li>
</ul>

<h2>Мексика (Ривьера Майя)</h2>
<ul>
  <li>Специальная пенсионная виза не нужна — достаточно подтверждения дохода</li>
  <li>Прямые рейсы в 200+ городов США/Канады</li>
  <li>Карибские пляжи, разнообразная культура</li>
  <li>Частные больницы мирового класса в Канкуне</li>
</ul>
<p><strong>Требование к доходу:</strong> ~$2,500 USD/месяц для временного резидентства</p>
<p><strong>Ежемесячный бюджет:</strong> $1,800–$3,500 USD/месяц (пара)</p>

<h2>Панама</h2>
<ul>
  <li><strong>Виза Pensionado</strong> — лучшая пенсионная виза в Латинской Америке: скидки 20–50% на рейсы, отели, рестораны и больницы</li>
  <li>Нет налога на иностранный доход</li>
  <li>Валюта USD — нет валютного риска</li>
  <li>Международно аккредитованные больницы в Панама-Сити</li>
</ul>
<p><strong>Требование к доходу:</strong> $1,000 USD/месяц из пенсии или инвестиций</p>

<h2>Коста-Рика</h2>
<ul>
  <li>Самая безопасная страна в Центральной Америке</li>
  <li>Стабильная демократия, без армии с 1948 года</li>
  <li>Публичная система здравоохранения CAJA</li>
</ul>
<p><strong>Требование к доходу:</strong> $2,500 USD/месяц (виза Rentista)</p>

<div class="info-box"><p><strong>Итог:</strong> Мексика лидирует по местоположению и авиадоступности. Панама — по пенсионным льготам и отсутствию налога на иностранный доход. Коста-Рика — по безопасности.</p></div>
""",
        'zh':"""
<h2>快速对比</h2>
<ul>
  <li><strong>生活成本：</strong>墨西哥 ★★★★☆ | 巴拿马 ★★★★☆ | 哥斯达黎加 ★★★☆☆</li>
  <li><strong>医疗质量：</strong>墨西哥 ★★★★☆ | 巴拿马 ★★★★★ | 哥斯达黎加 ★★★★☆</li>
  <li><strong>签证便利度：</strong>墨西哥 ★★★★☆ | 巴拿马 ★★★★★ | 哥斯达黎加 ★★★☆☆</li>
  <li><strong>安全性：</strong>墨西哥 ★★★☆☆ | 巴拿马 ★★★★☆ | 哥斯达黎加 ★★★★★</li>
  <li><strong>气候：</strong>墨西哥 ★★★★★ | 巴拿马 ★★★★☆ | 哥斯达黎加 ★★★★☆</li>
</ul>

<h2>墨西哥（里维埃拉玛雅）</h2>
<ul>
  <li>无需专门退休签证——通过收入证明即可申请</li>
  <li>直飞美国/加拿大200多个城市</li>
  <li>加勒比海滩和多元文化</li>
  <li>坎昆世界级私立医院</li>
  <li>庞大的英语外籍社区</li>
</ul>
<p><strong>收入要求：</strong>临时居留约2,500美元/月</p>
<p><strong>月度预算（舒适）：</strong>1,800–3,500美元/月（夫妻）</p>

<h2>巴拿马</h2>
<ul>
  <li><strong>Pensionado签证</strong>——拉美最优惠的退休签证，餐厅、航空、酒店、医院等享20–50%折扣</li>
  <li>境外收入免税</li>
  <li>美元货币，无汇率风险</li>
  <li>巴拿马城有JCI认证医院</li>
</ul>
<p><strong>收入要求：</strong>每月1,000美元养老金或投资收入</p>

<h2>哥斯达黎加</h2>
<ul>
  <li>持续被评为中美洲最安全国家</li>
  <li>稳定民主国家，1948年起无军队</li>
  <li>CAJA公共医疗系统（持居留权可使用）</li>
</ul>
<p><strong>收入要求：</strong>2,500美元/月（Rentista签证）</p>

<div class="info-box"><p><strong>总结：</strong>墨西哥在地理位置和航班方面领先。巴拿马在退休签证福利和境外收入免税方面最优。哥斯达黎加在安全性和政治稳定性方面胜出。</p></div>
""",
    },
    'related':{
        'en':[('retire-in-mexico-2026','Retire in Mexico 2026'),('mexico-temporary-residency-guide','Temporary Residency Guide'),('imss-health-insurance-foreigners-mexico','IMSS Health Insurance')],
        'es':[('jubilarse-mexico-2026','Jubilarse en México 2026'),('guia-residencia-temporal-mexico','Residencia Temporal'),('imss-seguro-salud-extranjeros-mexico','IMSS Seguro de Salud')],
        'ru':[('vyyti-na-pensiyu-v-meksike-2026','Выход на пенсию в Мексике'),('vremennoe-rezidentstvo-meksika','Временное резидентство'),('imss-meditsinskaya-strakhovka-meksika','Страховка IMSS')],
        'zh':[('zai-moxige-tuixiu-2026','在墨西哥退休2026'),('mexico-temporary-residency-guide','临时居留指南'),('imss-yiliao-baoxian-waiguoren-moxige','IMSS医疗保险')],
    },
}

ARTICLES['apostille-documents-mexico-immigration'] = {
    'slugs':{'en':'apostille-documents-mexico-immigration','es':'apostilla-documentos-mexico-inmigracion','ru':'apostil-dokumenty-meksika','zh':'gongzheng-wenjian-moxige-yimin'},
    'title':{
        'en':'Apostille Documents for Mexico Immigration 2026: Complete Guide',
        'es':'Apostilla de Documentos para Inmigración México 2026: Guía Completa',
        'ru':'Апостиль документов для иммиграции в Мексику 2026',
        'zh':'2026年墨西哥移民文件认证完整指南',
    },
    'desc':{
        'en':'How to apostille documents for Mexico immigration 2026 — which documents need apostille, how to get it, costs, and certified translation requirements.',
        'es':'Cómo apostillar documentos para inmigración a México 2026 — qué documentos necesitan apostilla, cómo obtenerla, costos y requisitos de traducción.',
        'ru':'Как апостилировать документы для иммиграции в Мексику 2026 — какие документы нужны, как получить апостиль, стоимость и перевод.',
        'zh':'如何为2026年墨西哥移民认证文件——哪些文件需要认证、如何获取、费用及翻译要求。',
    },
    'h1':{
        'en':'Apostille Documents for Mexico Immigration: <em>Step-by-Step Guide</em>',
        'es':'Apostilla para Inmigración a México: <em>Guía Paso a Paso</em>',
        'ru':'Апостиль документов для иммиграции в Мексику: <em>Пошаговое руководство</em>',
        'zh':'墨西哥移民文件认证：<em>分步操作指南</em>',
    },
    'lead':{
        'en':'An apostille is the international certification that makes your foreign documents legally valid in Mexico. Without it, INM will reject your application. Here\'s everything you need to know.',
        'es':'La apostilla es la certificación internacional que hace válidos tus documentos extranjeros en México. Sin ella, el INM rechazará tu solicitud.',
        'ru':'Апостиль — это международная сертификация, которая делает ваши иностранные документы юридически действительными в Мексике. Без неё INM отклонит заявку.',
        'zh':'公证书/海牙认证是使您的外国文件在墨西哥具有法律效力的国际认证。没有它，INM将拒绝您的申请。',
    },
    'breadcrumb':{'en':'Apostille Documents','es':'Apostilla Documentos','ru':'Апостиль документов','zh':'文件认证'},
    'faq':{
        'en':[
            ('What is an apostille?','An apostille is a form of authentication issued by a government authority that certifies the legitimacy of a document for use in other countries that are part of the 1961 Hague Convention.'),
            ('Which documents need apostille for Mexico immigration?','Birth certificate, marriage certificate, police clearance, divorce decree, academic degrees, and any other official document issued abroad.'),
            ('How long does an apostille take?','Typically 1–5 business days for US documents. Other countries vary from same-day to several weeks.'),
            ('Do I need a certified translation too?','Yes. Apostilled documents must also be translated into Spanish by a certified perito traductor (expert translator) recognized by Mexican courts.'),
        ],
        'es':[
            ('¿Qué es una apostilla?','Una apostilla es una forma de autenticación emitida por una autoridad gubernamental que certifica la legitimidad de un documento para uso en otros países parte del Convenio de La Haya de 1961.'),
            ('¿Qué documentos necesitan apostilla para inmigración a México?','Acta de nacimiento, acta de matrimonio, constancia de antecedentes penales, decreto de divorcio, títulos académicos y cualquier otro documento oficial emitido en el extranjero.'),
            ('¿Cuánto tiempo tarda una apostilla?','Generalmente 1–5 días hábiles para documentos de EE.UU. Otros países varían de un mismo día a varias semanas.'),
            ('¿También necesito traducción certificada?','Sí. Los documentos apostillados también deben ser traducidos al español por un perito traductor certificado reconocido por los tribunales mexicanos.'),
        ],
        'ru':[
            ('Что такое апостиль?','Апостиль — это форма аутентификации, выдаваемая государственным органом, подтверждающая подлинность документа для использования в других странах — участниках Гаагской конвенции 1961 года.'),
            ('Какие документы нужно апостилировать для иммиграции в Мексику?','Свидетельство о рождении, о браке, справка об отсутствии судимости, решение о разводе, дипломы и любые другие официальные документы, выданные за рубежом.'),
            ('Сколько времени занимает апостиль?','Для документов США — обычно 1–5 рабочих дней. Другие страны — от одного дня до нескольких недель.'),
            ('Нужен ли также сертифицированный перевод?','Да. Апостилированные документы также должны быть переведены на испанский язык сертифицированным переводчиком (perito traductor), признанным мексиканскими судами.'),
        ],
        'zh':[
            ('什么是海牙认证/公证书？','公证书是由政府机构颁发的认证形式，证明文件的合法性，使其在1961年《海牙公约》成员国中具有法律效力。'),
            ('哪些文件需要认证用于墨西哥移民？','出生证明、结婚证、无犯罪记录证明、离婚判决、学历证书及其他国外官方文件。'),
            ('认证需要多长时间？','美国文件通常需要1–5个工作日。其他国家从当天到数周不等。'),
            ('还需要认证翻译吗？','是的。经认证的文件还必须由墨西哥法院认可的认证译员（perito traductor）翻译成西班牙语。'),
        ],
    },
    'body':{
        'en':"""
<h2>Documents That Require Apostille for Mexico</h2>
<ul>
  <li><strong>Birth certificate</strong> — required for residency, CURP, and family reunification</li>
  <li><strong>Marriage certificate</strong> — for spousal residency applications</li>
  <li><strong>Divorce decree</strong> — if previously married</li>
  <li><strong>Police clearance / criminal background check</strong> — required for permanent residency and some temporary residency types</li>
  <li><strong>Academic degrees</strong> — for work permit applications</li>
  <li><strong>Bank statements / financial documents</strong> — these typically do NOT need apostille, only translation</li>
</ul>

<h2>How to Get an Apostille</h2>
<h3>United States</h3>
<p>Contact the Secretary of State office in the state where the document was issued. Most states offer online mail-in apostille services. Cost: $10–$25 per document. Time: 3–10 business days.</p>
<h3>United Kingdom</h3>
<p>Apply through the UK Foreign, Commonwealth & Development Office (FCDO) or an authorized agent. Cost: ~£30–£75. Time: 5–15 business days.</p>
<h3>Canada</h3>
<p>Global Affairs Canada handles apostilles for federal documents. Provincial documents go to the relevant provincial authority. Cost: ~CAD $35–$100. Time: 5–20 business days.</p>
<h3>Russia / CIS Countries</h3>
<p>Contact the Ministry of Justice or regional civil registry (ZAGS) office. Cost: varies significantly by region. Time: 1–10 business days.</p>

<div class="info-box"><p><strong>Important:</strong> Mexico is a member of the Hague Apostille Convention. If your country is also a member, apostille is sufficient. If not, you'll need full consular legalization (a longer process).</p></div>

<h2>Certified Translation Requirements</h2>
<p>After apostille, all documents must be translated into Spanish by a <strong>perito traductor</strong> (court-certified translator). Requirements:</p>
<ul>
  <li>The translator must be registered with a Mexican federal or state court</li>
  <li>Translation must include the translator's stamp, signature, and registration number</li>
  <li>Both original and translation must be presented together at INM</li>
</ul>
<p>Cost per document translation: typically <strong>$50–$150 USD</strong> depending on document length.</p>

<h2>Full Document Checklist for Residency Application</h2>
<ul>
  <li>☐ Valid passport (no apostille needed)</li>
  <li>☐ Birth certificate (apostille + Spanish translation)</li>
  <li>☐ Marriage/divorce certificate if applicable (apostille + translation)</li>
  <li>☐ Police clearance (apostille + translation) — for permanent residency</li>
  <li>☐ Bank statements showing required income (translation only, no apostille)</li>
  <li>☐ Photos (white background, no glasses)</li>
  <li>☐ INM application form</li>
</ul>
""",
        'es':"""
<h2>Documentos que Requieren Apostilla para México</h2>
<ul>
  <li><strong>Acta de nacimiento</strong> — requerida para residencia, CURP y reunificación familiar</li>
  <li><strong>Acta de matrimonio</strong> — para solicitudes de residencia de cónyuge</li>
  <li><strong>Decreto de divorcio</strong> — si estuvo casado anteriormente</li>
  <li><strong>Antecedentes penales</strong> — requeridos para residencia permanente</li>
  <li><strong>Títulos académicos</strong> — para solicitudes de permiso de trabajo</li>
  <li><strong>Estados de cuenta / documentos financieros</strong> — estos generalmente NO necesitan apostilla, solo traducción</li>
</ul>

<h2>Cómo Obtener una Apostilla</h2>
<h3>Estados Unidos</h3>
<p>Contacta la Secretaría de Estado del estado donde se emitió el documento. La mayoría de estados ofrecen servicios por correo. Costo: $10–$25 por documento. Tiempo: 3–10 días hábiles.</p>
<h3>México acepta</h3>
<p>México es miembro de la Convención de La Haya sobre Apostillas. Si tu país también es miembro, la apostilla es suficiente. Si no, necesitarás legalización consular completa.</p>

<h2>Requisitos de Traducción Certificada</h2>
<p>Después de la apostilla, todos los documentos deben ser traducidos al español por un <strong>perito traductor</strong> certificado. Requisitos:</p>
<ul>
  <li>El traductor debe estar registrado en un tribunal federal o estatal mexicano</li>
  <li>La traducción debe incluir sello, firma y número de registro del traductor</li>
  <li>Se debe presentar original y traducción juntos en el INM</li>
</ul>
<p>Costo por documento: generalmente <strong>$50–$150 USD</strong>.</p>

<h2>Lista Completa de Documentos para Solicitud de Residencia</h2>
<ul>
  <li>☐ Pasaporte vigente (sin apostilla)</li>
  <li>☐ Acta de nacimiento (apostilla + traducción al español)</li>
  <li>☐ Acta de matrimonio/divorcio si aplica (apostilla + traducción)</li>
  <li>☐ Antecedentes penales (apostilla + traducción) — para residencia permanente</li>
  <li>☐ Estados de cuenta con ingresos requeridos (solo traducción)</li>
  <li>☐ Fotos (fondo blanco, sin lentes)</li>
  <li>☐ Formulario de solicitud INM</li>
</ul>
""",
        'ru':"""
<h2>Документы, требующие апостиля для Мексики</h2>
<ul>
  <li><strong>Свидетельство о рождении</strong> — для резидентства, CURP и воссоединения семьи</li>
  <li><strong>Свидетельство о браке</strong> — для заявок на резидентство супруга</li>
  <li><strong>Решение о разводе</strong> — если был предыдущий брак</li>
  <li><strong>Справка об отсутствии судимости</strong> — для постоянного резидентства</li>
  <li><strong>Дипломы</strong> — для разрешений на работу</li>
  <li><strong>Банковские выписки</strong> — апостиль НЕ нужен, только перевод</li>
</ul>

<h2>Как получить апостиль</h2>
<h3>Россия / СНГ</h3>
<p>Обратитесь в Министерство юстиции или региональный орган ЗАГС. Стоимость: варьируется по регионам. Срок: 1–10 рабочих дней.</p>
<h3>США</h3>
<p>Обратитесь в Государственный секретариат штата, выдавшего документ. Большинство штатов предлагают услуги по почте. Стоимость: $10–$25 за документ. Срок: 3–10 рабочих дней.</p>

<div class="info-box"><p><strong>Важно:</strong> Мексика — член Гаагской конвенции об апостиле. Если ваша страна тоже является членом, апостиля достаточно. Если нет — потребуется полная консульская легализация.</p></div>

<h2>Требования к сертифицированному переводу</h2>
<p>После апостиля все документы должны быть переведены на испанский язык <strong>perito traductor</strong> — сертифицированным переводчиком, признанным мексиканскими судами. Стоимость: обычно <strong>$50–$150 USD</strong> за документ.</p>

<h2>Полный список документов для заявки на резидентство</h2>
<ul>
  <li>☐ Действующий паспорт (апостиль не нужен)</li>
  <li>☐ Свидетельство о рождении (апостиль + перевод на испанский)</li>
  <li>☐ Свидетельство о браке/разводе при необходимости (апостиль + перевод)</li>
  <li>☐ Справка об отсутствии судимости (апостиль + перевод) — для постоянного резидентства</li>
  <li>☐ Банковские выписки (только перевод)</li>
  <li>☐ Фотографии (белый фон, без очков)</li>
  <li>☐ Форма заявки INM</li>
</ul>
""",
        'zh':"""
<h2>哪些文件需要认证用于墨西哥移民</h2>
<ul>
  <li><strong>出生证明</strong>——居留权、CURP和家庭团聚所需</li>
  <li><strong>结婚证</strong>——配偶居留申请所需</li>
  <li><strong>离婚判决</strong>——如有过婚姻</li>
  <li><strong>无犯罪记录证明</strong>——永久居留所需</li>
  <li><strong>学历证书</strong>——工作许可申请所需</li>
  <li><strong>银行流水/财务文件</strong>——通常不需要认证，仅需翻译</li>
</ul>

<h2>如何获取认证</h2>
<h3>中国</h3>
<p>在外交部领事司或省级公证处申请。费用和时间因地区而异，通常需要1–2周。</p>
<h3>美国</h3>
<p>联系文件颁发所在州的州务卿办公室。大多数州提供邮寄服务。费用：每份10–25美元。时间：3–10个工作日。</p>

<div class="info-box"><p><strong>重要：</strong>墨西哥是《海牙公约》成员国。若您的国家也是成员国，认证书即可。若非成员国，则需完整的领事认证（流程更长）。</p></div>

<h2>认证翻译要求</h2>
<p>认证后，所有文件必须由墨西哥法院认可的<strong>perito traductor</strong>（认证译员）翻译成西班牙语。费用：通常每份文件<strong>50–150美元</strong>。</p>

<h2>居留申请完整文件清单</h2>
<ul>
  <li>☐ 有效护照（无需认证）</li>
  <li>☐ 出生证明（认证+西班牙语翻译）</li>
  <li>☐ 结婚证/离婚判决（如适用，认证+翻译）</li>
  <li>☐ 无犯罪记录证明（认证+翻译）——永久居留所需</li>
  <li>☐ 银行流水（仅翻译）</li>
  <li>☐ 照片（白色背景，不戴眼镜）</li>
  <li>☐ INM申请表</li>
</ul>
""",
    },
    'related':{
        'en':[('family-reunification-visa-mexico','Family Reunification Visa'),('curp-foreigners-mexico','CURP for Foreigners'),('mexico-temporary-residency-guide','Temporary Residency Guide')],
        'es':[('visa-reunion-familiar-mexico','Visa Reunificación Familiar'),('curp-extranjeros-mexico','CURP para Extranjeros'),('guia-residencia-temporal-mexico','Residencia Temporal')],
        'ru':[('viza-dlya-semi-meksika','Виза для семьи'),('curp-dlya-inostrantsev-meksika','CURP для иностранцев'),('vremennoe-rezidentstvo-meksika','Временное резидентство')],
        'zh':[('jiating-tuanju-qianzheng-moxige','家庭团聚签证'),('curp-waiguoren-moxige','外国人CURP'),('mexico-temporary-residency-guide','临时居留指南')],
    },
}

ARTICLES['marriage-mexican-citizen-visa'] = {
    'slugs':{'en':'marriage-mexican-citizen-visa','es':'visa-matrimonio-ciudadano-mexicano','ru':'viza-brak-meksikanskiy-grazhdanin','zh':'hunyin-moxige-gongmin-qianzheng'},
    'title':{
        'en':'Marriage to Mexican Citizen Visa 2026: Residency Through Marriage',
        'es':'Visa por Matrimonio con Ciudadano Mexicano 2026: Residencia por Matrimonio',
        'ru':'Виза через брак с гражданином Мексики 2026: Резидентство через брак',
        'zh':'2026年与墨西哥公民结婚签证：通过婚姻获得居留权',
    },
    'desc':{
        'en':'How to get residency in Mexico through marriage to a Mexican citizen 2026 — process, documents, permanent residency eligibility, and timeline.',
        'es':'Cómo obtener residencia en México por matrimonio con ciudadano mexicano 2026 — proceso, documentos, elegibilidad para residencia permanente y plazos.',
        'ru':'Как получить резидентство в Мексике через брак с гражданином Мексики 2026 — процесс, документы, право на постоянное резидентство.',
        'zh':'2026年通过与墨西哥公民结婚获得居留权——流程、材料、永久居留资格及时间线。',
    },
    'h1':{
        'en':'Marriage to Mexican Citizen: <em>Path to Permanent Residency</em>',
        'es':'Matrimonio con Ciudadano Mexicano: <em>Camino a la Residencia Permanente</em>',
        'ru':'Брак с гражданином Мексики: <em>Путь к постоянному резидентству</em>',
        'zh':'与墨西哥公民结婚：<em>通向永久居留权之路</em>',
    },
    'lead':{
        'en':'Marriage to a Mexican citizen is one of the fastest paths to permanent residency — and potentially Mexican citizenship. Foreign spouses of Mexican citizens can skip temporary residency and apply directly for permanent status.',
        'es':'El matrimonio con un ciudadano mexicano es uno de los caminos más rápidos hacia la residencia permanente y potencialmente la ciudadanía. Los cónyuges extranjeros pueden saltarse la residencia temporal.',
        'ru':'Брак с гражданином Мексики — один из самых быстрых путей к постоянному резидентству и потенциально к гражданству. Иностранные супруги могут пропустить этап временного резидентства.',
        'zh':'与墨西哥公民结婚是获得永久居留权的最快途径之一——外籍配偶可以跳过临时居留阶段，直接申请永久居留。',
    },
    'breadcrumb':{'en':'Marriage Visa Mexico','es':'Visa Matrimonio México','ru':'Виза через брак Мексика','zh':'婚姻签证墨西哥'},
    'faq':{
        'en':[
            ('Can I get permanent residency immediately by marrying a Mexican?','Yes. Foreign spouses of Mexican citizens are eligible to apply directly for permanent residency — you do not need to go through temporary residency first.'),
            ('Do I need to get married in Mexico?','No. Marriages performed abroad are recognized in Mexico if the marriage certificate is apostilled and translated into Spanish.'),
            ('How long after marriage can I apply for residency?','You can apply immediately after obtaining the apostilled marriage certificate. There is no waiting period.'),
            ('Does marrying a Mexican citizen give me automatic citizenship?','No. After permanent residency, you must wait 2 years (instead of the standard 5 years) to apply for naturalization.'),
        ],
        'es':[
            ('¿Puedo obtener residencia permanente inmediatamente al casarme con un mexicano?','Sí. Los cónyuges extranjeros de ciudadanos mexicanos son elegibles para solicitar directamente la residencia permanente.'),
            ('¿Necesito casarme en México?','No. Los matrimonios realizados en el extranjero son reconocidos en México si el acta está apostillada y traducida al español.'),
            ('¿Cuánto tiempo después del matrimonio puedo solicitar la residencia?','Puedes solicitar inmediatamente después de obtener el acta de matrimonio apostillada. No hay período de espera.'),
            ('¿Casarme con un ciudadano mexicano me da ciudadanía automática?','No. Después de la residencia permanente, debes esperar 2 años (en lugar de los 5 años estándar) para solicitar la naturalización.'),
        ],
        'ru':[
            ('Могу ли я получить постоянное резидентство сразу после брака с гражданином Мексики?','Да. Иностранные супруги граждан Мексики могут сразу подать заявку на постоянное резидентство, минуя временное.'),
            ('Нужно ли жениться в Мексике?','Нет. Браки, заключённые за рубежом, признаются в Мексике при наличии апостилированного свидетельства о браке с переводом на испанский.'),
            ('Как скоро после свадьбы можно подать на резидентство?','Сразу после получения апостилированного свидетельства о браке. Периода ожидания нет.'),
            ('Даёт ли брак с гражданином Мексики автоматическое гражданство?','Нет. После постоянного резидентства нужно подождать 2 года (вместо стандартных 5) для подачи на натурализацию.'),
        ],
        'zh':[
            ('与墨西哥公民结婚后能立即获得永久居留权吗？','是的。墨西哥公民的外籍配偶可以直接申请永久居留权，无需先办理临时居留。'),
            ('必须在墨西哥结婚吗？','不需要。在国外登记的婚姻在墨西哥受到认可，只要结婚证经过海牙认证并翻译成西班牙语。'),
            ('结婚后多久可以申请居留权？','获得认证的结婚证后即可立即申请，没有等待期。'),
            ('与墨西哥公民结婚会自动获得国籍吗？','不会。获得永久居留权后，需等待2年（而非通常的5年）才能申请入籍。'),
        ],
    },
    'body':{
        'en':"""
<h2>Why Marriage to a Mexican Citizen Is Special</h2>
<p>Mexican immigration law grants foreign spouses of Mexican nationals a privileged path:</p>
<ul>
  <li><strong>Direct permanent residency</strong> — no need to obtain temporary residency first</li>
  <li><strong>No income requirement</strong> — you don't need to prove $2,500/month income</li>
  <li><strong>Reduced naturalization wait</strong> — 2 years instead of 5 years to apply for citizenship</li>
  <li><strong>Work authorization</strong> — permanent residents can work in Mexico without a separate permit</li>
</ul>

<h2>Step-by-Step Process</h2>
<ol>
  <li><strong>Obtain marriage certificate</strong> — if married abroad, get it apostilled and translated</li>
  <li><strong>If applying from abroad:</strong> Get a family unity visa at a Mexican consulate (showing marriage certificate + partner's Mexican passport)</li>
  <li><strong>If applying in Mexico:</strong> Book an INM appointment and present your documents directly for permanent residency</li>
  <li><strong>Submit biometrics</strong> at INM</li>
  <li><strong>Receive permanent residency card</strong> (4–8 weeks)</li>
</ol>

<h2>Required Documents</h2>
<ul>
  <li>Valid passport (applicant)</li>
  <li>Apostilled marriage certificate + certified Spanish translation</li>
  <li>Mexican partner's passport or naturalization certificate (original + copies)</li>
  <li>Proof of cohabitation (lease, utility bills — both names if possible)</li>
  <li>2 passport-sized photos (white background)</li>
  <li>INM application form</li>
  <li>Payment of residency fee (~$225 USD / ~$4,500 MXN)</li>
</ul>

<div class="info-box"><p><strong>Important:</strong> Mexican authorities may ask for evidence of a genuine marriage — photos together, WhatsApp/message history, joint accounts, travel records. Have these ready.</p></div>

<h2>Getting Married in Mexico as a Foreigner</h2>
<p>If you want to marry in Mexico, you must register the marriage at the Registro Civil. Requirements:</p>
<ul>
  <li>Both partners' birth certificates (apostilled + translated)</li>
  <li>Medical certificates (blood tests) issued within 15 days</li>
  <li>4 witnesses (adults with valid ID)</li>
  <li>Fee varies by municipality (~$100–$300 USD)</li>
  <li>If previously married: divorce decree or death certificate of former spouse (apostilled)</li>
</ul>

<h2>Path to Mexican Citizenship</h2>
<p>After 2 years of permanent residency as the spouse of a Mexican citizen:</p>
<ol>
  <li>Apply for naturalization at the Secretaría de Relaciones Exteriores (SRE)</li>
  <li>Pass a Spanish language test and Mexican history/culture exam</li>
  <li>Renounce previous citizenship (Mexico generally requires this)</li>
  <li>Take the oath of citizenship</li>
</ol>
""",
        'es':"""
<h2>¿Por Qué el Matrimonio con Ciudadano Mexicano es Especial?</h2>
<p>La ley de inmigración mexicana otorga a los cónyuges extranjeros de ciudadanos mexicanos un camino privilegiado:</p>
<ul>
  <li><strong>Residencia permanente directa</strong> — sin necesidad de residencia temporal previa</li>
  <li><strong>Sin requisito de ingresos</strong> — no necesitas demostrar $2,500/mes</li>
  <li><strong>Reducción del período de naturalización</strong> — 2 años en lugar de 5 para solicitar ciudadanía</li>
  <li><strong>Autorización de trabajo</strong> — los residentes permanentes pueden trabajar sin permiso adicional</li>
</ul>

<h2>Proceso Paso a Paso</h2>
<ol>
  <li><strong>Obtener acta de matrimonio</strong> — si te casaste en el extranjero, apostíllala y tradúcela</li>
  <li><strong>Si aplicas desde el extranjero:</strong> obtén visa de unidad familiar en el consulado mexicano</li>
  <li><strong>Si aplicas en México:</strong> agenda cita INM y presenta documentos directamente para residencia permanente</li>
  <li><strong>Presentar biometría</strong> en el INM</li>
  <li><strong>Recibir tarjeta de residencia permanente</strong> (4–8 semanas)</li>
</ol>

<h2>Documentos Requeridos</h2>
<ul>
  <li>Pasaporte vigente del solicitante</li>
  <li>Acta de matrimonio apostillada + traducción certificada al español</li>
  <li>Pasaporte mexicano de la pareja (original + copias)</li>
  <li>Comprobante de cohabitación (contrato de arrendamiento, recibos)</li>
  <li>2 fotos tamaño pasaporte (fondo blanco)</li>
  <li>Formulario INM</li>
  <li>Pago de cuota de residencia (~$225 USD / ~$4,500 MXN)</li>
</ul>

<div class="info-box"><p><strong>Importante:</strong> Las autoridades mexicanas pueden pedir evidencia de matrimonio genuino — fotos juntos, historial de mensajes, cuentas conjuntas, registros de viaje.</p></div>

<h2>Casarse en México como Extranjero</h2>
<p>Para casarte en México debes registrar el matrimonio en el Registro Civil. Requisitos:</p>
<ul>
  <li>Actas de nacimiento de ambos (apostilladas + traducidas)</li>
  <li>Certificados médicos (análisis de sangre) expedidos en los últimos 15 días</li>
  <li>4 testigos (adultos con identificación válida)</li>
  <li>Cuota según municipio (~$100–$300 USD)</li>
</ul>
""",
        'ru':"""
<h2>Почему брак с гражданином Мексики особенный</h2>
<p>Мексиканское иммиграционное законодательство предоставляет иностранным супругам граждан Мексики привилегированный путь:</p>
<ul>
  <li><strong>Прямое постоянное резидентство</strong> — без временного резидентства</li>
  <li><strong>Нет требования к доходу</strong> — не нужно подтверждать $2,500/месяц</li>
  <li><strong>Сокращённый срок до натурализации</strong> — 2 года вместо 5</li>
  <li><strong>Разрешение на работу</strong> — постоянные резиденты работают без отдельного разрешения</li>
</ul>

<h2>Пошаговый процесс</h2>
<ol>
  <li><strong>Получить свидетельство о браке</strong> — если бракосочетание было за рубежом, апостилировать и перевести</li>
  <li><strong>При подаче из-за рубежа:</strong> получить визу семейного единства в мексиканском консульстве</li>
  <li><strong>При подаче в Мексике:</strong> записаться в INM и подать документы напрямую на постоянное резидентство</li>
  <li><strong>Сдать биометрию</strong> в INM</li>
  <li><strong>Получить карту постоянного резидента</strong> (4–8 недель)</li>
</ol>

<h2>Необходимые документы</h2>
<ul>
  <li>Действующий паспорт заявителя</li>
  <li>Апостилированное свидетельство о браке + сертифицированный перевод на испанский</li>
  <li>Мексиканский паспорт супруга (оригинал + копии)</li>
  <li>Подтверждение совместного проживания (договор аренды, квитанции)</li>
  <li>2 фото формата паспорта (белый фон)</li>
  <li>Форма заявки INM</li>
  <li>Оплата сбора (~$225 USD / ~$4,500 MXN)</li>
</ul>

<div class="info-box"><p><strong>Важно:</strong> Власти Мексики могут запросить доказательства подлинного брака — совместные фото, переписка, совместные счета, записи о поездках.</p></div>
""",
        'zh':"""
<h2>为什么与墨西哥公民结婚特别优越</h2>
<p>墨西哥移民法为墨西哥公民的外籍配偶提供了特殊通道：</p>
<ul>
  <li><strong>直接永久居留</strong>——无需先办理临时居留</li>
  <li><strong>无收入要求</strong>——无需证明每月2,500美元收入</li>
  <li><strong>缩短入籍等待期</strong>——2年而非通常的5年</li>
  <li><strong>工作授权</strong>——永久居民无需额外许可即可在墨工作</li>
</ul>

<h2>分步流程</h2>
<ol>
  <li><strong>获取结婚证</strong>——如在国外结婚，需办理海牙认证并翻译</li>
  <li><strong>从国外申请：</strong>在墨西哥使领馆申请家庭统一签证</li>
  <li><strong>在墨西哥申请：</strong>预约INM，直接提交永久居留材料</li>
  <li><strong>在INM提交生物信息</strong></li>
  <li><strong>领取永久居留卡</strong>（4–8周）</li>
</ol>

<h2>所需材料</h2>
<ul>
  <li>申请人有效护照</li>
  <li>经海牙认证的结婚证+西班牙语认证翻译</li>
  <li>墨西哥配偶护照（原件及复印件）</li>
  <li>共同居住证明（租房合同、水电账单）</li>
  <li>2张护照尺寸照片（白色背景）</li>
  <li>INM申请表</li>
  <li>居留费用（约225美元/约4,500墨西哥比索）</li>
</ul>

<div class="info-box"><p><strong>重要：</strong>墨西哥当局可能要求提供真实婚姻证明——合照、消息记录、共同账户、出行记录，请提前准备好。</p></div>
""",
    },
    'related':{
        'en':[('family-reunification-visa-mexico','Family Reunification Visa'),('apostille-documents-mexico-immigration','Apostille Documents'),('mexico-temporary-residency-guide','Temporary Residency Guide')],
        'es':[('visa-reunion-familiar-mexico','Visa Reunificación Familiar'),('apostilla-documentos-mexico-inmigracion','Apostilla Documentos'),('guia-residencia-temporal-mexico','Residencia Temporal')],
        'ru':[('viza-dlya-semi-meksika','Виза для семьи'),('apostil-dokumenty-meksika','Апостиль документов'),('vremennoe-rezidentstvo-meksika','Временное резидентство')],
        'zh':[('jiating-tuanju-qianzheng-moxige','家庭团聚签证'),('gongzheng-wenjian-moxige-yimin','文件认证'),('mexico-temporary-residency-guide','临时居留指南')],
    },
}

ARTICLES['mexico-border-run-visa-run'] = {
    'slugs':{'en':'mexico-border-run-visa-run','es':'salida-fronteriza-mexico','ru':'pogranichnyy-vyyezd-meksika','zh':'moxige-bianjing-chuxing'},
    'title':{
        'en':'Mexico Border Run / Visa Run 2026: What You Need to Know',
        'es':'Salida Fronteriza México 2026: Todo lo que Necesitas Saber',
        'ru':'Пограничная поездка в Мексике 2026: Всё что нужно знать',
        'zh':'2026年墨西哥边境出行/签证旅行：须知事项',
    },
    'desc':{
        'en':'Mexico border run guide 2026 — does it reset your tourist days, INM rules, risks, and legal alternatives to extend your stay.',
        'es':'Guía de salida fronteriza México 2026 — ¿restablece tus días de turista?, reglas del INM, riesgos y alternativas legales para extender tu estancia.',
        'ru':'Руководство по пограничным поездкам в Мексике 2026 — обнуляет ли счётчик дней, правила INM, риски и законные альтернативы.',
        'zh':'2026年墨西哥边境出行指南——是否重置旅游天数、INM规定、风险及延长停留的合法替代方案。',
    },
    'h1':{
        'en':'Mexico Border Run 2026: <em>Rules, Risks & Legal Alternatives</em>',
        'es':'Salida Fronteriza México 2026: <em>Reglas, Riesgos y Alternativas Legales</em>',
        'ru':'Пограничная поездка в Мексике 2026: <em>Правила, риски и законные альтернативы</em>',
        'zh':'2026年墨西哥边境出行：<em>规则、风险及合法替代方案</em>',
    },
    'lead':{
        'en':'A border run — briefly leaving and re-entering Mexico to reset your tourist permit — used to be straightforward. But INM has tightened enforcement in 2024–2026. Here\'s what actually works now.',
        'es':'La salida fronteriza — salir brevemente y reingresar a México para renovar el permiso de turista — solía ser sencilla. Pero el INM ha endurecido la aplicación en 2024–2026.',
        'ru':'Пограничная поездка — краткий выезд и повторный въезд в Мексику для обнуления туристического разрешения — раньше была простой. Но INM ужесточил контроль в 2024–2026 годах.',
        'zh':'边境出行——短暂离境后重新入境墨西哥以重置旅游许可——曾经很简单。但INM在2024–2026年加强了执法。',
    },
    'breadcrumb':{'en':'Mexico Border Run','es':'Salida Fronteriza México','ru':'Пограничная поездка Мексика','zh':'墨西哥边境出行'},
    'faq':{
        'en':[
            ('Does leaving Mexico reset your 180-day tourist permit?','Not automatically. INM officers have discretion over how many days they grant on re-entry. Frequent short trips raise red flags.'),
            ('How often can you do a border run in Mexico?','There is no legal limit stated, but patterns of repeated short exits and re-entries can result in being denied entry or being marked as attempting to reside without proper status.'),
            ('What is the safest way to extend legal stay in Mexico?','Apply for temporary residency. This is the only guaranteed legal long-term option. A tourist permit extension (prórroga) within Mexico is rarely granted.'),
            ('Can INM deny me re-entry after a border run?','Yes. If the officer believes you are using border runs to live in Mexico without residency status, they can deny entry or stamp fewer days than 180.'),
        ],
        'es':[
            ('¿Salir de México restablece mis 180 días de permiso de turista?','No automáticamente. Los oficiales del INM tienen discreción sobre cuántos días otorgan al reingresar. Los viajes cortos frecuentes generan alertas.'),
            ('¿Con qué frecuencia se puede hacer una salida fronteriza en México?','No hay un límite legal establecido, pero los patrones de salidas e ingresos cortos repetidos pueden resultar en denegación de entrada.'),
            ('¿Cuál es la forma más segura de extender la estadía legal en México?','Solicitar residencia temporal. Esta es la única opción legal garantizada a largo plazo.'),
            ('¿Puede el INM negarme el reingreso después de una salida fronteriza?','Sí. Si el oficial cree que usas salidas fronterizas para vivir en México sin estatus de residencia, puede negar la entrada o registrar menos de 180 días.'),
        ],
        'ru':[
            ('Обнуляет ли выезд из Мексики 180-дневное туристическое разрешение?','Не автоматически. Офицеры INM по своему усмотрению определяют количество дней при повторном въезде. Частые короткие поездки вызывают подозрения.'),
            ('Как часто можно совершать пограничные поездки в Мексике?','Законного ограничения нет, но систематические выезды и въезды могут привести к отказу во въезде.'),
            ('Какой самый безопасный способ продления легального пребывания в Мексике?','Подать на временное резидентство. Это единственный гарантированный законный долгосрочный вариант.'),
            ('Может ли INM отказать мне во въезде после пограничной поездки?','Да. Если офицер считает, что вы используете поездки для проживания без статуса резидента, он может отказать или проставить меньше 180 дней.'),
        ],
        'zh':[
            ('离开墨西哥会重置我的180天旅游许可吗？','不是自动的。INM官员可以自行决定再入境时给予的天数。频繁的短途旅行会引起注意。'),
            ('在墨西哥边境出行可以多频繁？','没有明文规定的次数限制，但频繁短途出入境的模式可能导致被拒绝入境。'),
            ('延长在墨西哥合法停留的最安全方式是什么？','申请临时居留权。这是唯一有保障的长期合法选择。'),
            ('边境出行后INM可以拒绝我再入境吗？','可以。如果官员认为您通过边境出行在没有居留身份的情况下居住，可以拒绝入境或标注少于180天。'),
        ],
    },
    'body':{
        'en':"""
<h2>The Reality of Border Runs in 2026</h2>
<p>Mexico's FMM (tourist card) allows stays of up to 180 days, but the number of days is determined by the immigration officer at entry — not automatic. In practice:</p>
<ul>
  <li>First-time visitors typically receive <strong>90–180 days</strong></li>
  <li>Visitors who recently left and re-entered may receive <strong>30–90 days</strong></li>
  <li>Frequent border-run patterns can result in <strong>entry denial</strong></li>
</ul>

<div class="info-box"><p><strong>Key change since 2023:</strong> INM now maintains a digital database of entries/exits. Officers can see your travel history instantly. The "just got here" approach no longer works.</p></div>

<h2>Common Border Run Routes</h2>
<h3>From Riviera Maya</h3>
<ul>
  <li><strong>Belize border (Chetumal)</strong> — 3-hour drive from Playa del Carmen. Cross at Belize → turn around → re-enter Mexico. Bus from Playa to Chetumal: ~$15 USD.</li>
  <li><strong>Fly to Belize City or Guatemala</strong> — overnight trip, more expensive but more convincing travel history</li>
</ul>
<h3>From Northern Mexico / US Border</h3>
<ul>
  <li>Cross to US side (San Diego/El Paso/Laredo), spend a few hours, re-enter Mexico</li>
</ul>

<h2>Risks and Consequences</h2>
<ul>
  <li><strong>Fewer days granted</strong> — officer discretion can cut your stay to 30 days</li>
  <li><strong>Entry ban</strong> — repeated abuse can result in a 3–10 year entry ban</li>
  <li><strong>Tax residence</strong> — if you're spending 183+ days via border runs, you're still a Mexican tax resident</li>
  <li><strong>No legal protection</strong> — as a tourist, you have no rights to appeal denial of entry</li>
</ul>

<h2>Legal Alternatives to Border Runs</h2>
<h3>Temporary Residency (Best Option)</h3>
<p>If you spend most of the year in Mexico, apply for temporary residency. It takes 4–8 weeks, requires proof of income ($2,500/month), and gives you 1–4 years of legal stay with renewal.</p>
<h3>Tourist Permit Extension (Prórroga)</h3>
<p>Theoretically, you can ask INM to extend your tourist permit without leaving. In practice, this is rarely approved and requires going to an INM office with a valid reason. Not recommended as a primary strategy.</p>
<h3>Student or Religious Visa</h3>
<p>If you're studying Spanish or taking courses at a registered institution, you can apply for a student visa — which gives legal residency status.</p>
""",
        'es':"""
<h2>La Realidad de las Salidas Fronterizas en 2026</h2>
<p>El FMM de México permite estancias de hasta 180 días, pero el número de días lo determina el oficial de inmigración al ingreso:</p>
<ul>
  <li>Visitantes por primera vez típicamente reciben <strong>90–180 días</strong></li>
  <li>Visitantes que recientemente salieron y reingresaron pueden recibir <strong>30–90 días</strong></li>
  <li>Patrones frecuentes de salida fronteriza pueden resultar en <strong>denegación de entrada</strong></li>
</ul>

<div class="info-box"><p><strong>Cambio clave desde 2023:</strong> El INM ahora mantiene una base de datos digital de entradas/salidas. Los oficiales pueden ver tu historial de viajes al instante.</p></div>

<h2>Rutas Comunes de Salida Fronteriza</h2>
<h3>Desde la Riviera Maya</h3>
<ul>
  <li><strong>Frontera de Belice (Chetumal)</strong> — 3 horas en auto desde Playa del Carmen. Cruzas a Belice y regresas. Autobús desde Playa a Chetumal: ~$15 USD.</li>
  <li><strong>Vuelo a Ciudad de Belice o Guatemala</strong> — viaje con noche, más caro pero más convincente</li>
</ul>

<h2>Riesgos y Consecuencias</h2>
<ul>
  <li><strong>Menos días otorgados</strong> — discreción del oficial puede reducir tu estancia a 30 días</li>
  <li><strong>Prohibición de entrada</strong> — el abuso repetido puede resultar en una prohibición de 3–10 años</li>
  <li><strong>Residencia fiscal</strong> — si pasas 183+ días vía salidas fronterizas, sigues siendo residente fiscal mexicano</li>
</ul>

<h2>Alternativas Legales a las Salidas Fronterizas</h2>
<h3>Residencia Temporal (Mejor Opción)</h3>
<p>Si pasas la mayor parte del año en México, solicita residencia temporal. Requiere prueba de ingresos ($2,500/mes) y otorga 1–4 años de estancia legal con renovación.</p>
<h3>Prórroga de Permiso de Turista</h3>
<p>Teóricamente puedes pedir al INM que extienda tu permiso sin salir. En la práctica, rara vez se aprueba.</p>
""",
        'ru':"""
<h2>Реальность пограничных поездок в 2026 году</h2>
<p>Мексиканская карта FMM позволяет пребывание до 180 дней, но количество дней определяет офицер при въезде:</p>
<ul>
  <li>Первый въезд: как правило <strong>90–180 дней</strong></li>
  <li>После недавнего выезда и повторного въезда: <strong>30–90 дней</strong></li>
  <li>Частые пограничные поездки могут привести к <strong>отказу во въезде</strong></li>
</ul>

<div class="info-box"><p><strong>Ключевое изменение с 2023 года:</strong> INM ведёт цифровую базу данных въездов/выездов. Офицеры мгновенно видят историю поездок.</p></div>

<h2>Популярные маршруты пограничных поездок</h2>
<h3>Из Ривьеры Майя</h3>
<ul>
  <li><strong>Граница с Белизом (Четумаль)</strong> — 3 часа езды от Плайя-дель-Кармен. Автобус ~$15 USD.</li>
  <li><strong>Перелёт в Белиз или Гватемалу</strong> — более дорого, но убедительнее</li>
</ul>

<h2>Риски и последствия</h2>
<ul>
  <li><strong>Меньше дней</strong> — офицер может сократить пребывание до 30 дней</li>
  <li><strong>Запрет на въезд</strong> — систематические злоупотребления могут привести к запрету на 3–10 лет</li>
  <li><strong>Налоговое резидентство</strong> — 183+ дней за счёт поездок всё равно делают вас налоговым резидентом</li>
</ul>

<h2>Законные альтернативы</h2>
<h3>Временное резидентство (лучший вариант)</h3>
<p>Если вы проводите большую часть года в Мексике, оформите временное резидентство. Требует подтверждения дохода ($2,500/месяц) и даёт 1–4 года легального пребывания.</p>
""",
        'zh':"""
<h2>2026年边境出行的现实</h2>
<p>墨西哥FMM旅游卡允许最多180天停留，但天数由入境时的移民官决定：</p>
<ul>
  <li>首次入境通常获得<strong>90–180天</strong></li>
  <li>近期出境后再次入境可能只获得<strong>30–90天</strong></li>
  <li>频繁边境出行模式可能导致<strong>拒绝入境</strong></li>
</ul>

<div class="info-box"><p><strong>2023年以来的关键变化：</strong>INM现在维护数字化入境/出境数据库。官员可即时查看您的旅行记录。</p></div>

<h2>常见边境出行路线</h2>
<h3>从里维埃拉玛雅出发</h3>
<ul>
  <li><strong>伯利兹边境（切图马尔）</strong>——距卡门海滩约3小时车程。越境至伯利兹后返回。巴士约15美元。</li>
  <li><strong>飞往伯利兹城或危地马拉</strong>——费用较高但旅行记录更可信</li>
</ul>

<h2>风险与后果</h2>
<ul>
  <li><strong>获得天数减少</strong>——官员可能将停留期缩短至30天</li>
  <li><strong>禁止入境</strong>——反复滥用可能导致3–10年禁令</li>
  <li><strong>税务居民身份</strong>——通过边境出行累计183天以上仍为墨西哥税务居民</li>
</ul>

<h2>合法替代方案</h2>
<h3>临时居留权（最佳选择）</h3>
<p>如果您一年中大部分时间在墨西哥，请申请临时居留权。需证明月收入2,500美元，可获得1–4年合法停留并可续签。</p>
""",
    },
    'related':{
        'en':[('mexico-tourist-visa-extension','Tourist Visa Extension'),('mexico-temporary-residency-guide','Temporary Residency Guide'),('digital-nomad-visa-mexico','Digital Nomad Visa Mexico')],
        'es':[('extension-visa-turista-mexico','Extensión Visa Turista'),('guia-residencia-temporal-mexico','Residencia Temporal'),('digital-nomad-visa-mexico','Visa Nómada Digital')],
        'ru':[('prodlenie-turisticheskoy-vizy-meksika','Продление туристической визы'),('vremennoe-rezidentstvo-meksika','Временное резидентство'),('tsifrovoy-nomad-viza-meksika','Виза цифрового кочевника')],
        'zh':[('moxige-lvyou-qianzheng-yanqi','旅游签证延期'),('mexico-temporary-residency-guide','临时居留指南'),('digital-nomad-visa-mexico','数字游民签证')],
    },
}

ARTICLES['pets-relocation-mexico'] = {
    'slugs':{'en':'pets-relocation-mexico','es':'mudarse-mexico-mascotas','ru':'pereezd-meksika-s-zhivotnymi','zh':'chongwu-qianyi-moxige'},
    'title':{
        'en':'Pets Relocation to Mexico 2026: Complete Guide for Dogs & Cats',
        'es':'Mudarse a México con Mascotas 2026: Guía Completa para Perros y Gatos',
        'ru':'Переезд в Мексику с животными 2026: Полное руководство для кошек и собак',
        'zh':'2026年携宠物搬迁墨西哥完整指南：狗和猫',
    },
    'desc':{
        'en':'How to bring pets to Mexico 2026 — import requirements for dogs and cats, health certificates, rabies vaccination, customs process, and vet tips.',
        'es':'Cómo llevar mascotas a México 2026 — requisitos de importación para perros y gatos, certificados de salud, vacunación antirrábica y trámite aduanal.',
        'ru':'Как привезти домашних животных в Мексику 2026 — требования для ввоза собак и кошек, ветеринарные справки, прививки от бешенства, таможня.',
        'zh':'2026年如何将宠物带入墨西哥——狗和猫的进口要求、健康证明、狂犬病疫苗、海关流程及兽医建议。',
    },
    'h1':{
        'en':'Pets Relocation to Mexico: <em>Bring Your Furry Family</em>',
        'es':'Mudarse a México con Mascotas: <em>Trae a tu Familia Peluda</em>',
        'ru':'Переезд в Мексику с животными: <em>Берите питомцев с собой</em>',
        'zh':'携宠物搬迁墨西哥：<em>带上您的毛茸茸家人</em>',
    },
    'lead':{
        'en':'Mexico welcomes pets! Dogs and cats can enter with relatively simple requirements compared to many countries. Here\'s the complete 2026 guide for bringing your pets to the Riviera Maya.',
        'es':'¡México da la bienvenida a las mascotas! Los perros y gatos pueden ingresar con requisitos relativamente simples en comparación con muchos países.',
        'ru':'Мексика рада домашним животным! Кошек и собак можно ввезти с относительно простыми требованиями по сравнению со многими странами.',
        'zh':'墨西哥欢迎宠物！与许多国家相比，狗和猫入境的要求相对简单。这是2026年将宠物带到里维埃拉玛雅的完整指南。',
    },
    'breadcrumb':{'en':'Pets to Mexico','es':'Mascotas a México','ru':'Животные в Мексику','zh':'宠物入境墨西哥'},
    'faq':{
        'en':[
            ('What vaccines does my pet need to enter Mexico?','Rabies vaccination is mandatory. Dogs also need distemper, parvovirus, and hepatitis vaccines. Cats need panleukopenia. All vaccines must be current (not expired).'),
            ('Do pets need a health certificate for Mexico?','Yes. A health certificate issued by a licensed veterinarian within 10 days of travel is required. The SENASICA form is accepted for most countries.'),
            ('Can I bring my pet in the cabin on flights to Mexico?','Most airlines allow small pets (under 8kg including carrier) in-cabin on flights to Mexico. Check with your specific airline.'),
            ('Is there a quarantine for pets entering Mexico?','No quarantine for dogs and cats from most countries, provided all documentation is in order.'),
        ],
        'es':[
            ('¿Qué vacunas necesita mi mascota para entrar a México?','La vacuna antirrábica es obligatoria. Los perros también necesitan vacunas contra moquillo, parvovirus y hepatitis. Los gatos necesitan panleucopenia. Todas deben estar vigentes.'),
            ('¿Las mascotas necesitan certificado de salud para México?','Sí. Se requiere un certificado de salud emitido por un veterinario autorizado dentro de los 10 días previos al viaje.'),
            ('¿Puedo llevar mi mascota en cabina en vuelos a México?','La mayoría de aerolíneas permiten mascotas pequeñas (menos de 8kg con transportadora) en cabina. Verifica con tu aerolínea.'),
            ('¿Hay cuarentena para mascotas que ingresan a México?','No hay cuarentena para perros y gatos de la mayoría de países, siempre que toda la documentación esté en orden.'),
        ],
        'ru':[
            ('Какие прививки нужны питомцу для въезда в Мексику?','Прививка от бешенства обязательна. Собакам также нужны прививки от чумы, парвовируса и гепатита. Кошкам — от панлейкопении. Все прививки должны быть действующими.'),
            ('Нужна ли ветеринарная справка для въезда в Мексику?','Да. Требуется ветеринарная справка от лицензированного ветеринара, выданная за 10 дней до поездки.'),
            ('Можно ли взять питомца в салон самолёта при перелёте в Мексику?','Большинство авиакомпаний разрешают маленьких питомцев (до 8 кг с переноской) в салоне. Уточняйте у конкретной авиакомпании.'),
            ('Есть ли карантин для животных при въезде в Мексику?','Карантина для кошек и собак из большинства стран нет, если все документы в порядке.'),
        ],
        'zh':[
            ('我的宠物入境墨西哥需要接种哪些疫苗？','狂犬病疫苗是必须的。狗还需要犬瘟热、细小病毒和肝炎疫苗。猫需要猫泛白细胞减少症疫苗。所有疫苗必须在有效期内。'),
            ('宠物入境墨西哥需要健康证明吗？','需要。必须提供由持牌兽医在出发前10天内签发的健康证明。'),
            ('我可以在飞往墨西哥的航班上将宠物带入机舱吗？','大多数航空公司允许小型宠物（含航空箱8公斤以下）进入客舱。请向具体航空公司确认。'),
            ('进入墨西哥的宠物需要隔离吗？','只要文件齐全，大多数国家的猫和狗无需隔离。'),
        ],
    },
    'body':{
        'en':"""
<h2>Mexico's Pet Import Requirements</h2>
<p>SENASICA (Mexico's agricultural and food safety authority) governs pet imports. Requirements are the same regardless of which Mexican airport you arrive at:</p>

<h3>Dogs</h3>
<ul>
  <li>Rabies vaccination (valid, not expired — minimum 30 days before travel, maximum 1 year)</li>
  <li>Distemper, parvovirus, and infectious hepatitis vaccines</li>
  <li>Internal and external parasite treatment within 6 months</li>
  <li>Veterinary health certificate (issued within 10 days of travel)</li>
  <li>Microchip (ISO 11784/11785 standard — strongly recommended, required in EU)</li>
</ul>
<h3>Cats</h3>
<ul>
  <li>Rabies vaccination (same rules as dogs)</li>
  <li>Panleukopenia (feline distemper) vaccine</li>
  <li>Veterinary health certificate (issued within 10 days)</li>
  <li>Microchip (recommended)</li>
</ul>

<div class="info-box"><p><strong>Important:</strong> The health certificate must be signed by a licensed (accredited) veterinarian. In the US, USDA endorsement is required for the certificate to be accepted at Mexican customs.</p></div>

<h2>The Health Certificate</h2>
<p>This is the most important document. Get it from your vet within <strong>10 calendar days</strong> of your departure date. It must include:</p>
<ul>
  <li>Pet's name, species, breed, age, sex, color</li>
  <li>Microchip number</li>
  <li>Vaccination history with dates</li>
  <li>Statement that the animal is healthy and free of visible signs of disease</li>
  <li>Veterinarian's signature, license number, and date</li>
</ul>

<h2>At Mexican Customs (Cancún / Mexico City Airport)</h2>
<p>Declare your pet at the red channel. A SENASICA inspector will review your documents. The process typically takes 15–30 minutes. There is no fee for bringing pets from most countries.</p>
<p>If documents are incomplete, the pet may be held for inspection or required to receive certain treatments at your expense before release.</p>

<h2>Finding a Vet in Riviera Maya</h2>
<p>Veterinary care is excellent and affordable in the Riviera Maya:</p>
<ul>
  <li><strong>Playa del Carmen:</strong> Several vet clinics on Constituyentes Ave and 30th Ave. Consultation: ~$20–$40 USD.</li>
  <li><strong>Cancún:</strong> Larger animal hospitals with 24-hour emergency services.</li>
  <li><strong>Tulum:</strong> A few clinics in Tulum Pueblo; serious cases should go to Playa or Cancún.</li>
</ul>

<h2>Pet-Friendly Housing Tips</h2>
<ul>
  <li>Many Mexican landlords restrict pets — always ask before signing a lease</li>
  <li>Say "¿Se aceptan mascotas?" (Are pets accepted?)</li>
  <li>Expect a higher security deposit if pets are allowed ($100–$300 USD extra)</li>
  <li>Facebook groups like "Pet-Friendly Rentals Playa del Carmen" are useful resources</li>
</ul>
""",
        'es':"""
<h2>Requisitos de Importación de Mascotas a México</h2>
<p>SENASICA (autoridad de sanidad agrícola de México) regula la importación de mascotas:</p>

<h3>Perros</h3>
<ul>
  <li>Vacuna antirrábica vigente (mínimo 30 días antes del viaje, máximo 1 año)</li>
  <li>Vacunas contra moquillo, parvovirus y hepatitis infecciosa</li>
  <li>Tratamiento antiparasitario interno y externo en los últimos 6 meses</li>
  <li>Certificado de salud veterinario (emitido en los 10 días previos al viaje)</li>
  <li>Microchip (estándar ISO 11784/11785 — muy recomendado)</li>
</ul>
<h3>Gatos</h3>
<ul>
  <li>Vacuna antirrábica (mismas reglas que perros)</li>
  <li>Vacuna contra panleucopenia felina</li>
  <li>Certificado de salud veterinario (emitido en los 10 días previos)</li>
  <li>Microchip (recomendado)</li>
</ul>

<div class="info-box"><p><strong>Importante:</strong> El certificado de salud debe estar firmado por un veterinario con licencia. Para viajeros de EE.UU., se requiere el aval del USDA para que sea aceptado en la aduana mexicana.</p></div>

<h2>En la Aduana Mexicana</h2>
<p>Declara tu mascota en el canal rojo. Un inspector de SENASICA revisará tus documentos. El proceso tarda 15–30 minutos. No hay cuota para la mayoría de países.</p>

<h2>Encontrar Veterinario en la Riviera Maya</h2>
<ul>
  <li><strong>Playa del Carmen:</strong> Varias clínicas en Av. Constituyentes y Av. 30. Consulta: ~$20–$40 USD.</li>
  <li><strong>Cancún:</strong> Hospitales veterinarios más grandes con servicios de emergencia 24 horas.</li>
  <li><strong>Tulum:</strong> Pocas clínicas en Tulum Pueblo; casos graves deben ir a Playa o Cancún.</li>
</ul>

<h2>Consejos para Vivienda Pet-Friendly</h2>
<ul>
  <li>Muchos propietarios mexicanos restringen mascotas — siempre pregunta antes de firmar</li>
  <li>Di "¿Se aceptan mascotas?"</li>
  <li>Espera un depósito adicional si aceptan mascotas ($100–$300 USD extra)</li>
</ul>
""",
        'ru':"""
<h2>Требования к ввозу домашних животных в Мексику</h2>
<p>SENASICA (ветеринарный надзор Мексики) регулирует ввоз домашних животных:</p>

<h3>Собаки</h3>
<ul>
  <li>Действующая прививка от бешенства (минимум 30 дней до поездки, максимум 1 год)</li>
  <li>Прививки от чумы, парвовируса и инфекционного гепатита</li>
  <li>Обработка от внутренних и внешних паразитов за последние 6 месяцев</li>
  <li>Ветеринарная справка (выдана за 10 дней до поездки)</li>
  <li>Микрочип (ISO 11784/11785 — настоятельно рекомендуется)</li>
</ul>
<h3>Кошки</h3>
<ul>
  <li>Прививка от бешенства (те же правила)</li>
  <li>Прививка от панлейкопении</li>
  <li>Ветеринарная справка (за 10 дней до поездки)</li>
  <li>Микрочип (рекомендуется)</li>
</ul>

<div class="info-box"><p><strong>Важно:</strong> Ветеринарная справка должна быть подписана лицензированным ветеринаром. Для путешественников из США требуется заверение USDA для принятия на мексиканской таможне.</p></div>

<h2>На мексиканской таможне</h2>
<p>Задекларируйте животное на красном канале. Инспектор SENASICA проверит документы — процедура занимает 15–30 минут. Для большинства стран плата не взимается.</p>

<h2>Ветеринары в Ривьере Майя</h2>
<ul>
  <li><strong>Плайя-дель-Кармен:</strong> Несколько клиник на Av. Constituyentes и 30 Ave. Приём: ~$20–$40 USD.</li>
  <li><strong>Канкун:</strong> Крупные ветеринарные больницы с круглосуточной экстренной помощью.</li>
  <li><strong>Тулум:</strong> Несколько клиник в Tulum Pueblo; серьёзные случаи лучше везти в Плайю или Канкун.</li>
</ul>

<h2>Советы по жилью с животными</h2>
<ul>
  <li>Многие мексиканские арендодатели не принимают животных — уточняйте до подписания договора</li>
  <li>Спросите: "¿Se aceptan mascotas?" (Принимаете ли животных?)</li>
  <li>Ожидайте дополнительный залог $100–$300 USD</li>
</ul>
""",
        'zh':"""
<h2>墨西哥宠物进口要求</h2>
<p>SENASICA（墨西哥农业和食品安全机构）负责宠物进口管理：</p>

<h3>狗</h3>
<ul>
  <li>有效的狂犬病疫苗（出发前至少30天，最多1年）</li>
  <li>犬瘟热、细小病毒和传染性肝炎疫苗</li>
  <li>过去6个月内的内外寄生虫治疗</li>
  <li>兽医健康证明（出发前10天内签发）</li>
  <li>芯片（ISO 11784/11785标准——强烈推荐）</li>
</ul>
<h3>猫</h3>
<ul>
  <li>有效的狂犬病疫苗（与狗相同规定）</li>
  <li>猫泛白细胞减少症疫苗</li>
  <li>兽医健康证明（出发前10天内）</li>
  <li>芯片（推荐）</li>
</ul>

<div class="info-box"><p><strong>重要：</strong>健康证明必须由持牌兽医签署。来自美国的旅客，证明需经USDA背书才能在墨西哥海关被接受。</p></div>

<h2>在墨西哥海关</h2>
<p>在红色通道申报您的宠物。SENASICA检查员将审查文件，通常需15–30分钟。大多数国家无需缴纳费用。</p>

<h2>在里维埃拉玛雅寻找兽医</h2>
<ul>
  <li><strong>卡门海滩：</strong>Constituyentes大道和30街有多家诊所。问诊费约20–40美元。</li>
  <li><strong>坎昆：</strong>更大的动物医院，提供24小时急诊服务。</li>
  <li><strong>图卢姆：</strong>Tulum Pueblo有几家诊所；严重病例应前往卡门海滩或坎昆。</li>
</ul>

<h2>宠物友好住房建议</h2>
<ul>
  <li>许多墨西哥房东不允许宠物——签租约前务必确认</li>
  <li>询问："¿Se aceptan mascotas?"（接受宠物吗？）</li>
  <li>如允许宠物，通常需额外缴纳100–300美元押金</li>
</ul>
""",
    },
    'related':{
        'en':[('residency-cancun-mexico','Residency in Cancún'),('residency-tulum-mexico','Residency in Tulum'),('mexico-temporary-residency-guide','Temporary Residency Guide')],
        'es':[('residencia-cancun-mexico','Residencia en Cancún'),('residencia-tulum-mexico','Residencia en Tulum'),('guia-residencia-temporal-mexico','Residencia Temporal')],
        'ru':[('rezidentstvo-kankun-meksika','Резидентство в Канкуне'),('rezidentstvo-tulum-meksika','Резидентство в Тулуме'),('vremennoe-rezidentstvo-meksika','Временное резидентство')],
        'zh':[('kankunju-liu-moxige','坎昆居留'),('tulumju-liu-moxige','图卢姆居留'),('mexico-temporary-residency-guide','临时居留指南')],
    },
}

# ── Generate all articles ────────────────────────────────────────────────────
if __name__ == '__main__':
    langs = ['en','es','ru','zh']
    for slug, data in ARTICLES.items():
        print(f'\n{slug}:')
        for lang in langs:
            lang_slug = data['slugs'][lang]
            write(lang, lang_slug, data)
    print(f'\nDone — {len(ARTICLES)*4} files written.')
