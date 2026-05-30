#!/usr/bin/env python3
"""Regenerate /en/, /es/, /ru/, /zh/ index.html from root index.html."""
import re, os

BASE = os.path.dirname(os.path.abspath(__file__))

with open(os.path.join(BASE, 'index.html'), 'r', encoding='utf-8') as f:
    root_html = f.read()

LANGS = {
    'en': {
        'html_lang': 'en',
        'title': 'MexVisa Pro — #1 Immigration Services in Riviera Maya, Mexico | Visas, Residency & Citizenship',
        'description': 'MexVisa Pro: #1 immigration consulting in Riviera Maya. Temporary & permanent residency, work permits, investor visas, citizenship & naturalization. 100% approval rate. Free WhatsApp consultation. Serving Cancún, Playa del Carmen, Tulum since 2009.',
        'keywords': 'immigration Mexico, visa Riviera Maya, residency Riviera Maya, work permit Mexico, INM, temporary residency Mexico, permanent residency Mexico, naturalization Mexico, immigration lawyer Riviera Maya, immigration consultant Riviera Maya, Mexico visa application, expat Mexico, digital nomad Mexico visa, immigration Cancun, immigration Playa del Carmen, immigration Tulum, investor visa Mexico, retirement visa Mexico, Mexico immigration 2026',
        'og_title': 'MexVisa Pro — #1 Immigration Services in Riviera Maya',
        'og_locale': 'en_US',
        'twitter_title': 'MexVisa Pro — Immigration in Riviera Maya',
        'faq': [
            ('How long does it take to get temporary residency in Mexico?', 'The process typically takes 2-4 weeks from document submission to card issuance, depending on the INM office workload in the Riviera Maya.'),
            ('Do I need to be in Mexico to start the immigration process?', 'For most visa types, you can start the process at a Mexican consulate in your home country.'),
            ('Can I work in Mexico with a temporary residency?', 'Temporary residency alone does not grant work permission. You need a specific work authorization added to your temporary resident card.'),
            ('What documents do I need for Mexican residency?', 'Requirements vary by visa type but typically include a valid passport, proof of income or employment, photographs, and completed application forms.'),
        ],
    },
    'es': {
        'html_lang': 'es',
        'title': 'MexVisa Pro — Servicios de Inmigración en Riviera Maya, México | Visas, Residencia y Ciudadanía',
        'description': 'MexVisa Pro: consultoría migratoria #1 en Riviera Maya. Residencia temporal y permanente, permisos de trabajo, visas de inversionista, ciudadanía y naturalización. 100% aprobación. Consulta gratuita por WhatsApp. Cancún, Playa del Carmen, Tulum desde 2009.',
        'keywords': 'inmigración México, visa Riviera Maya, residencia Riviera Maya, permiso de trabajo México, INM, residencia temporal México, residencia permanente México, naturalización México, abogado de inmigración Riviera Maya, consultor migratorio Riviera Maya, trámite visa México, extranjero México, visa nómada digital México, inmigración Cancún, inmigración Playa del Carmen, inmigración Tulum, visa inversionista México, visa jubilado México, inmigración México 2026',
        'og_title': 'MexVisa Pro — Servicios de Inmigración #1 en Riviera Maya',
        'og_locale': 'es_MX',
        'twitter_title': 'MexVisa Pro — Inmigración en Riviera Maya',
        'faq': [
            ('¿Cuánto tarda obtener la residencia temporal en México?', 'El proceso típicamente toma de 2 a 4 semanas desde la presentación de documentos hasta la emisión de la tarjeta, dependiendo de la carga de la oficina del INM en Riviera Maya.'),
            ('¿Necesito estar en México para iniciar el proceso migratorio?', 'Para la mayoría de los tipos de visa, puede iniciar el proceso en un consulado mexicano en su país de origen.'),
            ('¿Puedo trabajar en México con residencia temporal?', 'La residencia temporal por sí sola no otorga permiso de trabajo. Necesita una autorización de trabajo específica añadida a su tarjeta de residente temporal.'),
            ('¿Qué documentos necesito para la residencia mexicana?', 'Los requisitos varían según el tipo de visa, pero generalmente incluyen pasaporte vigente, comprobante de ingresos o empleo, fotografías y formularios de solicitud completados.'),
        ],
    },
    'ru': {
        'html_lang': 'ru',
        'title': 'MexVisa Pro — Иммиграция в Ривьеру-Майя, Мексика | Визы, ВНЖ, Гражданство',
        'description': 'MexVisa Pro: иммиграционная консультация №1 в Ривьере-Майя. Временное и постоянное резидентство, разрешения на работу, инвестиционные визы, гражданство. 100% одобрений. Бесплатная консультация WhatsApp. Канкун, Плайя-дель-Кармен, Тулум с 2009.',
        'keywords': 'иммиграция Мексика, виза Ривьера-Майя, ВНЖ Мексика, разрешение на работу Мексика, INM, временное резидентство Мексика, постоянное резидентство Мексика, гражданство Мексика, иммиграционный юрист Ривьера-Майя, иммиграционный консультант Ривьера-Майя, виза Канкун, виза Плайя-дель-Кармен, переезд в Мексику, виза Тулум, инвестиционная виза Мексика, пенсионная виза Мексика, иммиграция Мексика 2026',
        'og_title': 'MexVisa Pro — Иммиграция №1 в Ривьере-Майя',
        'og_locale': 'ru_RU',
        'twitter_title': 'MexVisa Pro — Иммиграция в Ривьеру-Майя',
        'faq': [
            ('Сколько времени занимает получение временного резидентства в Мексике?', 'Процесс обычно занимает от 2 до 4 недель с момента подачи документов до выдачи карты, в зависимости от загруженности офиса INM в Ривьере-Майя.'),
            ('Нужно ли мне находиться в Мексике, чтобы начать иммиграционный процесс?', 'Для большинства типов виз вы можете начать процесс в мексиканском консульстве в вашей стране.'),
            ('Могу ли я работать в Мексике с временным резидентством?', 'Временное резидентство само по себе не даёт разрешения на работу. Вам нужно специальное разрешение на работу, добавленное к вашей карте временного резидента.'),
            ('Какие документы нужны для резидентства в Мексике?', 'Требования зависят от типа визы, но обычно включают действующий паспорт, подтверждение дохода или занятости, фотографии и заполненные формы заявления.'),
        ],
    },
    'zh': {
        'html_lang': 'zh',
        'title': 'MexVisa Pro — 里维埃拉玛雅移民服务第一名 | 签证、居留与公民身份',
        'description': 'MexVisa Pro：里维埃拉玛雅排名第一的移民咨询。临时和永久居留、工作许可、投资签证、公民身份和入籍。100%通过率。WhatsApp免费咨询。服务坎昆、普拉亚德尔卡门、图卢姆，始于2009年。',
        'keywords': '墨西哥移民, 里维埃拉玛雅签证, 里维埃拉玛雅居留, 墨西哥工作许可, INM, 墨西哥临时居留, 墨西哥永久居留, 墨西哥归化, 里维埃拉玛雅移民律师, 里维埃拉玛雅移民顾问, 墨西哥签证申请, 墨西哥外籍人士, 墨西哥数字游民签证, 坎昆移民, 普拉亚德尔卡门移民, 图卢姆移民, 墨西哥投资签证, 墨西哥退休签证, 墨西哥移民2026',
        'og_title': 'MexVisa Pro — 里维埃拉玛雅第一移民服务',
        'og_locale': 'zh_CN',
        'twitter_title': 'MexVisa Pro — 里维埃拉玛雅移民',
        'faq': [
            ('在墨西哥获得临时居留需要多长时间？', '从提交文件到发卡，整个过程通常需要2至4周，具体取决于里维埃拉玛雅INM办公室的工作量。'),
            ('我需要在墨西哥才能开始移民流程吗？', '对于大多数签证类型，您可以在本国的墨西哥领事馆开始办理。'),
            ('持有临时居留可以在墨西哥工作吗？', '仅凭临时居留不能获得工作许可。您需要在临时居民卡上添加专门的工作授权。'),
            ('墨西哥居留需要什么文件？', '要求因签证类型而异，但通常包括有效护照、收入或就业证明、照片和填写完整的申请表。'),
        ],
    },
}

DOMAIN = 'https://mexvisapro.com'

for lang, cfg in LANGS.items():
    html = root_html

    # Fix asset paths: assets/ → ../assets/
    html = html.replace('href="assets/', 'href="../assets/')
    html = html.replace('src="assets/', 'src="../assets/')
    html = html.replace('href="manifest.json"', 'href="../manifest.json"')

    # Set <html lang>
    html = re.sub(r'<html lang="[^"]*">', f'<html lang="{cfg["html_lang"]}">', html)

    # Replace <title>
    html = re.sub(r'<title>[^<]+</title>', f'<title>{cfg["title"]}</title>', html)

    # Replace meta description
    html = re.sub(
        r'<meta name="description" content="[^"]*">',
        f'<meta name="description" content="{cfg["description"]}">',
        html
    )

    # Replace meta keywords
    html = re.sub(
        r'<meta name="keywords" content="[^"]*">',
        f'<meta name="keywords" content="{cfg["keywords"]}">',
        html
    )

    # Replace canonical
    html = html.replace(
        f'<link rel="canonical" href="{DOMAIN}/">',
        f'<link rel="canonical" href="{DOMAIN}/{lang}/">'
    )

    # Replace OG tags
    html = re.sub(
        r'<meta property="og:title" content="[^"]*">',
        f'<meta property="og:title" content="{cfg["og_title"]}">',
        html
    )
    html = re.sub(
        r'<meta property="og:url" content="[^"]*">',
        f'<meta property="og:url" content="{DOMAIN}/{lang}/">',
        html
    )
    html = re.sub(
        r'<meta property="og:locale" content="[^"]*">',
        f'<meta property="og:locale" content="{cfg["og_locale"]}">',
        html
    )

    # Replace Twitter title
    html = re.sub(
        r'<meta name="twitter:title" content="[^"]*">',
        f'<meta name="twitter:title" content="{cfg["twitter_title"]}">',
        html
    )

    # Replace Schema.org FAQPage
    faq_items = []
    for q, a in cfg['faq']:
        faq_items.append(f'{{"@type": "Question", "name": "{q}", "acceptedAnswer": {{"@type": "Answer", "text": "{a}"}}}}')
    faq_json = ',\n      '.join(faq_items)
    faq_block = f'''{{"@context": "https://schema.org",
    "@type": "FAQPage",
    "mainEntity": [
      {faq_json}
    ]
  }}'''
    html = re.sub(
        r'\{"@context": "https://schema\.org",\s*"@type": "FAQPage".*?\}(?=\s*</script>)',
        faq_block,
        html,
        flags=re.DOTALL
    )

    # Remove auto-redirect script (only root needs it)
    html = re.sub(
        r'\s*<!-- Auto-detect browser language.*?</script>',
        '',
        html,
        flags=re.DOTALL
    )

    # Add localStorage pre-set script before </head>
    lang_script = f'\n  <script>localStorage.setItem(\'lang\',\'{lang}\');localStorage.setItem(\'lang_redirect\',\'done\')</script>'
    html = html.replace('</head>', f'{lang_script}\n</head>')

    # Write
    out_dir = os.path.join(BASE, lang)
    os.makedirs(out_dir, exist_ok=True)
    out_path = os.path.join(out_dir, 'index.html')
    with open(out_path, 'w', encoding='utf-8') as f:
        f.write(html)
    print(f'  ✓ {lang}/index.html ({len(html):,} bytes)')

print('Done — all 4 language pages regenerated.')
