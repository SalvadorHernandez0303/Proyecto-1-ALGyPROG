from Interfaces.FileClassManager import FileClassManager

class Partido(FileClassManager):
    def __init__(self, id, numero, grupo, estadio, fecha, local, visitante):
        ''' 
        Inicializa la clase Partido.
        
        Parametros:
        
        id: Identificador del partido.
        grupo : Grupo al que pertenece el partido.
        nombre : Nombre del partido.
        estadio : Estadio donde se juega el partido.
        fecha : Fecha en que se juega el partido.
        local : Equipo local.
        visitante : Equipo visitante.
        
        '''
        self.id = id
        self.numero = numero
        self.grupo = grupo
        self.estadio = estadio
        self.fecha = fecha
        self.local = local
        self.visitante = visitante
    
    def __str__(self):
        #Devuelve un string que muestra la informacion de forma legible
        return f"Partido {self.id}: {self.local} vs {self.visitante}\n - Estadio: {self.estadio}\n - Fecha: {self.fecha}\n - Grupo: {self.grupo}"
    
    def Crear_cliente(self, registro):
        id = registro["id"]
        numero = registro["number"]
        grupo = registro["group"]
        estadio = registro["stadium_id"]
        fecha = registro["date"]
        local = registro["home"]
        visitante = registro["away"]
        
        return Partido(id, numero, grupo, estadio, fecha, local, visitante)
    
    def Mapear_str_a_clase(self, lista_str):
        pass
