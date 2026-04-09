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

  .container {
    width: min(var(--maxw), calc(100% - 32px));
    margin: 0 auto;
  }
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

  .btn:hover {
    transform: translateY(-1px);
  }

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
    margin: 18px 150px 0;
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

  .format-section {
    padding: 22px 0 34px;
  }

  .format-top {
    display: flex;
    justify-content: space-between;
    align-items: flex-start;
    gap: 20px;
    margin-bottom: 18px;
  }

  .format-head h2 {
    margin: 0 0 8px;
    font-size: 46px;
    line-height: 1.05;
    letter-spacing: -0.03em;
  }

  .format-head p {
    margin: 0;
    color: var(--muted);
    font-size: 18px;
    line-height: 1.6;
  }

  .format-pills {
    display: flex;
    flex-wrap: wrap;
    gap: 12px;
    justify-content: flex-end;
  }

  .format-pill {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    min-height: 54px;
    padding: 0 22px;
    border-radius: 18px;
    background: #ffffff;
    border: 1px solid #ece7f7;
    color: var(--text);
    font-size: 16px;
    font-weight: 500;
    box-shadow: var(--shadow);
  }

  .format-pill-outline {
    border: 2px solid #b89af4;
    color: var(--primary);
    font-weight: 700;
  }

  .format-grid {
    display: grid;
    grid-template-columns: 1fr 1fr;
    gap: 18px;
  }

  .format-card {
    background: #fcfaff;
    border: 1px solid #ece7f7;
    border-radius: 24px;
    padding: 25px 32px;
    display: grid;
    grid-template-columns: 1fr 180px;
    gap: 5px;
    align-items: center;
    box-shadow: var(--shadow);
  }

  .format-card h3 {
    margin: 0 0 8px;
    font-size: 46px;
    line-height: 1;
    letter-spacing: -0.03em;
  }

  .format-card-subtitle {
    margin: 0 0 22px;
    font-size: 20px;
    font-weight: 700;
    line-height: 1.4;
  }

  .format-badge {
    display: inline-flex;
    align-items: center;
    justify-content: center;
    padding: 8px 16px;
    border-radius: 999px;
    background: #efe7ff;
    color: var(--primary);
    font-size: 14px;
    font-weight: 700;
    margin-left: 12px;
    vertical-align: middle;
  }

  .format-list {
    margin: 0;
    padding: 0;
    list-style: none;
    display: grid;
    gap: 18px;
  }

  .format-list li {
    display: flex;
    align-items: flex-start;
    gap: 14px;
    font-size: 18px;
    line-height: 1.45;
  }

  .format-check {
    color: #7a4ce6;
    font-weight: 800;
    font-size: 24px;
    line-height: 1;
    margin-top: 2px;
    flex: 0 0 auto;
  }

  .format-image-wrap {
    display: flex;
    align-items: center;
    justify-content: center;
  }

  .format-image-wrap img {
    width: 100%;
    max-width: 150px;
    height: auto;
    display: block;
    object-fit: contain;
  }

  .steps-section {
    padding: 20px 0 32px;
  }

  .steps-heading {
    margin: 0 0 22px;
    font-size: 46px;
    line-height: 1.05;
    letter-spacing: -0.03em;
  }

  .steps-cards {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 18px;
    margin-bottom: 20px;
  }

  .step-card {
    background: #ffffff;
    border: 1px solid #ece7f7;
    border-radius: 22px;
    padding: 26px 24px;
    box-shadow: var(--shadow);
    display: flex;
    gap: 18px;
    align-items: flex-start;
  }
  .step-content {
  display: flex;
  flex-direction: column;
  gap: 20px;
  }

  .step-number {
    flex: 0 0 auto;
    font-size: 54px;
    line-height: 1;
    font-weight: 800;
    color: #7a4ce6;
    letter-spacing: -0.04em;
  }

  .step-card h3 {
    margin: 4px 0 20px;
    font-size: 18px;
    line-height: 1.35;
  }

  .step-card p {
    margin: 0;
    color: var(--muted);
    font-size: 15px;
    line-height: 1.55;
  }

  .trust-panel {
    background: #f7f2ff;
    border: 1px solid #ece7f7;
    border-radius: 26px;
    padding: 30px 32px;
    box-shadow: var(--shadow);
    display: grid;
    align-items: center;
    gap: 20px;
  }

  .trust-panel-left {
    display: grid;
    grid-template-columns: 1.1fr 0.9fr;
    gap: 28px;
    align-items: center;
    width: 100%;
  }

  .trust-panel-right {
    display: grid;
    grid-template-columns: 1.2fr 0.8fr;
    gap: 20px;
    align-items: center;
  }

  .trust-panel h3 {
    margin: 0 0 18px;
    font-size: 26px;
    line-height: 1.2;
  }

  .trust-panel p {
    margin: 0 0 18px;
    color: var(--muted);
    font-size: 18px;
    line-height: 1.6;
  }

  .rating-row {
    display: flex;
    align-items: center;
    gap: 14px;
    margin-bottom: 28px;
    flex-wrap: wrap;
  }

  .rating-value {
    display: flex;
    align-items: baseline;
    gap: 8px;
    flex-wrap: wrap;
  }

  .rating-value strong {
    font-size: 36px;
    line-height: 1;
  }

  .rating-value span {
    color: var(--muted);
    font-size: 18px;
    line-height: 1.4;
  }

  .stars {
    color: #ffbf2f;
    font-size: 34px;
    line-height: 1;
    letter-spacing: 2px;
  }

  .trust-features {
    display: grid;
    grid-template-columns: repeat(3, 1fr);
    gap: 18px;
  }

  .trust-feature {
    display: flex;
    align-items: flex-start;
    gap: 12px;
  }

  .trust-feature-icon {
    width: 44px;
    height: 44px;
    border-radius: 14px;
    background: #efe7ff;
    color: #7a4ce6;
    display: grid;
    place-items: center;
    font-size: 20px;
    font-weight: 800;
    flex: 0 0 44px;
  }

  .trust-feature strong {
    display: block;
    font-size: 16px;
    line-height: 1.35;
    margin-bottom: 4px;
  }

  .trust-feature span {
    color: var(--muted);
    font-size: 14px;
    line-height: 1.45;
  }

  .trust-visual {
    display: flex;
    align-items: center;
    justify-content: center;
  }

  .trust-visual img {
    width: 100%;
    max-width: 240px;
    height: auto;
    display: block;
    object-fit: contain;
  }

  .shield-note {
    display: flex;
    align-items: center;
    gap: 14px;
    margin-top: 18px;
  }

  .shield-note-icon {
    width: 44px;
    height: 44px;
    border-radius: 14px;
    background: #efe7ff;
    color: #7a4ce6;
    display: grid;
    place-items: center;
    font-size: 20px;
    font-weight: 800;
    flex: 0 0 44px;
  }

  .shield-note span {
    font-size: 16px;
    line-height: 1.45;
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

  .final-cta {
    padding: 18px 0 40px;
  }

  .final-cta-card {
    background: linear-gradient(90deg, #5f3dc8 0%, #7a4ce6 55%, #8c66f0 100%);
    border-radius: 28px;
    padding: 28px 42px;
    color: #ffffff;
    display: grid;
    grid-template-columns: 0.7fr 1fr 1fr;
    align-items: center;
    gap: 15px;
    box-shadow: 0 18px 40px rgba(110, 64, 216, 0.22);
  }

  .final-cta-copy h2 {
    margin: 0 0 15px;
    font-size: 22px;
    line-height: 1.15;
    letter-spacing: -0.02em;
  }

  .final-cta-copy p {
    margin: 0;
    font-size: 14px;
    line-height: 1.5;
    color: rgba(255, 255, 255, 0.9);
  }

  .final-cta-actions {
    display: flex;
    align-items: center;
    gap: 14px;
    flex-wrap: nowrap;
  }

  .final-cta-actions .btn {
    min-width: 190px;
    border-radius: 16px;
  }

  .final-cta-actions .btn-primary {
    background: #ffffff;
    color: var(--primary);
    box-shadow: none;
  }

  .final-cta-actions .btn-primary:hover {
    background: #f7f3ff;
  }

  .final-cta-actions .btn-secondary {
    background: transparent;
    color: #ffffff;
    border: 2px solid rgba(255, 255, 255, 0.45);
  }

  .final-cta-actions .btn-secondary:hover {
    background: rgba(255, 255, 255, 0.08);
  }

  .final-cta-support {
    display: flex;
    align-items: center;
    gap: 10px;
    min-width: 320px;
  }

  .final-cta-support img {
    width: 150px;
    height: 150px;
    object-fit: contain;
    display: block;
    flex: 0 0 96px;
  }

  .final-cta-support strong {
    display: block;
    font-size: 17px;
    line-height: 1.2;
    margin-bottom: 4px;
  }

  .final-cta-support span {
    font-size: 14px;
    line-height: 1.45;
    color: rgba(255, 255, 255, 0.9);
  }
  .footer {
    padding: 36px 0 64px;
    color: var(--muted);
    font-size: 14px;
  }

  .footer-grid {
    display: flex;
    align-items: center;
    gap: 20px;
    flex-wrap: nowrap;
    border-top: 1px solid var(--border);
    padding-top: 24px;
  }

  .footer-brand {
    display: flex;
    align-items: center;
    flex: 0 0 auto;
    margin-right: 12px;
  }

  .footer-brand img {
    height: 42px;
    width: auto;
    display: block;
  }

  .footer-text {
    color: var(--text);
    font-size: 16px;
    line-height: 1.45;
  }
  .format-title-row {
    display: flex;
    align-items: center;
    gap: 14px;
    flex-wrap: wrap;
    margin-bottom: 25px;
  }

  .format-title-row h3 {
    margin: 0;
  }
  }
  @media (max-width: 1024px) {
    .hero-top,
    .feature-row,
    .split,
    .steps-cards,
    .trust-panels,
    .trust-features,
    .trust-panel-left,
    .trust-panel-right {
      grid-template-columns: 1fr;
    }

    .hero-side {
      min-height: 240px;
    }

    .format-image-wrap {
      justify-content: flex-start;
    }
    .final-cta-card {
      grid-template-columns: 1fr;
      align-items: flex-start;
    }

    .final-cta-support {
      min-width: 0;
    }
  }
  

  @media (max-width: 720px) {
    .format-title-row {
      gap: 10px;
    }
    .footer-grid {
      flex-wrap: wrap;
      align-items: flex-start;
    }

    .footer-text {
      font-size: 14px;
    }
    .final-cta-card {
      padding: 24px 20px;
      gap: 20px;
    }

    .final-cta-copy h2 {
      font-size: 26px;
    }

    .final-cta-actions {
      width: 100%;
      flex-wrap: wrap;
    }

    .final-cta-actions .btn {
      flex: 1 1 100%;
      min-width: 0;
    }

    .final-cta-support strong {
      font-size: 18px;
    }

    .final-cta-support img {
      width: 72px;
      height: 72px;
      flex-basis: 72px;
    }

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

    .format-top {
      flex-direction: column;
      align-items: stretch;
    }

    .format-pills {
      justify-content: flex-start;
    }

    .format-head h2 {
      font-size: 34px;
    }

    .format-grid {
      grid-template-columns: 1fr;
    }

    .format-card {
      grid-template-columns: 1fr;
      padding: 22px 22px 24px;
    }

    .format-card h3 {
      font-size: 38px;
    }

    .format-card-subtitle {
      font-size: 18px;
    }

    .format-list li {
      font-size: 17px;
    }

    .steps-heading {
      font-size: 34px;
    }

    .step-card {
      padding: 20px 18px;
    }

    .step-number {
      font-size: 42px;
    }

    .trust-panel {
      padding: 22px 20px;
    }

    .rating-value strong {
      font-size: 36px;
    }

    .stars {
      font-size: 28px;
    }

    .trust-visual img {
      max-width: 220px;
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
                <span><i class="dot"></i> Поддержка 24/7</span>
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
   
    <section class="format-section">
      <div class="container">
        <div class="format-top">
          <div class="format-head">
            <h2>Какой формат подходит вам?</h2>
            <p>Ответьте на 3 вопроса — подскажем, что выбрать</p>
          </div>

          <div class="format-pills">
            <div class="format-pill">Планируете работать один?</div>
            <div class="format-pill">Нужны партнёры?</div>
            <div class="format-pill">Продаёте товары с НДС?</div>
            <a href="{url_for('register_page')}" class="format-pill format-pill-outline">Пройти подсказчик</a>
          </div>
        </div>

        <div class="format-grid">
          <article class="format-card">
            <div>
              <div class="format-title-row">
                <h3>ИП</h3>
                <span class="format-badge">Проще и быстрее</span>
              </div>
              <ul class="format-list">
                <li><span class="format-check">✓</span><span>Проще отчётность и налоги</span></li>
                <li><span class="format-check">✓</span><span>Быстрая регистрация</span></li>
                <li><span class="format-check">✓</span><span>Подходит для большинства услуг и торговли</span></li>
              </ul>
            </div>

            <div class="format-image-wrap">
              <img src="{url_for('serve_src', filename='bag.png')}" alt="ИП" />
            </div>
          </article>

          <article class="format-card">
            <div>
               <div class="format-title-row">
                <h3>ООО</h3>
                <span class="format-badge">Больше возможностей</span>
              </div>

              <ul class="format-list">
                <li><span class="format-check">✓</span><span>Партнёры и инвесторы</span></li>
                <li><span class="format-check">✓</span><span>Больше возможностей для роста</span></li>
                <li><span class="format-check">✓</span><span>Доверие со стороны крупного бизнеса</span></li>
              </ul>
            </div>

            <div class="format-image-wrap">
              <img src="{url_for('serve_src', filename='building.png')}" alt="ООО" />
            </div>
          </article>
        </div>
      </div>
        <div class="section" id="choice">
          <div class="helper-box">
            <strong>Не уверены, что выбрать?</strong>
            ИП — если вы начинаете один и хотите быстро стартовать. ООО — если планируете партнеров, совместный бизнес или работу с компаниями.
          </div>
      </div>
    </section>
  
    <section class="steps-section">
      <div class="container">
        <h2 class="steps-heading">3 шага к регистрации бизнеса</h2>

        <div class="steps-cards">
          <article class="step-card">
            <div class="step-number">01</div>
            <div class="step-content">
              <h3>Заполните онлайн-заявку</h3>
              <p>Простая форма займёт 5-10 минут</p>
            </div>
          </article>

          <article class="step-card">
            <div class="step-number">02</div>
            <div>
              <h3>Мы подготовим документы</h3>
              <p>Сформируем и проверим пакет для ФНС</p>
            </div>
          </article>

          <article class="step-card">
            <div class="step-number">03</div>
            <div>
              <h3>Получите решение и откройте счёт</h3>
              <p>Мы отправим документы и откроем счёт</p>
            </div>
          </article>
        </div>

        <div class="trust-panels">
          <article class="trust-panel trust-panel-left">
            <div>
              <h3>Надёжный банк для бизнеса</h3>

              <div class="rating-row">
                <div class="rating-value">
                  <strong>4,9</strong>
                  <div class="stars">★ ★ ★ ★ ★</div>
                  <span>рейтинг на основе отзывов клиентов</span>
                </div>
              </div>

              <div class="trust-features">
                <div class="trust-feature">
                  <div class="trust-feature-icon"><i class="dot"></i></div>
                  <div>
                    <strong>ТОП-5 среди</strong>
                    <span>для малого бизнеса</span>
                  </div>
                </div>

                <div class="trust-feature">
                  <div class="trust-feature-icon"><i class="dot"></i></div>
                  <div>
                    <strong>Работаем в 46</strong>
                    <span>регионах России</span>
                  </div>
                </div>

                <div class="trust-feature">
                  <div class="trust-feature-icon"><i class="dot"></i></div>
                  <div>
                    <strong>Более 30 лет</strong>
                    <span>в банковском бизнесе</span>
                  </div>
                </div>
              </div>
            </div>

            <div class="trust-visual">
              <img src="{url_for('serve_src', filename='big_circle.png')}" alt="Надёжный банк для бизнеса" />
            </div>
          </article>
        </div>
      </div>
    </section>
    <section class="final-cta">
      <div class="container">
        <div class="final-cta-card">
          <div class="final-cta-copy">
            <h2>Готовы зарегистрировать бизнес?</h2>
            <p>Это бесплатно и займёт всего несколько минут</p>
          </div>

          <div class="final-cta-actions">
            <a class="btn btn-primary" href="{{ url_for('ip_form_page') }}">Оформить ИП</a>
            <a class="btn btn-secondary" href="{{ url_for('ooo_form_page') }}">Оформить ООО</a>
          </div>

          <div class="final-cta-support">
            <div>
              <strong>Поддержка бизнеса 24/7</strong>
              <span>Поможем на каждом шаге</span>
            </div>
            <img src="{url_for('serve_src', filename='naushniki.png')}" alt="Поддержка 24/7" />
          </div>
        </div>
      </div>
    </section>
  </main>
  
  <footer class="footer">
    <div class="container footer-grid">
      <a class="footer-brand" href="{ url_for('landing') }" aria-label="Уралсиб">
        <img src="{url_for('serve_src', filename='logo2.png') }" alt="Уралсиб" />
      </a>
      <div class="footer-text">
        MVP-лендинг для хакатона: редизайн старта воронки онлайн-регистрации бизнеса.<br>
        © 2026. Концепт для презентации решения.
      </div>
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
