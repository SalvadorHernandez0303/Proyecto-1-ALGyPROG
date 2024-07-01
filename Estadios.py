import ast
from Interfaces.FileClassManager import FileClassManager

class Estadio(FileClassManager):
    def __init__(self, id = 0, nombre = "", ubicacion = "", capacidad_general = 0, capacidad_vip = 0, restaurantes = ""):
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
        self.capacidad_general = capacidad_general
        self.capacidad_vip = capacidad_vip
        self.restaurantes = restaurantes


    def __str__(self):
        # Devuelve una representación en string del estadio
        return f"Estadio: {self.nombre}\n - Ubicación: {self.ubicacion}\n - Capacidad: {self.capacidad}\n - Restaurantes: {self.restaurantes}"
    
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.nombre,
            "city": self.ubicacion,
            "capacity_general": self.capacidad_general,
            "capacity_vip": self.capacidad_vip,
            "restaurant": self.restaurantes
        }

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
                            if nombre_clase == "Estadio":
                                # Se extraen los datos del partido
                                estadio_id = data_dict['id']
                                estadio_nombre = data_dict['name']
                                estadio_ubicacion = data_dict['city']
                                estadio_general = data_dict['capacity'][0]
                                estadio_vip = data_dict['capacity'][1]
                                estadio_restaurante = ""
                                
                                # Se agrega el partido a la lista de datos
                                equipo_obj = Estadio(estadio_id, estadio_nombre, estadio_ubicacion, estadio_general, estadio_vip, estadio_restaurante)
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
