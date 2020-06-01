import csv
from Clase_sabor import Sabor
class ManejadorSabores:
    __sabores=[]
    def __init__(self):
        self.__sabores=[]
    def agregarSabor(self,sabor):
        if(type(sabor)==Sabor):
            self.__sabores.append(sabor)
        else:
            print("No se pudo añadir sabor, no era un objeto valido")
    def cargarSabores(self):
        archivo=open("sabores.csv")
        reader=csv.reader(archivo,delimiter=";")
        error=None
        numero=1
        for fila in reader:
            if(len(fila)==2):
                self.agregarSabor(Sabor(numero,fila[0],fila[1]))
                numero+=1
            else:
                print("Hay un error en una linea del archivo, por favor revisar el archivo")
                error=-100
        archivo.close()
        return error
    def mostrarSabores(self):
        print("Numero:, Sabor:")
        for sabor in self.__sabores:
            print("{}:  {}".format(sabor.getNumero(),sabor.getNombre()))
    def retornaSabor(self,numero):
        busqueda=self.buscarSaborPornumero(numero)
        if(busqueda!=-1):
            return self.__sabores[busqueda]
        else:
            print("No se encontro el sabor indicado")
    def buscarSaborPornumero(self,numero):
        valor=-1
        for v,sa in enumerate (self.__sabores):
            if (numero==sa.getNumero()):
                valor=v
        return valor
    def retornaNumerosSabores(self):
        return len(self.__sabores)