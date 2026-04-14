from flask import url_for
from pages.shared_forms.progress import render_subprogress_block


def get_ip_step1_content(substep: str = "basic") -> str:
    substep_map = {
        "basic": 1,
        "passport": 2,
        "contacts": 3,
    }

    current_substep = substep_map.get(substep, 1)

    subprogress_html = render_subprogress_block(
        ["Основная информация", "Паспортные данные", "Контакты и адрес"],
        current_step=current_substep,
    )

    if substep == "passport":
        form_html = _render_passport_form()
    elif substep == "contacts":
        form_html = _render_contacts_form()
    else:
        form_html = _render_basic_form()

    return f"""
    {subprogress_html}

    <section class="ip-step-layout">
      <div class="ip-step-main">
        {form_html}
      </div>

      <aside class="ip-step-aside">
        <div class="ip-aside-card">
          <div class="ip-aside-icon">🛡</div>
          <h3>Мы бережём ваши данные</h3>
          <p>Информация передаётся в зашифрованном виде и используется только для регистрации бизнеса.</p>
        </div>
      </aside>
    </section>

    <style>
      .ip-step-layout {{
        display: grid;
        grid-template-columns: minmax(0, 1fr) 320px;
        gap: 24px;
        align-items: start;
      }}

      .ip-card {{
        background: #ffffff;
        border: 1px solid var(--border);
        border-radius: 28px;
        padding: 30px 34px 26px;
        box-shadow: var(--shadow);
      }}

      .ip-card-title {{
        margin: 0 0 8px;
        font-size: 22px;
        line-height: 1.2;
      }}

      .ip-card-subtitle {{
        margin: 0 0 22px;
        color: var(--muted);
        font-size: 16px;
        line-height: 1.6;
      }}

      .ip-form-grid {{
        display: grid;
        gap: 18px;
      }}

      .ip-row {{
        display: grid;
        grid-template-columns: minmax(0, 1fr) minmax(0, 1fr);
        gap: 18px;
      }}

      .ip-row-3 {{
        display: grid;
        grid-template-columns: repeat(3, minmax(0, 1fr));
        gap: 18px;
      }}

      .ip-field {{
        display: grid;
        gap: 10px;
      }}

      .ip-field-full {{
        width: 100%;
      }}

      .ip-label {{
        font-size: 16px;
        font-weight: 600;
        color: var(--text);
      }}

      .ip-input,
      .ip-select {{
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

      .ip-input::placeholder {{
        color: #9a98ab;
      }}

      .ip-input:focus,
      .ip-select:focus {{
        border-color: var(--primary);
      }}

      .ip-input-icon-wrap,
      .ip-select-wrap {{
        position: relative;
      }}

      .ip-input-icon {{
        position: absolute;
        right: 16px;
        top: 50%;
        transform: translateY(-50%);
        color: #8f8ca5;
        font-size: 20px;
        pointer-events: none;
      }}

      .ip-select {{
        appearance: none;
        -webkit-appearance: none;
        -moz-appearance: none;
        padding-right: 48px;
      }}

      .ip-select-arrow {{
        position: absolute;
        right: 16px;
        top: 50%;
        transform: translateY(-50%);
        color: #8f8ca5;
        font-size: 22px;
        pointer-events: none;
      }}

      .ip-gender-row {{
        display: grid;
        grid-template-columns: 1fr 1fr;
        gap: 10px;
      }}

      .ip-gender-btn {{
        height: 58px;
        border-radius: 16px;
        border: 2px solid #d8d6e5;
        background: #fff;
        color: #7f7c92;
        font-size: 16px;
        font-weight: 600;
        cursor: pointer;
      }}

      .ip-gender-btn.active {{
        border-color: var(--primary);
        color: var(--primary);
        background: #faf7ff;
      }}

      .ip-helper {{
        margin-top: 12px;
        display: grid;
        grid-template-columns: 34px 1fr;
        gap: 14px;
        align-items: start;
        background: #eef4ff;
        border: 1px solid #d9e5ff;
        border-radius: 18px;
        padding: 18px 20px;
      }}

      .ip-helper-icon {{
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

      .ip-helper-title {{
        font-size: 16px;
        font-weight: 700;
        color: #4f73b7;
        margin-bottom: 6px;
      }}

      .ip-helper-text {{
        color: #5a6f9c;
        line-height: 1.55;
        font-size: 15px;
      }}

      .ip-upload {{
        margin-top: 18px;
        border: 2px dashed #e5d8ff;
        background: #f7f1ff;
        border-radius: 18px;
        min-height: 120px;
        display: grid;
        place-items: center;
        text-align: center;
        color: var(--primary);
        padding: 20px;
      }}

      .ip-upload small {{
        display: block;
        color: var(--muted);
        margin-top: 8px;
      }}

      .ip-checkbox {{
        display: flex;
        align-items: flex-start;
        gap: 12px;
        margin-top: 8px;
      }}

      .ip-checkbox input {{
        margin-top: 4px;
        width: 18px;
        height: 18px;
      }}

      .ip-checkbox-text strong {{
        display: block;
        font-size: 16px;
        color: var(--text);
        margin-bottom: 4px;
      }}

      .ip-checkbox-text span {{
        color: var(--muted);
        font-size: 14px;
        line-height: 1.5;
      }}

      .ip-actions {{
        margin-top: 26px;
        display: grid;
        grid-template-columns: auto 1fr auto;
        align-items: center;
        gap: 18px;
      }}

      .ip-save-btn,
      .ip-prev-btn {{
        min-width: 220px;
      }}

      .ip-next-btn {{
        min-width: 200px;
      }}

      .ip-actions-note {{
        text-align: center;
        color: #8a889d;
        font-size: 15px;
      }}

      .ip-step-aside {{
        position: sticky;
        top: 100px;
      }}

      .ip-aside-card {{
        background: #f7f2ff;
        border: 1px solid #ece7f7;
        border-radius: 24px;
        padding: 28px 24px;
      }}

      .ip-aside-icon {{
        width: 60px;
        height: 60px;
        border-radius: 999px;
        background: #efe7ff;
        display: grid;
        place-items: center;
        font-size: 26px;
        color: var(--primary);
        margin-bottom: 22px;
      }}

      .ip-aside-card h3 {{
        margin: 0 0 14px;
        font-size: 20px;
        line-height: 1.3;
      }}

      .ip-aside-card p {{
        margin: 0;
        color: var(--muted);
        font-size: 16px;
        line-height: 1.65;
      }}

      @media (max-width: 1100px) {{
        .ip-step-layout {{
          grid-template-columns: 1fr;
        }}

        .ip-step-aside {{
          position: static;
        }}
      }}

      @media (max-width: 720px) {{
        .ip-card {{
          padding: 22px 18px;
        }}

        .ip-row,
        .ip-row-3,
        .ip-gender-row {{
          grid-template-columns: 1fr;
        }}

        .ip-actions {{
          grid-template-columns: 1fr;
        }}

        .ip-actions-note {{
          order: 2;
          text-align: left;
        }}

        .ip-save-btn,
        .ip-prev-btn,
        .ip-next-btn {{
          width: 100%;
          min-width: 0;
        }}
      }}
    </style>
    """


def _render_basic_form() -> str:
    return f"""
    <div class="ip-card">
      <h2 class="ip-card-title">Основная информация</h2>
      <p class="ip-card-subtitle">Укажите ФИО, дату рождения и гражданство</p>

      <div class="ip-form-grid">
        <div class="ip-field ip-field-full">
          <label class="ip-label">ФИО</label>
          <input class="ip-input" type="text" placeholder="Например: Иванов Иван Иванович" />
        </div>

        <div class="ip-row">
          <div class="ip-field">
            <label class="ip-label">Дата рождения</label>
            <div class="ip-input-icon-wrap">
              <input class="ip-input" type="text" placeholder="ДД.ММ.ГГГГ" />
              <span class="ip-input-icon">🗓</span>
            </div>
          </div>

          <div class="ip-field">
            <label class="ip-label">Пол</label>
            <div class="ip-gender-row">
              <button type="button" class="ip-gender-btn active">♂&nbsp;&nbsp;Мужской</button>
              <button type="button" class="ip-gender-btn">♀&nbsp;&nbsp;Женский</button>
            </div>
          </div>
        </div>

        <div class="ip-field ip-field-full">
          <label class="ip-label">Гражданство</label>
          <div class="ip-select-wrap">
            <select class="ip-input ip-select">
              <option>Гражданин РФ</option>
              <option>Иностранный гражданин</option>
              <option>Лицо без гражданства</option>
            </select>
            <span class="ip-select-arrow">⌄</span>
          </div>
        </div>
      </div>

      <div class="ip-helper">
        <div class="ip-helper-icon">i</div>
        <div>
          <div class="ip-helper-title">Зачем нужны эти данные?</div>
          <div class="ip-helper-text">
            Данные должны совпадать с паспортом, чтобы документы прошли проверку в ФНС с первого раза.
          </div>
        </div>
      </div>

      <div class="ip-actions">
        <a href="{url_for('landing')}" class="btn btn-secondary ip-save-btn">💾&nbsp;&nbsp;Сохранить и выйти</a>
        <div class="ip-actions-note">Осталось 2 коротких шага в этом разделе</div>
        <a href="{url_for('ip_form_step_1_passport')}" class="btn btn-primary ip-next-btn">Далее</a>
      </div>
    </div>
    """


def _render_passport_form() -> str:
    return f"""
    <div class="ip-card">
      <h2 class="ip-card-title">Паспортные данные</h2>

      <div class="ip-helper">
        <div class="ip-helper-icon">i</div>
        <div>
          <div class="ip-helper-text">
            Чтобы пройти проверку в налоговой, данные должны полностью соответствовать паспорту
            (включая сокращения — г., гор., р-н и т.п.).
          </div>
        </div>
      </div>

      <p class="ip-card-subtitle" style="margin-top:20px; margin-bottom:12px;">
        Загрузите разворот с ФИО для распознавания и заполнения сведений
      </p>

      <div class="ip-upload">
        <div>
          Перетащите файл сюда или нажмите для выбора
          <small>Формат: JPEG, JPG, PNG, HEIC, PDF (первая страница). Размер до 16МБ.</small>
        </div>
      </div>

      <div class="ip-form-grid" style="margin-top:20px;">
        <div class="ip-row-3">
          <div class="ip-field">
            <input class="ip-input" type="text" placeholder="Фамилия" />
          </div>
          <div class="ip-field">
            <input class="ip-input" type="text" placeholder="Имя" />
          </div>
          <div class="ip-field">
            <input class="ip-input" type="text" placeholder="Отчество (при наличии)" />
          </div>
        </div>

        <div class="ip-row">
          <div class="ip-field">
            <input class="ip-input" type="text" placeholder="Дата рождения" />
          </div>
          <div class="ip-field">
            <div class="ip-select-wrap">
              <select class="ip-input ip-select">
                <option>-- Выберите --</option>
                <option>Мужской</option>
                <option>Женский</option>
              </select>
              <span class="ip-select-arrow">⌄</span>
            </div>
          </div>
        </div>

        <div class="ip-field ip-field-full">
          <input class="ip-input" type="text" placeholder="Место рождения (как в паспорте)" />
        </div>

        <div class="ip-row">
          <div class="ip-field">
            <input class="ip-input" type="text" placeholder="Серия паспорта" />
          </div>
          <div class="ip-field">
            <input class="ip-input" type="text" placeholder="Номер паспорта" />
          </div>
        </div>

        <div class="ip-field ip-field-full">
          <input class="ip-input" type="text" placeholder="Кем выдан (как в паспорте)" />
        </div>

        <div class="ip-row">
          <div class="ip-field">
            <input class="ip-input" type="text" placeholder="Дата выдачи" />
          </div>
          <div class="ip-field">
            <input class="ip-input" type="text" placeholder="Код подразделения" />
          </div>
        </div>
      </div>

      <div class="ip-actions">
        <a href="{url_for('ip_form_page')}" class="btn btn-secondary ip-prev-btn">Предыдущий подшаг</a>
        <div class="ip-actions-note">Остался 1 короткий шаг в этом разделе</div>
        <a href="{url_for('ip_form_step_1_contacts')}" class="btn btn-primary ip-next-btn">Далее</a>
      </div>
    </div>
    """


def _render_contacts_form() -> str:
    return f"""
    <div class="ip-card">
      <h2 class="ip-card-title">Адрес регистрации в РФ</h2>

      <div class="ip-helper">
        <div class="ip-helper-icon">i</div>
        <div>
          <div class="ip-helper-text">
            Введите или вставьте адрес, после чего выберите подходящий вариант из выпадающего списка.
            Адрес должен указываться в точном соответствии с ГАР (ФИАС).
          </div>
        </div>
      </div>

      <div class="ip-form-grid" style="margin-top:18px;">
        <div class="ip-field ip-field-full">
          <input class="ip-input" type="text" placeholder="Адрес регистрации в РФ" />
        </div>
      </div>

      <h2 class="ip-card-title" style="margin-top:32px;">Контактная информация</h2>

      <div class="ip-helper">
        <div class="ip-helper-icon">i</div>
        <div>
          <div class="ip-helper-title">Важно</div>
          <div class="ip-helper-text">
            Укажите корректные номер телефона и email. Телефон должен принадлежать человеку,
            на которого оформляется бизнес. Email используется для отправки уведомлений сервиса.
          </div>
        </div>
      </div>

      <div class="ip-form-grid" style="margin-top:18px;">
        <div class="ip-row">
          <div class="ip-field">
            <input class="ip-input" type="email" placeholder="E-mail" />
          </div>
          <div class="ip-field">
            <input class="ip-input" type="text" placeholder="Телефон +7" />
          </div>
        </div>
      </div>

      <h2 class="ip-card-title" style="margin-top:32px;">Особенности пакета документов</h2>

      <div class="ip-form-grid" style="margin-top:18px;">
        <div class="ip-field ip-field-full">
          <input class="ip-input" type="email" placeholder="E-mail для внесения в ЕГРИП" />
        </div>
      </div>

      <label class="ip-checkbox">
        <input type="checkbox" />
        <div class="ip-checkbox-text">
          <strong>Получить документы из ФНС на бумажном носителе</strong>
          <span>Если данное поле не будет отмечено, то ФНС вышлет документы только на электронную почту</span>
        </div>
      </label>

      <div class="ip-actions">
        <a href="{url_for('ip_form_step_1_passport')}" class="btn btn-secondary ip-prev-btn">Предыдущий подшаг</a>
        <div class="ip-actions-note">Раздел заполнен, дальше выбор деятельности</div>
        <a href="{url_for('ip_form_step_2')}" class="btn btn-primary ip-next-btn">Далее</a>
      </div>
    </div>
    """