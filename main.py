from flask import Flask, render_template_string, url_for, send_from_directory, request, jsonify, session, redirect
from pathlib import Path
import os

BASE_DIR = Path(__file__).resolve().parent
SRC_DIR = BASE_DIR / "src"

app = Flask(__name__)
app.secret_key = os.environ.get('SECRET_KEY', 'dev-secret-key-change-in-production')

from pages.landing import landing_page
from pages.auth import login_page_view, register_page_view
from pages.ip.routes import (
    ip_step_1,
    ip_step_1_passport,
    ip_step_1_contacts,
    ip_step_2,
    ip_step_3,
    ip_step_4,
)
from pages.ooo.routes import (
    ooo_step_1,
    ooo_step_2,
    ooo_step_3,
    ooo_step_3_charter,
    ooo_step_3_address,
    ooo_step_4,
    ooo_step_5,
    ooo_step_6,
)

from okved_service import searcher


@app.route("/src/<path:filename>")
def serve_src(filename: str):
    return send_from_directory(SRC_DIR, filename)


@app.route("/")
def landing():
    return landing_page()


@app.route("/login")
def login_page():
    return login_page_view()


@app.route("/register")
def register_page():
    return register_page_view()


# IP flow
@app.route("/ip/step-1")
def ip_form_page():
    return ip_step_1()


@app.route("/ip/step-1/passport")
def ip_form_step_1_passport():
    return ip_step_1_passport()


@app.route("/ip/step-1/contacts")
def ip_form_step_1_contacts():
    return ip_step_1_contacts()


@app.route("/ip/step-2", methods=['GET', 'POST'])
def ip_form_step_2():
    if request.method == 'POST':
        session['ip_okved_codes'] = request.form.getlist('okved_codes[]')
        session['ip_okved_names'] = request.form.getlist('okved_names[]')
        session['ip_main_okved'] = request.form.get('main_okved_code')
        return redirect(url_for('ip_form_step_3'))
    return ip_step_2()


@app.route("/ip/step-3")
def ip_form_step_3():
    return ip_step_3()


@app.route("/ip/step-4")
def ip_form_step_4():
    return ip_step_4()


# OOO flow
@app.route("/ooo/step-1")
def ooo_form_page():
    return ooo_step_1()


@app.route("/ooo/step-2")
def ooo_form_step_2():
    return ooo_step_2()


@app.route("/ooo/step-3")
def ooo_form_step_3():
    return ooo_step_3()


@app.route("/ooo/step-3/charter")
def ooo_form_step_3_charter():
    return ooo_step_3_charter()


@app.route("/ooo/step-3/address")
def ooo_form_step_3_address():
    return ooo_step_3_address()


@app.route("/ooo/step-4", methods=['GET', 'POST'])
def ooo_form_step_4():
    if request.method == 'POST':
        session['ooo_okved_codes'] = request.form.getlist('okved_codes[]')
        session['ooo_okved_names'] = request.form.getlist('okved_names[]')
        session['ooo_main_okved'] = request.form.get('main_okved_code')
        return redirect(url_for('ooo_form_step_5'))
    return ooo_step_4()


@app.route("/ooo/step-5")
def ooo_form_step_5():
    return ooo_step_5()


@app.route("/ooo/step-6")
def ooo_form_step_6():
    return ooo_step_6()


# API для поиска ОКВЭД
@app.route('/api/search_okved')
def search_okved():
    query = request.args.get('q', '')
    results = searcher.search(query, limit=50)
    return jsonify(results)


@app.route('/api/get_saved_okveds')
def get_saved_okveds():
    flow = request.args.get('flow', 'ip')
    codes = session.get(f'{flow}_okved_codes', [])
    names = session.get(f'{flow}_okved_names', [])
    main_code = session.get(f'{flow}_main_okved')
    return jsonify({'codes': codes, 'names': names, 'main_code': main_code})


if __name__ == "__main__":
    app.run(debug=True)