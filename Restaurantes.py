class Restaurante:
    def __init__(self, nombre, pruductos):
        """
        Inicializa un objeto Restaurante con un nombre y una lista de productos.
        
        Parametros:
        -Nombre: El nombre del restaurante
        -Productos: Los productos que ofrece dicho restaurante
        
        """
        self.nombre = nombre
        self.productos = pruductos
        
    def __str__(self):
        """
        Devuelve una representación en cadena del objeto Restaurante.
        """
        return f"- Restaurante: {self.nombre}\n - Productos:\n{self.str_productos()}"
    
    def str_productos(self):
        #Devuelve un string con la lista de productos formateada.
        productos_str = ""
        for producto in producto:
            productos_str += producto.show() + "\n"
        return productos_str

