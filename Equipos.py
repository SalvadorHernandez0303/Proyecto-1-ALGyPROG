from Data import obtener_datos_equipos
class Equipo:
    def __init__(self, nombre, codigo_fifa, grupo, id):
        self.nombre = nombre
        self.codigo_fifa = codigo_fifa
        self.grupo = grupo
        self.id= id

obtener_datos_equipos()

def __show__(self):
        return f"Nombre: {self.nombre}\nCodigo Fifa: {self.codigo_fifa}\nGrupo: {self.grupo}\nId: {self.id}"


def respaldar_datos(equipos):
    with open('equipos.txt', 'w') as file:
        for equipo in equipos:
            file.write(f"Nombre: {equipo.nombre}, Código FIFA: {equipo.codigo_fifa}, Grupo: {equipo.grupo}\n")