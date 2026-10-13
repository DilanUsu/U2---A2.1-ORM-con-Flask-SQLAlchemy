import os
from dotenv import load_dotenv
from flask import Flask, render_template, request, redirect, url_for
from flask_sqlalchemy import SQLAlchemy
from flask_migrate import Migrate

load_dotenv()

app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)
migrate = Migrate(app, db)

import models        # registra los modelos (después de crear db)
import controllers   # lógica CRUD con db.session


@app.route('/')
def index():
    juegos = controllers.listar_juegos()
    return render_template('lista.html', juegos=juegos)


@app.route('/nuevo', methods=['GET', 'POST'])
def nuevo():
    if request.method == 'POST':
        controllers.crear_juego(request.form['nombre'],
                                request.form['descripcion'],
                                request.form['precio'])
        return redirect(url_for('index'))
    return render_template('formulario.html', juego=None)


@app.route('/editar/<int:id>', methods=['GET', 'POST'])
def editar(id):
    juego = controllers.obtener_juego(id)
    if juego is None:
        return redirect(url_for('index'))
    if request.method == 'POST':
        controllers.actualizar_juego(juego, request.form['nombre'],
                                     request.form['descripcion'],
                                     request.form['precio'])
        return redirect(url_for('index'))
    return render_template('formulario.html', juego=juego)


@app.route('/eliminar/<int:id>', methods=['POST'])
def eliminar(id):
    juego = controllers.obtener_juego(id)
    if juego:
        controllers.eliminar_juego(juego)
    return redirect(url_for('index'))
