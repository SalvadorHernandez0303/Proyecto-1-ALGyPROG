import requests

class Equipo:
    def __init__(self, nombre, codigo_fifa, grupo):
        self.nombre = nombre
        self.codigo_fifa = codigo_fifa
        self.grupo = grupo

def obtener_datos_api():
    url = "https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/teams.json"
    respuesta = requests.get(url)
    datos = respuesta.json()
    return datos


def respaldar_datos(equipos):
    with open('equipos.txt', 'w') as file:
        for equipo in equipos:
            file.write(f"Nombre: {equipo.nombre}, Código FIFA: {equipo.codigo_fifa}, Grupo: {equipo.grupo}\n")
            pass