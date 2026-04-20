# Uralsib_MVP
MVP решения по повышению конверсии сервиса онлайн-регистрации бизнеса

Проект: Uralsib_MVP

Структура проекта организована по принципу:
- main.py только запускает Flask и подключает маршруты
- styles.py хранит общие стили
- pages/ содержит все страницы и сценарии
- shared_forms/ содержит переиспользуемые части форм
- ip/ и ooo/ содержат уникальные шаги сценариев ИП и ООО
- src/ хранит изображения и статические ассеты

Файловая структура

Uralsib_MVP/
├── main.py
├── styles.py
├── requirements.txt
├── Procfile
├── src/
│   ├── logo.png
│   ├── logo2.png
│   ├── rocket.png
│   ├── icon1.png
│   ├── icon2.png
│   ├── icon3.png
│   ├── bag.png
│   ├── building.png
│   ├── big_circle.png
│   ├── naushniki.png
│   └── ...
└── pages/
    ├── __init__.py
    ├── common.py
    ├── landing.py
    ├── auth.py
    ├── shared_forms/
    │   ├── __init__.py
    │   ├── layout.py
    │   ├── progress.py
    │   ├── step_activity.py
    │   ├── step_tax.py
    │   └── step_account.py
    ├── ip/
    │   ├── __init__.py
    │   ├── routes.py
    │   ├── step_wrapper.py
    │   └── step1_personal.py
    └── ooo/
        ├── __init__.py
        ├── common.py
        ├── routes.py
        ├── step_wrapper.py
        ├── step1_naming.py
        ├── step2_founders.py
        └── step3_company.py


Описание файлов

1. Корневые файлы

main.py
Главная точка входа в приложение.
Что делает:
- создает Flask app
- настраивает маршрут для раздачи картинок из src/
- подключает все маршруты лендинга, auth, ИП и ООО
- запускает приложение

styles.py
Файл с общими стилями проекта.
Что хранит:
- BASE_STYLES
- глобальные цвета, кнопки, header, footer, общие секции
- базовую адаптивность
- если стиль используется во многих страницах, он должен быть здесь
- стили конкретного шага формы допускается держать внутри соответствующего файла шага

requirements.txt
Список Python-зависимостей проекта.
Минимально:
- Flask
- gunicorn

Procfile
Команда запуска для Render.
Обычно:
gunicorn main:app


2. Папка src/

src/
Папка со всеми изображениями и визуальными ассетами проекта.

3. Папка pages/

pages/ — основной каталог страниц и сценариев.

pages/common.py
Общие элементы обычных страниц, не относящихся к формам.
Что может содержать:
- обычный header лендинга
- footer лендинга
- общие helper-функции для простых страниц

Используется в:
- landing.py
- auth.py
- других неформовых страницах

pages/landing.py
Лендинг проекта.
Что содержит:
- hero-секцию
- выбор ИП/ООО
- секцию шагов
- секцию преимуществ
- final CTA
- footer

pages/auth.py
Страницы, связанные с авторизацией и стартом сценария.
Например:
- login page
- register page
- старт новой заявки


4. Папка pages/shared_forms/

Это общие компоненты форм, которые используются и в ИП, и в ООО.

pages/shared_forms/layout.py
Общий layout для всех форм.
Что содержит:
- form-header с кнопкой “Личный кабинет”
- form-footer
- общую обертку страницы формы
- функцию render_form_page(...)

Задача:
собрать страницу формы из:
- page_title
- верхнего progress bar
- основного content_html
- общих header/footer

pages/shared_forms/progress.py
Общие progress bar-компоненты.
Что содержит:
- render_ip_progress(step_number)
- render_ooo_progress(step_number)
- render_subprogress_block(items, current_step)

Используется для:
- верхнего прогресс-бара формы
- внутреннего подпрогресса, если шаг разбит на подшаги

pages/shared_forms/step_activity.py
Общий шаг выбора ОКВЭД.
Используется в:
- ИП шаг 2
- ООО шаг 4

Что содержит:
- поиск по ключевым словам
- таблицу/список предложенных ОКВЭД
- sidebar “Как это работает?”
- кнопки назад/далее

Важно:
- если меняется логика ОКВЭД для обеих форм, менять нужно здесь

pages/shared_forms/step_tax.py
Общий шаг выбора режима налогообложения.
Используется в:
- ИП шаг 3
- ООО шаг 5

Что содержит:
- карточки режимов налогообложения
- блок-подсказку справа
- кнопки назад/далее
- для ИП может показываться дополнительный блок ПСН
- для ООО блок ПСН не показывается

pages/shared_forms/step_account.py
Общий шаг открытия счета.
Используется в:
- ИП шаг 4
- ООО шаг 6

Что содержит:
- форму заявки на расчетный счет
- правый блок “Что дальше?”
- кнопки сохранить/назад/завершить


5. Папка pages/ip/

Все, что относится только к сценарию ИП.

pages/ip/routes.py
Маршруты шагов формы ИП.
Что содержит:
- функции ip_step_1()
- ip_step_1_passport()
- ip_step_1_contacts()
- ip_step_2()
- ip_step_3()
- ip_step_4()

Задача:
- получить HTML конкретного шага
- передать его в render_ip_step(...)

pages/ip/step_wrapper.py
Обертка шагов ИП.
Что делает:
- подставляет progress bar для ИП
- вызывает общий layout форм
- собирает готовую страницу шага

Обычно содержит:
- render_ip_step(step_number, content_html, page_title)

pages/ip/step1_personal.py
Первый шаг ИП — персональные данные.
Что содержит:
- три подшага:
  1. основная информация
  2. паспортные данные
  3. контакты и адрес
- подпрогресс-бар внутри первого шага


6. Папка pages/ooo/

Все, что относится только к сценарию ООО.

pages/ooo/common.py
Общие helper-функции для шагов ООО.
Например:
- render_ooo_save_button()

Используется, чтобы одинаковые элементы не дублировать по всем шагам.

pages/ooo/routes.py
Маршруты шагов формы ООО.
Что содержит:
- ooo_step_1()
- ooo_step_2()
- ooo_step_3()
- ooo_step_3_charter()
- ooo_step_3_address()
- ooo_step_4()
- ooo_step_5()
- ooo_step_6()

Задача:
- собрать нужный шаг ООО
- передать HTML в render_ooo_step(...)

pages/ooo/step_wrapper.py
Обертка шагов ООО.
Что делает:
- подставляет progress bar для ООО
- вызывает общий layout форм
- собирает готовую страницу шага

pages/ooo/step1_naming.py
Шаг 1 формы ООО.
Что содержит:
- ввод сокращенного названия
- ввод полного названия
- подсказки по неймингу
- sidebar с рекомендациями
- email для ЕГРЮЛ
- checkbox бумажных документов

pages/ooo/step2_founders.py
Шаг 2 формы ООО.
Что содержит:
- выбор количества учредителей
- данные учредителя
- паспортные данные
- адрес регистрации
- контактную информацию
- sidebar с пояснениями по учредителям

pages/ooo/step3_company.py
Шаг 3 формы ООО.
Что содержит:
- внутренний подпрогресс
- 3 подшага:
  1. руководитель
  2. устав
  3. адрес, капитал и печать


Логика переиспользования шагов

ИП
- шаг 1: уникальный → pages/ip/step1_personal.py
- шаг 2: общий → pages/shared_forms/step_activity.py
- шаг 3: общий → pages/shared_forms/step_tax.py
- шаг 4: общий → pages/shared_forms/step_account.py

ООО
- шаг 1: уникальный → pages/ooo/step1_naming.py
- шаг 2: уникальный → pages/ooo/step2_founders.py
- шаг 3: уникальный → pages/ooo/step3_company.py
- шаг 4: общий → pages/shared_forms/step_activity.py
- шаг 5: общий → pages/shared_forms/step_tax.py
- шаг 6: общий → pages/shared_forms/step_account.py


Что менять в типовых случаях

Если нужно поменять хедер формы
→ pages/shared_forms/layout.py

Если нужно поменять общий прогресс бар
→ pages/shared_forms/progress.py

Если нужно поменять шаг ОКВЭД у ИП и ООО сразу
→ pages/shared_forms/step_activity.py

Если нужно поменять шаг налогообложения у ИП и ООО сразу
→ pages/shared_forms/step_tax.py

Если нужно поменять шаг открытия счета у ИП и ООО сразу
→ pages/shared_forms/step_account.py

Если нужно поменять только первый шаг ИП
→ pages/ip/step1_personal.py

Если нужно поменять только первый шаг ООО
→ pages/ooo/step1_naming.py

Если нужно поменять только второй шаг ООО
→ pages/ooo/step2_founders.py

Если нужно поменять только третий шаг ООО
→ pages/ooo/step3_company.py
