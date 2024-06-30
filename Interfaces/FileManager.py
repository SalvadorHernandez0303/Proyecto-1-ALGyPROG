from abc import ABC, abstractmethod

class FileManager(ABC):
    FilePath = ""
    
    @abstractmethod
    def Crear_archivo(self, filepath, content):
        pass
    
    @abstractmethod
    def Leer_Archivo(self, filepath):
        pass
    
    @abstractmethod
    def Actualizar_archivo(self, filepath):
        pass