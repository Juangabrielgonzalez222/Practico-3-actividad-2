from Clase_sabor import Sabor
class Helado:
    __gramos=0
    __sabores=[]
    def __init__(self,gramos=0):
        self.__gramos=gramos
        self.__sabores=[]
    def añadirSabor(self,sabor):
        if(type(sabor)==Sabor):
            self.__sabores.append(sabor)
        else:
            print("No se pudo añadir sabor, no era un objeto valido")
    def getSabores(self):
        return self.__sabores
    def getGramos(self):
        return self.__gramos