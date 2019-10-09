from wtforms import Form
from wtforms import validators
from wtforms import HiddenField
from wtforms import IntegerField
from wtforms import SelectField


def honeypot_len(form, field):
    if len(field.data) > 0:
        raise validators.ValidationError('ATAQUE DE BOT CACA')


class Formulario(Form):

    numero1 = IntegerField('Numero01: ', [
        validators.required('Numero requerido!!!'),
        validators.length(min=1, max=100, message='Numero demasiado largo!!!')
    ])

    operacion = SelectField('Seleciona la operación:',
        choices=[('+', 'sumar'), ('-', 'restar'), ('x', 'multiplicar'), ('/', 'dividir')
    ])

    numero2 = IntegerField('Numero02: ', [
        validators.required('Numero requerido!!!'),
        validators.length(min=1, max=100, message='Numero demasiado largo!!!')
    ])
    # Trampa Honeypot
    honeypot = HiddenField('', [honeypot_len])