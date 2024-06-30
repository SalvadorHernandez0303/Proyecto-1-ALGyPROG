from Euro_App import Euro_App
from Data import obtener_datos
from Euro_App import eurocopa_menu

#Codigo principal
def __main__():
    data = obtener_datos()
    euro2024_page = Euro_App()
    eurocopa_menu(euro2024_page)
    
if __name__==__main__():
    __main__()


