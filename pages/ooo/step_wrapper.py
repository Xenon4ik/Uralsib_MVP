from pages.shared_forms.layout import render_form_page
from pages.shared_forms.progress import render_ooo_progress


def render_ooo_step(
    step_number: int,
    content_html: str,
    page_title: str | None = None,
) -> str:
    progress_html = render_ooo_progress(step_number)

    return render_form_page(
        title="Форма ООО",
        subtitle="",
        progress_html=progress_html,
        content_html=content_html,
        page_title=page_title or f"ООО — шаг {step_number}",
    )