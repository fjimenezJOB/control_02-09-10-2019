from flask import Flask, render_template, redirect, url_for, request
from flask_wtf import CsrfProtect
import form as f

app = Flask(__name__)
# Clave secreta para el csrf token
app.secret_key = 'super_calculator'
# csrf sirve para encriptar la sesión y que los datos que introduzca el usuario no puedan ser robados desde otras pestañas
# abiertas en el navegador.
csrf = CsrfProtect(app)
# **********************************

@app.route('/', methods=['GET', 'POST'])
def home():
# Para sacar formulario de wtforms
    formulario = f.Formulario()
# *******************************
    if request.method == 'POST':  # Para que no pete la primera vez que entran a la pagina
    # Recoge la información del formulario
        num1 = int(request.form.get('numero1'))
        num2 = int(request.form.get('numero2'))
        operacion = request.form.get('operacion')
    # **************************************
    # Selecciona cual es la operacion a realizar y nos da el resultado
        if operacion == '+':
            resultado = num1 + num2

        elif operacion == '-':
            resultado = num1 - num2

        elif operacion == 'x':
            resultado = num1 * num2

        elif operacion == '/':
            resultado = num1 / num2
    # ******************************************
    # Graba la información en un txt
        historico = (f'{num1} {operacion} {num2} = {resultado}\n')
        esctibir_historial(historico)
    # ***********************************
    # Inicializa las variables para que no esten vacías antes que el usuario introduzca los datos
    else:
        resultado = 0
        num1 = 0
        num2 = 0
    # ******************************
    # Lee el historial del txt y lo introduce en un diccionario para poderlo pasar a la index
    historial = leer_historial()
    context = {
        'lineas': historial
    }
    # *******************************************************
    return render_template('index.html', formulario=formulario, resultado=resultado, **context)


def esctibir_historial(historico):
    with open('historial.txt', 'a') as f:
        f.write(historico)
    f.close()


def leer_historial():
    with open('historial.txt', 'r') as f:
        contenido = f.readlines()
    f.close()
    return contenido


@app.errorhandler(404)
def error(error):
    return '<h1> Pagina no encontrada...(404)<h1>'


if __name__ == "__main__":
    app.run('0.0.0.0', 5000, debug=True)