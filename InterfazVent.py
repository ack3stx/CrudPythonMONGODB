from tabulate import tabulate
from Clientes import Clientes
from Productos import Producto
from Ventas import Ventas
from InterfazClient import InterfazCliente
from InterfazProd import InterfazProd
class InterfazVent:

    def __init__(self, venta = None):
        if venta == None:
            self.venta = Ventas()
            self.venta = self.venta.CargarJson()
            self.Exito = False
        else:
            self.venta = venta
            self.Exito = True

    def menu(self):
        opcion = '0'
        while opcion != '6':
            print("1. Agregar")
            print("2. Modificar")
            print("3. Eliminar")
            print("4. Buscar")
            print("5. Mostrar")
            print("6. Salir")
            opcion = input('Ingrese una opcion: ')

            if opcion == '1':
                self.Agregar()

            if opcion == '2':
                self.Modificar()

            if opcion == '3':
                self.Eliminar()

            if opcion == '4':
                self.Buscar()

            if opcion == '5':
                self.Mostrar()

            if opcion == '6':
                print('Hasta luego')

    def Agregar(self):
        id = int(input('Ingrese el id: '))
        fecha = input('Ingrese la fecha: ')
        total = float(input('Ingrese el total: '))
        print("Agregue La Informacion Del Cliente")
        cliente = InterfazCliente().Agregar()
        print("Agregue Los Productos De La Venta")
        print("----------------------------------------------------------------------")
        productos = InterfazProd(Producto()).menu()
        venta = Ventas(id, fecha, cliente, productos, total)
        self.venta.agregar(venta)
        if self.Exito == False:
            self.venta.Json()

    def Modificar(self):
        id = int(input('Ingrese el indice de la venta a modificar: '))
        id_nuevo = int(input('Ingrese el id: '))
        fecha = input('Ingrese la fecha: ')  
        print("Modificar cliente")
        cliente = InterfazCliente().Agregar()
        print("Modificar Producto")
        producto_venta = self.venta.buscar(id).productos
        productos = InterfazProd(producto_venta).menu()
        total = float(input('Ingrese el total: '))
        venta = Ventas(id_nuevo, fecha, cliente, productos, total)
        self.venta.modificar(venta, id)
        if self.Exito == False:
            self.venta.Json()
        
    def Eliminar(self):
        id = int(input('Ingrese el indice: '))
        self.venta.eliminar(id)
        if self.Exito == False:
            self.venta.Json()
        
    def Buscar(self):
        id = int(input('Ingrese el indice: '))
        venta = self.venta.buscar(id)
        print("----------------------------------------------------------------------")
        print("Venta")
        print(f"ID Venta: {venta.id}")
        print(f"Fecha: {venta.fecha}")
        print(f"Total: {venta.total}")
        print("----------------------------------------------------------------------")
        print(f"Cliente")
        print(f"Nombre: {venta.cliente.nombre} {venta.cliente.apellido}")
        print(f"Edad: {venta.cliente.edad}")
        print(f"Género: {venta.cliente.genero}")
        print(f"Fecha de Nacimiento: {venta.cliente.fecha_nacimiento}")
        print("----------------------------------------------------------------------")
        productos = []
        for producto in venta.productos.devolver():
            productos.append([producto.id, producto.nombre, producto.descripcion, producto.precio, producto.cantidad, producto.marca])
        print(tabulate(productos, headers=["ID Producto", "Nombre", "Descripción", "Precio", "Cantidad", "Marca"]))
        print("----------------------------------------------------------------------")

    def Mostrar(self):
        for venta in self.venta.devolver():
            print("----------------------------------------------------------------------")
            print("Venta")
            print(f"ID Venta: {venta.id}")
            print(f"Fecha: {venta.fecha}")
            print(f"Total: {venta.total}")
            print("----------------------------------------------------------------------")
            print(f"Cliente")
            print(f"Nombre: {venta.cliente.nombre} {venta.cliente.apellido}")
            print(f"Edad: {venta.cliente.edad}")
            print(f"Género: {venta.cliente.genero}")
            print(f"Fecha de Nacimiento: {venta.cliente.fecha_nacimiento}")
            print("----------------------------------------------------------------------")
            productos = []
            for producto in venta.productos.devolver():
                productos.append([producto.id, producto.nombre, producto.descripcion, producto.precio, producto.cantidad, producto.marca])
            print(tabulate(productos, headers=["ID Producto", "Nombre", "Descripción", "Precio", "Cantidad", "Marca"]))
            print("----------------------------------------------------------------------")

if __name__ == "__main__":

    interfaz = InterfazVent()
    interfaz.menu()