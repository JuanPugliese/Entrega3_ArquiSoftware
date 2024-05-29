# models.py

import psycopg2
from psycopg2 import Error

class Producto:
    def __init__(self, id, nombre, categoria):
        self.id = id
        self.nombre = nombre
        self.categoria = categoria

class ProductoModel:
    def __init__(self):
        try:
            self.connection = psycopg2.connect(
                user="mipyt_usuario",
                password="123456789",
                host="localhost",
                port="5432",
                database="reciclaje_ur"
            )
            self.cursor = self.connection.cursor()
            print("Conexión exitosa a PostgreSQL")
        except (Exception, Error) as error:
            print("Error mientras se conectaba a PostgreSQL", error)

    def obtener_productos(self):
        try:
            self.cursor.execute("SELECT * FROM productos")
            productos = []
            for row in self.cursor.fetchall():
                producto = Producto(row[0], row[1], row[2])
                productos.append(producto)
            return productos
        except (Exception, Error) as error:
            print("Error al obtener productos:", error)
        finally:
            if self.connection:
                self.cursor.close()
                self.connection.close()
                print("Conexión cerrada a PostgreSQL")

    # Puedes agregar más métodos según sea necesario, como crear, actualizar o eliminar productos
