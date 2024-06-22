class Partido:
    def __init__(self,id,grupo,nombre,estadio,fecha, local,visitante):
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
        self.grupo = grupo
        self.nombre = nombre
        self.estadio = estadio
        self.fecha = fecha
        self.local = local
        self.visitante = visitante
    
    def __str__(self):
        #Devuelve un string que muestra la informacion de forma legible
        return f"Partido {self.id}: {self.nombre} - {self.local} vs {self.visitante}\n - Estadio: {self.estadio}\n - Fecha: {self.fecha}\n - Grupo: {self.grupo}"
