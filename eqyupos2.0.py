import requests

class Equipo:
    def __init__(self):
        # Copias y crea otra url por ejemplo para los estadios o jugadores
        self.equipos_url = "https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/teams.json"
        
        
    # Aqui igual se puede copiar y crear otra para los estadios o jugadores
    def obtener_equipos(self):
        response = requests.get(self.equipos_url)
        equipos = response.json()
        return equipos

euro_juegos = Equipo()

# Obtener equipos
equipos = euro_juegos.obtener_equipos()
print("Equipos:",equipos)