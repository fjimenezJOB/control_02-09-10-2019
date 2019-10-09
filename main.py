from flask import Flask, render_template, redirect, url_for, request
from flask_wtf import CsrfProtect
import form as f
# import calculadora as c

app = Flask(__name__)
app.secret_key = 'super_calculator'
csrf = CsrfProtect(app)


@app.route('/', methods=['GET', 'POST'])
def home():
    formulario = f.Formulario()
    if request.method == 'POST':
        num1 = int(request.form.get('numero1'))
        num2 = int(request.form.get('numero2'))
        operacion = request.form.get('operacion')

        if operacion == '+':
            resultado = num1 + num2

        elif operacion == '-':
            resultado = num1 - num2

        elif operacion == 'x':
            resultado = num1 * num2

        elif operacion == '/':
            resultado = num1 / num2
    else:
        resultado = 0

    return render_template('index.html', formulario=formulario, resultado = resultado)



if __name__ == "__main__":
    app.run('0.0.0.0', 5000, debug=True)