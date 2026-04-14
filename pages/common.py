from flask import url_for

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

def render_footer() -> str:
    return f"""
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
    """