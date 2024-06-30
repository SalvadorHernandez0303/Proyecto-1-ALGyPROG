from Euro_App import Euro_App
from Interfaces.FileApiManager import FileApiManager
from Cliente import *
from Ticket import *
from Partido import Partido
from Euro_App import eurocopa_menu

#Codigo principal
def __main__():
    cliente = Cliente()
    boleto = Ticket()
    partido = Partido()
    apiManager = FileApiManager()
    
    cliente.Crear_archivo("Storage/clientes.txt")
    boleto.Crear_archivo("Storage/boletos.txt")
    partido.Crear_archivo("Storage/partidos.txt")
    
    urls = [
        ("https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/teams.json", "datos_equipos"),
        ("https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/stadiums.json", "estadios"),
        ("https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/matches.json", "datos_partidos"),
        ("https://raw.githubusercontent.com/Algoritmos-y-Programacion/api-proyecto/main/rounds.json", "jornadas")
    ]
    FilePath_carga_inicial = "todos_datos.txt"
    
    apiManager.Crear_archivo(FilePath_carga_inicial)
    data = apiManager.Mapear_datos(urls, apiManager)
    apiManager.Actualizar_archivo(FilePath_carga_inicial, data)
    
    euro2024_page = Euro_App()
    euro2024_page.cliente = cliente.Leer_Archivo("Storage/clientes.txt", cliente.Crear_cliente)
    
    eurocopa_menu(euro2024_page)
    
if __name__==__main__():
    __main__()


