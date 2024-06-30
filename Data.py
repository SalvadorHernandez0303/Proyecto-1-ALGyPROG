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
        ("https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/matches.json", "datos_partidos"),
        ("https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/rounds.json", "jornadas")
    ]
    #Crear un diccionario con los datos
    datos = {}
    #Itera sobre la lista de URLs y obtiene los datos de cada una
    for url, clave_objeto in urls:
        #Llama a la funcion get_json_from url(url) para obtener los datos JSON de la URL
        datos[clave_objeto] = get_json_from_url(url)
    #Devuelve el diccionario
    return datos

def escribir_datos_para_guardado(f, valor_data):
    """
    Función que escribe los datos en un archivo para su guardado
    
    Parámetros: 
    f (file): Archivo donde se escribirán los datos
    valor_data (dict o list): Diccionario/lista con los datos a escribir en el archivo
    """
    # Si valor_data es un diccionario, se itera sobre sus items
    if isinstance(valor_data, dict):
        for key, value in valor_data.items():
            # Si el valor es una lista, se itera sobre sus elementos
            if isinstance(value, list):
                for item in value:
                    f.write(f"{{ '{key}': ")
                    f.write(f"{item} }}\n")
    # Si valor_data es una lista, se itera sobre sus elementos
    elif isinstance(valor_data, list):
        for item in valor_data:
            f.write(f"  {item}\n")

def guardar_datos_en_archivo_txt(datos):
    """
    Función que guarda los datos en un archivo TXT.
    
    Args:
        datos : El diccionario con los datos a guardar.
    """
    # for key, value in datos.items():
    #     archivo_individual = f'{key}.txt'
    #     with open(archivo_individual, 'w') as f:
    #         f.write(f'{key.upper()}\n\n')
    #         for item in value:
    #             f.write(f'  {item}\n')
    #         f.write('\n\n')
        
    # Crear un archivo que contiene toda la información
    nombre_archivo_txt = "todos_datos.txt"
    with open(nombre_archivo_txt, 'w', encoding="utf-8") as f:
        for key, value in datos.items():
            f.write(f"{key.upper()}:\n\n")
            escribir_datos_para_guardado(f, value)
            f.write('\n\n')
                

# Prueba del código
datos = obtener_datos()
# print("Datos obtenidos:")
# print(datos)
guardar_datos_en_archivo_txt(datos)
print("Datos guardados en archivos TXT \n")