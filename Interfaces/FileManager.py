from abc import ABC, abstractmethod
import os

class FileManager(ABC):
    FilePath = ""
    
    @abstractmethod
    def Crear_archivo(self, filepath):
        pass
    
    @abstractmethod
    def Leer_Archivo(self, filepath):
        pass
    
    @abstractmethod
    def Actualizar_archivo(self, filepath):
        pass
    
    def Archivo_existe(self, filepath):
        return os.path.exists(filepath)