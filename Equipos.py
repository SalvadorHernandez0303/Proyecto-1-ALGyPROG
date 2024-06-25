class Equipo:
    def __init__(self, nombre, codigo_fifa, grupo, id):
        """
        Crea un objeto Equipo con información básica.
        
        Parámetros:
        - nombre: El nombre del equipo 
        - codigo_fifa: El código FIFA del equipo 
        - grupo: El grupo en el que se encuentra el equipo 
        - id: El identificador único del equipo 
        
        """
        self.nombre = nombre
        self.codigo_fifa = codigo_fifa
        self.grupo = grupo
        self.id= id
    
    def __str__(self):
    #Devuelve un string con la información del equipo de forma legible.
        return f"- Nombre: {self.nombre}\n - Codigo Fifa: {self.codigo_fifa}\n - Grupo: {self.grupo}\n - Id: {self.id}"