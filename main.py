from flask import Flask, render_template, redirect, url_for, request
from flask_wtf import CsrfProtect
import form as form
import Calculadora as c

app = Flask(__name__)
csrf = CsrfProtect(app)


@app.route('/', methods=['GET', 'POST'])
def home():
    formulario = form.Formulario()
    numero01 = request.form.get('numero01')
    numero02 = request.form.get('numero02')
    operacion = request.form.get('operacion')

    if operacion == '+':
        resultado = c.Calculadora.sumar(numero01, numero02)

    elif operacion == '-':
        resultado = c.Calculadora.restar(numero01, numero02)

    elif operacion =='x':
        resultado = c.Calculadora.multiplicar(numero01, numero02)

    elif operacion == '/':
        resultado = c.Calculadora.dividir(numero01, numero02)

    return render_template('index.html', **formulario, resultado = resultado)


if __name__ == "__main__":
    app.run('0.0.0.0', 5000, debug=True)
