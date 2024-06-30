from Euro_App import Euro_App
from Cliente import *
from Data import obtener_datos
from Euro_App import eurocopa_menu

#Codigo principal
def __main__():
    cliente = Cliente()
    cliente.Crear_archivo("Storage/clientes.txt")
    data = obtener_datos()
    
    euro2024_page = Euro_App()
    euro2024_page.cliente = cliente.Leer_Archivo("Storage/clientes.txt", cliente.Crear_cliente)
    
    eurocopa_menu(euro2024_page)
    
if __name__==__main__():
    __main__()


