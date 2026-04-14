from flask import url_for
from pages.shared_forms.progress import render_subprogress_block


def get_ooo_step3_content(substep: str = "director") -> str:
    substep_map = {
        "director": 1,
        "charter": 2,
        "address": 3,
    }

    current_substep = substep_map.get(substep, 1)

    subprogress_html = render_subprogress_block(
        ["Руководитель", "Устав", "Адрес, капитал и печать"],
        current_step=current_substep,
    )

    if substep == "charter":
        content_html = _render_charter_substep()
    elif substep == "address":
        content_html = _render_address_substep()
    else:
        content_html = _render_director_substep()

    return f"""
    {subprogress_html}

    <section class="company-layout">
      <div class="company-main">
        {content_html}
      </div>

      <aside class="company-aside">
        <div class="company-aside-card">
          <div class="company-aside-icon">🛡</div>
          <h3>Зачем указывать руководителя?</h3>

          <p class="company-aside-text">
            Данные руководителя включаются в учредительные документы и используются
            для регистрации компании в налоговой.
          </p>

          <div class="company-aside-divider"></div>

          <div class="company-aside-list">
            <div class="company-aside-item">
              <div class="company-aside-check">✓</div>
              <div>
                <strong>Руководитель подписывает документы</strong>
                <span>Он будет подписывать документы от имени компании.</span>
              </div>
            </div>

            <div class="company-aside-item">
              <div class="company-aside-check">✓</div>
              <div>
                <strong>Данные проверяются налоговой</strong>
                <span>ФНС проверяет паспортные данные при регистрации.</span>
              </div>
            </div>

            <div class="company-aside-item">
              <div class="company-aside-check">✓</div>
              <div>
                <strong>В любой момент можно изменить</strong>
                <span>После регистрации данные руководителя можно будет обновить.</span>
              </div>
            </div>
          </div>

          <a href="#" class="company-aside-link">
            <span>Подробнее о руководителе</span>
            <span class="company-aside-link-arrow">›</span>
          </a>
        </div>
      </aside>
    </section>

    <style>
      .company-layout {{
        display: grid;
        grid-template-columns: minmax(0, 1fr) 370px;
        gap: 24px;
        align-items: start;
      }}

      .company-card {{
        background: #ffffff;
        border: 1px solid var(--border);
        border-radius: 28px;
        padding: 28px 28px 24px;
        box-shadow: var(--shadow);
      }}

      .company-card-title {{
        margin: 0 0 10px;
        font-size: 22px;
        line-height: 1.25;
      }}

      .company-card-subtitle {{
        margin: 0 0 18px;
        color: var(--muted);
        font-size: 16px;
        line-height: 1.6;
      }}

      .company-section-title {{
        margin: 28px 0 14px;
        font-size: 18px;
        line-height: 1.35;
        font-weight: 700;
        color: var(--text);
      }}

      .company-section-title:first-child {{
        margin-top: 0;
      }}

      .company-form-grid {{
        display: grid;
        gap: 16px;
      }}

      .company-row {{
        display: grid;
        grid-template-columns: repeat(2, minmax(0, 1fr));
        gap: 14px;
      }}

      .company-field {{
        display: grid;
        gap: 8px;
      }}

      .company-label {{
        font-size: 14px;
        font-weight: 600;
        color: #7b7891;
      }}

      .company-input,
      .company-select {{
        width: 100%;
        height: 54px;
        border-radius: 14px;
        border: 1.5px solid #d8d6e5;
        background: #fff;
        padding: 0 16px;
        font-size: 15px;
        color: var(--text);
        outline: none;
      }}

      .company-input::placeholder {{
        color: #a09db2;
      }}

      .company-input:focus,
      .company-select:focus {{
        border-color: var(--primary);
      }}

      .company-select-wrap {{
        position: relative;
      }}

      .company-select {{
        appearance: none;
        -webkit-appearance: none;
        -moz-appearance: none;
        padding-right: 44px;
      }}

      .company-select-arrow {{
        position: absolute;
        right: 14px;
        top: 50%;
        transform: translateY(-50%);
        color: #7f7c92;
        font-size: 20px;
        pointer-events: none;
      }}

      .company-checkbox {{
        display: flex;
        align-items: flex-start;
        gap: 12px;
        margin: 10px 0 14px;
      }}

      .company-checkbox input {{
        width: 18px;
        height: 18px;
        margin-top: 3px;
      }}

      .company-checkbox span {{
        color: #5a6f9c;
        font-size: 15px;
        line-height: 1.5;
      }}

      .company-helper {{
        display: grid;
        grid-template-columns: 26px 1fr;
        gap: 10px;
        align-items: start;
        background: #eef4ff;
        border: 1px solid #d9e5ff;
        border-radius: 16px;
        padding: 14px 16px;
      }}

      .company-helper.soft {{
        background: #f5f0ff;
        border-color: #e7dcff;
      }}

      .company-helper-icon {{
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

      .company-helper.soft .company-helper-icon {{
        border-color: var(--primary);
        color: var(--primary);
      }}

      .company-helper-title {{
        font-size: 15px;
        font-weight: 700;
        color: #315ea9;
        margin-bottom: 4px;
      }}

      .company-helper-text {{
        color: #5a6f9c;
        line-height: 1.55;
        font-size: 14px;
      }}

      .company-helper.soft .company-helper-title {{
        color: var(--primary);
      }}

      .company-radio-row {{
        display: flex;
        gap: 24px;
        flex-wrap: wrap;
        margin-top: 10px;
      }}

      .company-radio {{
        display: flex;
        align-items: center;
        gap: 10px;
        color: var(--text);
        font-size: 16px;
      }}

      .company-radio input {{
        width: 18px;
        height: 18px;
      }}

      .company-actions {{
        margin-top: 26px;
        display: flex;
        justify-content: space-between;
        gap: 18px;
        align-items: center;
        flex-wrap: wrap;
      }}

      .company-actions-right {{
        display: flex;
        gap: 12px;
        align-items: center;
        flex-wrap: wrap;
      }}

      .company-save-btn {{
        min-width: 190px;
      }}

      .company-back-btn,
      .company-next-btn {{
        min-width: 120px;
      }}

      .company-aside {{
        position: sticky;
        top: 100px;
      }}

      .company-aside-card {{
        background: #f7f2ff;
        border: 1px solid #ece7f7;
        border-radius: 24px;
        padding: 22px;
      }}

      .company-aside-icon {{
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

      .company-aside-card h3 {{
        margin: 0 0 14px;
        font-size: 18px;
        line-height: 1.35;
      }}

      .company-aside-text {{
        margin: 0;
        color: var(--muted);
        font-size: 15px;
        line-height: 1.6;
      }}

      .company-aside-divider {{
        height: 1px;
        background: #e6def6;
        margin: 18px 0;
      }}

      .company-aside-list {{
        display: grid;
        gap: 18px;
      }}

      .company-aside-item {{
        display: grid;
        grid-template-columns: 24px 1fr;
        gap: 12px;
        align-items: start;
      }}

      .company-aside-check {{
        width: 24px;
        height: 24px;
        border-radius: 999px;
        background: #efe7ff;
        color: var(--primary);
        display: grid;
        place-items: center;
        font-size: 13px;
        font-weight: 700;
      }}

      .company-aside-item strong {{
        display: block;
        margin-bottom: 4px;
        font-size: 15px;
        line-height: 1.35;
        color: var(--text);
      }}

      .company-aside-item span {{
        color: var(--muted);
        font-size: 14px;
        line-height: 1.55;
      }}

      .company-aside-link {{
        display: flex;
        align-items: center;
        gap: 10px;
        border: 1px solid #d8cef4;
        border-radius: 14px;
        background: #fff;
        color: var(--primary);
        padding: 14px 16px;
        font-weight: 600;
        margin-top: 20px;
      }}

      .company-aside-link-arrow {{
        margin-left: auto;
        font-size: 24px;
      }}

      @media (max-width: 1180px) {{
        .company-layout {{
          grid-template-columns: 1fr;
        }}

        .company-aside {{
          position: static;
        }}
      }}

      @media (max-width: 900px) {{
        .company-row {{
          grid-template-columns: 1fr;
        }}
      }}

      @media (max-width: 720px) {{
        .company-card {{
          padding: 20px 16px;
        }}

        .company-actions,
        .company-actions-right {{
          flex-direction: column;
          align-items: stretch;
        }}

        .company-save-btn,
        .company-back-btn,
        .company-next-btn {{
          width: 100%;
          min-width: 0;
        }}

        .company-radio-row {{
          flex-direction: column;
          gap: 12px;
        }}
      }}
    </style>
    """
    

def _render_director_substep() -> str:
    return f"""
    <div class="company-card">
      <h2 class="company-card-title">Руководитель компании</h2>
      <p class="company-card-subtitle">
        Руководитель осуществляет текущее руководство компанией и действует от её имени без доверенности.
      </p>

      <label class="company-checkbox">
        <input type="checkbox" checked />
        <span>Руководитель — то же лицо, что и учредитель</span>
      </label>

      <div class="company-helper">
        <div class="company-helper-icon">i</div>
        <div>
          <div class="company-helper-text">
            Данные руководителя будут подставлены из информации об учредителе.
            Если руководитель другой — снимите галочку, чтобы заполнить данные вручную.
          </div>
        </div>
      </div>

      <div style="height:1px; background:#ece7f7; margin:20px 0;"></div>

      <div class="company-helper soft">
        <div class="company-helper-icon">💡</div>
        <div>
          <div class="company-helper-title">Важно</div>
          <div class="company-helper-text">
            Онлайн-подача документов доступна только, если руководитель является учредителем.
          </div>
        </div>
      </div>

      <div class="company-actions">
        <a href="{url_for('landing')}" class="btn btn-secondary company-save-btn">💾&nbsp;&nbsp;Сохранить и выйти</a>

        <div class="company-actions-right">
          <a href="{url_for('ooo_form_step_2')}" class="btn btn-secondary company-back-btn">Назад</a>
          <a href="{url_for('ooo_form_step_3_charter')}" class="btn btn-primary company-next-btn">Далее</a>
        </div>
      </div>
    </div>
    """


def _render_charter_substep() -> str:
    return f"""
    <div class="company-card">
      <h2 class="company-card-title">Устав общества</h2>
      <p class="company-card-subtitle">
        Выберите устав, который вы хотите использовать при регистрации ООО.
      </p>

      <div class="company-radio-row">
        <label class="company-radio">
          <input type="radio" name="charter_type" checked />
          <span>Сгенерированный сервисом</span>
        </label>

        <label class="company-radio">
          <input type="radio" name="charter_type" />
          <span>Типовой</span>
        </label>
      </div>

      <div class="company-helper" style="margin-top:20px;">
        <div class="company-helper-icon">i</div>
        <div>
          <div class="company-helper-title">Что выбрать?</div>
          <div class="company-helper-text">
            Сгенерированный сервисом устав подходит для большинства новых компаний.
            Типовой устав — вариант, утверждённый государством, если вы хотите использовать стандартную форму.
          </div>
        </div>
      </div>

      <div class="company-actions">
        <a href="{url_for('landing')}" class="btn btn-secondary company-save-btn">💾&nbsp;&nbsp;Сохранить и выйти</a>

        <div class="company-actions-right">
          <a href="{url_for('ooo_form_step_3')}" class="btn btn-secondary company-back-btn">Назад</a>
          <a href="{url_for('ooo_form_step_3_address')}" class="btn btn-primary company-next-btn">Далее</a>
        </div>
      </div>
    </div>
    """


def _render_address_substep() -> str:
    return f"""
    <div class="company-card">
      <h2 class="company-card-title">Адрес, капитал и печать</h2>

      <h3 class="company-section-title">Юридический адрес организации</h3>

      <label class="company-checkbox">
        <input type="checkbox" />
        <span>Использовать адрес регистрации учредителя в качестве юр. адреса компании</span>
      </label>

      <div class="company-helper">
        <div class="company-helper-icon">i</div>
        <div>
          <div class="company-helper-text">
            Введите или вставьте адрес, после чего выберите подходящий вариант из выпадающего списка.
            Адрес должен указываться в точном соответствии с ГАР (ФИАС).
          </div>
        </div>
      </div>

      <div class="company-form-grid" style="margin-top:14px;">
        <div class="company-field">
          <input class="company-input" type="text" placeholder="Введите адрес" />
        </div>
      </div>

      <h3 class="company-section-title">Уставный капитал</h3>

      <div class="company-form-grid">
        <div class="company-field">
          <label class="company-label">Размер уставного капитала</label>
          <input class="company-input" type="text" placeholder="10000" />
        </div>
      </div>

      <h3 class="company-section-title">Организация работает с печатью?</h3>

      <div class="company-helper">
        <div class="company-helper-icon">i</div>
        <div>
          <div class="company-helper-text">
            Организация может выбрать способ заверения документов: с использованием оттиска печати или без.
            Выбранный способ будет указан в уставе. Если Вы планируете работать с печатью,
            то после регистрации ООО не забудьте заказать её изготовление.
          </div>
        </div>
      </div>

      <div class="company-radio-row">
        <label class="company-radio">
          <input type="radio" name="stamp_type" checked />
          <span>Без печати</span>
        </label>

        <label class="company-radio">
          <input type="radio" name="stamp_type" />
          <span>С печатью</span>
        </label>
      </div>

      <div class="company-actions">
        <a href="{url_for('landing')}" class="btn btn-secondary company-save-btn">💾&nbsp;&nbsp;Сохранить и выйти</a>

        <div class="company-actions-right">
          <a href="{url_for('ooo_form_step_3_charter')}" class="btn btn-secondary company-back-btn">Назад</a>
          <a href="{url_for('ooo_form_step_4')}" class="btn btn-primary company-next-btn">Далее</a>
        </div>
      </div>
    </div>
    """