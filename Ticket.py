from Cliente import Cliente
from Interfaces.FileClassManager import FileClassManager
class Ticket(FileClassManager):
    def __init__(self, codigo_ticket = 0, partido=None, tipo="General"):
        self.codigo_ticket = codigo_ticket
        self.partido = partido
        self.precio_base = 35 if tipo == "General" else 75
        
        def __str__():
            return f"Ticket {codigo_ticket} para el partido {partido}\n"
        
    def Crear_boleto(self, registro):
        codigo_ticket = registro["codigo_ticket"]
        partido = registro["partido"]
        precio_base = registro["precio_base"]
        return Ticket(codigo_ticket, partido, precio_base)
    
    def precio_final(self,cedula):
            precio == self.precio_base
            if cedula.es_vampiro():
                precio *=0.5
                print('Tienes un 50% de descuento')
            precio += precio *0.16
            return precio
        