class Persona:
    def __init__(self, id_persona, nombre, email):
        self.id_persona = id_persona
        self.nombre = nombre
        self.email = email

    def login(self):
        print(self.nombre, "ha iniciado sesión")

    def actualizar_perfil(self, nuevo_email):
        self.email = nuevo_email
        print("Email actualizado a:", self.email)


class Cliente(Persona):
    def __init__(self, id_persona, nombre, email):
        super().__init__(id_persona, nombre, email)
        self.puntos_fidelidad = 0
        self.historial_pedidos = []

    def realizar_pedido(self, pedido):
        self.historial_pedidos.append(pedido)
        self.puntos_fidelidad += 10
        print(self.nombre, "realizó un pedido")

    def consultar_historial(self):
        for p in self.historial_pedidos:
            print("Pedido:", p.id_pedido, "Total:", p.total)

    def canjear_puntos(self):
        if self.puntos_fidelidad >= 50:
            print("Canjeaste un café gratis")
            self.puntos_fidelidad -= 50
        else:
            print("No tienes suficientes puntos")


class Empleado(Persona):
    def __init__(self, id_persona, nombre, email, puestos):
        super().__init__(id_persona, nombre, email)
        
        self.rol = puestos

    def actualizar_inventario(self, producto, cantidad):
        producto.stock += cantidad
        print("Inventario actualizado")

    def cambiar_estado_pedido(self, pedido, estado):
        pedido.estado = estado
        print("Estado cambiado a", estado)


class ProductoBase:
    def __init__(self, id_producto, nombre, precio, stock):
        self.id_producto = id_producto
        self.nombre = nombre
        self.precio = precio
        self.stock = stock

    def mostrar_producto(self):
        print(self.nombre, "-", self.precio)


class Pedido:
    def __init__(self, id_pedido, cliente):
        self.id_pedido = id_pedido
        self.cliente = cliente
        self.productos = []
        self.total = 0
        self.estado = "pendiente"

    def agregar_producto(self, producto):
        self.productos.append(producto)
        self.total += producto.precio

    def mostrar_pedido(self):
        print("Pedido:", self.id_pedido)
        for p in self.productos:
            print("-", p.nombre)
        print("Total:", self.total)

class Bebida(ProductoBase):
    def __init__(self, id_producto, nombre, precio, stock, tamano, temperatura):
        super().__init__(id_producto, nombre, precio, stock)
        self.tamano = tamano
        self.temperatura = temperatura

    def calcular_precio_final(self):
        return self.precio