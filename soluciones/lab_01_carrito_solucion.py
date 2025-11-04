# Archivo: lab_01_carrito_solucion.py
"""
Laboratorio 1: Sistema de Carrito de Compras (SOLUCIÓN)
Objetivo: Practicar la creación de clases y objetos implementando
un sistema básico de carrito de compras.
"""

class Producto:
    """Clase base proporcionada para el ejercicio"""
    
    def __init__(self, codigo, nombre, precio, stock):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
    
    def actualizar_stock(self, cantidad):
        if self.stock + cantidad >= 0:
            self.stock += cantidad
            return True
        return False

class CarritoCompras:
    """
    Implementa un carrito de compras que gestiona productos
    """
    
    def __init__(self):
        """
        Inicializa un carrito vacío
        """
        self.items = {}  # Diccionario: {codigo_producto: (producto, cantidad)}
    
    def agregar_producto(self, producto, cantidad):
        """
        Agrega un producto al carrito
        Args:
            producto (Producto): El producto a agregar
            cantidad (int): Cantidad del producto
        Returns:
            bool: True si se agregó correctamente, False si no hay stock
        """
        if cantidad <= 0:
            return False
        
        if producto.stock < cantidad:
            return False
        
        if producto.codigo in self.items:
            # Actualizar cantidad si ya existe
            actual_producto, actual_cantidad = self.items[producto.codigo]
            nueva_cantidad = actual_cantidad + cantidad
            if producto.stock >= nueva_cantidad:
                self.items[producto.codigo] = (producto, nueva_cantidad)
                return True
            return False
        else:
            # Agregar nuevo producto
            self.items[producto.codigo] = (producto, cantidad)
            return True
    
    def remover_producto(self, codigo_producto):
        """
        Remueve un producto del carrito
        Args:
            codigo_producto (str): Código del producto a remover
        Returns:
            bool: True si se removió correctamente, False si no existe
        """
        if codigo_producto in self.items:
            del self.items[codigo_producto]
            return True
        return False
    
    def calcular_total(self):
        """
        Calcula el total de la compra con descuentos
        Returns:
            float: Total a pagar
        """
        total = 0
        for producto, cantidad in self.items.values():
            subtotal = producto.precio * cantidad
            # Aplicar descuento por cantidad
            if cantidad >= 3:
                subtotal *= 0.9  # 10% descuento
            total += subtotal
        return round(total, 2)
    
    def realizar_compra(self):
        """
        Finaliza la compra y actualiza el inventario
        Returns:
            bool: True si la compra fue exitosa, False si hubo problemas
        """
        # Verificar stock final
        for producto, cantidad in self.items.values():
            if producto.stock < cantidad:
                return False
        
        # Actualizar stock
        for producto, cantidad in self.items.values():
            producto.actualizar_stock(-cantidad)
        
        # Limpiar carrito
        self.items.clear()
        return True

def main():
    # Crear productos de prueba
    productos = [
        Producto("LAP001", "Laptop Pro", 1200, 5),
        Producto("CEL001", "Smartphone X", 800, 10),
        Producto("TAB001", "Tablet Pro", 500, 8)
    ]
    
    print("=== Sistema de Carrito de Compras ===")
    
    # Crear carrito
    carrito = CarritoCompras()
    
    # Prueba 1: Agregar productos
    print("\nPrueba 1: Agregando productos al carrito")
    print(f"Agregando 2 laptops: {carrito.agregar_producto(productos[0], 2)}")
    print(f"Agregando 1 smartphone: {carrito.agregar_producto(productos[1], 1)}")
    print(f"Total actual: ${carrito.calcular_total()}")
    
    # Prueba 2: Remover producto
    print("\nPrueba 2: Removiendo un producto")
    print(f"Removiendo laptop: {carrito.remover_producto('LAP001')}")
    print(f"Total después de remover: ${carrito.calcular_total()}")
    
    # Prueba 3: Realizar compra
    print("\nPrueba 3: Finalizando compra")
    if carrito.realizar_compra():
        print("Compra realizada con éxito")
        print(f"Stock final smartphone: {productos[1].stock}")
    else:
        print("Error al realizar la compra")

if __name__ == "__main__":
    main()