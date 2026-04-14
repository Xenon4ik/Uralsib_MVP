# Uralsib_MVP
MVP решения по повышению конверсии сервиса онлайн-регистрации бизнеса

Логика:

main.py
— только Flask app и маршруты верхнего уровня.

styles.py
— один общий BASE_STYLES.

pages/common.py
— общий header, footer, возможно общие helper-функции.

pages/landing.py
— лендинг.

pages/auth.py
— login и register.

pages/shared_forms/layout.py
— общий шаблон страницы формы.

pages/shared_forms/progress.py
— прогресс-бары для ИП и ООО.

pages/shared_forms/step_activity.py
— общий шаг “Виды деятельности / ОКВЭД”.
Используется:
	•	ИП шаг 2
	•	ООО шаг 4

pages/shared_forms/step_tax.py
— общий шаг “Режим налогообложения”.
Используется:
	•	ИП шаг 3
	•	ООО шаг 5

pages/shared_forms/step_account.py
— общий шаг “Открытие счёта”.
Используется:
	•	ИП шаг 4
	•	ООО шаг 6

pages/ip/step1_personal.py
— уникальный первый шаг ИП.

pages/ooo/step1_naming.py
— уникальный первый шаг ООО.

pages/ooo/step2_founders.py
— уникальный второй шаг ООО.

pages/ooo/step3_company.py
— уникальный третий шаг ООО.
