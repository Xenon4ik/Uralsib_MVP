from pages.shared_forms.layout import render_form_page
from pages.shared_forms.progress import render_ip_progress


def render_ip_step(
    step_number: int,
    content_html: str,
    page_title: str | None = None,
) -> str:
    progress_html = render_ip_progress(step_number)

    return render_form_page(
        title="Форма ИП",
        subtitle="",
        progress_html=progress_html,
        content_html=content_html,
        page_title=page_title or f"ИП — шаг {step_number}",
    )