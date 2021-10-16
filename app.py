from flask import Flask, render_template, request, jsonify
from werkzeug.utils import redirect
import formulario
import os
import db
import sqlite3

app = Flask(__name__)
app.config['JSON_AS_ASCII'] = False
app.secret_key = os.urandom(24)


@app.route('/')
def main():
    formulario1 = formulario.formularioWTF()
    return render_template('index.html', formulario1=formulario1)


@app.route('/recibido', methods=['POST'])
def recibido():
    nombre = request.form.get('nombre')
    correo = request.form.get("correo")
    """print(request.form)"""
    return login(nombre, correo)


def login(nombre, correo):
    connect_db = db.get_db()
    cursor = connect_db.cursor()
    consulta = "select * from usuario where nombre ='{}' and correo ='{}".format(
        nombre, correo)
    print(consulta)
    cursor.executescript(consulta)
    resultado = cursor.fetchall()
    return str(resultado)


def insert_record(usuario, correo, password, nombre):
    connect_db = db.get_db()
    cursor = connect_db.cursor()
    insert = "INSERT INTO usuario(usuario,correo,password,nombre) values ('{}','{}','{}','{}')".format(
        usuario, correo, password, nombre)
    cursor.executescript(insert)
    connect_db.commit()
    connect_db.close()
    return redirect("/usuarios")


@app.route('/usuarios/<usuario>/<correo>/<password>/<nombre>')
def call(usuario, correo, password, nombre):
    insert_record(usuario, correo, password, nombre)


@app.route('/usuarios')
def prueba():
    connect_db = db.get_db()
    cursor = connect_db.cursor()
    consulta = "select * from usuario "
    cursor.execute(consulta)
    resultado = cursor.fetchall()
    return jsonify(resultado)
