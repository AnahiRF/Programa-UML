from models import *

def crear_objetos():
    peliculas = [
        Pelicula("Avatar", "Accion", 100),
        Pelicula("Titanic", "Romance", 90),
        Pelicula("Batman", "Accion", 110),
        Pelicula("Frozen", "Infantil", 80),
        Pelicula("Joker", "Drama", 95),
        Pelicula("Coco", "Animacion", 85),
        Pelicula("Up", "Animacion", 75),
        Pelicula("Matrix", "Ciencia Ficcion", 120),
        Pelicula("Rocky", "Deporte", 70),
        Pelicula("Rapidos y Furiosos", "Accion", 105),
    ]

    usuarios = [
        Usuario("Anahi", 20),
        Usuario("Won", 17),
        Usuario("Carmen", 32),
        Usuario("Maria", 19),
        Usuario("Vladimir", 16),
        Usuario("Sofia", 21),
        Usuario("Luisa", 18),
        Usuario("Jorge", 15),
        Usuario("Lucia", 23),
        Usuario("Miguel", 36),
    ]

    empleados = [
        Empleado("Roberto", "Administrador"),
        Empleado("Laura", "Taquillero"),
        Empleado("Carlos", "Limpieza"),
        Empleado("Andrea", "Gerente"),
        Empleado("Luis", "Seguridad"),
        Empleado("Daniela", "Taquillero"),
        Empleado("Fer", "Administrador"),
        Empleado("Patricia", "Mantenimiento"),
        Empleado("Mario", "Mantenimiento"),
        Empleado("Claudia", "Recepcion"),
        ]

    salas = [
        Sala(1, 50),
        Sala(2, 30),
        Sala(3, 40),
        Sala(4, 60),
        Sala(5, 45),
        Sala(6, 35),
        Sala(7, 70),
        Sala(8, 25),
        Sala(9, 55),
        Sala(10, 20),
    ]
    return peliculas, usuarios, empleados, salas

def mostrar_objetos(peliculas, usuarios, empleados, salas):
    print("Peliculas:")
    for p in peliculas:
        print(p)

    print("Usuarios:")
    for u in usuarios:
        print(u)
    
    print("Empleados:")
    for e in empleados:
        print(e.nombre, "-", e.rol)

    print("Salas:")
    for s in salas:
        print("Sala", s.numero, "- Capacidad:", s.capacidad)


def probar_metodos(peliculas, usuarios, empleados, salas):
    print("Aplicando descuento a Avatar")
    nuevo_precio = peliculas[0].aplicar_descuento(10)
    print("Nuevo precio:", nuevo_precio)

    print("Verificando mayoría de edad:")
    for u in usuarios:
        print(u.nombre, "Mayor de edad:", u.es_mayor())

    print("Empleado marcando entrada: ")
    empleados[0].marcar_entrada()
    empleados[5].marcar_entrada()
    empleados[2].marcar_entrada()
    empleados[4].marcar_entrada()
    empleados[1].marcar_entrada()
    empleados[2].marcar_entrada()
    empleados[3].marcar_entrada()
    empleados[6].marcar_entrada()
    empleados[7].marcar_entrada()
    print("Probando reserva")
    funcion = [ Funcion(peliculas[0], salas[0], "18:00"),
        Funcion(peliculas[1], salas[1], "18:00"),
        Funcion(peliculas[2], salas[2], "20:00"),
        Funcion(peliculas[3], salas[3], "14:00"),
        Funcion(peliculas[4], salas[4], "19:00"),
        Funcion(peliculas[5], salas[5], "17:00"),
        Funcion(peliculas[6], salas[6], "21:00"),
        Funcion(peliculas[7], salas[7], "15:00"),
        Funcion(peliculas[8], salas[8], "13:00"),
        Funcion(peliculas[9], salas[9], "22:00"),]
    reserva =[
        Reserva(usuarios[0], funcion[0], ["A1", "A2", "A3"]),
        Reserva(usuarios[1], funcion[1], ["B1"]),
        Reserva(usuarios[2], funcion[2], ["C1", "C2", "C3"]),
        Reserva(usuarios[3], funcion[3], ["D1"]),
        Reserva(usuarios[4], funcion[4], ["E1", "E2"]),
        Reserva(usuarios[5], funcion[5], ["F1"]),
        Reserva(usuarios[6], funcion[6], ["G1", "G2"]),
        Reserva(usuarios[7], funcion[7], ["H1"]),
        Reserva(usuarios[8], funcion[8], ["I1", "I2"]),
        Reserva(usuarios[9], funcion[9], ["J1"]),
    ]
    reserva[0].confirmar()

    print("Asientos libres:", salas[0].asientos_libres())

def main():
    peliculas, usuarios, empleados, salas = crear_objetos()
    mostrar_objetos(peliculas, usuarios, empleados, salas)
    probar_metodos(peliculas, usuarios, empleados, salas)
    
if __name__ == "__main__":
    main()