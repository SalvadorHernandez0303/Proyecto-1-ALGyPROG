import requests

def get_json_from_url(url):
    try:
        respuesta = requests.get(url)
        respuesta.raise_for_status()
        return respuesta.json()
    except requests.RequestException as e:
        print(f"Error al obtener datos de {url}: {e}")
        return []

def obtener_datos():
    urls = [
        ("https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/teams.json", "datos_equipos"),
        ("https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/stadiums.json", "estadios"),
        ("https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/matches.json", "datos_partidos")
    ]

    datos = {}
    for url, nombre_variable in urls:
        datos[nombre_variable] = get_json_from_url(url)

    return datos

