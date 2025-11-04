# Archivo: demo_01_clases.py
"""
Demo 1: Introducción a Clases y Objetos
Objetivo: Mostrar los conceptos básicos de la programación orientada a objetos
en Python mediante un ejemplo de productos en un e-commerce.
"""

class Producto:
    """
    Clase que representa un producto en una tienda online.
    Demuestra conceptos básicos de POO: atributos, métodos, constructor.
    """
    
    def __init__(self, codigo, nombre, precio, stock=0):
        """Constructor de la clase"""
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
    
    def mostrar_info(self):
        """Muestra la información del producto"""
        return f"Producto: {self.nombre} (SKU: {self.codigo}) - ${self.precio}"
    
    def actualizar_stock(self, cantidad):
        """Actualiza el stock del producto"""
        self.stock += cantidad
        return f"Stock actualizado. Nuevo stock: {self.stock}"
    
    def esta_disponible(self):
        """Verifica si el producto tiene stock disponible"""
        return self.stock > 0

def demo_clases():
    print("=== Demo: Clases y Objetos en Python ===")
    
    # Ejemplo 1: Crear instancias de la clase
    print("\n1. Creando productos:")
    laptop = Producto("LAP001", "Laptop Pro", 1200, 5)
    smartphone = Producto("CEL001", "Smartphone X", 800)
    
    # Ejemplo 2: Usar métodos de la clase
    print("\n2. Información de productos:")
    print(laptop.mostrar_info())
    print(smartphone.mostrar_info())
    
    # Ejemplo 3: Manipular objetos
    print("\n3. Actualizando stock:")
    print(f"Stock inicial laptop: {laptop.stock}")
    print(laptop.actualizar_stock(3))
    print(f"¿Laptop disponible?: {laptop.esta_disponible()}")
    print(f"¿Smartphone disponible?: {smartphone.esta_disponible()}")

if __name__ == "__main__":
    demo_clases()