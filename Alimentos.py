from Producto import Producto

class Alimento(Producto):
    
    def __init__(self, nombre, cantidad, stock, precio, tipo, empaquetado):
        super().__init__(nombre, cantidad, stock, precio)
        self.tipo = "Alimento"
        self.empaquetado = empaquetado
        
    def __str__(self):
        return super.show() + f"\nPaquete: {self.empaquetado}"


