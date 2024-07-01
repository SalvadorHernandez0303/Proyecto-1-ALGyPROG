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
