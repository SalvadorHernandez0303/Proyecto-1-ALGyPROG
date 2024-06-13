import requests


class Estadio:
    def __init__(self, nombre, ubicacion):
        self.nombre = nombre
        self.ubicacion = ubicacion

def obtener_datos_api():
    url = "https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/teams.json"
    respuesta = requests.get(url)
    datos = respuesta.json()
    return datos