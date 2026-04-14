from flask import render_template_string, url_for

from styles import BASE_STYLES


def render_form_header() -> str:
    return f"""
    <header class="header">
      <div class="container header-inner">
        <a class="brand" href="{url_for('landing')}" aria-label="Уралсиб">
          <img src="{url_for('serve_src', filename='logo.png')}" alt="Уралсиб" />
        </a>

        <nav class="form-nav" aria-label="Навигация">
          <a href="{url_for('landing')}#packages">Пакеты</a>
          <a href="{url_for('ip_form_page')}">Оформление ИП</a>
          <a href="{url_for('ooo_form_page')}">Оформление ООО</a>
        </nav>

        <div class="header-actions">
          <a href="{url_for('login_page')}" class="btn btn-primary">Личный кабинет</a>
        </div>
      </div>
    </header>
    """


def render_form_footer() -> str:
    return f"""
    <footer class="footer">
      <div class="container footer-grid">
        <a class="footer-brand" href="{url_for('landing')}" aria-label="Уралсиб">
          <img src="{url_for('serve_src', filename='logo2.png')}" alt="Уралсиб" />
        </a>
        <div class="footer-text">
          MVP-лендинг для хакатона: редизайн старта воронки онлайн-регистрации бизнеса.<br>
          © 2026. Концепт для презентации решения.
        </div>
      </div>
    </footer>
    """


def render_form_page(
    title: str,
    subtitle: str,
    progress_html: str,
    content_html: str,
    page_title: str | None = None,
) -> str:
    page_title = page_title or title

    return render_template_string(
        f"""
<!DOCTYPE html>
<html lang="ru">
<head>
  <meta charset="UTF-8" />
  <meta name="viewport" content="width=device-width, initial-scale=1.0" />
  <title>{page_title}</title>
  {BASE_STYLES}
  <style>
    .form-nav {{
      display: flex;
      align-items: center;
      gap: 28px;
      font-size: 15px;
      color: var(--text);
    }}

    .form-nav a {{
      color: var(--text);
      opacity: 0.9;
    }}

    .form-page {{
      padding: 28px 0 48px;
      background: linear-gradient(180deg, #faf8ff 0%, #f6f4fb 100%);
      min-height: calc(100vh - 140px);
    }}

    .form-shell {{
      display: grid;
      gap: 28px;
    }}

    @media (max-width: 1024px) {{
      .form-nav {{
        display: none;
      }}
    }}
  </style>
</head>
<body>
  {render_form_header()}

  <main class="form-page">
    <div class="container">
      <div class="form-shell">
        {progress_html}
        {content_html}
      </div>
    </div>
  </main>

  {render_form_footer()}
</body>
</html>
        """
    )