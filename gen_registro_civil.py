#!/usr/bin/env python3
"""Generate /registro-civil-mexico/ service pages in EN/ES/RU/ZH"""
import os

WA = "529987583392"
SITE = "https://mexvisapro.com"

LANGS = {
    "en": {"pfx": "",    "dir": ""},
    "es": {"pfx": "/es", "dir": "es/"},
    "ru": {"pfx": "/ru", "dir": "ru/"},
    "zh": {"pfx": "/zh", "dir": "zh/"},
}

SLUG = "registro-civil-mexico"

DATA = {
    "en": {
        "title": "Civil Marriage Mexico for Foreigners 2026 — Registro Civil Services",
        "desc":  "Complete guide to getting married at Mexico's Registro Civil: foreigners, same-sex couples, LGBTQ+. Documents, process, costs and residency benefits.",
        "h1":    "Civil Marriage in Mexico: <em>Registro Civil for Foreigners</em>",
        "lead":  "Whether you are a heterosexual or same-sex couple, a foreign national, or part of the LGBTQ+ community — Mexico's Registro Civil is open to all. We handle the paperwork, appointments, and immigration follow-up so your wedding day stays stress-free.",
        "bc":    "Civil Marriage Mexico",
        "wa_text": "Hello! I need help with Registro Civil Mexico.",
        "consult": "Free Consultation",
        "partners": "Partners",
        "body": """
<h2>What is the Registro Civil?</h2>
<p>The <strong>Registro Civil</strong> (Civil Registry) is Mexico's official government office that performs and records civil marriages, births, and deaths. A civil ceremony is the <strong>only legally binding marriage</strong> in Mexico — religious ceremonies alone have no legal effect. The civil ceremony must happen first or simultaneously.</p>
<p>In the Riviera Maya, the main offices serving foreigners are in <strong>Playa del Carmen</strong> (Solidaridad municipality), <strong>Cancún</strong> (Benito Juárez municipality), and <strong>Tulum</strong>.</p>

<h2>Who Can Marry in Mexico?</h2>
<div class="info-box"><i class="bi bi-check-circle-fill me-2" style="color:var(--accent)"></i><strong>Foreigners marrying Mexicans</strong> — One partner can be a Mexican citizen or permanent/temporary resident.</div>
<div class="info-box mt-2"><i class="bi bi-check-circle-fill me-2" style="color:var(--accent)"></i><strong>Two foreigners</strong> — Both partners can be foreign nationals as long as at least one holds a valid Mexican visa or residency.</div>
<div class="info-box mt-2"><i class="bi bi-check-circle-fill me-2" style="color:var(--accent)"></i><strong>Same-sex couples (LGBTQ+)</strong> — Mexico's Supreme Court ruled same-sex marriage constitutional in 2015 and since June 2022 all 32 states are obligated to perform them without exceptions. Same-sex couples have exactly the same rights as heterosexual couples.</div>
<div class="info-box mt-2"><i class="bi bi-check-circle-fill me-2" style="color:var(--accent)"></i><strong>Trans and non-binary persons</strong> — Mexican law recognizes gender identity on official documents. Trans individuals can marry under their legal gender without prior surgery. Quintana Roo allows administrative gender marker changes since 2020.</div>

<h2>Required Documents for Foreigners</h2>
<ul class="doc-list">
  <li><i class="bi bi-file-earmark-text me-2" style="color:var(--gold)"></i>Valid passport (both partners)</li>
  <li><i class="bi bi-file-earmark-text me-2" style="color:var(--gold)"></i>Mexican visa, FMM tourist card, or residency card with sufficient validity</li>
  <li><i class="bi bi-file-earmark-text me-2" style="color:var(--gold)"></i>Birth certificate — apostilled and officially translated into Spanish</li>
  <li><i class="bi bi-file-earmark-text me-2" style="color:var(--gold)"></i>Single status certificate / certificate of no impediment to marriage (apostilled + translated) — issued within the last 6 months</li>
  <li><i class="bi bi-file-earmark-text me-2" style="color:var(--gold)"></i>If previously divorced: divorce decree (apostilled + translated)</li>
  <li><i class="bi bi-file-earmark-text me-2" style="color:var(--gold)"></i>If widowed: death certificate of previous spouse (apostilled + translated)</li>
  <li><i class="bi bi-file-earmark-text me-2" style="color:var(--gold)"></i>Medical blood test results (done in Mexico, valid 15 days) — HIV, syphilis, blood type</li>
  <li><i class="bi bi-file-earmark-text me-2" style="color:var(--gold)"></i>Two witnesses with valid IDs (Mexican or foreign)</li>
  <li><i class="bi bi-file-earmark-text me-2" style="color:var(--gold)"></i>Completed Registro Civil application form (we prepare this for you)</li>
</ul>
<p class="mt-3"><strong>For same-sex and trans couples:</strong> Exactly the same document list. No additional requirements or different procedures apply.</p>

<h2>Step-by-Step Process</h2>
<ol class="process-list">
  <li><strong>Document preparation</strong> — We review your documents, identify what needs apostille or translation, and coordinate certified translators.</li>
  <li><strong>Blood tests</strong> — Both partners attend a local clinic. Results are ready same day or next day.</li>
  <li><strong>Registro Civil appointment</strong> — We book the appointment at your chosen office. Wait times: 1–3 weeks in Playa del Carmen, up to 4 weeks in Cancún during peak season.</li>
  <li><strong>Document submission</strong> — We accompany you to submit and verify all documents. The officer sets the ceremony date (usually 5–10 business days after submission).</li>
  <li><strong>Civil ceremony</strong> — The ceremony takes about 20 minutes. Your two witnesses must be present. You receive the <em>acta de matrimonio</em> (marriage certificate) the same day or within 3 business days.</li>
  <li><strong>Apostille of Mexican marriage certificate</strong> — Optional but recommended if you need it recognized abroad. We arrange this.</li>
  <li><strong>Immigration follow-up</strong> — If applicable, we immediately begin your residency application based on family ties (see below).</li>
</ol>

<h2>Costs</h2>
<div class="cost-table">
  <div class="cost-row"><span>Registro Civil government fee</span><span>~$1,200–2,500 MXN (~$60–125 USD)</span></div>
  <div class="cost-row"><span>Blood tests (per person)</span><span>~$300–500 MXN (~$15–25 USD)</span></div>
  <div class="cost-row"><span>Apostille of Mexican marriage cert.</span><span>~$800–1,200 MXN (~$40–60 USD)</span></div>
  <div class="cost-row"><span>Certified translation (per document)</span><span>~$500–800 MXN (~$25–40 USD)</span></div>
  <div class="cost-row highlight"><span>MexVisa Pro full-service package</span><span>Contact us for quote</span></div>
</div>
<p class="mt-3 text-muted" style="font-size:.85rem">Prices as of 2026. Government fees may vary by municipality. Same price for all couples regardless of gender or nationality.</p>

<h2>Timeline</h2>
<div class="timeline-box">
  <div class="tl-item"><span class="tl-day">Day 1–3</span><span>Document audit &amp; blood tests</span></div>
  <div class="tl-item"><span class="tl-day">Day 3–10</span><span>Apostille &amp; translation processing</span></div>
  <div class="tl-item"><span class="tl-day">Day 10–25</span><span>Registro Civil appointment + document submission</span></div>
  <div class="tl-item"><span class="tl-day">Day 25–35</span><span>Civil ceremony &amp; receipt of marriage certificate</span></div>
  <div class="tl-item tl-highlight"><span class="tl-day">Total</span><span><strong>3–5 weeks</strong> from start to marriage certificate</span></div>
</div>

<h2>After Marriage: Residency Path</h2>
<p>Marriage to a Mexican citizen or permanent resident opens the fastest immigration path available in Mexico:</p>
<ul>
  <li><strong>Permanent residency directly</strong> — Spouses of Mexican citizens can skip temporary residency and apply directly for permanent residency (<em>residente permanente</em>).</li>
  <li><strong>Accelerated naturalization</strong> — After 2 years of permanent residency (vs. the standard 5 years), you can apply for Mexican citizenship.</li>
  <li><strong>Temporary residency</strong> — If your Mexican spouse holds temporary residency only, you qualify for temporary residency as a family member.</li>
</ul>
<p>We handle the complete immigration process immediately after the ceremony — most clients receive their residency card within 10–15 business days.</p>

<h2>Registro Civil Offices — Riviera Maya</h2>
<div class="office-grid">
  <div class="office-card"><h5><i class="bi bi-building me-2"></i>Playa del Carmen</h5><p>Registro Civil Solidaridad<br>Av. Juárez / Centro<br>Mon–Fri 8:00–14:00</p></div>
  <div class="office-card"><h5><i class="bi bi-building me-2"></i>Cancún</h5><p>Registro Civil Benito Juárez<br>Av. Kabah / SM 64<br>Mon–Fri 8:00–15:00</p></div>
  <div class="office-card"><h5><i class="bi bi-building me-2"></i>Tulum</h5><p>Registro Civil Tulum<br>Av. Satelite / Centro<br>Mon–Fri 9:00–14:00</p></div>
</div>
""",
        "faq": [
            ("Is same-sex marriage legal everywhere in Mexico?",
             "Yes. Since June 2022 all 32 Mexican states are required to perform same-sex marriages. Quintana Roo has recognized same-sex unions since 2012 and is one of the most welcoming states for LGBTQ+ couples."),
            ("Can two foreigners marry in Mexico without a Mexican citizen?",
             "Yes, as long as at least one partner has a valid Mexican visa, FMM tourist card, or residency document at the time of marriage."),
            ("Do I need to translate all my documents into Spanish?",
             "Yes. All foreign documents must be officially translated into Spanish by a certified perito traductor. We coordinate this for you."),
            ("What is apostille and do I need it?",
             "An apostille is an international certification that validates a document for use in another country. All foreign documents (birth certificates, single-status certificates, divorce decrees) must be apostilled by the issuing country before use in Mexico."),
            ("Can a trans person marry in Mexico under their preferred gender?",
             "Yes. Mexico recognizes gender identity. Trans individuals with legal gender marker changes on their documents can marry under their legal gender. Quintana Roo allows administrative gender changes (no surgery required)."),
            ("How quickly can we get married?",
             "With all documents ready, the minimum timeline is about 3 weeks. We can advise on expedited options depending on the municipality and time of year."),
        ],
    },
    "es": {
        "title": "Matrimonio Civil México para Extranjeros 2026 — Servicios Registro Civil",
        "desc":  "Guía completa para casarse en el Registro Civil de México: extranjeros, parejas del mismo sexo, LGBTQ+. Documentos, proceso, costos y residencia.",
        "h1":    "Matrimonio Civil en México: <em>Registro Civil para Extranjeros</em>",
        "lead":  "Ya seas pareja heterosexual u homosexual, extranjero o parte de la comunidad LGBTQ+ — el Registro Civil de México está abierto a todos. Nosotros gestionamos los trámites, citas y seguimiento migratorio para que tu boda sea sin estrés.",
        "bc":    "Matrimonio Civil México",
        "wa_text": "¡Hola! Necesito ayuda con el Registro Civil México.",
        "consult": "Consulta Gratis",
        "partners": "Socios",
        "body": """
<h2>¿Qué es el Registro Civil?</h2>
<p>El <strong>Registro Civil</strong> es la oficina gubernamental de México que realiza y registra matrimonios civiles, nacimientos y defunciones. La ceremonia civil es el <strong>único matrimonio legalmente válido</strong> en México — la ceremonia religiosa por sí sola no tiene efecto legal. El acto civil debe realizarse primero o simultáneamente.</p>
<p>En la Riviera Maya, las principales oficinas para extranjeros están en <strong>Playa del Carmen</strong> (municipio Solidaridad), <strong>Cancún</strong> (municipio Benito Juárez) y <strong>Tulum</strong>.</p>

<h2>¿Quién puede casarse en México?</h2>
<div class="info-box"><i class="bi bi-check-circle-fill me-2" style="color:var(--accent)"></i><strong>Extranjeros con mexicanos</strong> — Uno de los cónyuges puede ser ciudadano mexicano o residente.</div>
<div class="info-box mt-2"><i class="bi bi-check-circle-fill me-2" style="color:var(--accent)"></i><strong>Dos extranjeros</strong> — Ambos pueden ser extranjeros si al menos uno tiene visa o residencia válida en México.</div>
<div class="info-box mt-2"><i class="bi bi-check-circle-fill me-2" style="color:var(--accent)"></i><strong>Parejas del mismo sexo (LGBTQ+)</strong> — La Corte Suprema declaró inconstitucional prohibir el matrimonio igualitario en 2015 y desde junio 2022 los 32 estados están obligados a realizarlos. Las parejas del mismo sexo tienen exactamente los mismos derechos que las heterosexuales.</div>
<div class="info-box mt-2"><i class="bi bi-check-circle-fill me-2" style="color:var(--accent)"></i><strong>Personas trans y no binarias</strong> — La ley mexicana reconoce la identidad de género. Las personas trans pueden casarse bajo su género legal sin necesidad de cirugía previa. Quintana Roo permite el cambio de género administrativo desde 2020.</div>

<h2>Documentos Requeridos para Extranjeros</h2>
<ul class="doc-list">
  <li><i class="bi bi-file-earmark-text me-2" style="color:var(--gold)"></i>Pasaporte vigente (ambos cónyuges)</li>
  <li><i class="bi bi-file-earmark-text me-2" style="color:var(--gold)"></i>Visa mexicana, tarjeta FMM o tarjeta de residencia con vigencia suficiente</li>
  <li><i class="bi bi-file-earmark-text me-2" style="color:var(--gold)"></i>Acta de nacimiento — apostillada y traducida oficialmente al español</li>
  <li><i class="bi bi-file-earmark-text me-2" style="color:var(--gold)"></i>Constancia de soltería / fe de soltería (apostillada + traducida) — emitida en los últimos 6 meses</li>
  <li><i class="bi bi-file-earmark-text me-2" style="color:var(--gold)"></i>Si está divorciado/a: sentencia de divorcio (apostillada + traducida)</li>
  <li><i class="bi bi-file-earmark-text me-2" style="color:var(--gold)"></i>Si es viudo/a: acta de defunción del cónyuge anterior (apostillada + traducida)</li>
  <li><i class="bi bi-file-earmark-text me-2" style="color:var(--gold)"></i>Análisis de sangre (realizados en México, válidos 15 días) — VIH, sífilis, grupo sanguíneo</li>
  <li><i class="bi bi-file-earmark-text me-2" style="color:var(--gold)"></i>Dos testigos con identificación vigente (mexicanos o extranjeros)</li>
  <li><i class="bi bi-file-earmark-text me-2" style="color:var(--gold)"></i>Formato de solicitud del Registro Civil (nosotros lo preparamos)</li>
</ul>
<p class="mt-3"><strong>Para parejas del mismo sexo y personas trans:</strong> Exactamente la misma lista de documentos. No aplican requisitos adicionales ni procedimientos diferentes.</p>

<h2>Proceso Paso a Paso</h2>
<ol class="process-list">
  <li><strong>Revisión documental</strong> — Auditamos tus documentos, identificamos qué necesita apostilla o traducción y coordinamos traductores certificados.</li>
  <li><strong>Análisis de sangre</strong> — Ambos cónyuges acuden a una clínica local. Resultados en 24–48 horas.</li>
  <li><strong>Cita en el Registro Civil</strong> — Gestionamos la cita en tu oficina preferida. Tiempos de espera: 1–3 semanas en Playa del Carmen, hasta 4 semanas en Cancún en temporada alta.</li>
  <li><strong>Entrega de documentos</strong> — Te acompañamos a entregar y verificar todos los documentos. El oficial fija la fecha de la ceremonia (normalmente 5–10 días hábiles después).</li>
  <li><strong>Ceremonia civil</strong> — La ceremonia dura unos 20 minutos. Los dos testigos deben estar presentes. Recibes el <em>acta de matrimonio</em> el mismo día o en 3 días hábiles.</li>
  <li><strong>Apostilla del acta mexicana</strong> — Opcional pero recomendada para uso en el extranjero. Lo tramitamos nosotros.</li>
  <li><strong>Seguimiento migratorio</strong> — Si aplica, iniciamos inmediatamente el trámite de residencia por vínculo familiar.</li>
</ol>

<h2>Costos</h2>
<div class="cost-table">
  <div class="cost-row"><span>Cuota gubernamental Registro Civil</span><span>~$1,200–2,500 MXN (~$60–125 USD)</span></div>
  <div class="cost-row"><span>Análisis de sangre (por persona)</span><span>~$300–500 MXN (~$15–25 USD)</span></div>
  <div class="cost-row"><span>Apostilla del acta mexicana</span><span>~$800–1,200 MXN (~$40–60 USD)</span></div>
  <div class="cost-row"><span>Traducción certificada (por documento)</span><span>~$500–800 MXN (~$25–40 USD)</span></div>
  <div class="cost-row highlight"><span>Paquete integral MexVisa Pro</span><span>Contáctanos para cotización</span></div>
</div>
<p class="mt-3 text-muted" style="font-size:.85rem">Precios 2026. Las cuotas gubernamentales pueden variar por municipio. Mismo precio para todas las parejas.</p>

<h2>Cronograma</h2>
<div class="timeline-box">
  <div class="tl-item"><span class="tl-day">Día 1–3</span><span>Revisión documental y análisis de sangre</span></div>
  <div class="tl-item"><span class="tl-day">Día 3–10</span><span>Apostilla y traducción de documentos</span></div>
  <div class="tl-item"><span class="tl-day">Día 10–25</span><span>Cita y entrega en Registro Civil</span></div>
  <div class="tl-item"><span class="tl-day">Día 25–35</span><span>Ceremonia civil y entrega del acta</span></div>
  <div class="tl-item tl-highlight"><span class="tl-day">Total</span><span><strong>3–5 semanas</strong> desde inicio hasta acta de matrimonio</span></div>
</div>

<h2>Después del Matrimonio: Residencia</h2>
<p>Casarse con un ciudadano o residente permanente mexicano abre la vía migratoria más rápida disponible:</p>
<ul>
  <li><strong>Residencia permanente directa</strong> — Los cónyuges de ciudadanos mexicanos pueden solicitar directamente la residencia permanente sin pasar por la temporal.</li>
  <li><strong>Naturalización acelerada</strong> — Después de 2 años de residencia permanente (vs. los 5 años estándar) puedes solicitar la ciudadanía mexicana.</li>
  <li><strong>Residencia temporal</strong> — Si tu cónyuge mexicano solo tiene residencia temporal, calificas para residencia temporal como familiar.</li>
</ul>
<p>Iniciamos el proceso migratorio completo inmediatamente después de la ceremonia — la mayoría de clientes reciben su tarjeta de residencia en 10–15 días hábiles.</p>

<h2>Oficinas Registro Civil — Riviera Maya</h2>
<div class="office-grid">
  <div class="office-card"><h5><i class="bi bi-building me-2"></i>Playa del Carmen</h5><p>Registro Civil Solidaridad<br>Av. Juárez / Centro<br>Lun–Vie 8:00–14:00</p></div>
  <div class="office-card"><h5><i class="bi bi-building me-2"></i>Cancún</h5><p>Registro Civil Benito Juárez<br>Av. Kabah / SM 64<br>Lun–Vie 8:00–15:00</p></div>
  <div class="office-card"><h5><i class="bi bi-building me-2"></i>Tulum</h5><p>Registro Civil Tulum<br>Av. Satelite / Centro<br>Lun–Vie 9:00–14:00</p></div>
</div>
""",
        "faq": [
            ("¿Es legal el matrimonio igualitario en todo México?",
             "Sí. Desde junio de 2022 los 32 estados de México están obligados a realizar matrimonios igualitarios. Quintana Roo ha reconocido las uniones del mismo sexo desde 2012 y es uno de los estados más inclusivos del país."),
            ("¿Pueden casarse dos extranjeros sin un ciudadano mexicano?",
             "Sí, siempre que al menos uno tenga visa, tarjeta FMM o residencia mexicana vigente en el momento del matrimonio."),
            ("¿Necesito traducir todos mis documentos al español?",
             "Sí. Todos los documentos extranjeros deben ser traducidos oficialmente al español por un perito traductor certificado. Nosotros coordinamos esto."),
            ("¿Qué es la apostilla y la necesito?",
             "La apostilla es una certificación internacional que valida un documento para su uso en otro país. Todos los documentos extranjeros deben estar apostillados por el país emisor antes de usarse en México."),
            ("¿Puede casarse una persona trans bajo su género preferido?",
             "Sí. México reconoce la identidad de género. Las personas trans con cambio de marcador de género en sus documentos pueden casarse bajo su género legal. Quintana Roo permite cambios de género administrativos sin cirugía."),
            ("¿Cuánto tiempo tardan los trámites?",
             "Con todos los documentos listos, el mínimo es unas 3 semanas. Podemos orientarte sobre opciones aceleradas según el municipio y la época del año."),
        ],
    },
    "ru": {
        "title": "Гражданский брак в Мексике для иностранцев 2026 — Услуги Регистро Сивиль",
        "desc":  "Полное руководство по регистрации брака в Registro Civil Мексики: иностранцы, однополые пары, ЛГБТК+. Документы, процесс, стоимость и вид на жительство.",
        "h1":    "Гражданский брак в Мексике: <em>Registro Civil для иностранцев</em>",
        "lead":  "Разнополые и однополые пары, иностранные граждане и представители ЛГБТК+-сообщества — Registro Civil Мексики открыт для всех. Мы берём на себя оформление документов, запись на приём и последующее оформление ВНЖ.",
        "bc":    "Гражданский брак Мексика",
        "wa_text": "Здравствуйте! Нужна помощь с Registro Civil Мексика.",
        "consult": "Бесплатная консультация",
        "partners": "Партнёры",
        "body": """
<h2>Что такое Registro Civil?</h2>
<p><strong>Registro Civil</strong> (Гражданский реестр) — официальное государственное ведомство Мексики, регистрирующее браки, рождения и смерти. Гражданская церемония является <strong>единственным юридически обязательным браком</strong> в Мексике — религиозная церемония без гражданской регистрации не имеет правового значения.</p>
<p>В Ривьера-Майя основные офисы для иностранцев находятся в <strong>Плая-дель-Кармен</strong> (муниципалитет Соладарidad), <strong>Канкуне</strong> (муниципалитет Бенито Хуарес) и <strong>Туле</strong>.</p>

<h2>Кто может зарегистрировать брак в Мексике?</h2>
<div class="info-box"><i class="bi bi-check-circle-fill me-2" style="color:var(--accent)"></i><strong>Иностранец и гражданин Мексики</strong> — один из партнёров может быть мексиканским гражданином или резидентом.</div>
<div class="info-box mt-2"><i class="bi bi-check-circle-fill me-2" style="color:var(--accent)"></i><strong>Два иностранца</strong> — оба партнёра могут быть иностранцами, если хотя бы один имеет действующую мексиканскую визу или ВНЖ.</div>
<div class="info-box mt-2"><i class="bi bi-check-circle-fill me-2" style="color:var(--accent)"></i><strong>Однополые пары (ЛГБТК+)</strong> — Верховный суд Мексики признал запрет однополых браков неконституционным в 2015 году, а с июня 2022 года все 32 штата обязаны их регистрировать. Права однополых пар полностью равны правам разнополых.</div>
<div class="info-box mt-2"><i class="bi bi-check-circle-fill me-2" style="color:var(--accent)"></i><strong>Трансгендерные и небинарные лица</strong> — мексиканское законодательство признаёт гендерную идентичность. Трансгендерные люди могут вступить в брак в соответствии со своим юридическим полом без предварительных операций. Штат Кинтана-Роо допускает административную смену гендерного маркера с 2020 года.</div>

<h2>Необходимые документы для иностранцев</h2>
<ul class="doc-list">
  <li><i class="bi bi-file-earmark-text me-2" style="color:var(--gold)"></i>Действующий паспорт (оба партнёра)</li>
  <li><i class="bi bi-file-earmark-text me-2" style="color:var(--gold)"></i>Мексиканская виза, карточка FMM или карта резидента с достаточным сроком действия</li>
  <li><i class="bi bi-file-earmark-text me-2" style="color:var(--gold)"></i>Свидетельство о рождении — апостиль + официальный перевод на испанский</li>
  <li><i class="bi bi-file-earmark-text me-2" style="color:var(--gold)"></i>Справка о несостоянии в браке (апостиль + перевод) — выданная не позднее 6 месяцев назад</li>
  <li><i class="bi bi-file-earmark-text me-2" style="color:var(--gold)"></i>При разводе: решение суда о расторжении брака (апостиль + перевод)</li>
  <li><i class="bi bi-file-earmark-text me-2" style="color:var(--gold)"></i>При вдовстве: свидетельство о смерти предыдущего супруга (апостиль + перевод)</li>
  <li><i class="bi bi-file-earmark-text me-2" style="color:var(--gold)"></i>Результаты анализа крови (сданного в Мексике, действительны 15 дней) — ВИЧ, сифилис, группа крови</li>
  <li><i class="bi bi-file-earmark-text me-2" style="color:var(--gold)"></i>Два свидетеля с действующими удостоверениями личности (мексиканцы или иностранцы)</li>
  <li><i class="bi bi-file-earmark-text me-2" style="color:var(--gold)"></i>Заявление в Registro Civil (мы готовим за вас)</li>
</ul>
<p class="mt-3"><strong>Для однополых пар и трансгендерных лиц:</strong> список документов идентичен. Никаких дополнительных требований или иных процедур не предусмотрено.</p>

<h2>Пошаговый процесс</h2>
<ol class="process-list">
  <li><strong>Проверка документов</strong> — Аудируем ваши документы, определяем, что требует апостиля или перевода, координируем работу сертифицированных переводчиков.</li>
  <li><strong>Анализ крови</strong> — Оба партнёра сдают анализ в местной клинике. Результаты готовы в день сдачи или на следующий день.</li>
  <li><strong>Запись в Registro Civil</strong> — Записываемся в удобный для вас офис. Ожидание: 1–3 недели в Плая-дель-Кармен, до 4 недель в Канкуне в высокий сезон.</li>
  <li><strong>Подача документов</strong> — Сопровождаем вас на подачу и проверку всех документов. Чиновник назначает дату церемонии (обычно 5–10 рабочих дней после подачи).</li>
  <li><strong>Гражданская церемония</strong> — Занимает около 20 минут. Два свидетеля должны присутствовать. Вы получаете <em>acta de matrimonio</em> (свидетельство о браке) в тот же день или в течение 3 рабочих дней.</li>
  <li><strong>Апостиль мексиканского свидетельства</strong> — Необязательно, но рекомендуется для использования за рубежом. Организуем.</li>
  <li><strong>Оформление ВНЖ</strong> — При наличии оснований сразу же начинаем процедуру получения вида на жительство по семейным основаниям.</li>
</ol>

<h2>Стоимость</h2>
<div class="cost-table">
  <div class="cost-row"><span>Государственная пошлина Registro Civil</span><span>~1 200–2 500 MXN (~60–125 USD)</span></div>
  <div class="cost-row"><span>Анализ крови (с человека)</span><span>~300–500 MXN (~15–25 USD)</span></div>
  <div class="cost-row"><span>Апостиль мексиканского свидетельства</span><span>~800–1 200 MXN (~40–60 USD)</span></div>
  <div class="cost-row"><span>Сертифицированный перевод (за документ)</span><span>~500–800 MXN (~25–40 USD)</span></div>
  <div class="cost-row highlight"><span>Полный пакет MexVisa Pro</span><span>Запросите расчёт</span></div>
</div>
<p class="mt-3 text-muted" style="font-size:.85rem">Цены актуальны на 2026 год. Государственные пошлины могут отличаться в зависимости от муниципалитета. Стоимость одинакова для всех пар.</p>

<h2>Сроки</h2>
<div class="timeline-box">
  <div class="tl-item"><span class="tl-day">День 1–3</span><span>Аудит документов и анализ крови</span></div>
  <div class="tl-item"><span class="tl-day">День 3–10</span><span>Апостиль и перевод документов</span></div>
  <div class="tl-item"><span class="tl-day">День 10–25</span><span>Запись и подача документов в Registro Civil</span></div>
  <div class="tl-item"><span class="tl-day">День 25–35</span><span>Гражданская церемония и получение свидетельства</span></div>
  <div class="tl-item tl-highlight"><span class="tl-day">Итого</span><span><strong>3–5 недель</strong> от начала до получения свидетельства о браке</span></div>
</div>

<h2>После регистрации брака: вид на жительство</h2>
<p>Брак с гражданином Мексики или постоянным резидентом открывает самый быстрый иммиграционный путь:</p>
<ul>
  <li><strong>Постоянное ВНЖ сразу</strong> — Супруги мексиканских граждан могут подать напрямую на постоянное место жительства, минуя временный ВНЖ.</li>
  <li><strong>Ускоренная натурализация</strong> — После 2 лет постоянного ВНЖ (вместо стандартных 5 лет) можно подать заявление на мексиканское гражданство.</li>
  <li><strong>Временный ВНЖ</strong> — Если ваш мексиканский супруг имеет только временное ВНЖ, вы вправе получить временное ВНЖ как член семьи.</li>
</ul>
<p>Мы запускаем полный иммиграционный процесс сразу после церемонии — большинство клиентов получают карту резидента в течение 10–15 рабочих дней.</p>

<h2>Офисы Registro Civil — Ривьера-Майя</h2>
<div class="office-grid">
  <div class="office-card"><h5><i class="bi bi-building me-2"></i>Плая-дель-Кармен</h5><p>Registro Civil Solidaridad<br>Ав. Хуарес / Центр<br>Пн–Пт 8:00–14:00</p></div>
  <div class="office-card"><h5><i class="bi bi-building me-2"></i>Канкун</h5><p>Registro Civil Benito Juárez<br>Ав. Кабах / SM 64<br>Пн–Пт 8:00–15:00</p></div>
  <div class="office-card"><h5><i class="bi bi-building me-2"></i>Тулум</h5><p>Registro Civil Tulum<br>Ав. Satelite / Центр<br>Пн–Пт 9:00–14:00</p></div>
</div>
""",
        "faq": [
            ("Легализованы ли однополые браки во всей Мексике?",
             "Да. С июня 2022 года все 32 штата Мексики обязаны регистрировать однополые браки. Кинтана-Роо признаёт однополые союзы с 2012 года и является одним из наиболее инклюзивных штатов страны."),
            ("Могут ли два иностранца пожениться в Мексике без мексиканца?",
             "Да, при условии, что хотя бы один из них имеет действующую мексиканскую визу, карточку FMM или ВНЖ на момент заключения брака."),
            ("Нужно ли переводить все документы на испанский?",
             "Да. Все иностранные документы должны быть официально переведены на испанский язык сертифицированным переводчиком-экспертом. Мы координируем этот процесс."),
            ("Что такое апостиль и нужен ли он?",
             "Апостиль — международная сертификация, подтверждающая подлинность документа для использования в другой стране. Все иностранные документы (свидетельства о рождении, справки о несостоянии в браке, решения о разводе) должны быть апостилированы страной-эмитентом перед использованием в Мексике."),
            ("Может ли трансгендерный человек вступить в брак в своём гендере?",
             "Да. Мексика признаёт гендерную идентичность. Трансгендерные лица, изменившие гендерный маркер в документах, могут вступить в брак в соответствии со своим юридическим полом. Кинтана-Роо позволяет менять гендерный маркер административно, без хирургического вмешательства."),
            ("Каковы минимальные сроки оформления?",
             "При наличии всех документов — около 3 недель. Мы можем проконсультировать по ускоренным вариантам в зависимости от муниципалитета и времени года."),
        ],
    },
    "zh": {
        "title": "墨西哥民政结婚2026年 — 外国人民事登记服务",
        "desc":  "墨西哥Registro Civil民事结婚完整指南：外国人、同性伴侣、LGBTQ+。所需文件、流程、费用及居留权益。",
        "h1":    "墨西哥民事婚姻：<em>外国人Registro Civil指南</em>",
        "lead":  "无论您是异性或同性伴侣、外国公民，还是LGBTQ+群体成员——墨西哥民事登记处向所有人开放。我们负责处理文件、预约及后续移民手续，让您的婚礼无忧无虑。",
        "bc":    "墨西哥民事结婚",
        "wa_text": "您好！我需要关于墨西哥Registro Civil的帮助。",
        "consult": "免费咨询",
        "partners": "合作伙伴",
        "body": """
<h2>什么是Registro Civil？</h2>
<p><strong>Registro Civil</strong>（民事登记处）是墨西哥负责办理和记录民事婚姻、出生及死亡的官方政府机构。民事婚礼是墨西哥<strong>唯一具有法律效力的婚姻</strong>——仅凭宗教仪式在法律上无效，必须首先或同步完成民事登记。</p>
<p>在里维埃拉玛雅，为外国人服务的主要办事处位于<strong>卡门港</strong>（Solidaridad市）、<strong>坎昆</strong>（Benito Juárez市）和<strong>图卢姆</strong>。</p>

<h2>哪些人可以在墨西哥登记结婚？</h2>
<div class="info-box"><i class="bi bi-check-circle-fill me-2" style="color:var(--accent)"></i><strong>外国人与墨西哥公民</strong> — 一方可以是墨西哥公民或永久/临时居民。</div>
<div class="info-box mt-2"><i class="bi bi-check-circle-fill me-2" style="color:var(--accent)"></i><strong>两名外国人</strong> — 双方均可为外国人，但至少一方须持有有效的墨西哥签证或居留证。</div>
<div class="info-box mt-2"><i class="bi bi-check-circle-fill me-2" style="color:var(--accent)"></i><strong>同性伴侣（LGBTQ+）</strong> — 墨西哥最高法院2015年裁定禁止同性婚姻违宪，自2022年6月起全国32个州均须办理同性婚姻登记，同性伴侣享有与异性伴侣完全相同的权利。</div>
<div class="info-box mt-2"><i class="bi bi-check-circle-fill me-2" style="color:var(--accent)"></i><strong>跨性别及非二元性别人士</strong> — 墨西哥法律认可性别认同，跨性别者无需手术即可以法定性别结婚。金塔纳罗奥州自2020年起允许行政方式变更性别标记。</div>

<h2>外国人所需文件</h2>
<ul class="doc-list">
  <li><i class="bi bi-file-earmark-text me-2" style="color:var(--gold)"></i>有效护照（双方）</li>
  <li><i class="bi bi-file-earmark-text me-2" style="color:var(--gold)"></i>墨西哥签证、FMM旅游卡或有效期足够的居留卡</li>
  <li><i class="bi bi-file-earmark-text me-2" style="color:var(--gold)"></i>出生证明 — 需经海牙认证（附加证书）并正式翻译成西班牙语</li>
  <li><i class="bi bi-file-earmark-text me-2" style="color:var(--gold)"></i>未婚证明/无婚姻障碍证明（附加认证+翻译）— 6个月内签发</li>
  <li><i class="bi bi-file-earmark-text me-2" style="color:var(--gold)"></i>如已离婚：离婚判决书（附加认证+翻译）</li>
  <li><i class="bi bi-file-earmark-text me-2" style="color:var(--gold)"></i>如为寡妇/鳏夫：前配偶死亡证明（附加认证+翻译）</li>
  <li><i class="bi bi-file-earmark-text me-2" style="color:var(--gold)"></i>血液检查结果（在墨西哥检测，有效期15天）— HIV、梅毒、血型</li>
  <li><i class="bi bi-file-earmark-text me-2" style="color:var(--gold)"></i>两名证人及其有效身份证件（墨西哥人或外国人均可）</li>
  <li><i class="bi bi-file-earmark-text me-2" style="color:var(--gold)"></i>Registro Civil申请表（由我们代为填写）</li>
</ul>
<p class="mt-3"><strong>同性伴侣及跨性别人士：</strong>所需文件清单完全相同，无额外要求或不同程序。</p>

<h2>办理流程（逐步说明）</h2>
<ol class="process-list">
  <li><strong>文件审核</strong> — 审核您的文件，确定需要附加认证或翻译的内容，并协调认证翻译人员。</li>
  <li><strong>血液检查</strong> — 双方前往当地诊所采血，结果当天或次日出具。</li>
  <li><strong>预约Registro Civil</strong> — 为您预约首选办事处。等待时间：卡门港1–3周，旺季坎昆最长4周。</li>
  <li><strong>提交文件</strong> — 全程陪同提交并核验所有文件，官员确认婚礼日期（通常在提交后5–10个工作日）。</li>
  <li><strong>民事婚礼</strong> — 仪式约20分钟，两名证人须到场。当天或3个工作日内领取<em>acta de matrimonio</em>（结婚证）。</li>
  <li><strong>墨西哥结婚证附加认证</strong> — 可选，如需在境外使用建议办理，由我们代为处理。</li>
  <li><strong>移民后续</strong> — 如符合条件，婚礼结束后立即启动家庭关系居留申请。</li>
</ol>

<h2>费用</h2>
<div class="cost-table">
  <div class="cost-row"><span>Registro Civil政府规费</span><span>约1,200–2,500墨西哥比索（约60–125美元）</span></div>
  <div class="cost-row"><span>血液检查（每人）</span><span>约300–500墨西哥比索（约15–25美元）</span></div>
  <div class="cost-row"><span>墨西哥结婚证附加认证</span><span>约800–1,200墨西哥比索（约40–60美元）</span></div>
  <div class="cost-row"><span>认证翻译（每份文件）</span><span>约500–800墨西哥比索（约25–40美元）</span></div>
  <div class="cost-row highlight"><span>MexVisa Pro全程服务包</span><span>联系我们获取报价</span></div>
</div>
<p class="mt-3 text-muted" style="font-size:.85rem">2026年价格。政府规费因市镇而异。所有伴侣收费标准相同。</p>

<h2>时间安排</h2>
<div class="timeline-box">
  <div class="tl-item"><span class="tl-day">第1–3天</span><span>文件审核及血液检查</span></div>
  <div class="tl-item"><span class="tl-day">第3–10天</span><span>文件附加认证与翻译</span></div>
  <div class="tl-item"><span class="tl-day">第10–25天</span><span>预约并提交Registro Civil文件</span></div>
  <div class="tl-item"><span class="tl-day">第25–35天</span><span>民事婚礼及领取结婚证</span></div>
  <div class="tl-item tl-highlight"><span class="tl-day">总计</span><span><strong>3–5周</strong>从启动到取得结婚证</span></div>
</div>

<h2>婚后居留路径</h2>
<p>与墨西哥公民或永久居民结婚可享受最快的移民通道：</p>
<ul>
  <li><strong>直接永久居留</strong> — 墨西哥公民的外国配偶可跳过临时居留，直接申请永久居民（residente permanente）。</li>
  <li><strong>加速入籍</strong> — 持有永久居留满2年（而非通常的5年）即可申请墨西哥国籍。</li>
  <li><strong>临时居留</strong> — 若您的墨西哥配偶仅持有临时居留，您可以家庭成员身份申请临时居留。</li>
</ul>
<p>我们在婚礼结束后立即启动完整的移民流程——大多数客户在10–15个工作日内收到居留卡。</p>

<h2>Registro Civil办事处 — 里维埃拉玛雅</h2>
<div class="office-grid">
  <div class="office-card"><h5><i class="bi bi-building me-2"></i>卡门港</h5><p>Registro Civil Solidaridad<br>Av. Juárez / 市中心<br>周一至五 8:00–14:00</p></div>
  <div class="office-card"><h5><i class="bi bi-building me-2"></i>坎昆</h5><p>Registro Civil Benito Juárez<br>Av. Kabah / SM 64<br>周一至五 8:00–15:00</p></div>
  <div class="office-card"><h5><i class="bi bi-building me-2"></i>图卢姆</h5><p>Registro Civil Tulum<br>Av. Satelite / 市中心<br>周一至五 9:00–14:00</p></div>
</div>
""",
        "faq": [
            ("墨西哥同性婚姻在全国各地是否合法？",
             "是的。自2022年6月起，墨西哥所有32个州均须办理同性婚姻登记。金塔纳罗奥州自2012年起已承认同性伴侣关系，是全国最包容的州之一。"),
            ("两名外国人可以在没有墨西哥公民的情况下在墨西哥结婚吗？",
             "可以，只要至少一方在结婚时持有有效的墨西哥签证、FMM旅游卡或居留证即可。"),
            ("是否需要将所有文件翻译成西班牙语？",
             "是的。所有外国文件必须由经认证的法庭翻译员正式译成西班牙语，我们会为您协调安排。"),
            ("什么是附加认证（海牙认证）？是否需要？",
             "附加认证是验证文件可在另一国使用的国际认证。所有外国文件（出生证明、未婚证明、离婚判决等）在墨西哥使用前须经签发国进行附加认证。"),
            ("跨性别人士可以以其认同的性别结婚吗？",
             "可以。墨西哥法律认可性别认同。已更改证件性别标记的跨性别人士可以其法定性别结婚。金塔纳罗奥州允许通过行政途径更改性别标记，无需手术。"),
            ("最短需要多长时间完成手续？",
             "准备好全部文件后，最短约需3周。我们可根据市镇和季节为您提供加快办理方案的建议。"),
        ],
    },
}

CSS_EXTRA = """
    .info-box{background:#f0faf4;border-left:3px solid var(--accent);padding:.75rem 1rem;border-radius:0 8px 8px 0;font-size:.9rem}
    .doc-list{list-style:none;padding:0}
    .doc-list li{padding:.4rem 0;border-bottom:1px solid #f0f0f0;font-size:.9rem}
    .process-list{padding-left:1.2rem}
    .process-list li{padding:.4rem 0;font-size:.9rem}
    .cost-table{border:1px solid #eee;border-radius:8px;overflow:hidden;margin-top:.5rem}
    .cost-row{display:flex;justify-content:space-between;padding:.6rem 1rem;font-size:.85rem;border-bottom:1px solid #f4f4f4}
    .cost-row:last-child{border-bottom:none}
    .cost-row.highlight{background:rgba(240,165,0,.08);font-weight:600}
    .timeline-box{border:1px solid #eee;border-radius:8px;overflow:hidden}
    .tl-item{display:flex;align-items:center;gap:1rem;padding:.6rem 1rem;border-bottom:1px solid #f4f4f4;font-size:.85rem}
    .tl-item:last-child{border-bottom:none}
    .tl-item.tl-highlight{background:rgba(240,165,0,.08);font-weight:600}
    .tl-day{min-width:80px;color:var(--gold);font-weight:700}
    .office-grid{display:grid;grid-template-columns:repeat(auto-fit,minmax(180px,1fr));gap:1rem;margin-top:.5rem}
    .office-card{border:1px solid #eee;border-radius:8px;padding:1rem;font-size:.82rem}
    .office-card h5{font-size:.9rem;margin-bottom:.4rem;color:var(--navy)}
    .office-card p{color:#666;margin:0;line-height:1.5}
    article h2{font-size:1.3rem;font-weight:700;color:var(--navy);margin:2rem 0 .8rem}
    article ul,article ol{margin-bottom:1rem}
    article p{margin-bottom:.8rem}
"""

def faq_schema(lang, faqs):
    items = []
    for q, a in faqs:
        items.append(f'{{"@type":"Question","name":{repr(q)},"acceptedAnswer":{{"@type":"Answer","text":{repr(a)}}}}}')
    return '{"@context":"https://schema.org","@type":"FAQPage","mainEntity":[' + ','.join(items) + ']}'

def page(lang, d):
    pfx = LANGS[lang]["pfx"]
    url = f"{SITE}{pfx}/{SLUG}/"
    alt_en = f"{SITE}/{SLUG}/"
    alt_es = f"{SITE}/es/{SLUG}/"
    alt_ru = f"{SITE}/ru/{SLUG}/"
    alt_zh = f"{SITE}/zh/{SLUG}/"

    faq_rows = ""
    for i, (q, a) in enumerate(d["faq"]):
        show = "show" if i == 0 else ""
        collapsed = "" if i == 0 else "collapsed"
        expanded = "true" if i == 0 else "false"
        faq_rows += f"""
        <div class="accordion-item border-0 mb-2" style="border-radius:8px;overflow:hidden">
          <h3 class="accordion-header">
            <button class="accordion-button {collapsed} fw-semibold" type="button" data-bs-toggle="collapse" data-bs-target="#faq{i}" aria-expanded="{expanded}">
              {q}
            </button>
          </h3>
          <div id="faq{i}" class="accordion-collapse collapse {show}">
            <div class="accordion-body text-muted">{a}</div>
          </div>
        </div>"""

    if lang == "en":
        home_link = "/"
        blog_link = "/blog/"
        nav_home = "Home"
        nav_blog = "Blog"
        nav_services = "Services"
    elif lang == "es":
        home_link = "/es/"
        blog_link = "/es/blog/"
        nav_home = "Inicio"
        nav_blog = "Blog"
        nav_services = "Servicios"
    elif lang == "ru":
        home_link = "/ru/"
        blog_link = "/ru/blog/"
        nav_home = "Главная"
        nav_blog = "Блог"
        nav_services = "Услуги"
    else:
        home_link = "/zh/"
        blog_link = "/zh/blog/"
        nav_home = "首页"
        nav_blog = "博客"
        nav_services = "服务"

    lang_items = {
        "en": ("EN", f"/{SLUG}/"),
        "es": ("ES", f"/es/{SLUG}/"),
        "ru": ("RU", f"/ru/{SLUG}/"),
        "zh": ("ZH", f"/zh/{SLUG}/"),
    }
    desk_langs = ""
    mob_langs = ""
    for lc, (label, href) in lang_items.items():
        active = ' active' if lc == lang else ''
        desk_langs += f'<a href="{href}" class="lang-btn{active}">{label}</a>'
        mob_style = ' style="color:#fff;background:var(--gold)"' if lc == lang else ''
        mob_langs += f'<a href="{href}" class="lang-btn"{mob_style}>{label}</a>'

    service_schema = f'''{{
  "@context":"https://schema.org",
  "@type":"Service",
  "name":"Civil Marriage Mexico — Registro Civil",
  "url":"{url}",
  "provider":{{"@type":"Organization","name":"MexVisa Pro","url":"https://mexvisapro.com"}},
  "areaServed":"MX",
  "serviceType":"Civil Marriage Registration",
  "description":"{d['desc']}"
}}'''

    bc_schema = f'''{{
  "@context":"https://schema.org",
  "@type":"BreadcrumbList",
  "itemListElement":[
    {{"@type":"ListItem","position":1,"name":"Home","item":"https://mexvisapro.com/"}},
    {{"@type":"ListItem","position":2,"name":"{d['bc']}","item":"{url}"}}
  ]
}}'''

    return f"""<!DOCTYPE html>
<html lang="{lang}">
<head>
  <meta charset="UTF-8">
  <meta name="viewport" content="width=device-width, initial-scale=1.0">
  <meta http-equiv="X-Content-Type-Options" content="nosniff">
  <meta http-equiv="X-Frame-Options" content="DENY">
  <title>{d['title']}</title>
  <meta name="description" content="{d['desc']}">
  <meta name="author" content="MexVisa Pro">
  <meta name="robots" content="index, follow, max-image-preview:large, max-snippet:-1">
  <meta name="theme-color" content="#f0a500">
  <link rel="icon" href="/favicon.ico" sizes="32x32">
  <link rel="icon" type="image/png" sizes="192x192" href="/assets/img/icon-192.png">
  <link rel="apple-touch-icon" href="/assets/img/apple-touch-icon.png">
  <link rel="canonical" href="{url}">
  <link rel="alternate" hreflang="en" href="{alt_en}">
  <link rel="alternate" hreflang="es" href="{alt_es}">
  <link rel="alternate" hreflang="ru" href="{alt_ru}">
  <link rel="alternate" hreflang="zh" href="{alt_zh}">
  <link rel="alternate" hreflang="x-default" href="{alt_en}">
  <meta property="og:title" content="{d['title']}">
  <meta property="og:description" content="{d['desc']}">
  <meta property="og:type" content="website">
  <meta property="og:url" content="{url}">
  <meta property="og:site_name" content="MexVisa Pro">
  <meta property="og:image" content="https://mexvisapro.com/assets/img/og-image.png">
  <script type="application/ld+json">{service_schema}</script>
  <script type="application/ld+json">{bc_schema}</script>
  <script type="application/ld+json">{faq_schema(lang, d['faq'])}</script>
  <link rel="preconnect" href="https://cdn.jsdelivr.net" crossorigin>
  <link rel="preconnect" href="https://fonts.googleapis.com" crossorigin>
  <link rel="preconnect" href="https://fonts.gstatic.com" crossorigin>
  <style>
    :root{{--gold:#f0a500;--dark:#0b1120;--navy:#1a2744;--bg:#f7f8fc;--accent:#00c853;--primary:#0d6efd}}
    *{{margin:0;padding:0;box-sizing:border-box}}
    html{{scroll-behavior:smooth}}
    body{{font-family:Inter,system-ui,sans-serif;color:#1e1e2d;background:#fff;overflow-x:hidden}}
    .nav-bar{{background:#fff;border-bottom:1px solid #eee;padding:.7rem 0;position:sticky;top:0;z-index:100;box-shadow:0 1px 8px rgba(0,0,0,.04)}}
    .nav-inner{{max-width:1200px;margin:0 auto;padding:0 1.5rem;display:flex;align-items:center;justify-content:space-between}}
    .brand{{font-weight:800;font-size:1.1rem;color:var(--navy);text-decoration:none;display:flex;align-items:center;gap:.4rem}}
    .brand span{{color:var(--gold)}}
    .nav-links{{display:flex;align-items:center;gap:1.5rem}}
    .nav-links a{{color:#555;text-decoration:none;font-size:.85rem;font-weight:500;transition:color .2s}}
    .nav-links a:hover{{color:var(--gold)}}
    .lang-btns{{display:flex;gap:2px}}
    .lang-btn{{display:inline-block;padding:3px 8px;border-radius:4px;font-size:.7rem;font-weight:700;color:#888;background:#f0f0f0;text-decoration:none;transition:all .2s}}
    .lang-btn:hover,.lang-btn.active{{color:#fff;background:var(--gold)}}
    .nav-wa{{background:var(--gold);color:#fff!important;padding:.35rem .9rem;border-radius:20px;font-size:.8rem;font-weight:700;text-decoration:none;transition:opacity .2s}}
    .nav-wa:hover{{opacity:.88}}
    .mobile-toggle{{display:none;background:none;border:none;cursor:pointer;padding:.2rem}}
    .hero-service{{background:linear-gradient(135deg,var(--dark) 0%,var(--navy) 100%);color:#fff;padding:3.5rem 0 3rem}}
    .hero-service h1{{font-size:clamp(1.6rem,4vw,2.5rem);font-weight:800;line-height:1.2;margin-bottom:1rem}}
    .hero-service .lead{{font-size:1rem;color:rgba(255,255,255,.8);max-width:680px;line-height:1.7}}
    .breadcrumb-bar{{background:#f8f9fa;padding:.5rem 0;font-size:.8rem}}
    .breadcrumb-bar a{{color:var(--gold);text-decoration:none}}
    .main-content{{max-width:820px;margin:0 auto;padding:2.5rem 1.5rem}}
    .main-content article{{font-size:.95rem;line-height:1.8;color:#2d2d3d}}
    .sidebar{{max-width:320px}}
    .cta-box{{background:linear-gradient(135deg,var(--gold),#e09400);color:#fff;border-radius:16px;padding:1.5rem;margin-bottom:1.5rem;text-align:center}}
    .cta-box h4{{font-size:1.1rem;font-weight:800;margin-bottom:.5rem}}
    .cta-box p{{font-size:.82rem;opacity:.9;margin-bottom:1rem}}
    .btn-wa{{display:inline-flex;align-items:center;gap:.4rem;background:#fff;color:var(--gold);font-weight:700;font-size:.85rem;padding:.6rem 1.2rem;border-radius:20px;text-decoration:none;transition:opacity .2s}}
    .btn-wa:hover{{opacity:.88;color:var(--gold)}}
    .related-box{{border:1px solid #eee;border-radius:12px;padding:1.2rem}}
    .related-box h5{{font-size:.85rem;font-weight:700;color:var(--navy);margin-bottom:.8rem;text-transform:uppercase;letter-spacing:.05em}}
    .related-box a{{display:block;font-size:.82rem;color:#444;text-decoration:none;padding:.3rem 0;border-bottom:1px solid #f5f5f5}}
    .related-box a:hover{{color:var(--gold)}}
    .faq-section{{background:#f8f9fb;padding:3rem 0}}
    .faq-inner{{max-width:820px;margin:0 auto;padding:0 1.5rem}}
    .section-title{{font-size:1.6rem;font-weight:800;color:var(--navy);margin-bottom:1.5rem}}
    footer{{background:var(--dark);color:rgba(255,255,255,.6);text-align:center;padding:1.5rem;font-size:.8rem}}
    footer a{{color:var(--gold);text-decoration:none}}
    .mobile-menu{{display:none}}@media(max-width:767.98px){{.mobile-toggle{{display:block}}.nav-links .desk-link,.nav-links .lang-btns{{display:none!important}}.mobile-menu{{display:none;position:fixed;top:0;left:0;right:0;bottom:0;background:rgba(11,17,32,.97);z-index:200;flex-direction:column;align-items:center;justify-content:center;gap:1.5rem}}.mobile-menu.open{{display:flex}}.mobile-menu a{{color:#fff;font-size:1.2rem;text-decoration:none;font-weight:600}}.mobile-menu a:hover{{color:var(--gold)}}.mobile-menu .close-btn{{position:absolute;top:1rem;right:1.5rem;background:none;border:none;color:#fff;font-size:2rem;cursor:pointer}}.mobile-menu .lang-row{{display:flex;gap:6px}}.mobile-menu .lang-row .lang-btn{{color:#555}}}}
    @media(min-width:992px){{.content-grid{{display:grid;grid-template-columns:1fr 300px;gap:2.5rem;align-items:start}}}}
    {CSS_EXTRA}
  </style>
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/css/bootstrap.min.css" crossorigin="anonymous">
  <link rel="stylesheet" href="https://cdn.jsdelivr.net/npm/bootstrap-icons@1.11.3/font/bootstrap-icons.min.css" crossorigin="anonymous">
</head>
<body>

<!-- NAV -->
<nav class="nav-bar">
  <div class="nav-inner">
    <a href="{home_link}" class="brand">MexVisa<span>Pro</span></a>
    <div class="nav-links">
      <a href="{home_link}" class="desk-link">{nav_home}</a>
      <a href="{home_link}#services" class="desk-link">{nav_services}</a>
      <a href="{blog_link}" class="desk-link">{nav_blog}</a>
      <div class="lang-btns d-none d-md-flex gap-1">{desk_langs}</div>
      <a href="https://wa.me/{WA}?text={d['wa_text'].replace(' ','%20')}" target="_blank" rel="noopener" class="nav-wa d-none d-md-flex"><i class="bi bi-whatsapp me-1"></i>{d['consult']}</a>
    </div>
    <button class="mobile-toggle" onclick="document.getElementById('mobileNav').classList.toggle('open')">
      <svg width="24" height="24" fill="none" stroke="#333" stroke-width="2"><line x1="3" y1="6" x2="21" y2="6"/><line x1="3" y1="12" x2="21" y2="12"/><line x1="3" y1="18" x2="21" y2="18"/></svg>
    </button>
  </div>
</nav>

<!-- MOBILE MENU -->
<div id="mobileNav" class="mobile-menu">
  <button class="close-btn" onclick="document.getElementById('mobileNav').classList.remove('open')">&#x2715;</button>
  <a href="{home_link}">{nav_home}</a>
  <a href="{home_link}#services">{nav_services}</a>
  <a href="{blog_link}">{nav_blog}</a>
  <a href="https://wa.me/{WA}?text={d['wa_text'].replace(' ','%20')}" target="_blank" rel="noopener"><i class="bi bi-whatsapp me-1"></i>{d['consult']}</a>
  <div class="lang-row">{mob_langs}</div>
</div>

<!-- BREADCRUMB -->
<div class="breadcrumb-bar">
  <div class="container">
    <a href="{home_link}">{nav_home}</a> › {d['bc']}
  </div>
</div>

<!-- HERO -->
<section class="hero-service">
  <div class="container">
    <h1>{d['h1']}</h1>
    <p class="lead">{d['lead']}</p>
    <div class="mt-3 d-flex flex-wrap gap-2" style="font-size:.82rem">
      <span style="background:rgba(255,255,255,.1);padding:4px 12px;border-radius:20px"><i class="bi bi-people me-1"></i>Foreigners Welcome</span>
      <span style="background:rgba(255,255,255,.1);padding:4px 12px;border-radius:20px"><i class="bi bi-rainbow me-1"></i>LGBTQ+ Inclusive</span>
      <span style="background:rgba(255,255,255,.1);padding:4px 12px;border-radius:20px"><i class="bi bi-clock me-1"></i>3–5 Weeks</span>
      <span style="background:rgba(255,255,255,.1);padding:4px 12px;border-radius:20px"><i class="bi bi-translate me-1"></i>EN / ES / RU / ZH</span>
    </div>
  </div>
</section>

<!-- MAIN -->
<div class="container py-4">
  <div class="content-grid">
    <div class="main-content p-0">
      <article>{d['body']}</article>
    </div>
    <aside class="sidebar">
      <div class="cta-box">
        <h4>Ready to Start?</h4>
        <p>Free consultation — we'll review your documents and give you a clear action plan.</p>
        <a href="https://wa.me/{WA}?text={d['wa_text'].replace(' ','%20')}" target="_blank" rel="noopener" class="btn-wa">
          <i class="bi bi-whatsapp"></i>{d['consult']}
        </a>
      </div>
      <div class="related-box mt-3">
        <h5>Related Guides</h5>
        <a href="/blog/marriage-mexican-citizen-visa/"><i class="bi bi-arrow-right me-1"></i>Marriage Visa Guide</a>
        <a href="/blog/family-reunification-visa-mexico/"><i class="bi bi-arrow-right me-1"></i>Family Reunification</a>
        <a href="/blog/permanent-residency-mexico-requirements/"><i class="bi bi-arrow-right me-1"></i>Permanent Residency</a>
        <a href="/blog/mexico-citizenship-naturalization/"><i class="bi bi-arrow-right me-1"></i>Naturalization / Citizenship</a>
        <a href="/blog/apostille-documents-mexico-immigration/"><i class="bi bi-arrow-right me-1"></i>Apostille Documents Mexico</a>
      </div>
    </aside>
  </div>
</div>

<!-- FAQ -->
<section class="faq-section">
  <div class="faq-inner">
    <h2 class="section-title">FAQ</h2>
    <div class="accordion" id="faqAccordion">{faq_rows}
    </div>
  </div>
</section>

<!-- FOOTER -->
<footer>
  <p>© 2026 MexVisa Pro — <a href="/privacy/">Privacy</a> · <a href="/terms/">Terms</a> · <a href="{blog_link}">{nav_blog}</a></p>
</footer>

<script src="https://cdn.jsdelivr.net/npm/bootstrap@5.3.3/dist/js/bootstrap.bundle.min.js" crossorigin="anonymous"></script>
</body>
</html>"""

# ── Generate files ──────────────────────────────────────────────────────────
count = 0
for lang, cfg in LANGS.items():
    d = DATA[lang]
    if cfg["dir"]:
        out_dir = f"/home/olek/immigration-site/{cfg['dir']}{SLUG}"
    else:
        out_dir = f"/home/olek/immigration-site/{SLUG}"
    os.makedirs(out_dir, exist_ok=True)
    path = f"{out_dir}/index.html"
    with open(path, "w", encoding="utf-8") as f:
        f.write(page(lang, d))
    count += 1
    print(f"  {path}")

print(f"\nDone — {count} files written.")
