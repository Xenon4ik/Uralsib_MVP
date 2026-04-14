def _render_step_items(steps: list[str], current_step: int) -> str:
    items = []

    for index, label in enumerate(steps, start=1):
        active_class = " active" if index == current_step else ""
        done_class = " done" if index < current_step else ""

        items.append(
            f"""
            <div class="progress-step{active_class}{done_class}">
              <div class="progress-step-top">
                <div class="progress-step-circle">{index}</div>
                <div class="progress-step-label">{label}</div>
              </div>
              <div class="progress-step-line"></div>
            </div>
            """
        )

    return "".join(items)


def render_progress_block(
    title: str,
    subtitle: str,
    steps: list[str],
    current_step: int,
) -> str:
    steps_html = _render_step_items(steps, current_step)

    return f"""
    <section class="progress-block">
      <div class="progress-copy">
        <h1 class="progress-title">{title}</h1>
        <p class="progress-subtitle">{subtitle}</p>
      </div>

      <div class="progress-steps">
        {steps_html}
      </div>
    </section>

    <style>
      .progress-block {{
        display: grid;
        gap: 22px;
      }}

      .progress-title {{
        margin: 0 0 8px;
        font-size: 34px;
        line-height: 1.15;
        letter-spacing: -0.02em;
      }}

      .progress-subtitle {{
        margin: 0;
        color: var(--muted);
        font-size: 18px;
        line-height: 1.6;
      }}

      .progress-steps {{
        display: grid;
        grid-template-columns: repeat({len(steps)}, minmax(0, 1fr));
        gap: 8px;
        align-items: start;
      }}

      .progress-step {{
        display: grid;
        gap: 14px;
      }}

      .progress-step-top {{
        display: flex;
        align-items: center;
        gap: 14px;
      }}

      .progress-step-circle {{
        width: 44px;
        height: 44px;
        border-radius: 999px;
        border: 2px solid #d9d6e6;
        color: #7c7a8f;
        display: grid;
        place-items: center;
        font-weight: 700;
        font-size: 22px;
        background: #fff;
        flex: 0 0 44px;
      }}

      .progress-step-label {{
        font-size: 16px;
        line-height: 1.35;
        color: #7c7a8f;
        font-weight: 500;
      }}

      .progress-step-line {{
        height: 8px;
        border-radius: 999px;
        background: #e8e4f3;
      }}

      .progress-step.active .progress-step-circle,
      .progress-step.done .progress-step-circle {{
        border-color: var(--primary);
        color: var(--primary);
      }}

      .progress-step.active .progress-step-label,
      .progress-step.done .progress-step-label {{
        color: var(--primary);
        font-weight: 700;
      }}

      .progress-step.active .progress-step-line,
      .progress-step.done .progress-step-line {{
        background: var(--primary);
      }}

      .subprogress {{
        display: flex;
        align-items: center;
        justify-content: center;
        gap: 28px;
        margin-top: 6px;
      }}

      .subprogress-item {{
        display: flex;
        align-items: center;
        gap: 14px;
        color: #7c7a8f;
      }}

      .subprogress-dot {{
        width: 34px;
        height: 34px;
        border-radius: 999px;
        border: 2px solid #d9d6e6;
        display: grid;
        place-items: center;
        font-size: 18px;
        font-weight: 700;
        background: #fff;
        color: #7c7a8f;
        flex: 0 0 34px;
      }}

      .subprogress-label {{
        font-size: 16px;
        line-height: 1.35;
        font-weight: 500;
      }}

      .subprogress-sep {{
        width: 70px;
        height: 2px;
        background: #d9d6e6;
        border-radius: 999px;
      }}

      .subprogress-item.active .subprogress-dot,
      .subprogress-item.done .subprogress-dot {{
        border-color: var(--primary);
        color: var(--primary);
      }}

      .subprogress-item.active .subprogress-label,
      .subprogress-item.done .subprogress-label {{
        color: var(--primary);
        font-weight: 700;
      }}

      @media (max-width: 1100px) {{
        .subprogress {{
          justify-content: flex-start;
          overflow-x: auto;
          padding-bottom: 4px;
        }}
      }}

      @media (max-width: 900px) {{
        .progress-steps {{
          grid-template-columns: 1fr;
        }}

        .progress-step-line {{
          display: none;
        }}
      }}
    </style>
    """


def render_subprogress_block(steps: list[str], current_step: int) -> str:
    html_parts = []

    for index, label in enumerate(steps, start=1):
        active_class = " active" if index == current_step else ""
        done_class = " done" if index < current_step else ""

        html_parts.append(
            f"""
            <div class="subprogress-item{active_class}{done_class}">
              <div class="subprogress-dot">{index}</div>
              <div class="subprogress-label">{label}</div>
            </div>
            """
        )

        if index != len(steps):
            html_parts.append('<div class="subprogress-sep"></div>')

    return f"""
    <div class="subprogress">
      {''.join(html_parts)}
    </div>
    """


def render_ip_progress(current_step: int) -> str:
    steps = [
        "Личные данные",
        "Виды деятельности",
        "Режим налогообложения",
        "Открытие счёта",
    ]
    return render_progress_block(
        title=f"Шаг {current_step} из 4. " + steps[current_step - 1],
        subtitle="Начнём с основной информации. Это займет не больше пары минут.",
        steps=steps,
        current_step=current_step,
    )


def render_ooo_progress(current_step: int) -> str:
    steps = [
        "Наименование",
        "Учредители",
        "Данные компании",
        "Виды деятельности",
        "Режим налогообложения",
        "Открытие счёта",
    ]
    return render_progress_block(
        title=f"Шаг {current_step} из 6. " + steps[current_step - 1],
        subtitle="Заполняйте шаги по очереди — мы подскажем, что делать дальше.",
        steps=steps,
        current_step=current_step,
    )