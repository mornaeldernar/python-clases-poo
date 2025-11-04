# Archivo: lab_01_carrito.py
"""
Laboratorio 1: Sistema de Carrito de Compras
Objetivo: Practicar la creación de clases y objetos implementando
un sistema básico de carrito de compras.

La clase CarritoCompras debe:
1. Permitir agregar y remover productos
2. Calcular el total de la compra
3. Aplicar descuentos según cantidad
4. Gestionar el inventario al realizar la compra
"""

class Producto:
    """Clase base proporcionada para el ejercicio"""
    
    def __init__(self, codigo, nombre, precio, stock):
        self.codigo = codigo
        self.nombre = nombre
        self.precio = precio
        self.stock = stock
    
    def actualizar_stock(self, cantidad):
        """Actualiza el stock del producto"""
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
        # TODO: Implementar inicialización
        raise NotImplementedError("Debes implementar la inicialización del carrito")
    
    def agregar_producto(self, producto, cantidad):
        """
        Agrega un producto al carrito
        Args:
            producto (Producto): El producto a agregar
            cantidad (int): Cantidad del producto
        Returns:
            bool: True si se agregó correctamente, False si no hay stock
        """
        # TODO: Implementar agregar producto
        raise NotImplementedError("Debes implementar agregar_producto")
    
    def remover_producto(self, codigo_producto):
        """
        Remueve un producto del carrito
        Args:
            codigo_producto (str): Código del producto a remover
        Returns:
            bool: True si se removió correctamente, False si no existe
        """
        # TODO: Implementar remover producto
        raise NotImplementedError("Debes implementar remover_producto")
    
    def calcular_total(self):
        """
        Calcula el total de la compra con descuentos
        Returns:
            float: Total a pagar
        """
        # TODO: Implementar cálculo del total
        raise NotImplementedError("Debes implementar calcular_total")
    
    def realizar_compra(self):
        """
        Finaliza la compra y actualiza el inventario
        Returns:
            bool: True si la compra fue exitosa, False si hubo problemas
        """
        # TODO: Implementar realizar compra
        raise NotImplementedError("Debes implementar realizar_compra")

def main():
    # Crear productos de prueba
    productos = [
        Producto("LAP001", "Laptop Pro", 1200, 5),
        Producto("CEL001", "Smartphone X", 800, 10),
        Producto("TAB001", "Tablet Pro", 500, 8)
    ]
    
    print("=== Sistema de Carrito de Compras ===")
    
    try:
        # Crear carrito
        carrito = CarritoCompras()
        
        # Prueba 1: Agregar productos
        print("\nPrueba 1: Agregando productos al carrito")
        carrito.agregar_producto(productos[0], 2)
        carrito.agregar_producto(productos[1], 1)
        print(f"Total actual: ${carrito.calcular_total()}")
        
        # Prueba 2: Remover producto
        print("\nPrueba 2: Removiendo un producto")
        carrito.remover_producto("LAP001")
        print(f"Total después de remover: ${carrito.calcular_total()}")
        
        # Prueba 3: Realizar compra
        print("\nPrueba 3: Finalizando compra")
        if carrito.realizar_compra():
            print("Compra realizada con éxito")
        else:
            print("Error al realizar la compra")
            
    except NotImplementedError as e:
        print(f"\nError: {str(e)}")

if __name__ == "__main__":
    main()