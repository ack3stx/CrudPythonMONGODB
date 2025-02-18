from pymongo import MongoClient

class Padre:
    def _init_(self,id = None):
        if id == None:
            self.isArray = True
        else:
            self.isArray = False

        if self.isArray:
            self.lista_objetos = []
        else:
            self.id = id

    def agregar(self,objeto):
        if isinstance(objeto,type(self)):
            self.lista_objetos.append(objeto)
            return True
        
        return False
  
    def buscar(self,id):
        return self.lista_objetos[id]  
  
    def eliminar(self,indice):
        del self.lista_objetos[indice]
        return True
  
    def modificar(self, nuevo_objeto, indice = None):
        if indice == None:
            return False
        else:
            self.lista_objetos[indice] = nuevo_objeto
            return True

    def devolver(self):
        return self.lista_objetos
    
    def conexcionMongoDB(self,Coleccion):
        client = MongoClient("mongodb+srv://myAtlasDBUser:vmx123@myatlasclusteredu.eymom.mongodb.net/")
        db = client["PythonEjercico"]
        coleccion = db[Coleccion]
        return coleccion
        
        

