from tabulate import tabulate
from Productos import Producto
class InterfazProd:
    def __init__(self, producto = None):
        if producto == None:
            self.producto = Producto()
            self.producto = self.producto.CargarJson()
            self.isVenta = False
        else:
            self.producto = producto
            self.isVenta = True

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

            elif opcion == '2':
                self.Modificar()
            
            elif opcion == '3':
                self.Eliminar()

            elif opcion == '4':
                self.Buscar()

            elif opcion == '5':
                self.Mostrar()

            elif opcion == '6':
                print('Hasta luego')
                return self.producto
            
    def Agregar(self):
        id = int(input('Ingrese el id: '))
        nombre = input('Ingrese el nombre: ')
        descripcion = input('Ingrese la descripcion: ')
        precio = float(input('Ingrese el precio: '))
        cantidad = int(input('Ingrese la cantidad: '))
        marca = input('Ingrese la marca: ')
        producto = Producto(id, nombre, descripcion, precio, cantidad, marca)
        self.producto.agregar(producto)
        if self.isVenta == False:
            self.producto.Json()

    def Modificar(self):
        id = int(input('Ingrese el indice del producto a modificar: '))
        id_nuevo = int(input('Ingrese el id: '))
        nombre = input('Ingrese el nombre: ')
        descripcion = input('Ingrese la descripcion: ')
        precio = float(input('Ingrese el precio: '))
        cantidad = int(input('Ingrese la cantidad: '))
        marca = input('Ingrese la marca: ')
        producto = Producto(id_nuevo, nombre, descripcion, precio, cantidad, marca)
        self.producto.modificar(producto, id)
        if self.isVenta == False:
            self.producto.Json()

    def Eliminar(self):
        id = int(input('Ingrese el indice: '))
        self.producto.eliminar(id)
        if self.isVenta == False:
            self.producto.Json()

    def Buscar(self):
        id = int(input('Ingrese el indice: '))
        producto = self.producto.buscar(id)
        print("----------------------------------------------------------------------")
        print(f"Productos")
        print(f"Nombre: {producto.nombre}")
        print(f"Descripcion: {producto.descripcion}")
        print(f"Precio: {producto.precio}")
        print(f"Cantidad: {producto.cantidad}")
        print(f"Marca: {producto.marca}")
        print("----------------------------------------------------------------------")

    def Mostrar(self):
        productos = []
        for producto in self.producto.devolver():
            productos.append([producto.id, producto.nombre, producto.descripcion, producto.precio, producto.cantidad, producto.marca])
        print(tabulate(productos, headers=["ID Producto", "Nombre", "Descripción", "Precio", "Cantidad", "Marca"]))

if __name__ == "__main__":

    interfaz = InterfazProd()
    interfaz.menu()