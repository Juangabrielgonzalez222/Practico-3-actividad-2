class Sabor:
    __numero=0
    __nombre=""
    __descripcion=""
    def __init__(self,numero,nombre,descripcion):
        self.__numero=numero
        self.__nombre=nombre
        self.__descripcion=descripcion
    def getNumero(self):
        return self.__numero
    def getNombre(self):
        return self.__nombre
    def getDescripcion(self):
        return self.__descripcion
    
        