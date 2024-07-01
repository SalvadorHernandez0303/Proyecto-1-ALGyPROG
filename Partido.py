import ast
from Interfaces.FileClassManager import FileClassManager

class Partido(FileClassManager):
    def __init__(self, id = 0, numero = 0, local = None, visitante = None, fecha = "", grupo = "", estadio = ""):
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
        self.local = local
        self.visitante = visitante
        self.fecha = fecha
        self.grupo = grupo
        self.estadio = estadio
    
    def __str__(self):
        #Devuelve un string que muestra la informacion de forma legible
        return f"Partido {self.id}: {self.local} vs {self.visitante}\n - Estadio: {self.estadio}\n - Fecha: {self.fecha}\n - Grupo: {self.grupo}"
    
    def to_dict(self):
        return {
            "id": self.id,
            "number": self.numero,
            "home": self.local,
            "away": self.visitante,
            "date": self.fecha,
            "group": self.grupo,
            "stadium_id": self.estadio
        }
    
    # def Crear_cliente(self, registro):
    #     id = registro["id"]
    #     numero = registro["number"]
    #     grupo = registro["group"]
    #     estadio = registro["stadium_id"]
    #     fecha = registro["date"]
    #     local = registro["home"]
    #     visitante = registro["away"]
        
    #     return Partido(id, numero, grupo, estadio, fecha, local, visitante)
    
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
                            if nombre_clase == "Partido":
                                # Se extraen los datos del partido
                                partido_id = data_dict['id']
                                partido_numero = data_dict['number']
                                partido_local = data_dict['home']['id']
                                partido_visitante = data_dict['away']['id']
                                partido_fecha = data_dict['date']
                                partido_group = data_dict['group']
                                partido_estadio = data_dict['stadium_id']
                                
                                # Se agrega el partido a la lista de datos
                                partido_obj = Partido(partido_id, partido_numero, partido_local, partido_visitante, partido_fecha, partido_group, partido_estadio)
                                objecto_menu_data.append(partido_obj)
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
