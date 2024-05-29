# controllers.py

from models import ProductoModel

class ProductoController:
    def __init__(self):
        self.producto_model = ProductoModel()

    def obtener_productos(self):
        return self.producto_model.obtener_productos()
