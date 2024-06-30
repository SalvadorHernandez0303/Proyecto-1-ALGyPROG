import time, ast

from Restaurantes import Restaurante
from Data import obtener_datos
from Estadios import Estadio
from Equipos import Equipo
from Partido import Partido
from Cliente import Cliente
from Ticket import Ticket



class Euro_App:
    def __init__(self):
        self.partido = []
        self.estadio = []
        self.equipo = []
        self.restaurante = []
        self.cliente = []
        self.ticket = []
    
    def precargado_datos(self):
        self.datos = obtener_datos()
        self.datos_partidos = self.datos[0]
        self.datos_estadios = self.datos[1]
        self.datos_equipos = self.datos[2]
        self.restaurante = Restaurante()
        self.cliente = Cliente()
        self.ticket = Ticket()

    def ges_partidos_equipos():
        pass
    
    def ges_venta_entradas():
        pass
    
    def ges_asistencia():
        pass
    
    def ges_restaurantes():
        pass
    
    def ges_estadisticas():
        pass
    
    def obtener_menu_seleccion(self, titulo_data, nombre_clase):
        objecto_menu_data = []
        with open("todos_datos.txt", 'r', encoding="utf-8") as f:
            titulo_encontrado = False
            for linea in f:
                linea.strip()
                if titulo_encontrado:
                    if not linea:
                        break
                    try:
                        if linea != '\n':
                            data_dict = ast.literal_eval(linea.strip())
                            if (nombre_clase == "Partido"):
                                partido_id = data_dict['id']
                                partido_numero = data_dict['number']
                                partido_local = data_dict['home']['name']
                                partido_visitante = data_dict['away']['name']
                                partido_fecha = data_dict['date']
                                objecto_menu_data.append((partido_id, partido_numero, partido_local, partido_visitante, partido_fecha))
                            else:    
                                objecto_menu_data.append(data_dict["id"])
                        else:
                            if len(objecto_menu_data) == 0:
                                pass
                            else:
                                titulo_encontrado = False
                    except (SyntaxError, ValueError) as e:
                        break
                elif linea == titulo_data:
                    titulo_encontrado = True
        return objecto_menu_data
    
    def obtener_hora_partido(self, numero_partido):
        hora_data = []
        
        with open("todos_datos.txt", 'r', encoding="utf-8") as f:
            titulo = "JORNADAS:\n"
            titulo_encontrado = False
            for linea in f:
                linea.strip()
                if titulo_encontrado:
                    if not linea:
                        break
                    try:
                        if linea != '\n':
                            data_dict = ast.literal_eval(linea.strip())
                            # print(data_dict)
                            matches = data_dict['rounds']['matches']
                            for match in matches:
                                if match['num'] == numero_partido:
                                    return match['time']
                        else:
                            if len(hora_data) == 0:
                                pass
                            else:
                                titulo_encontrado = False
                    except (SyntaxError, ValueError) as e:
                        return 0
                        break
                elif linea == titulo:
                    titulo_encontrado = True
                    
    
    def menu_opcion_uno(self, eurocopa_2024):
        print("Gracias por escogernos.")
        print("Antes de comprar una entrada, debe registrarse.")
        while True:
            nombre = str(input("Por favor, indique su nombre: "))
            if nombre:
                break
            else:
                print("No puede dejar el campo vacío. Por favor, indique su nombre.")
        while True:
            cedula = input("Ahora, indique su cédula: ")
            if cedula.isdigit():
                cedula = int(cedula)
                break
            else:
                print("La cédula debe ser un número. Por favor, intente de nuevo.")
        while True:
            edad = input("Por último, indique su edad: ")
            if edad.isdigit():
                edad = int(edad)
                break
            else:
                print("La edad debe ser un número. Por favor, intente de nuevo.")
        
        eurocopa_2024.cliente.append(Cliente(nombre, cedula, edad))
        
        print("Se ha registrado exitosamente en el sistema")
        print("")
    
    def menu_opcion_dos(self):
        print("1. Buscar partidos por un país específico.")
        print("2. Buscar partidos en un estadio en específico.")
        print("3. Buscar partidos en una fecha específica.")
        while True:
            busqueda = input("Por favor, seleccione una opción: ")
            print("")
            if busqueda.isdigit():
                busqueda = int(busqueda)
                break
            else:
                print("Su opción es inválida. Por favor, intente de nuevo.")
                
        if busqueda == 1:
            pass
        if busqueda == 2:
            pass
        if busqueda == 3:
            pass

def eurocopa_menu(eurocopa_2024: Euro_App):

    while True:
        print("Bienvenido a la Eurocopa 2024!")
        print("Menú de opciones:")
        print("1. Registro de cliente.")
        print("2. Consultas.")
        print("3. Compra de entradas.")
        print("4. Compra en el restaurante (Solo VIP).")
        print("5. Registrar asistencia al partido.")
        print("6. Reportes.")
        
        while True:
            respuesta = input("Por favor, seleccione una opción: ")
            print("")
            if respuesta.isdigit():
                respuesta = int(respuesta)
                break
            else:
                print("Su opción es inválida. Por favor, intente de nuevo.")
        
        if respuesta == 1:
            eurocopa_2024.menu_opcion_uno(eurocopa_2024)
        elif respuesta == 2:
            eurocopa_2024.menu_opcion_dos()
        elif respuesta == 3:
            print("Seleccione un partido:")
            # Partido()
            opciones_partidos = eurocopa_2024.obtener_menu_seleccion("DATOS_PARTIDOS:\n", "Partido")
            partido_identificador = []
            indice = 0
            for opciones in opciones_partidos:
                indice += 1
                partido_id, partido_numero, partido_local, partido_visitante, partido_fecha = opciones
                partido_identificador.append((indice, partido_id))
                partido_hora = eurocopa_2024.obtener_hora_partido(partido_numero)
                print(f"{indice}. {partido_local} vs. {partido_visitante} - Fecha: {partido_fecha} {partido_hora}")
            
            partido_seleccionado = int(input("\nSeleccione el número del partido que desea comprar: "))
            for pos, id in partido_identificador:
                if pos == partido_seleccionado:
                    partido_seleccionado = id
                    
            # print(partido_seleccionado)
        elif respuesta == 4:
            pass
        elif respuesta == 5:
            pass
        elif respuesta == 6:
            pass
        else:
            print("Su opción es inválida. Por favor, intente de nuevo.")
            print("")
        
        time.sleep(5)
        # partido = Partido(input)

        # print("Seleccione el tipo de entrada:")
        # print("1. General ($35)")
        # print("2. VIP ($75)")
        # tipo = input("Ingrese el número del tipo de entrada: ")
        # tipo = "General" if tipo == "1" else "VIP"

        # print("Ingrese sus datos:")
        # nombre = input("Nombre: ")
        # cedula = input("Cédula: ")
        # edad = int(input("Edad: "))

        # entrada = Ticket(tipo, partido, None)

        # print("Seleccione un asiento:")
        # Estadio.mapa_estadio()
        # fila = int(input("Ingrese la fila: "))
        # columna = int(input("Ingrese la columna: "))
        # if Estadio.seleccionar_asiento(fila, columna):
        #     entrada.asiento = f"Fila {fila}, Columna {columna}"
        # else:
        #     continue

        # precio = entrada.calcular_precio(cedula)
        # print(f"Subtotal: ${entrada.precio_base:.2f}")
        # print(f"Descuento: ${precio - entrada.precio_base:.2f}")
        # print(f"IVA: ${precio * 0.16:.2f}")
        # print(f"Total: ${precio:.2f}")

        # print("¿Desea proceder a pagar la entrada?")
        # respuesta = input("Ingrese 's' para sí o 'n' para no: ")
        # if respuesta.lower() == 's':
        #     print("Pago exitoso!")
        #     break
        # else:
        #     print("Operación cancelada.")
            
            