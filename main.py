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
    white-space: nowrap;
  }

  .btn:hover { transform: translateY(-1px); }

  .btn-primary {
    background: linear-gradient(135deg, #7a4ce6 0%, #6437d0 100%);
    color: white;
    box-shadow: 0 12px 26px rgba(110, 64, 216, 0.22);
  }

  .btn-primary:hover {
    background: linear-gradient(135deg, #6f40df 0%, #5c32bc 100%);
  }

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
    padding: 26px 0 28px;
    background: radial-gradient(circle at top right, rgba(144, 116, 236, 0.16), transparent 35%), #fbf9ff;
  }

  .hero-card {
    padding: 34px;
  }

  .hero-top {
    display: grid;
    grid-template-columns: 1.05fr 0.95fr;
    gap: 24px;
    align-items: center;
    margin-bottom: 22px;
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
    font-size: clamp(34px, 5vw, 60px);
    line-height: 1.02;
    letter-spacing: -0.03em;
  }

  .hero-title-accent {
    color: var(--primary);
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
    margin-bottom: 18px;
  }

  .hero-benefits {
    display: flex;
    flex-wrap: wrap;
    gap: 18px;
    color: var(--muted);
    font-size: 15px;
  }

  .hero-benefits span {
    display: inline-flex;
    gap: 10px;
    align-items: center;
  }

  .dot {
    width: 10px;
    height: 10px;
    border-radius: 50%;
    background: #9d78ff;
    box-shadow: 0 0 0 4px rgba(157,120,255,0.16);
  }

  .hero-side {
    display: flex;
    align-items: center;
    justify-content: center;
    min-height: 320px;
  }

  .hero-side img {
    width: 100%;
    max-width: 520px;
    height: auto;
    display: block;
    object-fit: contain;
  }

  .feature-row {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 16px;
  }

  .feature-strip {
    background: white;
    border: 1px solid var(--border);
    border-radius: 20px;
    padding: 18px 20px;
    box-shadow: var(--shadow);
    display: flex;
    align-items: center;
    gap: 16px;
  }

  .feature-strip img {
    width: 42px;
    height: 42px;
    object-fit: contain;
    flex: 0 0 42px;
  }

  .feature-strip h3 {
    margin: 0 0 4px;
    font-size: 18px;
  }

  .feature-strip p {
    margin: 0;
    color: var(--muted);
    line-height: 1.5;
    font-size: 15px;
  }

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

  .choice-list {
    margin: 0 0 18px;
    padding-left: 20px;
    color: var(--text);
  }

  .choice-list li {
    margin: 10px 0;
  }

  .helper-box {
    margin-top: 18px;
    background: #faf7ff;
    border: 1px dashed #d8cef4;
    border-radius: 18px;
    padding: 18px;
    color: var(--muted);
  }

  .helper-box strong {
    display: block;
    color: var(--text);
    margin-bottom: 6px;
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

  @media (max-width: 1024px) {
    .hero-top,
    .feature-row,
    .split {
      grid-template-columns: 1fr;
    }

    .hero-side {
      min-height: 240px;
    }
  }

  @media (max-width: 720px) {
    .header-inner {
      min-height: 68px;
      align-items: center;
    }

    .brand img {
      height: 34px;
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
    }

    .hero-card {
      padding: 22px 18px 18px;
    }

    h1 {
      font-size: 38px;
    }

    .hero-actions {
      flex-direction: row;
      flex-wrap: wrap;
    }

    .hero-actions .btn {
      flex: 1 1 160px;
    }

    .hero-benefits {
      flex-direction: column;
      align-items: flex-start;
      gap: 10px;
    }
  }
</style>
"""


def render_header():
    return f"""
    <header class="header">
      <div class="container header-inner">
        <a class="brand" href="{url_for('landing')}" aria-label="Уралсиб">
          <img src="{url_for('serve_src', filename='logo.png')}" alt="Уралсиб" />
        </a>
        <div class="header-actions">
          <a href="{url_for('login_page')}" class="btn btn-secondary">Войти</a>
          <a href="{url_for('register_page')}" class="btn btn-primary">Зарегистрироваться</a>
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
<html lang="ru">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Регистрация бизнеса — Уралсиб</title>
  {BASE_STYLES}
</head>
<body>
  {render_header()}

  <main>
    <section class="hero">
      <div class="container">
        <div class="hero-card">
          <div class="hero-top">
            <div>
              <div class="eyebrow">0 ₽ за регистрацию</div>
              <h1>Бесплатная регистрация <span class="hero-title-accent">бизнеса в Уралсибе</span></h1>
              <p class="lead">Подготовим и отправим все документы в ФНС онлайн. Откройте счёт и начните работать — без визита в налоговую.</p>

              <div class="hero-actions">
                <a class="btn btn-primary" href="{url_for('ip_form_page')}">Оформить ИП</a>
                <a class="btn btn-secondary" href="{url_for('ooo_form_page')}">Оформить ООО</a>
              </div>

              <div class="hero-benefits">
                <span><i class="dot"></i> Без оплаты госпошлины</span>
                <span><i class="dot"></i> Без походов в банк</span>
                <span><i class="dot"></i> Готово от 1 дня</span>
              </div>
            </div>

            <div class="hero-side">
              <img src="{url_for('serve_src', filename='rocket.png')}" alt="Регистрация бизнеса" />
            </div>
          </div>

          <div class="feature-row">
            <div class="feature-strip">
              <img src="{url_for('serve_src', filename='icon1.png')}" alt="Бесплатно откроем счёт" />
              <div>
                <h3>Бесплатно откроем счёт</h3>
                <p>Без условий и комиссий</p>
              </div>
            </div>

            <div class="feature-strip">
              <img src="{url_for('serve_src', filename='icon2.png')}" alt="Всё онлайн" />
              <div>
                <h3>Всё онлайн</h3>
                <p>Без посещения банка и налоговой</p>
              </div>
            </div>

            <div class="feature-strip">
              <img src="{url_for('serve_src', filename='icon3.png')}" alt="Поможем на каждом шаге" />
              <div>
                <h3>Поможем на каждом шаге</h3>
                <p>Подсказки, понятные инструкции и поддержка</p>
              </div>
            </div>
          </div>
        </div>
      </div>
    </section>

    <section class="section" id="choice">
      <div class="container">
        <h2 class="section-title">Какой формат подходит вам?</h2>
        <p class="section-subtitle">Если вы еще не уверены, начните с короткой подсказки — она поможет выбрать сценарий без ошибки.</p>

        <div class="split">
          <article class="choice-card">
            <span class="tag">Проще и быстрее</span>
            <h3>ИП</h3>
            <p>Подходит для старта, работы без партнеров и большинства услуг.</p>
            <ul class="choice-list">
              <li>Меньше документов и проще учет</li>
              <li>Часто оптимально для фриланса, маркетплейсов и собственных услуг</li>
              <li>Быстрый старт без сложной структуры компании</li>
            </ul>
            <a class="btn btn-primary" href="{url_for('ip_form_page')}">Оформить ИП</a>
          </article>

          <article class="choice-card">
            <span class="tag">Для роста и партнеров</span>
            <h3>ООО</h3>
            <p>Подходит для совместного бизнеса, партнеров и работы с компаниями.</p>
            <ul class="choice-list">
              <li>Удобно, если планируете развивать компанию вместе с партнерами</li>
              <li>Больше возможностей для работы с юрлицами</li>
              <li>Надежнее воспринимается в ряде B2B-сценариев</li>
            </ul>
            <a class="btn btn-secondary" href="{url_for('ooo_form_page')}">Оформить ООО</a>
          </article>
        </div>

        <div class="helper-box">
          <strong>Не уверены, что выбрать?</strong>
          ИП — если вы начинаете один и хотите быстро стартовать. ООО — если планируете партнеров, совместный бизнес или работу с компаниями.
        </div>
      </div>
    </section>
  </main>

  <footer class="footer">
    <div class="container footer-grid">
      <div>
        <a class="brand" href="{url_for('landing')}" aria-label="Уралсиб">
          <img src="{url_for('serve_src', filename='logo.png')}" alt="Уралсиб" />
        </a>
        <div style="margin-top: 12px;">MVP-лендинг для хакатона: редизайн старта воронки онлайн-регистрации бизнеса.</div>
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
<html lang="ru">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Войти — Уралсиб</title>
  {BASE_STYLES}
</head>
<body>
  {render_header()}
  <main>
    <section class="page-card">
      <div class="eyebrow">Продолжить начатую заявку</div>
      <h1>Вход в личный кабинет</h1>
      <p>Здесь будет отдельный сценарий для пользователей, которые уже начали регистрацию и хотят вернуться к заявке.</p>
      <div style="margin-top: 22px; display:flex; gap:12px; flex-wrap:wrap;">
        <a href="{url_for('landing')}" class="btn btn-secondary">Назад на лендинг</a>
        <a href="{url_for('register_page')}" class="btn btn-primary">Новая регистрация</a>
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
<html lang="ru">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Зарегистрироваться — Уралсиб</title>
  {BASE_STYLES}
</head>
<body>
  {render_header()}
  <main>
    <section class="page-card">
      <div class="eyebrow">Новый пользователь</div>
      <h1>Начало регистрации бизнеса</h1>
      <p>Здесь будет отдельный сценарий старта новой регистрации: выбор ИП или ООО, короткая подсказка и переход в форму.</p>
      <div style="margin-top: 22px; display:flex; gap:12px; flex-wrap:wrap;">
        <a href="{url_for('landing')}" class="btn btn-secondary">Назад на лендинг</a>
        <a href="{url_for('login_page')}" class="btn btn-ghost">Уже есть заявка?</a>
      </div>
    </section>
  </main>
</body>
</html>
        """
    )

@app.route('/ip-form')
def ip_form_page():
    return render_template_string(
        f"""
<!DOCTYPE html>
<html lang="ru">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Форма ИП — Уралсиб</title>
  {BASE_STYLES}
</head>
<body>
  {render_header()}
  <main>
    <section class="page-card">
      <div class="eyebrow">Сценарий ИП</div>
      <h1>Форма регистрации ИП</h1>
      <p>Здесь будет форма регистрации ИП. Пока это заглушка для MVP.</p>
      <div style="margin-top: 22px; display:flex; gap:12px; flex-wrap:wrap;">
        <a href="{url_for('landing')}" class="btn btn-secondary">Назад на лендинг</a>
        <a href="{url_for('ooo_form_page')}" class="btn btn-ghost">Перейти к ООО</a>
      </div>
    </section>
  </main>
</body>
</html>
        """
    )


@app.route('/ooo-form')
def ooo_form_page():
    return render_template_string(
        f"""
<!DOCTYPE html>
<html lang="ru">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>Форма ООО — Уралсиб</title>
  {BASE_STYLES}
</head>
<body>
  {render_header()}
  <main>
    <section class="page-card">
      <div class="eyebrow">Сценарий ООО</div>
      <h1>Форма регистрации ООО</h1>
      <p>Здесь будет форма регистрации ООО. Пока это заглушка для MVP.</p>
      <div style="margin-top: 22px; display:flex; gap:12px; flex-wrap:wrap;">
        <a href="{url_for('landing')}" class="btn btn-secondary">Назад на лендинг</a>
        <a href="{url_for('ip_form_page')}" class="btn btn-ghost">Перейти к ИП</a>
      </div>
    </section>
  </main>
</body>
</html>
        """
    )

if __name__ == '__main__':
    app.run(debug=True)
