import os, json, requests
from Interfaces.FileManager import *

class FileApiManager(FileManager):
    
    def Crear_archivo(self, filepath):
        if not self.Archivo_existe(filepath):
            with open(filepath, "w", encoding="utf-8") as f:
                pass

    def Leer_Archivo(self, filepath, constructor):
        pass
    
    def Actualizar_archivo(self, filepath, content):
        """
        Función que guarda los datos en un archivo TXT.
    
        Args:
            datos : El diccionario con los datos a guardar.
        """
            
        # Crear un archivo que contiene toda la información
        with open(filepath, 'w', encoding="utf-8") as f:
            for key, value in content.items():
                f.write(f"{key.upper()}:\n\n")
                self.escribir_datos_para_guardado(f, value)
                f.write('\n\n')
        
        print("Documento llenado con éxito")
    
    def Mapear_data_a_clase(self, filepath, constructor):
        pass
    
    def Obtener_data_json_url(self, url):
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
        
    def escribir_datos_para_guardado(self, f, valor_data):
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
                
    def Mapear_datos(self, urls, apiManager):
        """
        Función que obtiene datos de varias URLs y los almacena en un diccionario.
        
        Returns:
            dict: Un diccionario con los datos obtenidos de las URLs.
        """
        if isinstance(apiManager, FileApiManager):
            
            #Crear un diccionario con los datos
            datos = {}
            #Itera sobre la lista de URLs y obtiene los datos de cada una
            for url, clave_objeto in urls:
                #Llama a la funcion get_json_from url(url) para obtener los datos JSON de la URL
                datos[clave_objeto] = apiManager.Obtener_data_json_url(url)
            #Devuelve el diccionario
            return datos
        else:
            return []
            