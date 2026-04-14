from flask import url_for


def get_ooo_step1_content() -> str:
    return f"""
    <section class="ooo-step-layout">
      <div class="ooo-step-main">
        <div class="ooo-card">
          <h2 class="ooo-card-title">Введите наименование компании</h2>

          <div class="ooo-form-grid">
            <div class="ooo-field ooo-field-full">
              <label class="ooo-label">
                Сокращённое наименование <span class="ooo-required">(обязательно)</span>
                <span class="ooo-help">?</span>
              </label>
              <input
                class="ooo-input"
                type="text"
                placeholder="Например: ООО «Альфа»"
              />
              <div class="ooo-field-note">
                Будет использоваться в документах и договорах.
              </div>
            </div>

            <div class="ooo-field ooo-field-full">
              <div class="ooo-label-row">
                <label class="ooo-label">
                  Полное наименование <span class="ooo-required">(обязательно)</span>
                  <span class="ooo-help">?</span>
                </label>
                <div class="ooo-counter">0 / 200</div>
              </div>

              <input
                class="ooo-input"
                type="text"
                placeholder="Например: Общество с ограниченной ответственностью «Альфа»"
              />
              <div class="ooo-field-note">
                Должно содержать организационно-правовую форму и полное наименование.
              </div>
            </div>
          </div>

          <div class="ooo-helper">
            <div class="ooo-helper-icon">i</div>
            <div>
              <div class="ooo-helper-title">Проверим название автоматически</div>
              <div class="ooo-helper-text">
                Мы проверим, соответствует ли наименование требованиям ФНС и свободно ли оно.
                Если будут проблемы — подскажем, как исправить.
              </div>
            </div>
          </div>

          <div class="ooo-section-subtitle">Особенности пакета документов</div>

          <div class="ooo-form-grid">
            <div class="ooo-field ooo-field-full">
              <input
                class="ooo-input"
                type="email"
                placeholder="E-mail для внесения в ЕГРЮЛ"
              />
            </div>
          </div>

          <label class="ooo-checkbox">
            <input type="checkbox" />
            <div class="ooo-checkbox-text">
              <strong>Получить документы из ФНС на бумажном носителе</strong>
              <span>
                Если данное поле не будет отмечено, то ФНС вышлет документы только на электронную почту
              </span>
            </div>
          </label>

          <div class="ooo-actions">
            <a href="{url_for('landing')}" class="btn btn-secondary ooo-save-btn">
              💾&nbsp;&nbsp;Сохранить и выйти
            </a>

            <div class="ooo-actions-right">
              <a href="{url_for('landing')}" class="btn btn-secondary ooo-back-btn">Назад</a>
              <a href="{url_for('ooo_form_step_2')}" class="btn btn-primary ooo-next-btn">Далее</a>
            </div>
          </div>
        </div>
      </div>

      <aside class="ooo-step-aside">
        <div class="ooo-aside-card">
          <div class="ooo-aside-icon">💡</div>
          <h3>Как придумать название</h3>

          <div class="ooo-aside-list">
            <div class="ooo-aside-item">
              <div class="ooo-aside-check">✓</div>
              <div>
                <strong>Коротко и понятно</strong>
                <span>Лучше всего работают простые названия из 1–3 слов.</span>
              </div>
            </div>

            <div class="ooo-aside-item">
              <div class="ooo-aside-check">✓</div>
              <div>
                <strong>Без лишних слов</strong>
                <span>Избегайте сложных формулировок и аббревиатур, которые трудно запомнить.</span>
              </div>
            </div>

            <div class="ooo-aside-item">
              <div class="ooo-aside-check">✓</div>
              <div>
                <strong>Уникальность важна</strong>
                <span>Название не должно совпадать с другими компаниями. Мы проверим это за вас.</span>
              </div>
            </div>

            <div class="ooo-aside-item">
              <div class="ooo-aside-check">✓</div>
              <div>
                <strong>Соответствие требованиям</strong>
                <span>
                  В полном наименовании обязательно должна быть указана организационно-правовая форма
                  «Общество с ограниченной ответственностью».
                </span>
              </div>
            </div>
          </div>
        </div>

        <div class="ooo-example-card">
          <div class="ooo-example-head">
            <span class="ooo-example-icon">i</span>
            <strong>Примеры удачных названий</strong>
          </div>
          <div class="ooo-example-links">
            <a href="#">ООО «ТехноПрофи»</a>
            <a href="#">ООО «Новые решения»</a>
          </div>
          <span class="ooo-example-arrow">›</span>
        </div>

        <a href="#" class="ooo-more-link">
          <span class="ooo-more-icon">i</span>
          <span>Подробнее о требованиях к наименованию</span>
          <span class="ooo-more-arrow">›</span>
        </a>
      </aside>
    </section>

    <style>
      .ooo-step-layout {{
        display: grid;
        grid-template-columns: minmax(0, 1fr) 370px;
        gap: 28px;
        align-items: start;
      }}

      .ooo-card {{
        background: #ffffff;
        border: 1px solid var(--border);
        border-radius: 28px;
        padding: 28px 28px 24px;
        box-shadow: var(--shadow);
      }}

      .ooo-card-title {{
        margin: 0 0 22px;
        font-size: 22px;
        line-height: 1.25;
      }}

      .ooo-form-grid {{
        display: grid;
        gap: 18px;
      }}

      .ooo-field {{
        display: grid;
        gap: 10px;
      }}

      .ooo-field-full {{
        width: 100%;
      }}

      .ooo-label-row {{
        display: flex;
        justify-content: space-between;
        align-items: center;
        gap: 14px;
      }}

      .ooo-label {{
        display: flex;
        align-items: center;
        gap: 6px;
        font-size: 16px;
        font-weight: 600;
        color: var(--text);
      }}

      .ooo-required {{
        color: #8b88a3;
        font-weight: 500;
      }}

      .ooo-help {{
        width: 18px;
        height: 18px;
        border-radius: 999px;
        border: 1.5px solid #a8a4bf;
        color: #8b88a3;
        display: inline-grid;
        place-items: center;
        font-size: 11px;
        font-weight: 700;
      }}

      .ooo-counter {{
        color: #8b88a3;
        font-size: 14px;
        font-weight: 600;
      }}

      .ooo-input {{
        width: 100%;
        height: 58px;
        border-radius: 16px;
        border: 2px solid #d8d6e5;
        background: #fff;
        padding: 0 18px;
        font-size: 16px;
        color: var(--text);
        outline: none;
      }}

      .ooo-input::placeholder {{
        color: #9a98ab;
      }}

      .ooo-input:focus {{
        border-color: var(--primary);
      }}

      .ooo-field-note {{
        color: #8b88a3;
        font-size: 14px;
        line-height: 1.5;
      }}

      .ooo-helper {{
        margin-top: 18px;
        display: grid;
        grid-template-columns: 34px 1fr;
        gap: 14px;
        align-items: start;
        background: #eef4ff;
        border: 1px solid #d9e5ff;
        border-radius: 18px;
        padding: 18px 20px;
      }}

      .ooo-helper-icon {{
        width: 34px;
        height: 34px;
        border-radius: 999px;
        border: 2px solid #7da2e8;
        color: #5b82cf;
        display: grid;
        place-items: center;
        font-weight: 700;
        font-size: 18px;
      }}

      .ooo-helper-title {{
        font-size: 18px;
        font-weight: 700;
        color: #315ea9;
        margin-bottom: 6px;
      }}

      .ooo-helper-text {{
        color: #5a6f9c;
        line-height: 1.55;
        font-size: 15px;
      }}

      .ooo-section-subtitle {{
        margin: 28px 0 16px;
        font-size: 20px;
        font-weight: 700;
        color: var(--text);
      }}

      .ooo-checkbox {{
        display: flex;
        align-items: flex-start;
        gap: 12px;
        margin-top: 18px;
      }}

      .ooo-checkbox input {{
        margin-top: 4px;
        width: 18px;
        height: 18px;
      }}

      .ooo-checkbox-text strong {{
        display: block;
        font-size: 16px;
        color: var(--text);
        margin-bottom: 4px;
      }}

      .ooo-checkbox-text span {{
        color: var(--muted);
        font-size: 14px;
        line-height: 1.5;
      }}

      .ooo-actions {{
        margin-top: 28px;
        display: flex;
        justify-content: space-between;
        gap: 18px;
        align-items: center;
        flex-wrap: wrap;
      }}

      .ooo-actions-right {{
        display: flex;
        gap: 12px;
        align-items: center;
        flex-wrap: wrap;
      }}

      .ooo-save-btn {{
        min-width: 190px;
      }}

      .ooo-back-btn {{
        min-width: 120px;
      }}

      .ooo-next-btn {{
        min-width: 120px;
      }}

      .ooo-step-aside {{
        display: grid;
        gap: 16px;
        position: sticky;
        top: 100px;
      }}

      .ooo-aside-card,
      .ooo-example-card {{
        background: #f7f2ff;
        border: 1px solid #ece7f7;
        border-radius: 24px;
      }}

      .ooo-aside-card {{
        padding: 22px;
      }}

      .ooo-aside-icon {{
        width: 52px;
        height: 52px;
        border-radius: 999px;
        background: #efe7ff;
        display: grid;
        place-items: center;
        color: var(--primary);
        font-size: 24px;
        margin-bottom: 16px;
      }}

      .ooo-aside-card h3 {{
        margin: 0 0 18px;
        font-size: 18px;
        line-height: 1.3;
      }}

      .ooo-aside-list {{
        display: grid;
        gap: 16px;
      }}

      .ooo-aside-item {{
        display: grid;
        grid-template-columns: 22px 1fr;
        gap: 12px;
        align-items: start;
      }}

      .ooo-aside-check {{
        width: 22px;
        height: 22px;
        border-radius: 999px;
        background: #efe7ff;
        color: var(--primary);
        display: grid;
        place-items: center;
        font-size: 13px;
        font-weight: 700;
        margin-top: 2px;
      }}

      .ooo-aside-item strong {{
        display: block;
        margin-bottom: 4px;
        font-size: 16px;
        line-height: 1.35;
        color: var(--text);
      }}

      .ooo-aside-item span {{
        color: var(--muted);
        font-size: 14px;
        line-height: 1.55;
      }}

      .ooo-example-card {{
        position: relative;
        padding: 18px 20px;
      }}

      .ooo-example-head {{
        display: flex;
        align-items: center;
        gap: 10px;
        margin-bottom: 12px;
      }}

      .ooo-example-icon {{
        width: 24px;
        height: 24px;
        border-radius: 999px;
        border: 1.5px solid var(--primary);
        display: inline-grid;
        place-items: center;
        color: var(--primary);
        font-size: 12px;
        font-weight: 700;
      }}

      .ooo-example-head strong {{
        color: var(--primary);
        font-size: 16px;
      }}

      .ooo-example-links {{
        display: grid;
        gap: 8px;
      }}

      .ooo-example-links a {{
        color: #476ab3;
        font-size: 15px;
        line-height: 1.45;
      }}

      .ooo-example-arrow {{
        position: absolute;
        right: 18px;
        top: 50%;
        transform: translateY(-50%);
        color: var(--primary);
        font-size: 28px;
      }}

      .ooo-more-link {{
        display: flex;
        align-items: center;
        gap: 12px;
        border: 1px solid #d8cef4;
        border-radius: 18px;
        background: #fff;
        color: var(--primary);
        padding: 16px 18px;
        font-weight: 600;
      }}

      .ooo-more-icon {{
        width: 24px;
        height: 24px;
        border-radius: 999px;
        border: 1.5px solid var(--primary);
        display: inline-grid;
        place-items: center;
        font-size: 12px;
        font-weight: 700;
        flex: 0 0 24px;
      }}

      .ooo-more-arrow {{
        margin-left: auto;
        font-size: 24px;
      }}

      @media (max-width: 1180px) {{
        .ooo-step-layout {{
          grid-template-columns: 1fr;
        }}

        .ooo-step-aside {{
          position: static;
        }}
      }}

      @media (max-width: 720px) {{
        .ooo-card {{
          padding: 22px 18px;
        }}

        .ooo-label-row,
        .ooo-actions,
        .ooo-actions-right {{
          flex-direction: column;
          align-items: stretch;
        }}

        .ooo-save-btn,
        .ooo-back-btn,
        .ooo-next-btn {{
          width: 100%;
          min-width: 0;
        }}
      }}
    </style>
    """