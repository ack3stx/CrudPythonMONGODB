import json
from Padre import Padre
class Clientes(Padre):
    def __init__(self, id = None, nombre = None, apellido = None, edad = None, genero = None, fecha_nacimiento = None, Clientes = None):

        if id == None and nombre == None and apellido == None and edad == None and genero == None and fecha_nacimiento == None:
            self.isArray = True
        else:
            self.isArray = False

        if self.isArray:
            super()._init_(id)
        else:
            self.id = id
            self.nombre = nombre
            self.apellido = apellido
            self.edad = edad
            self.genero = genero
            self.fecha_nacimiento = fecha_nacimiento
    
    def __str__(self):
        cadena = f' {self.id},{self.nombre},{self.apellido},{self.edad},{self.genero},{self.fecha_nacimiento} '
        return cadena
    
    def ConvertirJson(self):
        if not self.isArray:
            clientes = {"id":self.id,"nombre":self.nombre,"apellido":self.apellido,"edad":self.edad,"genero":self.genero,"fecha_nacimiento":self.fecha_nacimiento} 
        else :
            clientes = []
            for cliente in super().devolver():
                clientes.append(cliente.ConvertirJson())

        return clientes
    
    def GuardarJson(self,json_datos):
        with open('Clientes.json', 'w') as file:
            file.write(json_datos)
        return json_datos
    
    def Json(self):
        datos = self.ConvertirJson()
        json_convertido = json.dumps(datos, indent = 4)
        return self.GuardarJson(json_convertido)
    
    def CargarJson(self):
        with open('Clientes.json', 'r') as file:
            datos = json.load(file)

        return self.ConvertirJson_Objetos(datos)
    
    def ConvertirJson_Objetos(self, json_datos):
        if isinstance(json_datos, list):
            clientes = Clientes()
            for cliente in json_datos:
                nuevo_cliente = self.ConvertirJson_Objetos(cliente)
                clientes.agregar(nuevo_cliente)
        else:
            clientes = Clientes(json_datos["id"], json_datos["nombre"], json_datos["apellido"], json_datos["edad"], json_datos["genero"], json_datos["fecha_nacimiento"])
        return clientes

if __name__ == "__main__":

    # cliente1 = Clientes(1,"cliente1","apellido1", 12,"masculino","12/12/2000")
    # cliente2 = Clientes(2,"cliente2","apellido2", 24,"femenino","12/12/1999")
    # cliente3 = Clientes(3,"cliente3","apellido3", 36,"masculino","12/12/1998")

    clientes = Clientes()

    # print(clientes.agregar(cliente1))
    # print(clientes.agregar(cliente2))
    # print(clientes.agregar(cliente3))
    # print(clientes.Json())

    clientes = clientes.CargarJson()

    # interfaz = InterfazCliente(clientes)

    # interfaz.menu()

    clientes.Json()

    