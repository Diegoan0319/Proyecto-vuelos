from flask.app import Flask
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField, BooleanField
from wtforms.validators import DataRequired

class Login(FlaskForm):
    username = StringField("Usuario", validators=[DataRequired("Usuario es obligatorio")])
    password = PasswordField("Password", validators=[DataRequired("Password es obligatorio")])
    enviar = SubmitField ("Enviar")
    
class Registro(FlaskForm):
    username = StringField("Usuario")
    nombre = StringField("Nombre")
    correo = StringField("Correo")
    password = PasswordField("Password")
    registrar = SubmitField("Registrar")
    rol = SelectField("Rol", coerce=int, choices=[("0","-- Elija opción -- "),("1","Piloto"),("2","Usuario")], validators=[DataRequired(message="Debe escoger una opción")])
    check = BooleanField('Acepto términos y condiciones', validators=[DataRequired()])