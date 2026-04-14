from flask import url_for


def get_ooo_step2_content() -> str:
    return f"""
    <section class="founders-layout">
      <div class="founders-main">
        <div class="founders-card">
          <h2 class="founders-title">Количество учредителей</h2>
          <p class="founders-subtitle">Сколько человек или компаний будут учредителями ООО?</p>

          <div class="founders-switch">
            <button type="button" class="founders-switch-btn active">◉&nbsp;&nbsp;Один учредитель</button>
            <button type="button" class="founders-switch-btn">○&nbsp;&nbsp;Несколько учредителей</button>
          </div>

          <div class="founders-divider"></div>

          <div class="founders-content-grid">
            <div class="founders-left">
              <h3 class="founders-section-title">Данные учредителя</h3>

              <div class="founders-form-grid">
                <div class="founders-field founders-field-full">
                  <label class="founders-label">Гражданство</label>
                  <div class="founders-select-wrap">
                    <select class="founders-input founders-select">
                      <option>Гражданин РФ</option>
                      <option>Иностранный гражданин</option>
                    </select>
                    <span class="founders-select-arrow">⌄</span>
                  </div>
                </div>

                <div class="founders-row">
                  <div class="founders-field">
                    <input class="founders-input" type="text" placeholder="ИНН" />
                  </div>
                  <div class="founders-field">
                    <input class="founders-input" type="text" placeholder="СНИЛС" />
                  </div>
                </div>

                <h3 class="founders-section-title founders-section-title--inner">Паспортные данные</h3>

                <div class="founders-row founders-row-3">
                  <div class="founders-field">
                    <input class="founders-input" type="text" placeholder="Серия паспорта" />
                  </div>
                  <div class="founders-field">
                    <input class="founders-input" type="text" placeholder="Номер паспорта" />
                  </div>
                  <div class="founders-field">
                    <div class="founders-input-icon-wrap">
                      <input class="founders-input" type="text" placeholder="Дата выдачи ДД.ММ.ГГГГ" />
                      <span class="founders-input-icon">🗓</span>
                    </div>
                  </div>
                </div>

                <div class="founders-row">
                  <div class="founders-field">
                    <input class="founders-input" type="text" placeholder="Кем выдан (как в паспорте)" />
                  </div>
                  <div class="founders-field">
                    <input class="founders-input" type="text" placeholder="Код подразделения" />
                  </div>
                </div>

                <div class="founders-field founders-field-full">
                  <input class="founders-input" type="text" placeholder="Место рождения (как в паспорте)" />
                </div>

                <h3 class="founders-section-title founders-section-title--inner">Адрес регистрации учредителя в РФ</h3>

                <div class="founders-helper">
                  <div class="founders-helper-icon">i</div>
                  <div class="founders-helper-text">
                    Введите или вставьте адрес, после чего выберите подходящий вариант из выпадающего списка.
                    Адрес должен указываться в точном соответствии с ГАР (ФИАС).
                  </div>
                </div>

                <div class="founders-field founders-field-full">
                  <input class="founders-input" type="text" placeholder="Адрес регистрации учредителя в РФ" />
                </div>
              </div>
            </div>

            <div class="founders-right">
              <h3 class="founders-section-title">Контактная информация</h3>

              <div class="founders-helper founders-helper--blue">
                <div class="founders-helper-icon">i</div>
                <div>
                  <div class="founders-helper-title">Важно.</div>
                  <div class="founders-helper-text">
                    Укажите корректные номер телефона и email. Телефон должен принадлежать человеку,
                    на которого оформляется бизнес — он нужен для выпуска КЭП в myDSS.
                    Email используется для отправки уведомлений сервиса.
                  </div>
                </div>
              </div>

              <div class="founders-form-grid" style="margin-top:18px;">
                <div class="founders-field founders-field-full">
                  <input class="founders-input" type="email" placeholder="E-mail" />
                </div>

                <div class="founders-field founders-field-full">
                  <input class="founders-input" type="text" placeholder="Телефон +7 (___) ___-__-__" />
                </div>
              </div>
            </div>
          </div>

          <div class="founders-actions">
            <a href="{url_for('landing')}" class="btn btn-secondary founders-save-btn">💾&nbsp;&nbsp;Сохранить и выйти</a>

            <div class="founders-actions-right">
              <a href="{url_for('ooo_form_page')}" class="btn btn-secondary founders-back-btn">Назад</a>
              <a href="{url_for('ooo_form_step_3')}" class="btn btn-primary founders-next-btn">Далее</a>
            </div>
          </div>
        </div>
      </div>

      <aside class="founders-aside">
        <div class="founders-aside-card">
          <div class="founders-aside-icon">👤</div>
          <h3>Кто может быть учредителем?</h3>

          <div class="founders-aside-list">
            <div class="founders-aside-item">
              <div class="founders-aside-check">✓</div>
              <div>
                <strong>Физическое лицо</strong>
                <span>Гражданин РФ или иностранный гражданин.</span>
              </div>
            </div>

            <div class="founders-aside-item">
              <div class="founders-aside-check">✓</div>
              <div>
                <strong>Юридическое лицо</strong>
                <span>Российская или иностранная компания.</span>
              </div>
            </div>

            <div class="founders-aside-item">
              <div class="founders-aside-check">✓</div>
              <div>
                <strong>Несколько учредителей</strong>
                <span>ООО может иметь от одного до 50 учредителей.</span>
              </div>
            </div>
          </div>

          <div class="founders-aside-divider"></div>

          <div class="founders-aside-important">
            <div class="founders-aside-important-icon">💡</div>
            <div>
              <strong>Важно</strong>
              <span>Доля в уставном капитале указывается на следующем шаге.</span>
            </div>
          </div>

          <a href="#" class="founders-aside-link">
            <span>Подробнее о ролях и правах учредителей</span>
            <span class="founders-aside-link-arrow">›</span>
          </a>
        </div>
      </aside>
    </section>

    <style>
      .founders-layout {{
        display: grid;
        grid-template-columns: minmax(0, 1fr) 360px;
        gap: 22px;
        align-items: start;
      }}

      .founders-card {{
        background: #ffffff;
        border: 1px solid var(--border);
        border-radius: 28px;
        padding: 24px 24px 20px;
        box-shadow: var(--shadow);
      }}

      .founders-title {{
        margin: 0 0 6px;
        font-size: 22px;
        line-height: 1.25;
      }}

      .founders-subtitle {{
        margin: 0 0 16px;
        color: var(--muted);
        font-size: 15px;
        line-height: 1.55;
      }}

      .founders-switch {{
        display: flex;
        gap: 14px;
        flex-wrap: wrap;
      }}

      .founders-switch-btn {{
        min-height: 42px;
        padding: 0 18px;
        border-radius: 12px;
        border: 2px solid #d8d6e5;
        background: #fff;
        color: #6f6b86;
        font-size: 15px;
        font-weight: 600;
        cursor: pointer;
      }}

      .founders-switch-btn.active {{
        border-color: var(--primary);
        color: var(--primary);
        background: #faf7ff;
      }}

      .founders-divider {{
        height: 1px;
        background: #ece7f7;
        margin: 22px 0 16px;
      }}

      .founders-content-grid {{
        display: grid;
        grid-template-columns: minmax(0, 1fr) 320px;
        gap: 28px;
        align-items: start;
      }}

      .founders-section-title {{
        margin: 0 0 14px;
        font-size: 18px;
        line-height: 1.3;
      }}

      .founders-section-title--inner {{
        margin-top: 8px;
      }}

      .founders-form-grid {{
        display: grid;
        gap: 16px;
      }}

      .founders-row {{
        display: grid;
        grid-template-columns: repeat(2, minmax(0, 1fr));
        gap: 14px;
      }}

      .founders-row-3 {{
        grid-template-columns: repeat(3, minmax(0, 1fr));
      }}

      .founders-field {{
        display: grid;
        gap: 8px;
      }}

      .founders-field-full {{
        width: 100%;
      }}

      .founders-label {{
        font-size: 14px;
        font-weight: 600;
        color: #7b7891;
      }}

      .founders-input,
      .founders-select {{
        width: 100%;
        height: 52px;
        border-radius: 12px;
        border: 1.5px solid #d8d6e5;
        background: #fff;
        padding: 0 16px;
        font-size: 15px;
        color: var(--text);
        outline: none;
      }}

      .founders-input::placeholder {{
        color: #a09db2;
      }}

      .founders-input:focus,
      .founders-select:focus {{
        border-color: var(--primary);
      }}

      .founders-select-wrap,
      .founders-input-icon-wrap {{
        position: relative;
      }}

      .founders-select {{
        appearance: none;
        -webkit-appearance: none;
        -moz-appearance: none;
        padding-right: 44px;
      }}

      .founders-select-arrow {{
        position: absolute;
        right: 14px;
        top: 50%;
        transform: translateY(-50%);
        color: #7f7c92;
        font-size: 20px;
        pointer-events: none;
      }}

      .founders-input-icon {{
        position: absolute;
        right: 14px;
        top: 50%;
        transform: translateY(-50%);
        color: #8f8ca5;
        font-size: 18px;
        pointer-events: none;
      }}

      .founders-helper {{
        display: grid;
        grid-template-columns: 26px 1fr;
        gap: 10px;
        align-items: start;
        background: #eef4ff;
        border: 1px solid #d9e5ff;
        border-radius: 14px;
        padding: 14px 16px;
      }}

      .founders-helper--blue {{
        margin-top: 2px;
      }}

      .founders-helper-icon {{
        width: 26px;
        height: 26px;
        border-radius: 999px;
        border: 1.5px solid #7da2e8;
        color: #5b82cf;
        display: grid;
        place-items: center;
        font-weight: 700;
        font-size: 14px;
      }}

      .founders-helper-title {{
        font-size: 14px;
        font-weight: 700;
        color: #4f73b7;
        margin-bottom: 4px;
      }}

      .founders-helper-text {{
        color: #5a6f9c;
        line-height: 1.55;
        font-size: 14px;
      }}

      .founders-actions {{
        margin-top: 22px;
        display: flex;
        justify-content: space-between;
        gap: 18px;
        align-items: center;
        flex-wrap: wrap;
      }}

      .founders-actions-right {{
        display: flex;
        gap: 12px;
        align-items: center;
        flex-wrap: wrap;
      }}

      .founders-save-btn {{
        min-width: 190px;
      }}

      .founders-back-btn,
      .founders-next-btn {{
        min-width: 132px;
      }}

      .founders-aside {{
        position: sticky;
        top: 100px;
      }}

      .founders-aside-card {{
        background: #f7f2ff;
        border: 1px solid #ece7f7;
        border-radius: 24px;
        padding: 22px;
      }}

      .founders-aside-icon {{
        width: 52px;
        height: 52px;
        border-radius: 999px;
        background: #efe7ff;
        display: grid;
        place-items: center;
        color: var(--primary);
        font-size: 24px;
        margin-bottom: 14px;
      }}

      .founders-aside-card h3 {{
        margin: 0 0 18px;
        font-size: 18px;
        line-height: 1.35;
      }}

      .founders-aside-list {{
        display: grid;
        gap: 18px;
      }}

      .founders-aside-item {{
        display: grid;
        grid-template-columns: 26px 1fr;
        gap: 12px;
        align-items: start;
      }}

      .founders-aside-check {{
        width: 26px;
        height: 26px;
        border-radius: 999px;
        background: #efe7ff;
        color: var(--primary);
        display: grid;
        place-items: center;
        font-size: 14px;
        font-weight: 700;
      }}

      .founders-aside-item strong {{
        display: block;
        margin-bottom: 4px;
        font-size: 16px;
        line-height: 1.35;
        color: var(--text);
      }}

      .founders-aside-item span {{
        color: var(--muted);
        font-size: 14px;
        line-height: 1.55;
      }}

      .founders-aside-divider {{
        height: 1px;
        background: #e6def6;
        margin: 18px 0;
      }}

      .founders-aside-important {{
        display: grid;
        grid-template-columns: 34px 1fr;
        gap: 12px;
        align-items: start;
        margin-bottom: 18px;
      }}

      .founders-aside-important-icon {{
        width: 34px;
        height: 34px;
        border-radius: 999px;
        background: #efe7ff;
        display: grid;
        place-items: center;
        color: var(--primary);
        font-size: 16px;
      }}

      .founders-aside-important strong {{
        display: block;
        margin-bottom: 4px;
        color: var(--text);
        font-size: 16px;
      }}

      .founders-aside-important span {{
        color: var(--muted);
        font-size: 14px;
        line-height: 1.5;
      }}

      .founders-aside-link {{
        display: flex;
        align-items: center;
        gap: 10px;
        border: 1px solid #d8cef4;
        border-radius: 14px;
        background: #fff;
        color: var(--primary);
        padding: 14px 16px;
        font-weight: 600;
      }}

      .founders-aside-link-arrow {{
        margin-left: auto;
        font-size: 24px;
      }}

      @media (max-width: 1180px) {{
        .founders-layout {{
          grid-template-columns: 1fr;
        }}

        .founders-aside {{
          position: static;
        }}
      }}

      @media (max-width: 900px) {{
        .founders-content-grid {{
          grid-template-columns: 1fr;
        }}
      }}

      @media (max-width: 720px) {{
        .founders-card {{
          padding: 20px 16px;
        }}

        .founders-row,
        .founders-row-3,
        .founders-actions,
        .founders-actions-right {{
          grid-template-columns: 1fr;
          flex-direction: column;
          align-items: stretch;
        }}

        .founders-save-btn,
        .founders-back-btn,
        .founders-next-btn {{
          width: 100%;
          min-width: 0;
        }}
      }}
    </style>
    """