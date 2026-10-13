from app import db
from models import Juego


def crear_juego(nombre, descripcion, precio):
    juego = Juego(nombre=nombre, descripcion=descripcion, precio=precio)
    db.session.add(juego)
    db.session.commit()
    return juego


def listar_juegos():
    return Juego.query.all()


def obtener_juego(id):
    return db.session.get(Juego, id)   # equivale a Juego.query.get(id) (forma moderna)


def actualizar_juego(juego, nombre, descripcion, precio):
    juego.nombre = nombre
    juego.descripcion = descripcion
    juego.precio = precio
    db.session.commit()


def eliminar_juego(juego):
    db.session.delete(juego)
    db.session.commit()
