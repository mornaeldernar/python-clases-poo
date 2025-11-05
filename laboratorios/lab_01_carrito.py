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
        self.items = {}
    
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
        # Verificamos si existe en el carrito
        if producto.codigo in self.items: #si existe entonces actualizamos la cantidad de productos que vamos a comprar
            producto_actual, cantidad_actual = self.items[producto.codigo]
            nueva_cantidad = cantidad_actual + cantidad
            if producto.stock >= nueva_cantidad: #si la nueva cantidad que vamos a comprar es menor o igual actualizamos la cantidad en el carrito
                self.items[producto.codigo] = (producto, nueva_cantidad)
                return True
            return False 
        else: #no lo tenemos en el carrito, entonces lo agregamos al carrito
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
        if codigo_producto in self.items: #Existe en nuestro carrito???
            del self.items[codigo_producto] #¡si existe! Elimínalo
            return True
        return False #No existe,no lo podemos eliminar porque no existe
    
    def calcular_total(self):
        """
        Calcula el total de la compra con descuentos
        Returns:
            float: Total a pagar
        """
        total = 0
        for producto, cantidad in self.items.values():
            subtotal = producto.precio * cantidad
            if cantidad >= 2:
                subtotal *= 0.9
                print(f"El producto {producto.nombre} tiene un descuento por comprar {cantidad} productos teniendo un subtotal de ${subtotal}")
            total += subtotal
        return round(total, 2)
    

    def realizar_compra(self):
        """
        Finaliza la compra y actualiza el inventario
        Returns:
            bool: True si la compra fue exitosa, False si hubo problemas
        """
        for producto, cantidad in self.items.values():
            if producto.stock < cantidad:
                return False
        for producto, cantidad in self.items.values():
            producto.actualizar_stock(cantidad)
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