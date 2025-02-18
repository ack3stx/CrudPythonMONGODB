import json
from Clientes import Clientes
from Productos import Producto
from Padre import Padre

class Ventas(Padre):

    def __init__(self, id = None, fecha = None, cliente = None, productos = None, total = None):

        if id == None and fecha == None and cliente == None and productos == None and total == None:
            self.isArray = True
        else:
            self.isArray = False

        if self.isArray:
            super()._init_(id)
        else:
            self.id = id
            self.fecha = fecha
            self.cliente = cliente
            self.productos = productos
            self.total = total

    def __str__(self):

        cadena = f' {self.id},{self.fecha},{self.cliente},{self.productos.ConvertirJson()},{self.total} '
        return cadena
    
    def ConvertirJson(self):
        if not self.isArray:
            ventas = {"id":self.id,"fecha":self.fecha,"cliente":self.cliente,"productos":self.productos,"total":self.total} 
        else :
            ventas = []
            for venta in super().devolver():
                cliente = venta.cliente.ConvertirJson()
                productos = venta.productos.ConvertirJson()
                lista_ventas = {"id": venta.id, "fecha": venta.fecha, "cliente": cliente, "productos": productos, "total": venta.total}
                ventas.append(lista_ventas)
        return ventas
    
    def GuardarJson(self,json_datos):
        with open('Ventas.json', 'w') as file:
            file.write(json_datos)
        return json_datos
    
    def Json(self):
        datos = self.ConvertirJson()
        json_convertido = json.dumps(datos, indent = 4)
        return self.GuardarJson(json_convertido)

    def CargarJson(self):
        with open('Ventas.json', 'r') as file:
            datos = json.load(file)

        return self.ConvertirJson_Objetos(datos)
    
    def ConvertirJson_Objetos(self, json_datos):
        if isinstance(json_datos, list):
            ventas = Ventas()
            for venta in json_datos:
                nueva_venta = self.ConvertirJson_Objetos(venta)
                ventas.agregar(nueva_venta)
        else:
            cliente_data = json_datos["cliente"]
            cliente = Clientes()
            cliente = cliente.ConvertirJson_Objetos(cliente_data)
            productos_data = json_datos["productos"]
            productos = Producto()
            productos = productos.ConvertirJson_Objetos(productos_data)

            ventas = Ventas(json_datos["id"], json_datos["fecha"], cliente, productos, json_datos["total"])
        return ventas

        

if __name__ == "__main__":

    productos = Producto()
    productos.agregar(Producto(1,"producto1","descripcion1", 100,12,"marca1"))
    productos.agregar(Producto(2,"producto2","descripcion2",600,6,"marca2"))
    productos.agregar(Producto(3,"producto3","descripcion3",50,5,"marca3"))

    cliente1 = Clientes(1, "Juan", "Perez", 30, "M", "1991-01-01")
    cliente2 = Clientes(2, "Maria", "Lopez", 25, "F", "1996-01-01")
    cliente3 = Clientes(3, "Pedro", "Gomez", 35, "M", "1986-01-01")
    venta1 = Ventas(1, "2021-10-01", cliente1, productos, 20)
    venta2 = Ventas(2, "2021-10-02", cliente2, productos, 30)
    venta3 = Ventas(3, "2021-10-03", cliente3, productos, 40)
    ventaNueva = Ventas(4, "2021-10-04", cliente1, productos, 50)

    ventas = Ventas()
    ventas.agregar(venta1)
    ventas.agregar(venta2)
    ventas.agregar(venta3)

    # print(ventas.devolver()[0].productos.devolver())
    # ventas.eliminar(0)

    # ventas.modificar(ventaNueva, 1)

    print(ventas.Json())
    ventas = ventas.CargarJson()

    # ventaNueva = Ventas(5, "2021-10-14", cliente1, productos, 20)
    # ventas.agregar(ventaNueva)
    print(ventas.Json())

    