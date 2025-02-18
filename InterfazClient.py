from tabulate import tabulate
from Clientes import Clientes
from pymongo import MongoClient

class InterfazCliente:
    def __init__(self, cliente = None):
        if cliente == None:
            self.cliente = Clientes()
            self.cliente = self.cliente.CargarJson()
            self.isCliente = False
        else:
            self.cliente = cliente
            self.isCliente = True
    
    def menu(self):
        opcion = '0'
        while opcion != '6':
            print("1. Agregar")
            print("2. Modificar")
            print("3. Eliminar")
            print("4. Buscar")
            print("5. Mostrar")
            print("6. Salir")
            opcion = input("Ingrese una opcion: ")
            
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

    def Agregar(self):
        id = int(input('Ingrese el id: '))
        nombre = input('Ingrese el nombre: ')
        apellido = input('Ingrese el apellido: ')
        edad = int(input('Ingrese la edad: '))
        genero = input('Ingrese la genero: ')
        fecha_nacimiento = input('Ingrese la fecha de nacimiento: ')
        cliente = Clientes(id, nombre, apellido, edad, genero, fecha_nacimiento)
        self.cliente.agregar(cliente)
        self.InsertarDB(cliente.Json())
        if self.isCliente == False:
            self.cliente.Json()
        return cliente
        
    def Modificar(self):
        id = int(input('Ingrese el indice del cliente a modificar: '))
        id_nuevo = int(input('Ingrese el id: '))
        nombre = input('Ingrese el nombre: ')
        apellido = input('Ingrese el apellido: ')
        edad = int(input('Ingrese la edad: '))
        genero = input('Ingrese la genero: ')
        fecha_nacimiento = input('Ingrese la fecha de nacimiento: ')
        cliente = self.cliente.ConvertirJson_Objetos({'id': id_nuevo, 'nombre': nombre, 'apellido': apellido, 'edad': edad, 'genero': genero, 'fecha_nacimiento': fecha_nacimiento})
        self.cliente.modificar(cliente, id)
        if self.isCliente == False:
            self.cliente.Json()

    def Eliminar(self):
        id = int(input('Ingrese el indice: '))
        self.cliente.eliminar(id)
        if self.isCliente == False:
            self.cliente.Json()

    def Buscar(self):
        id = int(input('Ingrese el indice: '))
        cliente = self.cliente.buscar(id)
        print("----------------------------------------------------------------------")
        print(f"Cliente")
        print(f"Nombre: {cliente.nombre} {cliente.apellido}")
        print(f"Edad: {cliente.edad}")
        print(f"Género: {cliente.genero}")
        print(f"Fecha de Nacimiento: {cliente.fecha_nacimiento}")
        print("----------------------------------------------------------------------")

    def Mostrar(self):
        clientes = []
        for cliente in self.cliente.devolver():
            clientes.append([cliente.id, cliente.nombre, cliente.apellido, cliente.edad, cliente.genero, cliente.fecha_nacimiento])
        print(tabulate(clientes, headers=["ID", "Nombre", "Apellido", "Edad", "Genero", "Fecha de Nacimiento"]))


    
    def InsertarDB(Self,cliente = None):
        coleccion = Clientes().conexcionMongoDB("Clientes")
        resultado = coleccion.insert_one(cliente)
        print(f"Documento insertado con ID: {resultado.inserted_id}")
    
if __name__ == "__main__":

    interfaz = InterfazCliente()
    interfaz.menu()