from flask import url_for


def get_activity_content(flow: str = "ip") -> str:
    if flow == "ooo":
        back_url = url_for("ooo_form_step_3")
        next_url = url_for("ooo_form_step_4")
        flow_type = "ooo"
    else:
        back_url = url_for("ip_form_step_1_contacts")
        next_url = url_for("ip_form_step_2")    
        flow_type = "ip"

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
              id="okved-search-input"
              class="activity-search-input"
              type="text"
              placeholder="Например: розничная торговля одеждой, ремонт телефонов, фотоуслуги"
              autocomplete="off"
            />
          </div>

          <div class="activity-hints">
            <span>Например:</span>
            <button type="button" class="activity-hint" data-query="доставка еды">доставка еды</button>
            <button type="button" class="activity-hint" data-query="интернет-магазин">интернет-магазин</button>
            <button type="button" class="activity-hint" data-query="ремонт автомобилей">ремонт автомобилей</button>
          </div>

          <div class="activity-results-head">
            <div class="activity-results-title">
              Подходящие виды деятельности
              <span id="results-badge" class="activity-badge">Введите запрос</span>
            </div>
          </div>

          <div class="activity-table" id="activity-table-container">
            <div class="activity-table-head">
              <div>Выбрать</div>
              <div>Код ОКВЭД</div>
              <div>Наименование вида деятельности</div>
              <div></div>
            </div>
            <div id="search-results-container">
              <div class="activity-row">
                <div class="activity-check-wrap"></div>
                <div class="activity-code"></div>
                <div class="activity-name" style="color: #9a98ab; text-align: center; padding: 20px 0;">
                  Введите запрос для поиска ОКВЭД
                </div>
                <div class="activity-expand"></div>
              </div>
            </div>
          </div>

          <!-- Секция выбранных ОКВЭДов -->
          <div id="selected-section" style="margin-top: 24px; display: none;">
            <div class="activity-results-head">
              <div class="activity-results-title">
                Выбранные виды деятельности
                <span id="selected-badge" class="activity-badge">0</span>
              </div>
            </div>
            
            <div class="activity-table">
              <div class="activity-table-head">
                <div>Основной</div>
                <div>Код ОКВЭД</div>
                <div>Наименование вида деятельности</div>
                <div>Удалить</div>
              </div>
              <div id="selected-results-container">
              </div>
            </div>
            
            <div id="main-hint" style="margin-top: 12px; padding: 10px 16px; background: #fff9e6; border-radius: 8px; color: #b8860b; font-size: 14px; display: none;">
              ⭐ Нажмите на звёздочку, чтобы выбрать основной вид деятельности
            </div>
          </div>

          <div class="activity-footer">
            <div class="activity-selected">
              Выбрано: <strong id="selected-count">0</strong>
            </div>

            <div class="activity-actions">
              <a href="{back_url}" class="btn btn-secondary activity-btn-back">Назад</a>
              <button id="next-step-btn" class="btn btn-primary activity-btn-next" disabled>Далее</button>
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
              <div class="activity-aside-step-icon">☑</div>
              <div>
                <strong>Выберите подходящее</strong>
                <span>Отметьте один или несколько видов деятельности</span>
              </div>
            </div>

            <div class="activity-aside-step">
              <div class="activity-aside-step-icon">⭐</div>
              <div>
                <strong>Укажите основной</strong>
                <span>В списке выбранных нажмите на звёздочку</span>
              </div>
            </div>
          </div>

          <div class="activity-aside-note">
            <div class="activity-aside-note-icon">i</div>
            <div>Основной вид деятельности — тот, который приносит наибольший доход.</div>
          </div>
        </div>
      </aside>
    </section>

    <!-- Скрытая форма для отправки данных -->
    <form id="okved-form" method="POST" action="{next_url}" style="display: none;">
      <input type="hidden" name="flow_type" value="{flow_type}">
      <div id="form-hidden-inputs"></div>
    </form>

    <style>
        {get_styles()}
        
        .activity-checkbox {{
            cursor: pointer;
            transition: all 0.2s ease;
        }}
        
        .activity-checkbox:hover {{
            border-color: var(--primary);
        }}
        
        .activity-hint {{
            transition: all 0.2s ease;
            cursor: pointer;
        }}
        
        .activity-hint:hover {{
            color: #6b3fd4;
            text-decoration: underline;
        }}
        
        #next-step-btn:disabled {{
            opacity: 0.5;
            cursor: not-allowed;
        }}
        
        .loading-message {{
            text-align: center;
            padding: 30px !important;
            color: var(--muted);
        }}
        
        .activity-row {{
            transition: background 0.15s ease;
        }}
        
        .activity-expand {{
            cursor: pointer;
            user-select: none;
        }}
        
        .main-star {{
            cursor: pointer;
            font-size: 22px;
            color: #b8b3cc;
            transition: all 0.2s ease;
            text-align: center;
        }}
        
        .main-star:hover {{
            transform: scale(1.2);
        }}
        
        .main-star.primary {{
            color: var(--primary);
        }}
        
        .remove-btn {{
            cursor: pointer;
            color: #dc3545;
            font-size: 20px;
            font-weight: bold;
            text-align: center;
            transition: all 0.2s ease;
        }}
        
        .remove-btn:hover {{
            color: #a71d2a;
            transform: scale(1.1);
        }}
        
        /* Обновлённые колонки для таблицы поиска */
        .activity-table .activity-table-head,
        .activity-table .activity-row {{
            display: grid;
            grid-template-columns: 72px 110px minmax(320px, 1fr) 56px;
            align-items: center;
        }}
        
        /* Колонки для таблицы выбранных */
        #selected-section .activity-table .activity-table-head,
        #selected-section .activity-table .activity-row {{
            display: grid;
            grid-template-columns: 92px 110px minmax(320px, 1fr) 80px;
            align-items: center;
        }}
    </style>

    <script>
        let selectedOkveds = new Map();
        let mainOkvedCode = null;
        let currentSearchResults = [];
        let debounceTimer = null;
        
        const searchInput = document.getElementById('okved-search-input');
        const resultsContainer = document.getElementById('search-results-container');
        const resultsBadge = document.getElementById('results-badge');
        const selectedCountEl = document.getElementById('selected-count');
        const nextBtn = document.getElementById('next-step-btn');
        const formHiddenInputs = document.getElementById('form-hidden-inputs');
        const okvedForm = document.getElementById('okved-form');
        const selectedSection = document.getElementById('selected-section');
        const selectedResultsContainer = document.getElementById('selected-results-container');
        const selectedBadge = document.getElementById('selected-badge');
        const mainHint = document.getElementById('main-hint');
        
        async function searchOkved(query) {{
            if (!query || query.length < 2) {{
                resultsContainer.innerHTML = `
                    <div class="activity-row">
                        <div class="activity-check-wrap"></div>
                        <div class="activity-code"></div>
                        <div class="activity-name loading-message">
                            ${{query ? 'Введите минимум 2 символа' : 'Введите запрос для поиска ОКВЭД'}}
                        </div>
                        <div class="activity-expand"></div>
                    </div>
                `;
                resultsBadge.textContent = 'Введите запрос';
                return;
            }}
            
            resultsContainer.innerHTML = `
                <div class="activity-row">
                    <div class="activity-check-wrap"></div>
                    <div class="activity-code"></div>
                    <div class="activity-name loading-message">Поиск...</div>
                    <div class="activity-expand"></div>
                </div>
            `;
            
            try {{
                const response = await fetch(`/api/search_okved?q=${{encodeURIComponent(query)}}`);
                const data = await response.json();
                currentSearchResults = data;
                
                if (data.length === 0) {{
                    resultsContainer.innerHTML = `
                        <div class="activity-row">
                            <div class="activity-check-wrap"></div>
                            <div class="activity-code"></div>
                            <div class="activity-name loading-message">Ничего не найдено</div>
                            <div class="activity-expand"></div>
                        </div>
                    `;
                    resultsBadge.textContent = 'Ничего не найдено';
                }} else {{
                    renderSearchResults(data);
                    resultsBadge.textContent = `Найдено ${{data.length}} вариантов`;
                }}
            }} catch (error) {{
                console.error('Ошибка поиска:', error);
                resultsContainer.innerHTML = `
                    <div class="activity-row">
                        <div class="activity-check-wrap"></div>
                        <div class="activity-code"></div>
                        <div class="activity-name loading-message">Ошибка при поиске</div>
                        <div class="activity-expand"></div>
                    </div>
                `;
                resultsBadge.textContent = 'Ошибка';
            }}
        }}
        
        function renderSearchResults(results) {{
            let html = '';
            
            results.forEach(item => {{
                const isSelected = selectedOkveds.has(item.code);
                const checkboxClass = isSelected ? 'activity-checkbox selected' : 'activity-checkbox';
                const checkboxMark = isSelected ? '✓' : '';
                
                html += `
                    <div class="activity-row" data-code="${{item.code}}">
                        <div class="activity-check-wrap">
                            <div class="${{checkboxClass}}" onclick="toggleOkved('${{item.code}}', '${{escapeJs(item.name)}}')">${{checkboxMark}}</div>
                        </div>
                        <div class="activity-code">${{item.code}}</div>
                        <div class="activity-name">${{escapeHtml(item.name)}}</div>
                        <div class="activity-expand" onclick="toggleDetails(this)">⌄</div>
                    </div>
                `;
            }});
            
            resultsContainer.innerHTML = html;
        }}
        
        function renderSelectedOkveds() {{
            const count = selectedOkveds.size;
            
            if (count === 0) {{
                selectedSection.style.display = 'none';
                return;
            }}
            
            selectedSection.style.display = 'block';
            selectedBadge.textContent = count;
            
            let html = '';
            const sortedItems = Array.from(selectedOkveds.values()).sort((a, b) => a.code.localeCompare(b.code));
            
            sortedItems.forEach(item => {{
                const isMain = mainOkvedCode === item.code;
                const starClass = isMain ? 'main-star primary' : 'main-star';
                const starSymbol = isMain ? '★' : '☆';
                
                html += `
                    <div class="activity-row" data-code="${{item.code}}">
                        <div class="${{starClass}}" onclick="setMainOkved('${{item.code}}')">${{starSymbol}}</div>
                        <div class="activity-code">${{item.code}}</div>
                        <div class="activity-name">${{escapeHtml(item.name)}}</div>
                        <div class="remove-btn" onclick="removeOkved('${{item.code}}')">✕</div>
                    </div>
                `;
            }});
            
            selectedResultsContainer.innerHTML = html;
            
            // Показываем подсказку если нет основного
            if (!mainOkvedCode) {{
                mainHint.style.display = 'block';
            }} else {{
                mainHint.style.display = 'none';
            }}
        }}
        
        function toggleOkved(code, name) {{
            if (selectedOkveds.has(code)) {{
                selectedOkveds.delete(code);
                if (mainOkvedCode === code) {{
                    mainOkvedCode = null;
                }}
            }} else {{
                selectedOkveds.set(code, {{code, name}});
            }}
            
            updateUI();
        }}
        
        function removeOkved(code) {{
            selectedOkveds.delete(code);
            if (mainOkvedCode === code) {{
                mainOkvedCode = null;
            }}
            updateUI();
        }}
        
        function setMainOkved(code) {{
            if (!selectedOkveds.has(code)) return;
            mainOkvedCode = code;
            updateUI();
        }}
        
        function updateUI() {{
            const count = selectedOkveds.size;
            selectedCountEl.textContent = count;
            
            // Обновляем кнопку Далее
            nextBtn.disabled = count === 0 || !mainOkvedCode;
            
            // Обновляем таблицу поиска
            if (currentSearchResults.length > 0) {{
                let html = '';
                currentSearchResults.forEach(item => {{
                    const isSelected = selectedOkveds.has(item.code);
                    const checkboxClass = isSelected ? 'activity-checkbox selected' : 'activity-checkbox';
                    const checkboxMark = isSelected ? '✓' : '';
                    
                    html += `
                        <div class="activity-row" data-code="${{item.code}}">
                            <div class="activity-check-wrap">
                                <div class="${{checkboxClass}}" onclick="toggleOkved('${{item.code}}', '${{escapeJs(item.name)}}')">${{checkboxMark}}</div>
                            </div>
                            <div class="activity-code">${{item.code}}</div>
                            <div class="activity-name">${{escapeHtml(item.name)}}</div>
                            <div class="activity-expand" onclick="toggleDetails(this)">⌄</div>
                        </div>
                    `;
                }});
                resultsContainer.innerHTML = html;
            }}
            
            // Обновляем секцию выбранных
            renderSelectedOkveds();
            
            // Обновляем скрытые поля
            updateHiddenInputs();
        }}
        
        function updateHiddenInputs() {{
            let html = '';
            const sortedItems = Array.from(selectedOkveds.values()).sort((a, b) => a.code.localeCompare(b.code));
            
            sortedItems.forEach((item) => {{
                html += `<input type="hidden" name="okved_codes[]" value="${{item.code}}">`;
                html += `<input type="hidden" name="okved_names[]" value="${{escapeHtml(item.name)}}">`;
            }});
            
            html += `<input type="hidden" name="main_okved_code" value="${{mainOkvedCode || ''}}">`;
            formHiddenInputs.innerHTML = html;
        }}
        
        function toggleDetails(element) {{
            const row = element.closest('.activity-row');
            const code = row.querySelector('.activity-code').textContent;
            console.log('Детали для', code);
        }}
        
        function escapeHtml(text) {{
            const div = document.createElement('div');
            div.textContent = text;
            return div.innerHTML;
        }}
        
        function escapeJs(text) {{
            return text.replace(/'/g, "\\'").replace(/"/g, '\\"');
        }}
        
        document.addEventListener('DOMContentLoaded', function() {{
            searchInput.addEventListener('input', function() {{
                clearTimeout(debounceTimer);
                debounceTimer = setTimeout(() => {{
                    searchOkved(this.value.trim());
                }}, 300);
            }});
            
            document.querySelectorAll('.activity-hint').forEach(hint => {{
                hint.addEventListener('click', function() {{
                    const query = this.dataset.query;
                    searchInput.value = query;
                    searchOkved(query);
                }});
            }});
            
            nextBtn.addEventListener('click', function(e) {{
                e.preventDefault();
                if (!nextBtn.disabled) {{
                    okvedForm.submit();
                }}
            }});
            
            loadPreSelectedData();
        }});
        
        async function loadPreSelectedData() {{
            const flowType = '{flow_type}';
            
            try {{
                const response = await fetch(`/api/get_saved_okveds?flow=${{flowType}}`);
                if (!response.ok) return;
                
                const data = await response.json();
                if (data.codes && data.codes.length > 0) {{
                    for (let i = 0; i < data.codes.length; i++) {{
                        selectedOkveds.set(data.codes[i], {{
                            code: data.codes[i],
                            name: data.names[i]
                        }});
                    }}
                    
                    mainOkvedCode = data.main_code;
                    updateUI();
                    resultsBadge.textContent = `Загружено ${{data.codes.length}} сохранённых ОКВЭД`;
                }}
            }} catch (error) {{
                console.error('Ошибка загрузки сохранённых данных:', error);
            }}
        }}
        
        window.toggleOkved = toggleOkved;
        window.removeOkved = removeOkved;
        window.setMainOkved = setMainOkved;
        window.toggleDetails = toggleDetails;
    </script>
    """


def get_styles() -> str:
    return """
        .activity-layout {
            display: grid;
            grid-template-columns: minmax(0, 1fr) 340px;
            gap: 24px;
            align-items: start;
        }
        .activity-main { min-width: 0; }
        .activity-card {
            background: #ffffff;
            border: 1px solid var(--border);
            border-radius: 28px;
            padding: 30px 28px 22px;
            box-shadow: var(--shadow);
        }
        .activity-title { margin: 0 0 10px; font-size: 22px; line-height: 1.2; }
        .activity-subtitle { margin: 0 0 18px; color: var(--muted); font-size: 16px; line-height: 1.6; max-width: 760px; }
        .activity-search-wrap { position: relative; margin-bottom: 14px; }
        .activity-search-icon { position: absolute; left: 16px; top: 50%; transform: translateY(-50%); color: #8f8ca5; font-size: 20px; }
        .activity-search-input {
            width: 100%; height: 56px; border-radius: 16px; border: 2px solid #8c66f0;
            background: #fff; padding: 0 18px 0 48px; font-size: 16px; outline: none;
        }
        .activity-search-input::placeholder { color: #9a98ab; }
        .activity-hints { display: flex; align-items: center; flex-wrap: wrap; gap: 8px; margin-bottom: 20px; color: var(--muted); font-size: 15px; }
        .activity-hint { background: none; border: none; padding: 0; color: var(--primary); font-size: 15px; font-weight: 600; cursor: pointer; }
        .activity-results-head { margin-bottom: 10px; }
        .activity-results-title { display: flex; align-items: center; gap: 12px; flex-wrap: wrap; font-size: 18px; font-weight: 700; color: var(--text); }
        .activity-badge { display: inline-flex; align-items: center; justify-content: center; height: 28px; padding: 0 12px; border-radius: 999px; background: #efe7ff; color: var(--primary); font-size: 13px; font-weight: 700; }
        .activity-table { border: 1px solid #e6e1f2; border-radius: 18px; overflow: hidden; background: #fff; }
        .activity-table-head { min-height: 48px; padding: 0 14px; background: #ffffff; color: #7e7b91; font-size: 14px; font-weight: 600; border-bottom: 1px solid #ece7f7; }
        .activity-row { min-height: 72px; padding: 0 14px; border-bottom: 1px solid #ece7f7; }
        .activity-row:last-child { border-bottom: none; }
        .activity-check-wrap { display: flex; justify-content: center; }
        .activity-checkbox { width: 20px; height: 20px; border-radius: 6px; border: 2px solid #cbbcf5; display: grid; place-items: center; color: white; background: #fff; font-size: 14px; }
        .activity-checkbox.selected { border-color: var(--primary); background: var(--primary); }
        .activity-code { font-size: 15px; font-weight: 600; color: #4a4760; }
        .activity-name { font-size: 15px; line-height: 1.5; color: var(--text); padding-right: 10px; }
        .activity-expand { display: flex; justify-content: center; color: #746f8e; font-size: 20px; }
        .activity-footer { display: flex; justify-content: space-between; align-items: center; gap: 18px; margin-top: 20px; flex-wrap: wrap; }
        .activity-selected { color: #7a7693; font-size: 18px; }
        .activity-selected strong { color: var(--primary); }
        .activity-actions { display: flex; gap: 14px; flex-wrap: wrap; }
        .activity-btn-back { min-width: 136px; }
        .activity-btn-next { min-width: 150px; }
        .activity-aside { position: sticky; top: 100px; }
        .activity-aside-card { background: #f7f2ff; border: 1px solid #ece7f7; border-radius: 24px; padding: 24px; }
        .activity-aside-icon { width: 56px; height: 56px; border-radius: 999px; display: grid; place-items: center; background: #efe7ff; font-size: 24px; color: var(--primary); margin-bottom: 18px; }
        .activity-aside-card h3 { margin: 0 0 20px; font-size: 18px; line-height: 1.3; }
        .activity-aside-steps { display: grid; gap: 18px; }
        .activity-aside-step { display: grid; grid-template-columns: 48px 1fr; gap: 14px; align-items: start; }
        .activity-aside-step-icon { width: 48px; height: 48px; border-radius: 999px; background: #efe7ff; display: grid; place-items: center; color: var(--primary); font-size: 22px; }
        .activity-aside-step strong { display: block; margin-bottom: 4px; color: var(--primary); font-size: 16px; line-height: 1.35; }
        .activity-aside-step span { color: var(--muted); font-size: 15px; line-height: 1.5; }
        .activity-aside-note { margin-top: 22px; display: grid; grid-template-columns: 34px 1fr; gap: 12px; padding: 16px 18px; background: #f2ebff; border-radius: 18px; color: #7d6ab3; line-height: 1.5; font-size: 15px; }
        .activity-aside-note-icon { width: 34px; height: 34px; border-radius: 999px; border: 2px solid var(--primary); color: var(--primary); display: grid; place-items: center; font-weight: 700; }
        @media (max-width: 1180px) { .activity-layout { grid-template-columns: 1fr; } .activity-aside { position: static; } }
        @media (max-width: 900px) {
            .activity-card { padding: 22px 18px; }
            .activity-table { overflow-x: auto; border-radius: 16px; }
            .activity-table-head, .activity-row { min-width: 680px; }
            .activity-aside-card { padding: 20px 18px; }
        }
        @media (max-width: 720px) {
            .activity-card { padding: 18px 14px; border-radius: 22px; }
            .activity-title { font-size: 20px; }
            .activity-subtitle { font-size: 15px; margin-bottom: 16px; }
            .activity-search-input { height: 50px; font-size: 14px; border-radius: 14px; padding-left: 42px; }
            .activity-search-icon { left: 14px; font-size: 18px; }
            .activity-footer { flex-direction: column; align-items: stretch; gap: 14px; }
            .activity-selected { font-size: 16px; }
            .activity-actions { width: 100%; flex-direction: column; }
            .activity-actions .btn { width: 100%; min-width: 0; }
        }
    """