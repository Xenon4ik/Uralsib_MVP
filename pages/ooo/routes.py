from pages.ooo.step_wrapper import render_ooo_step
from pages.ooo.step1_naming import get_ooo_step1_content
from pages.ooo.step2_founders import get_ooo_step2_content
from pages.ooo.step3_company import get_ooo_step3_content
from pages.shared_forms.step_activity import get_activity_content
from pages.shared_forms.step_tax import get_tax_content
from pages.shared_forms.step_account import get_account_content


def ooo_step_1():
    content = get_ooo_step1_content()
    return render_ooo_step(
        step_number=1,
        content_html=content,
        page_title="ООО — шаг 1. Наименование компании",
    )


def ooo_step_2():
    content = get_ooo_step2_content()
    return render_ooo_step(
        step_number=2,
        content_html=content,
        page_title="ООО — шаг 2. Учредители",
    )


def ooo_step_3():
    content = get_ooo_step3_content(substep="director")
    return render_ooo_step(
        step_number=3,
        content_html=content,
        page_title="ООО — шаг 3. Данные компании",
    )


def ooo_step_3_charter():
    content = get_ooo_step3_content(substep="charter")
    return render_ooo_step(
        step_number=3,
        content_html=content,
        page_title="ООО — шаг 3. Устав общества",
    )


def ooo_step_3_address():
    content = get_ooo_step3_content(substep="address")
    return render_ooo_step(
        step_number=3,
        content_html=content,
        page_title="ООО — шаг 3. Адрес, капитал и печать",
    )


def ooo_step_4():
    content = get_activity_content(flow="ooo")
    return render_ooo_step(
        step_number=4,
        content_html=content,
        page_title="ООО — шаг 4. Виды деятельности",
    )


def ooo_step_5():
    content = get_tax_content(flow="ooo")
    return render_ooo_step(
        step_number=5,
        content_html=content,
        page_title="ООО — шаг 5. Режим налогообложения",
    )


def ooo_step_6():
    content = get_account_content(flow="ooo")
    return render_ooo_step(
        step_number=6,
        content_html=content,
        page_title="ООО — шаг 6. Открытие счёта",
    )