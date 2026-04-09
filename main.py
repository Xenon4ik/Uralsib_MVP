from flask import Flask, render_template_string, url_for, send_from_directory
from pathlib import Path

BASE_DIR = Path(__file__).resolve().parent
SRC_DIR = BASE_DIR / "src"

app = Flask(__name__)

BASE_STYLES = """
<style>
  :root {
    --bg: #f6f4fb;
    --surface: #ffffff;
    --surface-2: #f2eefc;
    --text: #1f2430;
    --muted: #667085;
    --primary: #6e40d8;
    --primary-dark: #5c32bc;
    --border: #e7e1f6;
    --success: #2e9e61;
    --shadow: 0 10px 30px rgba(74, 34, 137, 0.08);
    --radius: 22px;
    --maxw: 1180px;
  }

  * { box-sizing: border-box; }
  body {
    margin: 0;
    font-family: Inter, ui-sans-serif, system-ui, -apple-system, BlinkMacSystemFont, "Segoe UI", sans-serif;
    background: linear-gradient(180deg, #faf8ff 0%, #f6f4fb 100%);
    color: var(--text);
  }
  a { color: inherit; text-decoration: none; }
  .container { width: min(var(--maxw), calc(100% - 32px)); margin: 0 auto; }

  .header {
    position: sticky;
    top: 0;
    z-index: 10;
    backdrop-filter: blur(10px);
    background: #ffffff;
    border-bottom: 1px solid rgba(231,225,246,0.9);
  }
  .header-inner {
    display: flex;
    justify-content: space-between;
    align-items: center;
    min-height: 76px;
    gap: 18px;
  }
  .brand {
    display: flex;
    align-items: center;
    gap: 12px;
  }
  .brand img {
    height: 54px;
    width: auto;
    display: block;
  }
  .header-actions {
    display: flex;
    align-items: center;
    gap: 12px;
    flex-wrap: wrap;
  }

  .btn {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    gap: 8px;
    padding: 14px 22px;
    border-radius: 14px;
    border: 1px solid transparent;
    font-weight: 700;
    transition: .2s ease;
    cursor: pointer;
  }
  .btn:hover { transform: translateY(-1px); }
  .btn-primary {
    background: linear-gradient(135deg, #7a4ce6 0%, #6437d0 100%);
    color: white;
    box-shadow: 0 12px 26px rgba(110, 64, 216, 0.22);
  }
  .btn-primary:hover { background: linear-gradient(135deg, #6f40df 0%, #5c32bc 100%); }
  .btn-secondary {
    background: white;
    color: var(--primary);
    border-color: #d8cef4;
  }
  .btn-ghost {
    background: var(--surface-2);
    color: var(--primary);
    border-color: var(--border);
  }

  .hero {
    padding: 40px 0 26px;
  }
  .hero-card {
    background: radial-gradient(circle at top right, rgba(144, 116, 236, 0.18), transparent 35%), var(--surface);
    border: 1px solid var(--border);
    border-radius: 30px;
    box-shadow: var(--shadow);
    padding: 40px;
    display: grid;
    grid-template-columns: 1.1fr 0.9fr;
    gap: 28px;
    align-items: center;
    overflow: hidden;
  }
  .eyebrow {
    display: inline-flex;
    align-items: center;
    gap: 10px;
    padding: 8px 14px;
    border-radius: 999px;
    background: #f3edff;
    color: var(--primary);
    font-size: 14px;
    font-weight: 700;
    margin-bottom: 18px;
  }
  h1 {
    margin: 0 0 16px;
    font-size: clamp(36px, 5vw, 58px);
    line-height: 1.02;
    letter-spacing: -0.03em;
  }
  .lead {
    margin: 0 0 22px;
    font-size: 18px;
    line-height: 1.65;
    color: var(--muted);
    max-width: 680px;
  }
  .hero-actions {
    display: flex;
    gap: 14px;
    flex-wrap: wrap;
    margin-bottom: 20px;
  }
  .micro-benefits {
    display: flex;
    flex-wrap: wrap;
    gap: 14px;
    color: var(--muted);
    font-size: 15px;
  }
  .micro-benefits span {
    display: inline-flex;
    gap: 8px;
    align-items: center;
    padding: 10px 14px;
    background: #faf7ff;
    border: 1px solid #ece4ff;
    border-radius: 999px;
  }
  .dot {
    width: 10px;
    height: 10px;
    border-radius: 50%;
    background: var(--success);
    box-shadow: 0 0 0 4px rgba(46,158,97,0.12);
  }

  .hero-side {
    position: relative;
    min-height: 360px;
  }
  .hero-visual {
    position: absolute;
    inset: 0;
    border-radius: 26px;
    background: linear-gradient(135deg, rgba(126,79,232,0.16), rgba(126,79,232,0.04));
    border: 1px solid rgba(126,79,232,0.16);
    display: grid;
    place-items: center;
    overflow: hidden;
  }
  .visual-folder {
    width: 280px;
    height: 200px;
    border-radius: 28px;
    background: linear-gradient(180deg, #ffffff 0%, #efe8ff 100%);
    border: 1px solid #dccffb;
    box-shadow: 0 30px 60px rgba(110, 64, 216, 0.16);
    position: relative;
  }
  .visual-folder::before {
    content: "";
    position: absolute;
    width: 120px;
    height: 34px;
    left: 26px;
    top: -12px;
    border-radius: 16px 16px 0 0;
    background: #f5efff;
    border: 1px solid #dccffb;
    border-bottom: none;
  }
  .visual-folder::after {
    content: "0₽";
    position: absolute;
    right: -22px;
    top: -38px;
    font-size: 54px;
    font-weight: 800;
    color: rgba(110, 64, 216, 0.75);
  }
  .visual-badge {
    position: absolute;
    right: 16px;
    bottom: 18px;
    width: 76px;
    height: 76px;
    border-radius: 22px;
    background: linear-gradient(180deg, #bb9cff 0%, #7a4ce6 100%);
    display: grid;
    place-items: center;
    color: white;
    font-size: 36px;
    box-shadow: 0 18px 34px rgba(110, 64, 216, 0.3);
  }
  .floating-note {
    position: absolute;
    top: 16px;
    right: 10px;
    width: 250px;
    background: rgba(255,255,255,0.96);
    border: 1px solid var(--border);
    border-radius: 18px;
    box-shadow: var(--shadow);
    padding: 16px;
    font-size: 14px;
    color: var(--muted);
  }
  .floating-note strong { display: block; margin-bottom: 8px; color: var(--text); }

  .section {
    padding: 18px 0 28px;
  }
  .section-title {
    margin: 0 0 8px;
    font-size: 34px;
    line-height: 1.15;
    letter-spacing: -0.02em;
  }
  .section-subtitle {
    margin: 0 0 20px;
    color: var(--muted);
    font-size: 18px;
  }

  .features-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 16px;
  }
  .feature {
    background: white;
    border: 1px solid var(--border);
    border-radius: 20px;
    padding: 20px;
    box-shadow: var(--shadow);
  }
  .feature-icon {
    width: 42px;
    height: 42px;
    border-radius: 14px;
    background: #f2ebff;
    color: var(--primary);
    display: grid;
    place-items: center;
    font-weight: 800;
    margin-bottom: 14px;
  }
  .feature h3 { margin: 0 0 8px; font-size: 20px; }
  .feature p { margin: 0; color: var(--muted); line-height: 1.6; }

  .split {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 18px;
  }
  .choice-card {
    background: white;
    border: 1px solid var(--border);
    border-radius: 24px;
    padding: 28px;
    box-shadow: var(--shadow);
    position: relative;
  }
  .choice-card h3 {
    margin: 0 0 6px;
    font-size: 34px;
    color: var(--primary);
  }
  .choice-card p {
    margin: 0 0 14px;
    color: var(--muted);
    font-size: 18px;
  }
  .tag {
    display: inline-block;
    padding: 8px 12px;
    border-radius: 999px;
    font-size: 13px;
    font-weight: 700;
    background: #f1ebff;
    color: var(--primary);
    margin-bottom: 12px;
  }
  .choice-list { margin: 0 0 18px; padding-left: 20px; color: var(--text); }
  .choice-list li { margin: 10px 0; }
  .helper-box {
    margin-top: 18px;
    background: #faf7ff;
    border: 1px dashed #d8cef4;
    border-radius: 18px;
    padding: 18px;
    color: var(--muted);
  }
  .helper-box strong { display: block; color: var(--text); margin-bottom: 6px; }

  .steps-grid {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 16px;
  }
  .step {
    background: white;
    border: 1px solid var(--border);
    border-radius: 22px;
    padding: 22px;
    box-shadow: var(--shadow);
  }
  .step-num {
    color: var(--primary);
    font-weight: 800;
    font-size: 30px;
    margin-bottom: 10px;
  }
  .step h3 { margin: 0 0 8px; font-size: 22px; }
  .step p { margin: 0; color: var(--muted); line-height: 1.65; }

  .trust-grid {
    display: grid;
    grid-template-columns: 1.15fr 0.85fr;
    gap: 16px;
  }
  .trust-card, .faq-card, .cta-band {
    background: white;
    border: 1px solid var(--border);
    border-radius: 24px;
    box-shadow: var(--shadow);
  }
  .trust-card { padding: 28px; }
  .trust-card h3 { margin: 0 0 12px; font-size: 28px; }
  .trust-card p, .trust-card li { color: var(--muted); line-height: 1.7; }
  .trust-list { margin: 0; padding-left: 20px; }

  .faq {
    display: grid;
    gap: 12px;
  }
  details {
    background: white;
    border: 1px solid var(--border);
    border-radius: 16px;
    padding: 18px 20px;
    box-shadow: var(--shadow);
  }
  summary {
    cursor: pointer;
    font-weight: 700;
    list-style: none;
  }
  summary::-webkit-details-marker { display: none; }
  details p { margin: 12px 0 0; color: var(--muted); line-height: 1.65; }

  .cta-band {
    margin-top: 24px;
    padding: 26px;
    background: linear-gradient(135deg, #7a4ce6 0%, #5e33bf 100%);
    color: white;
    display: flex;
    justify-content: space-between;
    gap: 18px;
    align-items: center;
    flex-wrap: wrap;
  }
  .cta-band h3 { margin: 0 0 8px; font-size: 30px; }
  .cta-band p { margin: 0; color: rgba(255,255,255,0.86); }
  .cta-band .btn-secondary { color: white; border-color: rgba(255,255,255,0.35); background: rgba(255,255,255,0.08); }

  .footer {
    padding: 32px 0 48px;
    color: var(--muted);
    font-size: 14px;
  }
  .footer-grid {
    display: flex;
    justify-content: space-between;
    gap: 20px;
    flex-wrap: wrap;
    border-top: 1px solid var(--border);
    padding-top: 24px;
  }

  .page-card {
    width: min(760px, calc(100% - 32px));
    margin: 56px auto;
    padding: 36px;
    border-radius: 28px;
    background: white;
    border: 1px solid var(--border);
    box-shadow: var(--shadow);
  }
  .page-card h1 {
    font-size: 38px;
    margin-bottom: 14px;
  }
  .page-card p {
    color: var(--muted);
    font-size: 18px;
    line-height: 1.7;
  }

  @media (max-width: 1024px) {
    .hero-card, .split, .steps-grid, .features-grid, .trust-grid { grid-template-columns: 1fr; }
    .hero-side { min-height: 320px; }
  }
  @media (max-width: 720px) {
    .header-inner {
      min-height: 68px;
      align-items: center;
    }

    .hero-card {
      padding: 24px;
    }

    h1 {
      font-size: 38px;
    }

    .section-title {
      font-size: 28px;
    }

    .floating-note {
      position: static;
      width: auto;
      margin-top: 16px;
    }

    .hero-side {
      min-height: 260px;
    }

    .visual-folder {
      width: 220px;
      height: 160px;
    }

    .hero-actions,
    .micro-benefits {
      flex-direction: column;
      align-items: stretch;
    }

    .hero-actions .btn {
      width: 100%;
    }

    .header-actions {
      flex-direction: row;
      align-items: center;
      gap: 8px;
      flex-wrap: nowrap;
    }

    .header-actions .btn {
      width: auto;
      padding: 10px 14px;
      font-size: 14px;
      border-radius: 12px;
      white-space: nowrap;
    }

    .brand img {
      height: 34px;
    }
  }
</style>
"""


def render_header():
    return f"""
    <header class=\"header\">
      <div class=\"container header-inner\">
        <a class=\"brand\" href=\"{url_for('landing')}\" aria-label=\"Уралсиб\">
          <img src=\"{url_for('serve_src', filename='logo.png')}\" alt=\"Уралсиб\" />
        </a>
        <div class=\"header-actions\">
          <a href=\"{url_for('login_page')}\" class=\"btn btn-secondary\">Войти</a>
          <a href=\"{url_for('register_page')}\" class=\"btn btn-primary\">Зарегистрироваться</a>
        </div>
      </div>
    </header>
    """


@app.route('/src/<path:filename>')
def serve_src(filename: str):
    return send_from_directory(SRC_DIR, filename)


@app.route('/')
def landing():
    return render_template_string(
        f"""
<!DOCTYPE html>
<html lang=\"ru\">
<head>
  <meta charset=\"UTF-8\" />
  <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\" />
  <title>Регистрация бизнеса — Уралсиб</title>
  {BASE_STYLES}
</head>
<body>
  {render_header()}

  <main>
    <section class=\"hero\">
      <div class=\"container\">
        <div class=\"hero-card\">
          <div>
            <div class=\"eyebrow\">0 ₽ за регистрацию бизнеса</div>
            <h1>Бесплатная регистрация бизнеса в Уралсибе</h1>
            <p class=\"lead\">Подготовим и отправим документы в ФНС онлайн. Без походов в банк и налоговую. Начать можно за 5–10 минут.</p>
            <div class=\"hero-actions\" id=\"start\">
              <a class=\"btn btn-primary\" href=\"#choice\">Начать новую регистрацию</a>
              <a class=\"btn btn-secondary\" href=\"#continue\">Уже начали? Продолжить</a>
            </div>
            <div class=\"micro-benefits\">
              <span><i class=\"dot\"></i> Без госпошлины</span>
              <span><i class=\"dot\"></i> Понадобятся базовые данные</span>
              <span><i class=\"dot\"></i> Документы сформируем за вас</span>
            </div>
          </div>
          <div class=\"hero-side\">
            <div class=\"hero-visual\">
              <div class=\"visual-folder\">
                <div class=\"visual-badge\">✓</div>
              </div>
            </div>
            <div class=\"floating-note\">
              <strong>Что будет дальше?</strong>
              1) Вы выберете ИП или ООО. 2) Заполните короткую анкету. 3) Мы подготовим комплект документов и отправим его в ФНС.
            </div>
          </div>
        </div>
      </div>
    </section>

    <section class=\"section\">
      <div class=\"container features-grid\">
        <div class=\"feature\">
          <div class=\"feature-icon\">₽</div>
          <h3>Бесплатно откроем счет</h3>
          <p>Без комиссий за регистрацию и без оплаты госпошлины.</p>
        </div>
        <div class=\"feature\">
          <div class=\"feature-icon\">⌁</div>
          <h3>Все онлайн</h3>
          <p>Не нужно ехать в банк или налоговую — пройдете путь дистанционно.</p>
        </div>
        <div class=\"feature\">
          <div class=\"feature-icon\">✓</div>
          <h3>Поможем на каждом шаге</h3>
          <p>Понятные подсказки, короткие правила и помощь в выборе сценария.</p>
        </div>
      </div>
    </section>

    <section class=\"section\" id=\"choice\">
      <div class=\"container\">
        <h2 class=\"section-title\">Какой формат подходит вам?</h2>
        <p class=\"section-subtitle\">Если вы еще не уверены, начните с короткой подсказки — она поможет выбрать сценарий без ошибки.</p>
        <div class=\"split\">
          <article class=\"choice-card\">
            <span class=\"tag\">Проще и быстрее</span>
            <h3>ИП</h3>
            <p>Подходит для старта, работы без партнеров и большинства услуг.</p>
            <ul class=\"choice-list\">
              <li>Меньше документов и проще учет</li>
              <li>Часто оптимально для фриланса, маркетплейсов и собственных услуг</li>
              <li>Быстрый старт без сложной структуры компании</li>
            </ul>
            <a class=\"btn btn-primary\" href=\"#steps\">Оформить ИП</a>
          </article>
          <article class=\"choice-card\">
            <span class=\"tag\">Для роста и партнеров</span>
            <h3>ООО</h3>
            <p>Подходит для совместного бизнеса, партнеров и работы с компаниями.</p>
            <ul class=\"choice-list\">
              <li>Удобно, если планируете развивать компанию вместе с партнерами</li>
              <li>Больше возможностей для работы с юрлицами</li>
              <li>Надежнее воспринимается в ряде B2B-сценариев</li>
            </ul>
            <a class=\"btn btn-secondary\" href=\"#steps\">Оформить ООО</a>
          </article>
        </div>
        <div class=\"helper-box\">
          <strong>Не уверены, что выбрать?</strong>
          ИП — если вы начинаете один и хотите быстро стартовать. ООО — если планируете партнеров, совместный бизнес или работу с компаниями.
        </div>
      </div>
    </section>

    <section class=\"section\" id=\"steps\">
      <div class=\"container\">
        <h2 class=\"section-title\">3 коротких шага до регистрации бизнеса</h2>
        <p class=\"section-subtitle\">Мы убираем лишнюю неопределенность на старте и ведем пользователя по понятному сценарию.</p>
        <div class=\"steps-grid\">
          <article class=\"step\">
            <div class=\"step-num\">01</div>
            <h3>Выберите сценарий</h3>
            <p>Подскажем, что подойдет — ИП или ООО, и сразу покажем, что понадобится дальше.</p>
          </article>
          <article class=\"step\">
            <div class=\"step-num\">02</div>
            <h3>Заполните короткую анкету</h3>
            <p>Форма разбита на логичные шаги, а сложные поля объясняются простым языком.</p>
          </article>
          <article class=\"step\">
            <div class=\"step-num\">03</div>
            <h3>Проверьте и отправьте</h3>
            <p>Покажем финальный summary, чтобы пользователь видел, что именно уйдет в ФНС.</p>
          </article>
        </div>
      </div>
    </section>

    <section class=\"section\">
      <div class=\"container trust-grid\">
        <div class=\"trust-card\">
          <h3>Почему это снижает drop-off?</h3>
          <ul class=\"trust-list\">
            <li>Разводим сценарии нового и возвращающегося пользователя.</li>
            <li>Помогаем выбрать ИП или ООО до старта формы.</li>
            <li>Снижаем perceived effort за счет коротких и понятных шагов.</li>
            <li>Делаем первый вход менее тревожным и более прозрачным.</li>
          </ul>
        </div>
        <div class=\"trust-card\" id=\"continue\">
          <h3>Уже начали регистрацию?</h3>
          <p>Продолжите с того места, где остановились. В текущем MVP этот сценарий выделен отдельно и не конкурирует со стартом новой регистрации.</p>
          <div style=\"margin-top:16px; display:flex; gap:12px; flex-wrap:wrap;\">
            <a class=\"btn btn-secondary\" href=\"{url_for('login_page')}\">Войти в кабинет</a>
            <a class=\"btn btn-ghost\" href=\"#\">Зачем нужен вход?</a>
          </div>
        </div>
      </div>
    </section>

    <section class=\"section\">
      <div class=\"container\">
        <h2 class=\"section-title\">Частые вопросы</h2>
        <div class=\"faq\">
          <details open>
            <summary>Сколько времени займет регистрация?</summary>
            <p>Старт сценария занимает 5–10 минут. Далее пользователь проходит форму по шагам, а комплект документов мы формируем автоматически.</p>
          </details>
          <details>
            <summary>Нужно ли идти в банк или налоговую?</summary>
            <p>Нет, основной путь проходит онлайн. В MVP мы подчеркиваем это уже на первом экране, чтобы снизить тревожность на старте.</p>
          </details>
          <details>
            <summary>Что делать, если я не знаю, оформлять ИП или ООО?</summary>
            <p>Для этого добавлен отдельный блок выбора с короткой подсказкой: ИП — для быстрого старта без партнеров, ООО — для роста, партнеров и работы с компаниями.</p>
          </details>
        </div>

        <div class=\"cta-band\">
          <div>
            <h3>Готовы зарегистрировать бизнес?</h3>
            <p>Начните новый сценарий или продолжите уже начатую заявку — без лишних развилок и путаницы.</p>
          </div>
          <div style=\"display:flex; gap:12px; flex-wrap:wrap;\">
            <a class=\"btn btn-secondary\" href=\"#choice\">Начать регистрацию</a>
            <a class=\"btn btn-secondary\" href=\"{url_for('login_page')}\">Продолжить начатую</a>
          </div>
        </div>
      </div>
    </section>
  </main>

  <footer class=\"footer\">
    <div class=\"container footer-grid\">
      <div>
        <a class=\"brand\" href=\"{url_for('landing')}\" aria-label=\"Уралсиб\">
          <img src=\"{url_for('serve_src', filename='logo.png')}\" alt=\"Уралсиб\" />
        </a>
        <div style=\"margin-top: 12px;\">МVP-лендинг для хакатона: редизайн старта воронки онлайн-регистрации бизнеса.</div>
      </div>
      <div>© 2026. Концепт для презентации решения.</div>
    </div>
  </footer>
</body>
</html>
        """
    )


@app.route('/login')
def login_page():
    return render_template_string(
        f"""
<!DOCTYPE html>
<html lang=\"ru\">
<head>
  <meta charset=\"UTF-8\" />
  <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\" />
  <title>Войти — Уралсиб</title>
  {BASE_STYLES}
</head>
<body>
  {render_header()}
  <main>
    <section class=\"page-card\">
      <div class=\"eyebrow\">Продолжить начатую заявку</div>
      <h1>Вход в личный кабинет</h1>
      <p>Здесь будет отдельный сценарий для пользователей, которые уже начали регистрацию и хотят вернуться к заявке.</p>
      <div style=\"margin-top: 22px; display:flex; gap:12px; flex-wrap:wrap;\">
        <a href=\"{url_for('landing')}\" class=\"btn btn-secondary\">Назад на лендинг</a>
        <a href=\"{url_for('register_page')}\" class=\"btn btn-primary\">Новая регистрация</a>
      </div>
    </section>
  </main>
</body>
</html>
        """
    )


@app.route('/register')
def register_page():
    return render_template_string(
        f"""
<!DOCTYPE html>
<html lang=\"ru\">
<head>
  <meta charset=\"UTF-8\" />
  <meta name=\"viewport\" content=\"width=device-width, initial-scale=1.0\" />
  <title>Зарегистрироваться — Уралсиб</title>
  {BASE_STYLES}
</head>
<body>
  {render_header()}
  <main>
    <section class=\"page-card\">
      <div class=\"eyebrow\">Новый пользователь</div>
      <h1>Начало регистрации бизнеса</h1>
      <p>Здесь будет отдельный сценарий старта новой регистрации: выбор ИП или ООО, короткая подсказка и переход в форму.</p>
      <div style=\"margin-top: 22px; display:flex; gap:12px; flex-wrap:wrap;\">
        <a href=\"{url_for('landing')}\" class=\"btn btn-secondary\">Назад на лендинг</a>
        <a href=\"{url_for('login_page')}\" class=\"btn btn-ghost\">Уже есть заявка?</a>
      </div>
    </section>
  </main>
</body>
</html>
        """
    )


if __name__ == '__main__':
    app.run(debug=True)
