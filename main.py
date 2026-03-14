from models import *

productos = []
nombres =["Americano","Latte","Mocha","vainilla","Frappe","Chocolate","Caramelo","Machiat","Expreso","Capuchino"]
precios = [30,35,40,35,38,50,52,56,55,45]
for i in range(10):
    p = ProductoBase(i, nombres[i], precios[i], 20)
    productos.append(p)

print("*Lista de productos*")
for p in productos:
    p.mostrar_producto()

clientes = []
nombres_clientes = ["Ana","Luis","Carlos","María","Sofía",
"Jorge","Lucía","Pedro","Valeria","Diego"]
emails = ["jorg@mail.com","luc@mail.com","pedro@mail.com","val@mail.com","dig@mail.com","ana@mail.com","luis@mail.com","carl@mail.com","mar@mail.com","sof@mail.com",]
for i in range(5):
    c = Cliente(i, nombres_clientes[i], emails[i])
    clientes.append(c)

print("*Lista de cliente*")
for c in clientes:
    print(c.nombre, "-", c.email)

empleados = []
nombre_empleado= ["Laura","Miguel","Fernando","Patricia","Andrés","Carmen","Ricardo","Valentin","Carmen","Emilio"]
puestos =["Cajero", "Barista","Gerente","Mesero","Limpieza", "Cajero", "Barista","Gerente","Mesero","Limpieza"]
for i in range(10):
    e = Empleado(i, nombre_empleado[i], "E"+str(i), puestos[i])
    empleados.append(e)
print("*Lista de empleados*")
for e in empleados:
    print(e.nombre, "-", e.rol)

print("*Prueba*")
clientes[0].login()
clientes[0].actualizar_perfil("nuevo@email.com")
productos[0].mostrar_producto()

print("*Crear pedido*")
pedido1 = Pedido(1, clientes[0])
pedido1.agregar_producto(productos[0])
pedido1.agregar_producto(productos[1])

clientes[0].realizar_pedido(pedido1)
pedido1.mostrar_pedido()

print("*Historial*")
clientes[0].consultar_historial()
clientes[0].canjear_puntos()

print("*cambio estado*")

empleados[0].cambiar_estado_pedido(pedido1, "preparando")

empleados[0].actualizar_inventario(productos[0], 5)