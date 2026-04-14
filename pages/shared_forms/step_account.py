from flask import url_for


def get_account_content(flow: str = "ip") -> str:
    if flow == "ooo":
        back_url = url_for("ooo_form_step_5")
        submit_url = url_for("landing")
        title = "Заявка на открытие расчётного счёта"
        subtitle = "Заполните контактные данные — с вами свяжется менеджер банка"
    else:
        back_url = url_for("ip_form_step_3")
        submit_url = url_for("landing")
        title = "Заявка на открытие расчётного счёта"
        subtitle = "Заполните контактные данные — с вами свяжется менеджер банка"

    return f"""
    <section class="account-layout">
      <div class="account-main">
        <div class="account-card">
          <h2 class="account-title">{title}</h2>
          <p class="account-subtitle">{subtitle}</p>

          <div class="account-form-grid">
            <div class="account-field account-field-full">
              <label class="account-label">ФИО</label>
              <div class="account-input-icon-wrap">
                <span class="account-input-icon">👤</span>
                <input class="account-input" type="text" value="Иванов Иван Иванович" />
              </div>
            </div>

            <div class="account-row">
              <div class="account-field">
                <label class="account-label">Регион</label>
                <div class="account-select-wrap">
                  <span class="account-input-icon">📍</span>
                  <select class="account-input account-select">
                    <option>Москва</option>
                    <option>Санкт-Петербург</option>
                    <option>Казань</option>
                  </select>
                  <span class="account-select-arrow">⌄</span>
                </div>
              </div>

              <div class="account-field">
                <label class="account-label">Город</label>
                <div class="account-select-wrap">
                  <span class="account-input-icon">🏢</span>
                  <select class="account-input account-select">
                    <option>Москва</option>
                    <option>Зеленоград</option>
                    <option>Химки</option>
                  </select>
                  <span class="account-select-arrow">⌄</span>
                </div>
              </div>
            </div>

            <div class="account-field account-field-full">
              <label class="account-label">Отделение банка (необязательно)</label>
              <div class="account-select-wrap">
                <span class="account-input-icon">🏦</span>
                <select class="account-input account-select">
                  <option>Любое удобное отделение</option>
                  <option>Москва, ул. Тверская</option>
                  <option>Москва, Ленинградский проспект</option>
                </select>
                <span class="account-select-arrow">⌄</span>
              </div>
            </div>

            <div class="account-row">
              <div class="account-field">
                <label class="account-label">Телефон</label>
                <div class="account-input-icon-wrap">
                  <span class="account-input-icon">📞</span>
                  <input class="account-input" type="text" value="+7 (999) 123-45-67" />
                </div>
              </div>

              <div class="account-field">
                <label class="account-label">E-mail</label>
                <div class="account-input-icon-wrap">
                  <span class="account-input-icon">✉️</span>
                  <input class="account-input" type="email" value="ivanov@example.ru" />
                </div>
              </div>
            </div>
          </div>

          <div class="account-benefit">
            <div class="account-benefit-icon">🎁</div>
            <div>
              <div class="account-benefit-title">Бесплатное открытие счёта</div>
              <div class="account-benefit-text">Без посещения банка. Всё онлайн.</div>
            </div>
          </div>

          <div class="account-actions">
            <a href="{url_for('landing')}" class="btn btn-secondary account-btn-save">💾&nbsp;&nbsp;Сохранить и выйти</a>

            <div class="account-actions-right">
                <a href="{back_url}" class="btn btn-secondary account-btn-back">Назад</a>
                <a href="{submit_url}" class="btn btn-primary account-btn-next">Сформировать пакет документов</a>
            </div>
         </div>
        <div class="account-protection-note">
          🔒 Ваши данные защищены и используются только для подготовки документов в ФНС
        </div>
      </div>

      <aside class="account-aside">
        <div class="account-aside-card">
          <h3>Что дальше?</h3>

          <div class="account-aside-list">
            <div class="account-aside-item">
              <div class="account-aside-icon">📄</div>
              <div>
                <strong>Мы проверим данные</strong>
                <span>Проверим заполненную информацию и подготовим документы</span>
              </div>
            </div>

            <div class="account-aside-item">
              <div class="account-aside-icon">☁️</div>
              <div>
                <strong>Отправим документы в ФНС</strong>
                <span>Отправим документы в налоговую в электронном виде</span>
              </div>
            </div>

            <div class="account-aside-item">
              <div class="account-aside-icon">✅</div>
              <div>
                <strong>Получите подтверждение</strong>
                <span>Вы получите уведомление о регистрации на e-mail</span>
              </div>
            </div>

            <div class="account-aside-item">
              <div class="account-aside-icon">💳</div>
              <div>
                <strong>Откроем счёт</strong>
                <span>Поможем выбрать тариф и откроем расчётный счёт</span>
              </div>
            </div>
          </div>

          <div class="account-aside-success">
            <div class="account-aside-success-icon">🛡</div>
            <div>
              <strong>Без визита в налоговую</strong>
              <span>Oнлайн, быстро и безопасно</span>
            </div>
          </div>
        </div>
      </aside>
    </section>

    <style>
      .account-layout {{
        display: grid;
        grid-template-columns: minmax(0, 1fr) 360px;
        gap: 24px;
        align-items: start;
      }}

      .account-card {{
        background: #ffffff;
        border: 1px solid var(--border);
        border-radius: 28px;
        padding: 28px 28px 24px;
        box-shadow: var(--shadow);
      }}

      .account-title {{
        margin: 0 0 10px;
        font-size: 22px;
        line-height: 1.25;
      }}

      .account-subtitle {{
        margin: 0 0 18px;
        color: var(--muted);
        font-size: 16px;
        line-height: 1.6;
      }}

      .account-form-grid {{
        display: grid;
        gap: 18px;
      }}

      .account-row {{
        display: grid;
        grid-template-columns: minmax(0, 1fr) minmax(0, 1fr);
        gap: 18px;
      }}

      .account-field {{
        display: grid;
        gap: 10px;
      }}

      .account-field-full {{
        width: 100%;
      }}

      .account-label {{
        font-size: 14px;
        font-weight: 600;
        color: #7a7693;
      }}

      .account-input,
      .account-select {{
        width: 100%;
        height: 58px;
        border-radius: 16px;
        border: 2px solid #d8d6e5;
        background: #fff;
        padding: 0 18px 0 46px;
        font-size: 16px;
        color: var(--text);
        outline: none;
      }}

      .account-input:focus,
      .account-select:focus {{
        border-color: var(--primary);
      }}

      .account-input-icon-wrap,
      .account-select-wrap {{
        position: relative;
      }}

      .account-input-icon {{
        position: absolute;
        left: 14px;
        top: 50%;
        transform: translateY(-50%);
        color: #8f8ca5;
        font-size: 18px;
        pointer-events: none;
      }}

      .account-select {{
        appearance: none;
        -webkit-appearance: none;
        -moz-appearance: none;
        padding-right: 48px;
      }}

      .account-select-arrow {{
        position: absolute;
        right: 16px;
        top: 50%;
        transform: translateY(-50%);
        color: #8f8ca5;
        font-size: 22px;
        pointer-events: none;
      }}

      .account-benefit {{
        margin-top: 20px;
        display: grid;
        grid-template-columns: 48px 1fr;
        gap: 14px;
        align-items: center;
        background: #f5f0ff;
        border: 1px solid #e7dcff;
        border-radius: 18px;
        padding: 16px 18px;
      }}

      .account-benefit-icon {{
        width: 48px;
        height: 48px;
        border-radius: 16px;
        background: #efe7ff;
        display: grid;
        place-items: center;
        font-size: 22px;
        color: var(--primary);
      }}

      .account-benefit-title {{
        font-size: 18px;
        font-weight: 700;
        color: var(--primary);
        margin-bottom: 4px;
      }}

      .account-benefit-text {{
        color: var(--muted);
        font-size: 15px;
        line-height: 1.5;
      }}

      .account-actions {{
        margin-top: 26px;
        display: flex;
        justify-content: space-between;
        gap: 14px;
        flex-wrap: wrap;
      }}

      .account-btn-back {{
        min-width: 140px;
      }}

      .account-btn-next {{
        min-width: 290px;
      }}

      .account-protection-note {{
        margin-top: 14px;
        color: #8a889d;
        font-size: 14px;
        line-height: 1.5;
        text-align: center;
      }}

      .account-aside {{
        position: sticky;
        top: 100px;
      }}

      .account-aside-card {{
        background: #f7f2ff;
        border: 1px solid #ece7f7;
        border-radius: 24px;
        padding: 24px;
      }}

      .account-aside-card h3 {{
        margin: 0 0 18px;
        font-size: 18px;
        line-height: 1.3;
      }}

      .account-aside-list {{
        display: grid;
        gap: 18px;
      }}

      .account-aside-item {{
        display: grid;
        grid-template-columns: 48px 1fr;
        gap: 14px;
        align-items: start;
      }}

      .account-aside-icon {{
        width: 48px;
        height: 48px;
        border-radius: 999px;
        background: #efe7ff;
        display: grid;
        place-items: center;
        color: var(--primary);
        font-size: 20px;
      }}

      .account-aside-item strong {{
        display: block;
        margin-bottom: 4px;
        font-size: 16px;
        line-height: 1.35;
        color: var(--text);
      }}

      .account-aside-item span {{
        color: var(--muted);
        font-size: 14px;
        line-height: 1.55;
      }}

      .account-aside-success {{
        margin-top: 22px;
        display: grid;
        grid-template-columns: 44px 1fr;
        gap: 12px;
        align-items: start;
        background: #eef8ef;
        border: 1px solid #d8ead9;
        border-radius: 18px;
        padding: 16px 18px;
      }}

      .account-aside-success-icon {{
        width: 44px;
        height: 44px;
        border-radius: 999px;
        background: #dff0e1;
        display: grid;
        place-items: center;
        color: #4f9b61;
        font-size: 20px;
      }}

      .account-aside-success strong {{
        display: block;
        margin-bottom: 4px;
        font-size: 16px;
        line-height: 1.35;
        color: #4b8f5c;
      }}

      .account-aside-success span {{
        color: #6a9072;
        font-size: 14px;
        line-height: 1.5;
      }}

      @media (max-width: 1180px) {{
        .account-layout {{
          grid-template-columns: 1fr;
        }}

        .account-aside {{
          position: static;
        }}
      }}

      @media (max-width: 720px) {{
        .account-card {{
          padding: 22px 18px;
        }}

        .account-row {{
          grid-template-columns: 1fr;
        }}

        .account-actions {{
          flex-direction: column;
        }}

        .account-btn-back,
        .account-btn-next {{
          width: 100%;
          min-width: 0;
        }}
      }}
    </style>
    """