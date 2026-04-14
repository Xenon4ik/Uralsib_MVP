from flask import render_template_string, url_for

from styles import BASE_STYLES
from pages.common import render_header, render_footer


def login_page_view():
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
      <p>
        Здесь будет отдельный сценарий для пользователей, которые уже начали
        регистрацию и хотят вернуться к заявке.
      </p>

      <div style="margin-top: 22px; display:flex; gap:12px; flex-wrap:wrap;">
        <a href="{url_for('landing')}" class="btn btn-secondary">Назад на лендинг</a>
        <a href="{url_for('register_page')}" class="btn btn-primary">Новая регистрация</a>
      </div>
    </section>
  </main>

  {render_footer()}
</body>
</html>
        """
    )


def register_page_view():
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
      <p>
        Здесь будет отдельный сценарий старта новой регистрации:
        выбор ИП или ООО, короткая подсказка и переход в форму.
      </p>

      <div style="margin-top: 22px; display:flex; gap:12px; flex-wrap:wrap;">
        <a href="{url_for('landing')}" class="btn btn-secondary">Назад на лендинг</a>
        <a href="{url_for('ip_form_page')}" class="btn btn-primary">Оформить ИП</a>
        <a href="{url_for('ooo_form_page')}" class="btn btn-ghost">Оформить ООО</a>
      </div>
    </section>
  </main>

  {render_footer()}
</body>
</html>
        """
    )