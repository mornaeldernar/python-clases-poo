# Archivo: demo_02_herencia.py
"""
Demo 2: Herencia y Polimorfismo
Objetivo: Mostrar conceptos avanzados de POO como herencia, polimorfismo
y encapsulamiento usando un sistema de productos y categorías.
"""

class ProductoBase:
    """Clase base para productos"""
    
    def __init__(self, codigo, nombre, precio):
        self._codigo = codigo  # Atributo protegido
        self._nombre = nombre
        self._precio = precio
        self._vendido = False
    
    @property
    def nombre(self):
        """Getter para el nombre"""
        return self._nombre
    
    @property
    def precio(self):
        """Getter para el precio"""
        return self._precio
    
    def calcular_precio_final(self):
        """Método base para calcular precio final"""
        return self._precio
    
    def marcar_como_vendido(self):
        """Marca el producto como vendido"""
        self._vendido = True

class ProductoFisico(ProductoBase):
    """Clase para productos físicos que requieren envío"""
    
    def __init__(self, codigo, nombre, precio, peso):
        super().__init__(codigo, nombre, precio)
        self.peso = peso
        self.costo_envio = peso * 10  # $10 por kg
    
    def calcular_precio_final(self):
        """Sobrescribe el método para incluir costo de envío"""
        return self._precio + self.costo_envio

class ProductoDigital(ProductoBase):
    """Clase para productos digitales (ej: software, ebooks)"""
    
    def __init__(self, codigo, nombre, precio, formato):
        super().__init__(codigo, nombre, precio)
        self.formato = formato
    
    

def demo_herencia():
    print("=== Demo: Herencia y Polimorfismo en Python ===")
    
    # Ejemplo 1: Crear diferentes tipos de productos
    print("\n1. Creando productos:")
    libro = ProductoFisico("LIB001", "Python Básico", 29.99, 0.5)
    ebook = ProductoDigital("EBK001", "Python Básico (Digital)", 19.99, "PDF")
    
    # Ejemplo 2: Demostrar polimorfismo
    print("\n2. Precios finales (polimorfismo):")
    productos = [libro, ebook]
    for producto in productos:
        precio_final = producto.calcular_precio_final()
        print(f"{producto.nombre}: ${precio_final:.2f}")
    
    # Ejemplo 3: Usar encapsulamiento
    print("\n3. Usando propiedades:")
    print(f"Nombre del libro: {libro.nombre}")  # Usa el getter
    libro.marcar_como_vendido()  # Método público
    # No podemos acceder directamente a _vendido (encapsulamiento)

if __name__ == "__main__":
    demo_herencia()