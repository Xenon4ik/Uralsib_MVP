from flask import render_template_string, url_for

from styles import BASE_STYLES
from pages.common import render_header, render_footer


def landing_page():
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
              <h1>
                Бесплатная регистрация
                <span class="hero-title-accent">бизнеса в Уралсибе</span>
              </h1>
              <p class="lead">
                Подготовим и отправим все документы в ФНС онлайн.
                Откройте счёт и начните работать — без визита в налоговую.
              </p>

              <div class="hero-actions">
                <a class="btn btn-primary" href="{url_for('ip_form_page')}">Оформить ИП</a>
                <a class="btn btn-secondary" href="{url_for('ooo_form_page')}">Оформить ООО</a>
              </div>

              <div class="hero-benefits">
                <span><i class="dot"></i>Без оплаты госпошлины</span>
                <span><i class="dot"></i>Поддержка 24/7</span>
                <span><i class="dot"></i>Готово от 1 дня</span>
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

        <div class="helper-box">
          <strong>Не уверены, что выбрать?</strong>
          ИП — если вы начинаете один и хотите быстро стартовать.
          ООО — если планируете партнёров, совместный бизнес или работу с компаниями.
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
              <p>Простая форма займёт 5–10 минут</p>
            </div>
          </article>

          <article class="step-card">
            <div class="step-number">02</div>
            <div class="step-content">
              <h3>Мы подготовим документы</h3>
              <p>Сформируем и проверим пакет для ФНС</p>
            </div>
          </article>

          <article class="step-card">
            <div class="step-number">03</div>
            <div class="step-content">
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
            <a class="btn btn-primary" href="{url_for('ip_form_page')}">Оформить ИП</a>
            <a class="btn btn-secondary" href="{url_for('ooo_form_page')}">Оформить ООО</a>
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

  {render_footer()}
</body>
</html>
        """
    )