from flask import Flask, render_template, redirect, url_for
from flask_wtf import CsrfProtect
import form as form


app = Flask(__name__)
csrf = CsrfProtect(app)


@app.route('/', methods=['GET', 'POST'])
def home():
    
    formulario = form.Formulario()
    return render_template('index.html', **formulario)


if __name__ == "__main__":
    app.run('0.0.0.0', 5000, debug=True)