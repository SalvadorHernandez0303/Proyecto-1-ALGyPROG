class Producto:
    def __init__(self, nombre, precio, cantidad, stock, tipo):
        self.nombre = nombre
        self.precio = precio
        self.cantidad = cantidad
        self.stock = stock
        self.tipo = tipo
        
        def __str__():
            return f"Nombre: {self.nombre}\n, - Precio: {self.precio}\n, - Cantidad:{self.cantidad}\n, - Stock:{self.stock}"
    
    def stock_disponible(self,cantidad):
        self.stock = cantidad
        if self.stock < 0:
            self.stock = 0
        else:
            self.stock = cantidad