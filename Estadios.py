class Estadio:
    def __init__(self, id, nombre, ubicacion,capacidad,restaurantes):
        self.id = id
        self.nombre = nombre
        self.ubicacion = ubicacion
        self.capacidad = capacidad
        self.restaurantes = restaurantes


def __str__(self):
        return f"Estadio: {self.nombre}\n - Ubicación: {self.ubicacion}\n - Capacidad: {self.capacidad}\n - Restaurantes: {','.join([r.nombre for r in self.restaurantes])}"
    

def mapa_estadio(self):
        mapa = ""
        for i in range(self.capacidad[0]):
            for j in range(self.capacidad[1]):
                mapa += f"{i+1}{j+1}"
            mapa += "\n" 
        return mapa


def __show__restaurantes__(self):
    if self.restaurantes:
        restaurantes = ""
        for restaurantes in self.restaurantes:
            restaurantes += restaurantes.show() + "\n"

        return restaurantes

