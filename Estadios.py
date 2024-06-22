class Estadio:
    def __init__(self, id, nombre, ubicacion,capacidad,restaurantes):
        '''
        Inicializa la clase Estadio
        
        Parametros:
        id : Identificador del estadio
        nombre: Nombre del estadio
        ubicacion: Ciudad donde esta ubicado el estadio
        capacidad: Capacidad del estadio
        restaurantes: restaurantes que hay en el estadio
        
        '''
        self.id = id
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.capacidad = capacidad
        self.restaurantes = restaurantes


    def __str__(self):
        # Devuelve una representación en string del estadio
        return f"Estadio: {self.nombre}\n - Ubicación: {self.ubicacion}\n - Capacidad: {self.capacidad}\n - Restaurantes: {self.restaurantes}"
    

    def mapa_estadio(self):
        # Devuelve un mapa del estadio
        mapa = ""
        for i in range(self.capacidad[0]):
            for j in range(self.capacidad[1]):
                mapa += f"{i+1}{j+1}"
            mapa += "\n" 
        return mapa


    def show__restaurantes(self):
    # Muestra la lista de restaurantes del estadio
    # Utiliza la capacidad del estadio para determinar el número de filas y columnas
        if self.restaurantes:
            restaurantes_str = ""
            for restaurantes in self.restaurantes:
                restaurantes_str += restaurantes.show() + "\n"
            return restaurantes_str

