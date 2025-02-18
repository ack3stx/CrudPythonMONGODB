import json
from Padre import Padre
class Producto(Padre):

    def __init__(self, id = None, nombre = None, descripcion = None, precio = None, cantidad = None, marca = None):

        if id == None and nombre == None and descripcion == None and precio == None and cantidad == None and marca == None:
            self.isArray = True
        else:
            self.isArray = False 
    
        if not self.isArray:
            self.id=id
            self.nombre=nombre
            self.descripcion=descripcion
            self.precio=precio
            self.cantidad=cantidad
            self.marca=marca
        else:
            super()._init_(id)

    def __str__(self):
        cadena = f' {self.id},{self.nombre},{self.descripcion},{self.precio},{self.cantidad},{self.marca} '
        return cadena
    
    def ConvertirJson(self):
        if not self.isArray:
            productos = {"id":self.id,"nombre":self.nombre,"descripcion":self.descripcion,"precio":self.precio,"cantidad":self.cantidad,"marca":self.marca} 
        else :
            productos = []
            for producto in super().devolver():
                productos.append(producto.ConvertirJson())
        return productos

    def GuardarJson(self,json_datos):
        with open('Productos.json', 'w') as file:
            file.write(json_datos)
        return json_datos

    def Json(self):
        datos = self.ConvertirJson()
        json_convertido = json.dumps(datos, indent = 4)
        return self.GuardarJson(json_convertido)
    
    def CargarJson(self):
        with open('Productos.json', 'r') as file:
            datos = json.load(file)
        
        return self.ConvertirJson_Objetos(datos)
    
    def ConvertirJson_Objetos(self, json_datos):
        if isinstance(json_datos, list):
            productos = Producto()
            for producto in json_datos:
                nuevo_producto = self.ConvertirJson_Objetos(producto)
                productos.agregar(nuevo_producto)
        else:
            productos = Producto(json_datos["id"], json_datos["nombre"], json_datos["descripcion"], json_datos["precio"], json_datos["cantidad"], json_datos["marca"])
        return productos

if __name__ == "__main__":
    # producto1 = Producto(1,"producto1","descripcion1", 100,12,"marca1")
    # producto2 = Producto(2,"producto2","descripcion2",600,6,"marca2")
    # producto3 = Producto(3,"producto3","descripcion3",50,5,"marca3")

    productos = Producto()
    # print(productos.agregar(producto1))
    # print(productos.agregar(producto2))
    # print(productos.agregar(producto3))
    # print(productos.Json())

    
    # productos = productos.CargarJson()

    # productos.Json()

