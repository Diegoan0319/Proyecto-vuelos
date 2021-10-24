from flask.app import Flask
from flask_wtf import FlaskForm
from wtforms import StringField, PasswordField, SubmitField, SelectField, BooleanField, TextAreaField
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
    perfil = SelectField("Perfil", coerce=int, choices=[("0","-- Elija opción -- "),("1","piloto"),("2","usuario"),("3","administrador")], validators=[DataRequired(message="Debe escoger una opción")])
    registrar = SubmitField("Registrar")

class NewRegistro(FlaskForm):
    username = StringField("Usuario")
    nombre = StringField("Nombre")
    correo = StringField("Correo")
    password = PasswordField("Password")
    perfil = SelectField("Perfil", coerce=int, choices=[("0","-- Elija opción -- "),("2","usuario")], validators=[DataRequired(message="Debe escoger una opción")])
    registrar = SubmitField("Registrar")

class Vuelos(FlaskForm):
    codigo = StringField("Codigo")
    avion = StringField("Avion")
    piloto = StringField("Piloto")
    capacidad = StringField("Capacidad")
    estado = StringField("Estado")
    origen = StringField("Origen")
    destino = StringField("Destino")
    id_piloto_fk = StringField("ID Piloto Asignado")
    guardar = SubmitField("Guardar", render_kw=({"onfocus":"cambiarRuta('/vuelos/save')"}))
    consultar = SubmitField("Consultar", render_kw=({"onfocus":"cambiarRuta('/vuelos/get')"}))
    editar = SubmitField("Editar", render_kw=({"onfocus":"cambiarRuta('/vuelos/update')"}))
    eliminar = SubmitField("Eliminar", render_kw=({"onfocus":"cambiarRuta('/vuelos/delete')"}))

class User(FlaskForm):
    codigo = StringField("Codigo")
    avion = StringField("Avion")
    piloto = StringField("Piloto")
    capacidad = StringField("Capacidad")
    estado = StringField("Estado")
    origen = StringField("Origen")
    destino = StringField("Destino")
    id_piloto_fk = StringField("ID del Piloto")
    nombre = StringField("Nombre del Piloto")
    consultar = SubmitField("Consultar",render_kw=({"onfocus":"cambiarRuta2('/usuario/dashboard')"}))
    reservar = SubmitField("Reservar",render_kw=({"onfocus":"cambiarRuta2('/usuario/reserva')"}))

class Comentarios(FlaskForm):
    id_usuario = StringField("ID Usuario")
    cod_vuelo = StringField("Codigo vuelo")
    comentario = TextAreaField("Comentario")
    enviar = SubmitField("Enviar") 
    rol = SelectField("Rol", coerce=int, choices=[("0","-- Elija opción -- "),("1","Piloto"),("2","Usuario")], validators=[DataRequired(message="Debe escoger una opción")])
    check = BooleanField('Acepto términos y condiciones', validators=[DataRequired()])
 