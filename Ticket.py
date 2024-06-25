class Ticket:
    def __init__(self, codigo_ticket, partido, precio):
        self.codigo_ticket = codigo_ticket
        self.partido = partido
        self.precio = precio
        
        def __str__():
            return f"Ticket {self.codigo_ticket}\n - Partido: {self.partido}\n - Precio: {self.precio}"
        
    def vip(self):
        if self.codigo_ticket == "VIP":
            for precio in self.precio:
                precio = '75$'
                self.precio = precio
        elif self.codigo_ticket == "General":
            for precio in self.precio:
                precio = '35$'
                self.precio = precio
        return precio

    def descuento(self):
        for cliente in self.codigo_ticket:
            if cliente == "Posee una cedula Vampira":
                for precio in self.precio:
                    precio = precio * 0.5