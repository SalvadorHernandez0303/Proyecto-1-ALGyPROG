from Cliente import Cliente
class Ticket:
    def __init__(self, codigo_ticket, partido, tipo):
        self.codigo_ticket = codigo_ticket
        self.partido = partido
        self.precio_base = 35 if tipo == "General" else 75
        
        def __str__():
            return f"Ticket {codigo_ticket} para el partido {partido}\n"
        
    def precio_final(self,cedula):
            precio == self.precio_base
            if cedula.es_vampiro():
                precio *=0.5
                print('Tienes un 50% de descuento')
            precio += precio *0.16
            return precio
        