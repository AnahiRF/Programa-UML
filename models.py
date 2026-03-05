class Persona: 
    def __init__(self, nombre):
        self.nombre = nombre

    def login(self):
        print(self.nombre, "inició sesión")

class Usuario(Persona):
    def __init__(self, nombre, edad):
        super().__init__(nombre)
        self.edad= edad

    def es_mayor(self):
        return self.edad>=18

    def __str__(self):
        return (f"Usuario: {self.nombre}, Edad: {self.edad}")

class Empleado(Persona):
    def __init__(self, nombre, rol):
        super().__init__(nombre)
        self.rol = rol

    def marcar_entrada(self):
        print(self.nombre, "marcó entrada")

class Pelicula:
    def __init__(self, nombre, genero, precio):
        self.nom=nombre
        self.gen=genero
        self.pre=precio
        

    def aplicar_descuento(self, porcentaje):
        descuento=(self.pre+porcentaje)/100
        self.pre-=descuento
        return self.pre
    def __str__(self):
        return (f"Pelicula: {self.nom}, Genero: {self.gen}, Precio: ${self.pre}")

class Espacio:
    def __init__(self, nombre):
        self.nombre = nombre

    def limpiar_espacio(self):
        print(self.nombre, "fue limpiado")
        
class Sala:
    def __init__(self,numero, capacidad):
        self.numero = numero
        self.capacidad = capacidad
        self.asientos_ocupados = []

    def asientos_libres(self):
        return self.capacidad - len(self.asientos_ocupados)
    
class Funcion:
    def __init__(self, pelicula, sala, horario):
        self.pelicula = pelicula
        self.sala = sala
        self.horario = horario

class Reserva:
    def __init__(self, usuario, funcion, asientos):
        self.usuario = usuario
        self.funcion = funcion
        self.asientos = asientos

    def confirmar(self):
        for asiento in self.asientos:
            self.funcion.sala.asientos_ocupados.append(asiento)
            print("Reserva confirmada")

    def mostrar_ticket(self):
        print("Reserva:", self.id_reserva)
        print("Usuario:", self.usuario.nombre)
        print("Película:", self.funcion.pelicula.titulo)
        print("Total:", self.monto_total)
