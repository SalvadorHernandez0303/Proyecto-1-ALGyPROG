from Cliente import Cliente
from Interfaces.FileClassManager import FileClassManager
class Ticket(FileClassManager):
    def __init__(self, codigo_ticket = 0, cedula_cliente = 0, partido=None, asiento = 0, precio_base=0, precio_descuento = 0, precio_mas_iva = 0, precio_total = 0, tipo="General"):
        self.codigo_ticket = codigo_ticket
        self.cedula_cliente = cedula_cliente
        self.partido = partido
        self.asiento = asiento
        self.precio_base = 35 if tipo == "General" else 75
        self.precio_descuento = (self.precio_base * 0.50) if self.es_vampiro() else self.precio_base
        self.precio_mas_iva = self.precio_descuento * 0.16
        self.precio_total = self.precio_descuento + self.precio_mas_iva
        self.tipo = tipo
        
        def __str__():
            return f"Ticket {codigo_ticket} para el partido {partido}\n"
        
    def Crear_boleto(self, registro):
        codigo_ticket = registro["codigo_ticket"]
        cedula_cliente = registro["cedula_cliente"]
        partido = registro["partido"]
        asiento = registro["asiento"]
        precio_base = registro["precio_base"]
        precio_descuento = registro["precio_descuento"],
        precio_mas_iva = registro['precio_mas_iva'],
        precio_total = registro["precio_total"],
        tipo = registro["tipo"]
        return Ticket(codigo_ticket, cedula_cliente, partido, asiento, precio_base, precio_descuento, precio_mas_iva, precio_total, tipo)
    
    def to_dict(self):
        return {
            "id": self.codigo_ticket,
            "identification_client": self.cedula_cliente,
            "match": self.partido,
            "seat": self.asiento,
            "base_price": self.precio_base,
            "type" : self.tipo
        }
        
    def es_vampiro(self):
    # Convertimos el número a una cadena para obtener fácilmente el número de dígitos
        str_cedula = str(self.cedula_cliente)
        digitos_cedula= len(str_cedula)

    # Verificamos si el número tiene un número par de dígitos
        if digitos_cedula % 2 != 0:
            return False

    # Calculamos el número de dígitos en cada factor
        digitos_factor = digitos_cedula // 2
        
        cadena_factor = ""

    # Generamos todos los posibles factores
        for i in range(10**(digitos_factor-1), 10**digitos_factor):
            for j in range(i, 10**digitos_factor):
            # Verificamos si el producto de los factores es igual al número original
                if i * j == self.cedula_cliente:
                # Convertimos los factores a cadenas y los combinamos
                    cadena_factor = str(i) + str(j)
                # Verificamos si la cadena combinada contiene todos los dígitos del número original exactamente una vez
                if set(str_cedula) == set(cadena_factor):
                    return True

        return False
    
    # def precio_final(self, cedula):
    #         precio == self.precio_base
    #         if cedula.es_vampiro():
    #             precio *=0.5
    #             print('Tienes un 50% de descuento')
    #         precio += precio *0.16
    #         return precio
        