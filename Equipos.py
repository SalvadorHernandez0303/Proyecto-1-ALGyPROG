import ast
from Interfaces.FileClassManager import FileClassManager

class Equipo(FileClassManager):
    def __init__(self, id = "", codigo_fifa = "", nombre = "",  grupo = ""):
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
    
    def to_dict(self):
        return {
            "id": self.id,
            "code": self.codigo_fifa,
            "name": self.nombre,
            "group": self.grupo
        }
    
    def Mapear_json_a_clase(self, titulo_data, nombre_clase):
        """
        Obtiene los datos de un menú seleccionado desde un archivo.
        
        Parámetros:
        self: Instancia de la clase que llama al método.
        titulo_data (str): Título del menú que se busca.
        nombre_clase (str): Nombre de la clase que se utiliza para filtrar los datos.
        
        Retorna:
        list: Lista de objetos que se encuentran en el menú seleccionado.
        """
        # Se crea una lista vacía para almacenar los datos del menú seleccionado
        objecto_menu_data = []
        # Se abre el archivo "todos_datos.txt" en modo de lectura
        with open("todos_datos.txt", 'r', encoding="utf-8") as f:
            # Se busca el título del menú en el archivo
            titulo_encontrado = False
            for linea in f:
                # Se elimina el espacio en blanco al final de la línea
                linea.strip()
                if titulo_encontrado:
                    # Si se encuentra el título, se itera sobre las líneas siguientes
                    if not linea:
                        # Si se encuentra una línea vacía, se sale del ciclo
                        break
                    try:
                        # Se intenta evaluar la línea como un diccionario
                        if linea != '\n':
                            data_dict = ast.literal_eval(linea.strip())
                            # Se filtran los datos según la clase
                            if nombre_clase == "Equipo":
                                # Se extraen los datos del partido
                                equipo_id = data_dict['id']
                                equipo_codigo = data_dict['code']
                                equipo_nombre = data_dict['name']
                                equipo_grupo = data_dict['group']
                                
                                # Se agrega el partido a la lista de datos
                                equipo_obj = Equipo(equipo_id, equipo_codigo, equipo_nombre, equipo_grupo)
                                objecto_menu_data.append(equipo_obj)
                            else:
                                # Se agrega el id del objeto a la lista de datos    
                                objecto_menu_data.append(data_dict["id"])
                        else:
                            # Si se encuentra una línea vacía, se sale del ciclo
                            if len(objecto_menu_data) == 0:
                                pass
                            else:
                                titulo_encontrado = False
                    except (SyntaxError, ValueError) as e:
                        # Si ocurre un error, se sale del ciclo
                        break
                elif linea == titulo_data:
                    # Se encuentra el título del menú
                    titulo_encontrado = True
        # Se devuelve la lista de datos del menú seleccionado
        return objecto_menu_data
    