from flask import url_for


def get_tax_content(flow: str = "ip") -> str:
    if flow == "ooo":
        back_url = url_for("ooo_form_step_4")
        next_url = url_for("ooo_form_step_6")
        extra_block = ""
    else:
        back_url = url_for("ip_form_step_2")
        next_url = url_for("ip_form_step_4")
        extra_block = f"""
        <div class="tax-extra-title">Дополнительно</div>

        <div class="tax-patent-card">
          <div class="tax-patent-icon">📄</div>

          <div class="tax-patent-main">
            <h3>ПСН - Патентная система налогообложения</h3>
            <ul>
              <li><strong>Налог:</strong> фиксированная сумма, по умолчанию рассчитывается по ставке 6% от потенциального дохода, установленного государством</li>
              <li><strong>Учёт:</strong> не требуется ведение бухгалтерии и кассы (если работаешь без сотрудников)</li>
              <li><strong>Кому подходит:</strong> для ИП с ограниченным видом деятельности и небольшими оборотами</li>
            </ul>

            <div class="tax-patent-actions">
              <button type="button" class="btn btn-secondary tax-inline-btn">Выбрать</button>
              <button type="button" class="tax-link-btn">Подробнее</button>
            </div>
          </div>

          <div class="tax-patent-note">
            Если данное поле будет отмечено, то Вы сможете заполнить данные для патента на следующем шаге
          </div>
        </div>
        """

    return f"""
    <section class="tax-layout">
      <div class="tax-main">
        <div class="tax-section-title">Выберите режим налогообложения</div>

        <div class="tax-cards">
          {render_tax_card(
              title="УСН «Доходы» (6%)",
              rate="6%",
              rate_caption="УСН<br>«Доходы»",
              details=[
                  "Налог: 6% с дохода",
                  "Учёт: простая отчётность, без учёта расходов",
                  "Кому подходит: если у бизнеса небольшие расходы",
              ],
              calc_title="Пример расчёта",
              calc_rows=[
                  ("Доход в месяц", "100 000 ₽"),
                  ("Налог (6%)", "6 000 ₽ / мес"),
              ],
              selected=True,
              accent="purple",
              button_text="Выбран",
          )}

          {render_tax_card(
              title="УСН «Доходы минус расходы» (15%)",
              rate="15%",
              rate_caption="УСН<br>«Доходы минус<br>расходы»",
              details=[
                  "Налог: 15% с разницы доходов и расходов",
                  "Учёт: нужен учёт расходов и подтверждающие документы",
                  "Кому подходит: если у бизнеса есть значительные расходы",
              ],
              calc_title="Пример расчёта",
              calc_rows=[
                  ("Доход в месяц", "100 000 ₽"),
                  ("Расходы в месяц", "60 000 ₽"),
                  ("Налог (15%)", "6 000 ₽ / мес"),
              ],
              selected=False,
              accent="green",
              button_text="Выбрать",
          )}

          {render_tax_card(
              title="ОСН (общая система налогообложения)",
              rate="20%",
              rate_caption="ОСН<br>(общая система)",
              details=[
                  "Налог: 20% на прибыль + НДС 20%",
                  "Учёт: полная бухгалтерская отчётность и декларации по НДС",
                  "Кому подходит: для работы с крупными компаниями и НДС",
              ],
              calc_title="Пример расчёта",
              calc_rows=[
                  ("Прибыль в месяц", "50 000 ₽"),
                  ("Налог на прибыль (20%)", "10 000 ₽"),
                  ("+ НДС (20%)", "отдельно"),
              ],
              selected=False,
              accent="blue",
              button_text="Выбрать",
          )}
        </div>

        {extra_block}

        <div class="tax-actions">
          <a href="{back_url}" class="btn btn-secondary tax-btn-back">Назад</a>
          <a href="{next_url}" class="btn btn-primary tax-btn-next">Далее</a>
        </div>
      </div>

      <aside class="tax-aside">
        <div class="tax-aside-card">
          <h3>Как выбрать режим?</h3>

          <div class="tax-aside-list">
            <div class="tax-aside-item">
              <div class="tax-aside-icon">🧮</div>
              <div>
                <strong>Мало расходов?</strong>
                <span>Если расходы составляют менее 60% от доходов — выбирайте УСН «Доходы».</span>
              </div>
            </div>

            <div class="tax-aside-item">
              <div class="tax-aside-icon">📄</div>
              <div>
                <strong>Есть большие расходы?</strong>
                <span>УСН «Доходы минус расходы» поможет платить меньше налогов.</span>
              </div>
            </div>

            <div class="tax-aside-item">
              <div class="tax-aside-icon">💼</div>
              <div>
                <strong>Работаете с компаниями и НДС?</strong>
                <span>ОСН подходит, если вам нужен НДС и работа с крупными партнёрами.</span>
              </div>
            </div>
          </div>
        </div>

        <div class="tax-note-card">
          <div class="tax-note-icon">i</div>
          <div>
            Вы всегда сможете изменить режим налогообложения после регистрации, уведомив налоговую.
          </div>
        </div>
      </aside>
    </section>

    <style>
      .tax-layout {{
        display: grid;
        grid-template-columns: minmax(0, 1fr) 340px;
        gap: 24px;
        align-items: start;
      }}

      .tax-section-title {{
        margin: 0 0 18px;
        font-size: 22px;
        line-height: 1.25;
        font-weight: 700;
        color: var(--text);
      }}

      .tax-cards {{
        display: grid;
        gap: 14px;
      }}

      .tax-card {{
        display: grid;
        grid-template-columns: 34px 120px minmax(0, 1fr) 170px;
        gap: 18px;
        align-items: center;
        background: #fff;
        border: 1px solid #e8e2f5;
        border-radius: 20px;
        padding: 18px 18px 16px;
        box-shadow: var(--shadow);
      }}

      .tax-card.selected {{
        border: 2px solid var(--primary);
      }}

      .tax-radio {{
        width: 22px;
        height: 22px;
        border-radius: 999px;
        border: 2px solid #d2c8ef;
        display: grid;
        place-items: center;
      }}

      .tax-card.selected .tax-radio {{
        border-color: var(--primary);
      }}

      .tax-radio-dot {{
        width: 10px;
        height: 10px;
        border-radius: 999px;
        background: transparent;
      }}

      .tax-card.selected .tax-radio-dot {{
        background: var(--primary);
      }}

      .tax-rate-box {{
        height: 102px;
        border-radius: 16px;
        display: grid;
        place-items: center;
        text-align: center;
        padding: 8px;
        font-weight: 700;
      }}

      .tax-rate-box.purple {{
        background: #f1ebff;
        color: #6e40d8;
      }}

      .tax-rate-box.green {{
        background: #edf8f1;
        color: #2ea463;
      }}

      .tax-rate-box.blue {{
        background: #edf5ff;
        color: #2f7ee5;
      }}

      .tax-rate-value {{
        font-size: 26px;
        line-height: 1;
        margin-bottom: 8px;
      }}

      .tax-rate-caption {{
        font-size: 13px;
        line-height: 1.25;
      }}

      .tax-content h3 {{
        margin: 0 0 10px;
        font-size: 18px;
        line-height: 1.35;
      }}

      .tax-list {{
        margin: 0;
        padding-left: 16px;
        color: var(--muted);
        font-size: 15px;
        line-height: 1.55;
      }}

      .tax-list li {{
        margin: 6px 0;
      }}

      .tax-card-footer {{
        display: flex;
        align-items: center;
        gap: 18px;
        margin-top: 14px;
        flex-wrap: wrap;
      }}

      .tax-inline-btn {{
        min-width: 100px;
        height: 40px;
        padding: 0 18px;
        border-radius: 12px;
        font-size: 14px;
      }}

      .tax-card.selected .tax-inline-btn {{
        background: var(--primary);
        color: #fff;
        border-color: var(--primary);
      }}

      .tax-link-btn {{
        border: none;
        background: none;
        color: var(--primary);
        font-size: 14px;
        font-weight: 700;
        cursor: pointer;
        padding: 0;
      }}

      .tax-calc {{
        border-radius: 14px;
        padding: 14px 14px 12px;
        font-size: 13px;
        line-height: 1.45;
      }}

      .tax-calc.purple {{
        background: #f5f0ff;
        color: #6445b4;
      }}

      .tax-calc.green {{
        background: #eef8f1;
        color: #418b60;
      }}

      .tax-calc.blue {{
        background: #eef5ff;
        color: #4177c2;
      }}

      .tax-calc-title {{
        font-weight: 700;
        margin-bottom: 10px;
      }}

      .tax-calc-row {{
        display: flex;
        justify-content: space-between;
        gap: 12px;
        padding: 4px 0;
        border-bottom: 1px solid rgba(0,0,0,0.06);
      }}

      .tax-calc-row:last-child {{
        border-bottom: none;
      }}

      .tax-extra-title {{
        margin: 18px 0 10px;
        font-size: 20px;
        font-weight: 700;
      }}

      .tax-patent-card {{
        display: grid;
        grid-template-columns: 60px minmax(0, 1fr) 220px;
        gap: 18px;
        align-items: start;
        background: #fff;
        border: 1px solid #e8e2f5;
        border-radius: 20px;
        padding: 18px;
        box-shadow: var(--shadow);
      }}

      .tax-patent-icon {{
        width: 52px;
        height: 52px;
        border-radius: 999px;
        background: #f1ebff;
        display: grid;
        place-items: center;
        color: var(--primary);
        font-size: 22px;
      }}

      .tax-patent-main h3 {{
        margin: 0 0 10px;
        font-size: 18px;
        line-height: 1.35;
      }}

      .tax-patent-main ul {{
        margin: 0;
        padding-left: 18px;
        color: var(--muted);
        font-size: 15px;
        line-height: 1.55;
      }}

      .tax-patent-main li {{
        margin: 6px 0;
      }}

      .tax-patent-actions {{
        display: flex;
        gap: 16px;
        align-items: center;
        margin-top: 14px;
        flex-wrap: wrap;
      }}

      .tax-patent-note {{
        background: #f5f0ff;
        border: 1px solid #eadfff;
        border-radius: 14px;
        padding: 14px;
        color: #7b65b5;
        font-size: 14px;
        line-height: 1.5;
      }}

      .tax-actions {{
        margin-top: 18px;
        display: flex;
        justify-content: space-between;
        gap: 14px;
        flex-wrap: wrap;
      }}

      .tax-btn-back {{
        min-width: 140px;
      }}

      .tax-btn-next {{
        min-width: 140px;
      }}

      .tax-aside {{
        position: sticky;
        top: 100px;
        display: grid;
        gap: 16px;
      }}

      .tax-aside-card,
      .tax-note-card {{
        background: #f7f2ff;
        border: 1px solid #ece7f7;
        border-radius: 22px;
        padding: 22px;
      }}

      .tax-aside-card h3 {{
        margin: 0 0 18px;
        font-size: 18px;
        line-height: 1.35;
      }}

      .tax-aside-list {{
        display: grid;
        gap: 18px;
      }}

      .tax-aside-item {{
        display: grid;
        grid-template-columns: 46px 1fr;
        gap: 14px;
        align-items: start;
      }}

      .tax-aside-icon {{
        width: 46px;
        height: 46px;
        border-radius: 999px;
        background: #efe7ff;
        display: grid;
        place-items: center;
        color: var(--primary);
        font-size: 20px;
      }}

      .tax-aside-item strong {{
        display: block;
        margin-bottom: 4px;
        font-size: 15px;
        line-height: 1.35;
        color: var(--text);
      }}

      .tax-aside-item span {{
        color: var(--muted);
        font-size: 14px;
        line-height: 1.55;
      }}

      .tax-note-card {{
        display: grid;
        grid-template-columns: 34px 1fr;
        gap: 12px;
        align-items: start;
        color: #7b65b5;
        line-height: 1.55;
        font-size: 14px;
      }}

      .tax-note-icon {{
        width: 34px;
        height: 34px;
        border-radius: 999px;
        border: 2px solid var(--primary);
        display: grid;
        place-items: center;
        color: var(--primary);
        font-weight: 700;
      }}

      @media (max-width: 1180px) {{
        .tax-layout {{
          grid-template-columns: 1fr;
        }}

        .tax-aside {{
          position: static;
        }}
      }}

      @media (max-width: 980px) {{
        .tax-card {{
          grid-template-columns: 34px 100px 1fr;
        }}

        .tax-calc {{
          grid-column: 2 / -1;
        }}

        .tax-patent-card {{
          grid-template-columns: 1fr;
        }}
      }}

      @media (max-width: 720px) {{
        .tax-card {{
          grid-template-columns: 1fr;
          gap: 14px;
        }}

        .tax-radio {{
          order: -1;
        }}

        .tax-rate-box {{
          width: 100%;
        }}

        .tax-calc {{
          width: 100%;
        }}

        .tax-actions {{
          flex-direction: column;
        }}

        .tax-btn-back,
        .tax-btn-next {{
          width: 100%;
        }}
      }}
    </style>
    """


def render_tax_card(
    title: str,
    rate: str,
    rate_caption: str,
    details: list[str],
    calc_title: str,
    calc_rows: list[tuple[str, str]],
    selected: bool = False,
    accent: str = "purple",
    button_text: str = "Выбрать",
) -> str:
    selected_class = " selected" if selected else ""
    tax_list_html = "".join([f"<li>{item}</li>" for item in details])
    calc_rows_html = "".join(
        [f'<div class="tax-calc-row"><span>{label}</span><strong>{value}</strong></div>' for label, value in calc_rows]
    )

    return f"""
    <div class="tax-card{selected_class}">
      <div class="tax-radio">
        <div class="tax-radio-dot"></div>
      </div>

      <div class="tax-rate-box {accent}">
        <div>
          <div class="tax-rate-value">{rate}</div>
          <div class="tax-rate-caption">{rate_caption}</div>
        </div>
      </div>

      <div class="tax-content">
        <h3>{title}</h3>
        <ul class="tax-list">
          {tax_list_html}
        </ul>

        <div class="tax-card-footer">
          <button type="button" class="btn btn-secondary tax-inline-btn">{button_text}</button>
          <button type="button" class="tax-link-btn">Подробнее</button>
        </div>
      </div>

      <div class="tax-calc {accent}">
        <div class="tax-calc-title">{calc_title}</div>
        {calc_rows_html}
      </div>
    </div>
    """
