from Euro_App import Euro_App
from Interfaces.FileApiManager import FileApiManager
from Cliente import *
from Ticket import *
from Equipos import *
from Estadios import *
from Partido import *
from Euro_App import eurocopa_menu

#Codigo principal
def __main__():
    cliente = Cliente()
    equipo = Equipo()
    estadio = Estadio()
    partido = Partido()
    boleto = Ticket()
    apiManager = FileApiManager()
    
    cliente.Crear_archivo("Storage/clientes.txt")
    equipo.Crear_archivo("Storage/equipos.txt")
    estadio.Crear_archivo("Storage/estadios.txt")
    partido.Crear_archivo("Storage/partidos.txt")
    boleto.Crear_archivo("Storage/boletos.txt")
    
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
    euro2024_page.ticket = boleto.Leer_Archivo("Storage/boletos.txt", boleto.Crear_boleto)
    
    Lectura_inicial_datos_json(euro2024_page, equipo, estadio, partido)
    
    eurocopa_menu(euro2024_page)

def Lectura_inicial_datos_json(euro2024_page, equipo, estadio, partido):
    lista_equipos = equipo.Mapear_json_a_clase("DATOS_EQUIPOS:\n", "Equipo")
    lista_estadios = estadio.Mapear_json_a_clase("ESTADIOS:\n", "Estadio")
    lista_partidos = partido.Mapear_json_a_clase("DATOS_PARTIDOS:\n", "Partido")
    
    equipos_existentes = equipo.Leer_registros_existentes("Storage/equipos.txt")
    estadios_existentes = estadio.Leer_registros_existentes("Storage/estadios.txt")
    partidos_existentes = partido.Leer_registros_existentes("Storage/partidos.txt")
    
    for item in lista_equipos:
        euro2024_page.equipo.append(item)
        
        if isinstance(item, Equipo):
            item = item.to_dict()

        if not equipo.Registro_existe(equipos_existentes, item):
            equipo.Actualizar_archivo("Storage/equipos.txt", item)
    
    for item in lista_estadios:
        euro2024_page.estadio.append(item)
        
        if isinstance(item, Estadio):
            item = item.to_dict()

        if not estadio.Registro_existe(estadios_existentes, item):
            estadio.Actualizar_archivo("Storage/estadios.txt", item)
            
    for item in lista_partidos:
        
        for item_estadio in euro2024_page.estadio:
            if item_estadio.id == item.estadio:
                item.estadio = item_estadio.to_dict()
                break
            
        for item_local in euro2024_page.equipo:
            if item_local.id == item.local:
                item.local = item_local.to_dict()
                
        for item_visitante in euro2024_page.equipo:
            if item_visitante.id == item.visitante:
                item.visitante = item_visitante.to_dict()       
        
        euro2024_page.partido.append(item)
        
        if isinstance(item, Partido):
            item = item.to_dict()

        if not partido.Registro_existe(partidos_existentes, item):
            partido.Actualizar_archivo("Storage/partidos.txt", item)

if __name__==__main__():
    __main__()


