from flask import Blueprint, redirect, url_for, render_template 
from models.Producto import Producto
from views import show_tasks, show_add_task_form, show_delete_task_form

from models.Producto import *

app = Flask(__name__)


@app.route('/registrarProducto', methods=['POST'])
def registrarProducto():
    nombre = request.form['nombre']
    categoria = request.form['categoria']
    tienda = request.form['tienda']
    producto = registrarProducto(nombre, categoria, tienda)

def consultarProducto(producto):
    nombre = producto.getNombre()
    categoria = producto.getCategoria()
    tienda = producto.getTienda()

    return nombre, categoria, tienda # Devolver la información consultada

def modificarProducto(producto, nombre, categoria, tienda):
    producto.setNombre(nombre)
    producto.setCategoria(categoria)
    producto.setTienda(tienda)


