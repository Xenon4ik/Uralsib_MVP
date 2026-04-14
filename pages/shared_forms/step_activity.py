from flask import url_for


def get_activity_content(flow: str = "ip") -> str:
    if flow == "ooo":
        back_url = url_for("ooo_form_step_3")
        next_url = url_for("ooo_form_step_5")
    else:
        back_url = url_for("ip_form_step_1_contacts")
        next_url = url_for("ip_form_step_3")

    return f"""
    <section class="activity-layout">
      <div class="activity-main">
        <div class="activity-card">
          <h2 class="activity-title">Подбор видов деятельности</h2>
          <p class="activity-subtitle">
            Введите ключевые слова или фразу, чем вы планируете заниматься.
            Мы предложим подходящие коды ОКВЭД — выберите подходящие из списка.
          </p>

          <div class="activity-search-wrap">
            <span class="activity-search-icon">⌕</span>
            <input
              class="activity-search-input"
              type="text"
              placeholder="Например: розничная торговля одеждой, ремонт телефонов, фотоуслуги"
            />
          </div>

          <div class="activity-hints">
            <span>Например:</span>
            <button type="button" class="activity-hint">доставка еды</button>
            <button type="button" class="activity-hint">интернет-магазин</button>
            <button type="button" class="activity-hint">ремонт автомобилей</button>
          </div>

          <div class="activity-results-head">
            <div class="activity-results-title">
              Подходящие виды деятельности
              <span class="activity-badge">Найдено 7 вариантов</span>
            </div>
          </div>

          <div class="activity-table">
            <div class="activity-table-head">
              <div>Выбрать</div>
              <div>Код ОКВЭД</div>
              <div>Наименование вида деятельности</div>
              <div></div>
              <div>Основной</div>
            </div>

            {render_activity_row("47.71", "Торговля розничная одеждой в специализированных магазинах")}
            {render_activity_row("47.72", "Торговля розничная обувью и изделиями из кожи в специализированных магазинах")}
            {render_activity_row("47.19", "Торговля розничная прочая в неспециализированных магазинах")}
            {render_activity_row("47.91", "Торговля розничная по почте или по информационно-коммуникационной сети Интернет", selected=True, primary=True)}
            {render_activity_row("47.99", "Торговля розничная прочая вне магазинов, палаток, рынков")}
          </div>

          <div class="activity-footer">
            <div class="activity-selected">Выбрано: <strong>1</strong></div>

            <div class="activity-actions">
              <a href="{back_url}" class="btn btn-secondary activity-btn-back">Назад</a>
              <a href="{next_url}" class="btn btn-primary activity-btn-next">Далее</a>
            </div>
          </div>
        </div>
      </div>

      <aside class="activity-aside">
        <div class="activity-aside-card">
          <div class="activity-aside-icon">💡</div>
          <h3>Как это работает?</h3>

          <div class="activity-aside-steps">
            <div class="activity-aside-step">
              <div class="activity-aside-step-icon">⌕</div>
              <div>
                <strong>Введите ключевые слова</strong>
                <span>Напишите, чем планируете заниматься</span>
              </div>
            </div>

            <div class="activity-aside-step">
              <div class="activity-aside-step-icon">☰</div>
              <div>
                <strong>Выберите подходящее</strong>
                <span>Отметьте один или несколько видов деятельности</span>
              </div>
            </div>

            <div class="activity-aside-step">
              <div class="activity-aside-step-icon">☆</div>
              <div>
                <strong>Укажите основной</strong>
                <span>Выберите основной вид деятельности</span>
              </div>
            </div>
          </div>

          <div class="activity-aside-note">
            <div class="activity-aside-note-icon">i</div>
            <div>Вы сможете добавить или изменить виды деятельности позже.</div>
          </div>
        </div>
      </aside>
    </section>

    <style>
        .activity-layout {{
            display: grid;
            grid-template-columns: minmax(0, 1fr) 340px;
            gap: 24px;
            align-items: start;
        }}

        .activity-main {{
            min-width: 0;
        }}

        .activity-card {{
            background: #ffffff;
            border: 1px solid var(--border);
            border-radius: 28px;
            padding: 30px 28px 22px;
            box-shadow: var(--shadow);
        }}

        .activity-title {{
            margin: 0 0 10px;
            font-size: 22px;
            line-height: 1.2;
        }}

        .activity-subtitle {{
            margin: 0 0 18px;
            color: var(--muted);
            font-size: 16px;
            line-height: 1.6;
            max-width: 760px;
        }}

        .activity-search-wrap {{
            position: relative;
            margin-bottom: 14px;
        }}

        .activity-search-icon {{
            position: absolute;
            left: 16px;
            top: 50%;
            transform: translateY(-50%);
            color: #8f8ca5;
            font-size: 20px;
        }}

        .activity-search-input {{
            width: 100%;
            height: 56px;
            border-radius: 16px;
            border: 2px solid #8c66f0;
            background: #fff;
            padding: 0 18px 0 48px;
            font-size: 16px;
            outline: none;
        }}

        .activity-search-input::placeholder {{
            color: #9a98ab;
        }}

        .activity-hints {{
            display: flex;
            align-items: center;
            flex-wrap: wrap;
            gap: 8px;
            margin-bottom: 20px;
            color: var(--muted);
            font-size: 15px;
        }}

        .activity-hint {{
            background: none;
            border: none;
            padding: 0;
            color: var(--primary);
            font-size: 15px;
            font-weight: 600;
            cursor: pointer;
        }}

        .activity-results-head {{
            margin-bottom: 10px;
        }}

        .activity-results-title {{
            display: flex;
            align-items: center;
            gap: 12px;
            flex-wrap: wrap;
            font-size: 18px;
            font-weight: 700;
            color: var(--text);
        }}

        .activity-badge {{
            display: inline-flex;
            align-items: center;
            justify-content: center;
            height: 28px;
            padding: 0 12px;
            border-radius: 999px;
            background: #efe7ff;
            color: var(--primary);
            font-size: 13px;
            font-weight: 700;
        }}

        .activity-table {{
            border: 1px solid #e6e1f2;
            border-radius: 18px;
            overflow: hidden;
            background: #fff;
        }}

        .activity-table-head,
        .activity-row {{
            display: grid;
            grid-template-columns: 72px 110px minmax(320px, 1fr) 56px 92px;
            align-items: center;
        }}

        .activity-table-head {{
            min-height: 48px;
            padding: 0 14px;
            background: #ffffff;
            color: #7e7b91;
            font-size: 14px;
            font-weight: 600;
            border-bottom: 1px solid #ece7f7;
        }}

        .activity-row {{
            min-height: 72px;
            padding: 0 14px;
            border-bottom: 1px solid #ece7f7;
        }}

        .activity-row:last-child {{
            border-bottom: none;
        }}

        .activity-check-wrap {{
            display: flex;
            justify-content: center;
        }}

        .activity-checkbox {{
            width: 20px;
            height: 20px;
            border-radius: 6px;
            border: 2px solid #cbbcf5;
            display: grid;
            place-items: center;
            color: white;
            background: #fff;
            font-size: 14px;
        }}

        .activity-checkbox.selected {{
            border-color: var(--primary);
            background: var(--primary);
        }}

        .activity-code {{
            font-size: 15px;
            font-weight: 600;
            color: #4a4760;
        }}

        .activity-name {{
            font-size: 15px;
            line-height: 1.5;
            color: var(--text);
            padding-right: 10px;
        }}

        .activity-expand {{
            display: flex;
            justify-content: center;
            color: #746f8e;
            font-size: 20px;
        }}

        .activity-star-wrap {{
            display: flex;
            justify-content: center;
        }}

        .activity-star {{
            color: #b8b3cc;
            font-size: 22px;
        }}

        .activity-star.primary {{
            color: var(--primary);
        }}

        .activity-footer {{
            display: flex;
            justify-content: space-between;
            align-items: center;
            gap: 18px;
            margin-top: 20px;
            flex-wrap: wrap;
        }}

        .activity-selected {{
            color: #7a7693;
            font-size: 18px;
        }}

        .activity-selected strong {{
            color: var(--primary);
        }}

        .activity-actions {{
            display: flex;
            gap: 14px;
            flex-wrap: wrap;
        }}

        .activity-btn-back {{
            min-width: 136px;
        }}

        .activity-btn-next {{
            min-width: 150px;
        }}

        .activity-aside {{
            position: sticky;
            top: 100px;
        }}

        .activity-aside-card {{
            background: #f7f2ff;
            border: 1px solid #ece7f7;
            border-radius: 24px;
            padding: 24px;
        }}

        .activity-aside-icon {{
            width: 56px;
            height: 56px;
            border-radius: 999px;
            display: grid;
            place-items: center;
            background: #efe7ff;
            font-size: 24px;
            color: var(--primary);
            margin-bottom: 18px;
        }}

        .activity-aside-card h3 {{
            margin: 0 0 20px;
            font-size: 18px;
            line-height: 1.3;
        }}

        .activity-aside-steps {{
            display: grid;
            gap: 18px;
        }}

        .activity-aside-step {{
            display: grid;
            grid-template-columns: 48px 1fr;
            gap: 14px;
            align-items: start;
        }}

        .activity-aside-step-icon {{
            width: 48px;
            height: 48px;
            border-radius: 999px;
            background: #efe7ff;
            display: grid;
            place-items: center;
            color: var(--primary);
            font-size: 22px;
        }}

        .activity-aside-step strong {{
            display: block;
            margin-bottom: 4px;
            color: var(--primary);
            font-size: 16px;
            line-height: 1.35;
        }}

        .activity-aside-step span {{
            color: var(--muted);
            font-size: 15px;
            line-height: 1.5;
        }}

        .activity-aside-note {{
            margin-top: 22px;
            display: grid;
            grid-template-columns: 34px 1fr;
            gap: 12px;
            padding: 16px 18px;
            background: #f2ebff;
            border-radius: 18px;
            color: #7d6ab3;
            line-height: 1.5;
            font-size: 15px;
        }}

        .activity-aside-note-icon {{
            width: 34px;
            height: 34px;
            border-radius: 999px;
            border: 2px solid var(--primary);
            color: var(--primary);
            display: grid;
            place-items: center;
            font-weight: 700;
        }}

        @media (max-width: 1180px) {{
            .activity-layout {{
            grid-template-columns: 1fr;
            }}

            .activity-aside {{
            position: static;
            }}
        }}

        @media (max-width: 900px) {{
            .activity-card {{
            padding: 22px 18px;
            }}

            .activity-table {{
            overflow-x: auto;
            border-radius: 16px;
            }}

            .activity-table-head,
            .activity-row {{
            min-width: 760px;
            }}

            .activity-aside-card {{
            padding: 20px 18px;
            }}
        }}

        @media (max-width: 720px) {{
            .activity-card {{
            padding: 18px 14px;
            border-radius: 22px;
            }}

            .activity-title {{
            font-size: 20px;
            }}

            .activity-subtitle {{
            font-size: 15px;
            margin-bottom: 16px;
            }}

            .activity-search-input {{
            height: 50px;
            font-size: 14px;
            border-radius: 14px;
            padding-left: 42px;
            }}

            .activity-search-icon {{
            left: 14px;
            font-size: 18px;
            }}

            .activity-hints {{
            font-size: 14px;
            margin-bottom: 16px;
            }}

            .activity-hint {{
            font-size: 14px;
            }}

            .activity-results-title {{
            font-size: 16px;
            gap: 8px;
            }}

            .activity-badge {{
            font-size: 12px;
            height: 24px;
            padding: 0 10px;
            }}

            .activity-table {{
            border-radius: 14px;
            }}

            .activity-table-head,
            .activity-row {{
            min-width: 680px;
            }}

            .activity-footer {{
            flex-direction: column;
            align-items: stretch;
            gap: 14px;
            }}

            .activity-selected {{
            font-size: 16px;
            }}

            .activity-actions {{
            width: 100%;
            flex-direction: column;
            }}

            .activity-actions .btn {{
            width: 100%;
            min-width: 0;
            }}

            .activity-aside-card {{
            padding: 18px 14px;
            border-radius: 20px;
            }}

            .activity-aside-icon {{
            width: 48px;
            height: 48px;
            font-size: 20px;
            margin-bottom: 14px;
            }}

            .activity-aside-card h3 {{
            font-size: 17px;
            margin-bottom: 16px;
            }}

            .activity-aside-step {{
            grid-template-columns: 40px 1fr;
            gap: 10px;
            }}

            .activity-aside-step-icon {{
            width: 40px;
            height: 40px;
            font-size: 18px;
            }}

            .activity-aside-step strong {{
            font-size: 15px;
            }}

            .activity-aside-step span {{
            font-size: 14px;
            }}

            .activity-aside-note {{
            grid-template-columns: 30px 1fr;
            gap: 10px;
            padding: 14px;
            font-size: 14px;
            border-radius: 16px;
            }}

            .activity-aside-note-icon {{
            width: 30px;
            height: 30px;
            font-size: 14px;
            }}
        }}

        @media (max-width: 480px) {{
            .activity-card {{
            padding: 16px 12px;
            }}

            .activity-title {{
            font-size: 18px;
            }}

            .activity-subtitle {{
            font-size: 14px;
            }}

            .activity-search-input {{
            font-size: 13px;
            }}

            .activity-table-head,
            .activity-row {{
            min-width: 620px;
            }}

            .activity-selected {{
            font-size: 15px;
            }}
        }}
        </style>
    """


def render_activity_row(code: str, name: str, selected: bool = False, primary: bool = False) -> str:
    checkbox_class = "activity-checkbox selected" if selected else "activity-checkbox"
    checkbox_mark = "✓" if selected else ""
    star_class = "activity-star primary" if primary else "activity-star"
    star_symbol = "★" if primary else "☆"

    return f"""
    <div class="activity-row">
      <div class="activity-check-wrap">
        <div class="{checkbox_class}">{checkbox_mark}</div>
      </div>
      <div class="activity-code">{code}</div>
      <div class="activity-name">{name}</div>
      <div class="activity-expand">⌄</div>
      <div class="activity-star-wrap">
        <div class="{star_class}">{star_symbol}</div>
      </div>
    </div>
    """