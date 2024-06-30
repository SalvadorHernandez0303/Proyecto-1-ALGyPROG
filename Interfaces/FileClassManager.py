import os, json
from Interfaces.FileManager import *

class FileClassManager(FileManager):
    
    def Crear_archivo(self, filepath):
        if not self.Archivo_existe(filepath):
            with open(filepath, "w", encoding="utf-8") as f:
                f.write("[]\n")

    def Leer_Archivo(self, filepath, constructor):
        objetos = []
        with open(filepath, "r", encoding="utf-8") as f:
            data = json.load(f)
            for registro_str in data:
                registro = json.loads(registro_str)
                obj = constructor(registro)
                objetos.append(obj)
        return objetos
    
    def Actualizar_archivo(self, filepath, content):
        
        # archivo_vacio = self.Archivo_validar_vacio(filepath) == 0
        
        with open(filepath, "r+", encoding="utf-8") as f:
            
            try:
                data = self.Leer_archivo_para_actualizacion(f)
            except json.JSONDecodeError:
                data = []
            
            data.append(content)
            
            f.seek(0)
            json.dump(data, f, indent=2)
            f.truncate()
    
    def Archivo_validar_vacio(self, filepath):
        return os.path.isfile(filepath) and os.path.getsize(filepath)
    
    def Leer_archivo_para_actualizacion(self, file):
        return json.load(file)