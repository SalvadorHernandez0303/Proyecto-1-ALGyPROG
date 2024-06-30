import time, ast, json

from Interfaces.FileApiManager import FileApiManager
from Restaurantes import Restaurante
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
    
    def precargado_datos(self, data):
        self.datos = FileApiManager().Mapear_datos(data)
        self.datos_partidos = self.datos[0]
        self.datos_estadios = self.datos[1]
        self.datos_equipos = self.datos[2]
        self.restaurante = Restaurante()
        self.cliente = Cliente()
        self.ticket = Ticket()
    
    def obtener_menu_seleccion(self, titulo_data, nombre_clase):
        """
    Obtiene los datos de un menú seleccionado desde un archivo.
    
    Parámetros:
    self: Instancia de la clase que llama al método.
    titulo_data (str): Título del menú que se busca.
    nombre_clase (str): Nombre de la clase que se utiliza para filtrar los datos.
    
    Retorna:
    list: Lista de objetos que se encuentran en el menú seleccionado.
        """
        # Se crea una lista vacía para almacenar los datos del menú seleccionado
        objecto_menu_data = []
        # Se abre el archivo "todos_datos.txt" en modo de lectura
        with open("todos_datos.txt", 'r', encoding="utf-8") as f:
            # Se busca el título del menú en el archivo
            titulo_encontrado = False
            for linea in f:
                # Se elimina el espacio en blanco al final de la línea
                linea.strip()
                if titulo_encontrado:
                    # Si se encuentra el título, se itera sobre las líneas siguientes
                    if not linea:
                        # Si se encuentra una línea vacía, se sale del ciclo
                        break
                    try:
                        # Se intenta evaluar la línea como un diccionario
                        if linea != '\n':
                            data_dict = ast.literal_eval(linea.strip())
                            # Se filtran los datos según la clase
                            if nombre_clase == "Partido":
                                # Se extraen los datos del partido
                                partido_id = data_dict['id']
                                partido_numero = data_dict['number']
                                partido_local = data_dict['home']['name']
                                partido_visitante = data_dict['away']['name']
                                partido_fecha = data_dict['date']
                                # Se agrega el partido a la lista de datos
                                objecto_menu_data.append((partido_id, partido_numero, partido_local, partido_visitante, partido_fecha))
                            else:
                                # Se agrega el id del objeto a la lista de datos    
                                objecto_menu_data.append(data_dict["id"])
                        else:
                            # Si se encuentra una línea vacía, se sale del ciclo
                            if len(objecto_menu_data) == 0:
                                pass
                            else:
                                titulo_encontrado = False
                    except (SyntaxError, ValueError) as e:
                        # Si ocurre un error, se sale del ciclo
                        break
                elif linea == titulo_data:
                    # Se encuentra el título del menú
                    titulo_encontrado = True
        # Se devuelve la lista de datos del menú seleccionado
        return objecto_menu_data
    
    def obtener_hora_partido(self, numero_partido):
        """
    Obtiene la hora de un partido desde un archivo.
    
    Parámetros:
    self: Instancia de la clase que llama al método.
    numero_partido (int): Número del partido que se busca.
    
    Retorna:
    str: Hora del partido.
        """
        # Se crea una lista vacía para almacenar la hora del partido
        hora_data = []
        # Se abre el archivo "todos_datos.txt" en modo de lectura
        with open("todos_datos.txt", 'r', encoding="utf-8") as f:
            # Se busca el título "JORNADAS:" en el archivo
            titulo = "JORNADAS:\n"
            titulo_encontrado = False
            for linea in f:
                # Se elimina el espacio en blanco al final de la línea
                linea.strip()
                if titulo_encontrado:
                    if not linea:
                        # Si se encuentra una línea vacía, se sale del ciclo
                        break
                    try:
                        if linea != '\n':
                            data_dict = ast.literal_eval(linea.strip())
                            # Si se encuentra una línea vacía, se sale del ciclo
                            # print(data_dict)
                            matches = data_dict['rounds']['matches']
                            for match in matches:
                                if match['num'] == numero_partido:
                                    # Se devuelve la hora del partido
                                    return match['time']
                        else:
                            if len(hora_data) == 0:
                                pass
                            else:
                                titulo_encontrado = False
                    except (SyntaxError, ValueError) as e:
                        # Si ocurre un error, se devuelve 0
                        return 0
                        break
                elif linea == titulo:
                    # Se encuentra el título "JORNADAS:"
                    titulo_encontrado = True
                    
    def menu_opcion_uno_reg_cli(self, eurocopa_2024):
        """
    Muestra el menú de registro de cliente.
    
    Parámetros:
    self: Instancia de la clase que llama al método.
    eurocopa_2024: Instancia de la clase Euro_App.
        """
        if isinstance(eurocopa_2024, Euro_App):
            print("Gracias por escogernos.")
            print("Antes de comprar una entrada, debe registrarse.")
            # Se solicita el nombre del cliente
            while True:
                nombre = str(input("Por favor, indique su nombre: "))
                if nombre:
                    # Si el nombre no está vacío, se sale del ciclo
                    break
                else:
                    print("No puede dejar el campo vacío. Por favor, indique su nombre.")
            # Se solicita la cédula del cliente
            while True:
                cedula = input("Ahora, indique su cédula: ")
                if cedula.isdigit():
                    # Si la cédula es un número, se sale del ciclo
                    cedula = int(cedula)
                    break
                else:
                    print("La cédula debe ser un número. Por favor, intente de nuevo.")
            # Se solicita la edad del cliente
            while True:
                edad = input("Por último, indique su edad: ")
                if edad.isdigit():
                    # Si la edad es un número, se sale del ciclo
                    edad = int(edad)
                    break
                else:
                    print("La edad debe ser un número. Por favor, intente de nuevo.")
            # Se crea un objeto Cliente con los datos del cliente
            
            cliente_nuevo = Cliente(nombre, cedula, edad)
            eurocopa_2024.cliente.append(cliente_nuevo)
            
            cliente_nuevo_json = json.dumps({
                "nombre": cliente_nuevo.nombre,
                "cedula": cliente_nuevo.cedula,
                "edad": cliente_nuevo.edad
            })
            
            cliente_nuevo.Actualizar_archivo("Storage/clientes.txt", str(cliente_nuevo_json))
            
            print("Se ha registrado exitosamente en el sistema")
            print("")
        else:
            raise TypeError("Clase incorrecta entregada. Por favor, revisar el código")
    
    def menu_opcion_dos_ges_par_asis(self):
        """
    Muestra el menú de consultas de partidos y estadios.
        """
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
    
    def menu_opcion_tres_comp_tkt(self, eurocopa_2024):
        if isinstance(eurocopa_2024, Euro_App):
            while True:
                cedula = input("Para comprar un boleto, debe indicar su cédula para verificar que está registrado(a). Ingrese su cédula a continuación: ")
                if cedula.isdigit():
                    # Si la cédula es un número, se sale del ciclo
                    cedula = int(cedula)
                    break
                else:
                    print("La cédula debe ser un número. Por favor, intente de nuevo.")
            
            Cedula_registrada = False

            for item in eurocopa_2024.cliente:
                if cedula == item.cedula:
                    Cedula_registrada = True
                    break
            
            if Cedula_registrada:      
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
            else:
                print("La cédula no está registrada. Por favor, registrese en el sistema usando la opción 1 del menú.\n")
        else:
            raise TypeError("Clase incorrecta entregada. Por favor, revisar el código")

def eurocopa_menu(eurocopa_2024: Euro_App):

    while True:
        print("Bienvenido a la Eurocopa 2024!")
        print("Menú de opciones:")
        print("1. Registro de cliente.") # Mitad de gestion de venta de entrada
        print("2. Consultas.") # Gestion de partidos y estadios
        print("3. Compra de entradas.") # Mitad de destion de venta de entrada
        print("4. Compra en el restaurante (Solo VIP).") # Gestion restaurante/venta restaurante
        print("5. Registrar asistencia al partido.") # Gestion de asistencia de partido
        print("6. Reportes.") # Gestion de estadistica
        
        while True:
            respuesta = input("Por favor, seleccione una opción: ")
            print("")
            if respuesta.isdigit():
                respuesta = int(respuesta)
                break
            else:
                print("Su opción es inválida. Por favor, intente de nuevo.")
        
        if respuesta == 1:
            eurocopa_2024.menu_opcion_uno_reg_cli(eurocopa_2024)
        elif respuesta == 2:
            eurocopa_2024.menu_opcion_dos_ges_par_asis()
        elif respuesta == 3:
            eurocopa_2024.menu_opcion_tres_comp_tkt(eurocopa_2024)
        elif respuesta == 4:
            pass
        elif respuesta == 5:
            pass
        elif respuesta == 6:
            pass
        else:
            print("Su opción es inválida. Por favor, intente de nuevo.")
            print("")
        
        time.sleep(1)
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
            
            