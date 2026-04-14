from pages.ip.step_wrapper import render_ip_step
from pages.ip.step1_personal import get_ip_step1_content
from pages.shared_forms.step_activity import get_activity_content
from pages.shared_forms.step_tax import get_tax_content
from pages.shared_forms.step_account import get_account_content


def ip_step_1():
    content = get_ip_step1_content(substep="basic")
    return render_ip_step(
        step_number=1,
        content_html=content,
        page_title="ИП — шаг 1. Личные данные",
    )


def ip_step_1_passport():
    content = get_ip_step1_content(substep="passport")
    return render_ip_step(
        step_number=1,
        content_html=content,
        page_title="ИП — шаг 1. Паспортные данные",
    )


def ip_step_1_contacts():
    content = get_ip_step1_content(substep="contacts")
    return render_ip_step(
        step_number=1,
        content_html=content,
        page_title="ИП — шаг 1. Контакты и адрес",
    )


def ip_step_2():
    content = get_activity_content(flow="ip")
    return render_ip_step(
        step_number=2,
        content_html=content,
        page_title="ИП — шаг 2. Виды деятельности",
    )


def ip_step_3():
    content = get_tax_content(flow="ip")
    return render_ip_step(
        step_number=3,
        content_html=content,
        page_title="ИП — шаг 3. Режим налогообложения",
    )


def ip_step_4():
    content = get_account_content(flow="ip")
    return render_ip_step(
        step_number=4,
        content_html=content,
        page_title="ИП — шаг 4. Открытие счёта",
    )