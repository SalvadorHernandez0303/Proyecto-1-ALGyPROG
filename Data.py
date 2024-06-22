import requests

def get_json_from_url(url):
    """
    Función que obtiene el contenido JSON de una URL.
    
    Args:
        url (str): La URL desde la que se va a obtener el contenido JSON.
    
    Returns:
        dict: El contenido JSON obtenido de la URL. Si ocurre un error, se devuelve una lista vacía.
    """
    try:
        # Se realiza una solicitud GET a la URL proporcionada
        respuesta = requests.get(url)
        # Verificar si la respuesta fue exitosa y lanzar una excepción si no lo es
        respuesta.raise_for_status()
        #Devuelve el contenido del JSON
        return respuesta.json()
    except requests.RequestException as e:
        #Imprime una lista vacia si ocurre algun error
        print(f"Error al obtener datos de {url}: {e}")
        return []

def obtener_datos():
    """
    Función que obtiene datos de varias URLs y los almacena en un diccionario.
    
    Returns:
        dict: Un diccionario con los datos obtenidos de las URLs.
    """
    urls = [
        ("https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/teams.json", "datos_equipos"),
        ("https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/stadiums.json", "estadios"),
        ("https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/matches.json", "datos_partidos")
        ("https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/rounds.json", "jornadas")
    ]
    #Crear un diccionario con los datos
    datos = {}
    #Itera sobre la lista de URLs y obtiene los datos de cada una
    for url, nombre_variable in urls:
        #Llama a la funcion get_json_from url(url) para obtener los datos JSON de la URL
        datos[nombre_variable] = get_json_from_url(url)
    #Devuelve el diccionario
    return datos

def guardar_datos_en_archivotxt(datos):
    """
    Función que guarda los datos en un archivo TXT.
    
    Args:
        datos : El diccionario con los datos a guardar.
    """
    for key, value in datos.items():
        archivo_individual = f'{key}.txt'
        with open(archivo_individual, 'w') as f:
            f.write(f'{value}')
        
    # Crear un archivo que contiene toda la información
    archivo_todos = "todos_datos.txt"
    with open(archivo_todos, 'w') as f:
        for key, value in datos.items():
            f.write(f"{key}: {value}\n")
pass