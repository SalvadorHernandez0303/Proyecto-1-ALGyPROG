from Interfaces.FileClassManager import *

class Cliente(FileClassManager):
    '''
    Crea un objeto con informacion basica de los clientes
    
    Parametros:
    -Nombre: Nombre del cliente
    -Cedula: Cedula del cliente
    -Edad: Edad del cliente
    
    '''
    def __init__(self, nombre = "", cedula = 0, edad = 0):
        self.nombre = nombre
        self.cedula = cedula
        self.edad = edad
        
        def __str__():
            #Devuelve la informacion en un string de forma legible
            return f" - Nombre: {self.nombre}\n - Cédula de Identidad: {self.cedula}\n - Edad: {self.edad}"

    def Crear_cliente(self, registro):
        nombre = registro["nombre"]
        cedula = registro["cedula"]
        edad = registro["edad"]
        return Cliente(nombre, cedula, edad)

    def es_vampiro(self):
    # Convertimos el número a una cadena para obtener fácilmente el número de dígitos
        str_cedula = str(self.cedula)
        digitos_cedula= len(str_cedula)

    # Verificamos si el número tiene un número par de dígitos
        if digitos_cedula % 2 != 0:
            return False

    # Calculamos el número de dígitos en cada factor
        digitos_factor = digitos_cedula // 2

    # Generamos todos los posibles factores
        for i in range(10**(digitos_factor-1), 10**digitos_factor):
            for j in range(i, 10**digitos_factor):
            # Verificamos si el producto de los factores es igual al número original
                if i * j == self.cedula:
                # Convertimos los factores a cadenas y los combinamos
                    cadena_factor = str(i) + str(j)
                # Verificamos si la cadena combinada contiene todos los dígitos del número original exactamente una vez
                if set(str_cedula) == set(cadena_factor):
                    return True

        return False
