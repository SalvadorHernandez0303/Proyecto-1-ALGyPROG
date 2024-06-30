from Producto import Producto

class Bebida(Producto):
    def __init__(self, nombre, precio, cantidad, tipo, alcoholico):
        super().__init__(nombre, precio, cantidad)
        self.tipo = "Bebida"
        self.alcoholico = alcoholico
        
        def __str__():
            super.show() + f"\n Alcoholico: {self.alcoholico}"