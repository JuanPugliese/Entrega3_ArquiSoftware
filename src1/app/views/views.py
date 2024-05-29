# views.py

from flask import Blueprint, render_template
print("Intentando importar ProductoController...")
from ..controller.controller import ProductoController
print("Importación exitosa.")


producto_bp = Blueprint('producto_bp', __name__)
producto_controller = ProductoController()  # Crea una instancia del controlador

@producto_bp.route('/productos')
def mostrar_productos():
    productos = producto_controller.obtener_productos()  # Usa el método del controlador
    return render_template('productos.html', productos=productos)
