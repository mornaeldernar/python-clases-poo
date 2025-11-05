
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
    

class ProductoDigital(ProductoBase):
    """Clase para productos digitales (ej: software, ebooks)"""
    
    def __init__(self, codigo, nombre, precio, formato):
        super().__init__(codigo, nombre, precio)
        self.formato = formato