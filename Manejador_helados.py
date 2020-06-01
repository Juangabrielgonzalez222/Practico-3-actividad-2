from Clase_helado import Helado
class ManejadorHelados:
    __helados=[]
    def __init__(self):
        self.__helados=[]
    def agregarHelado(self,helado):
        if(type(helado)==Helado):
            self.__helados.append(helado)
        else:
            print("No se pudo añadir el helado, no era un objeto valido")
    def buscarSaboresMasPedidos(self,numero):
        numeros={}
        for i in range (1,numero+1):
            numeros[i]=0
        for helado in self.__helados:
            sabores=helado.getSabores()
            for sabor in sabores:
                numero=sabor.getNumero()
                numeros[numero]+=1
        dicOrdenado=sorted(numeros.items(),key=lambda x:x[1],reverse=True)
        lista5populares=[]
        if(len(dicOrdenado)>5):
            lista5populares=dicOrdenado[0:5]
        else:
            lista5populares=dicOrdenado
        return lista5populares
    def estimarGramosVendidos(self,numero):
        gramos=0
        for helado in self.__helados:
            sabores=helado.getSabores()
            for sabor in sabores:
                if sabor.getNumero()==numero:
                    gramos+=helado.getGramos()/len(sabores)
        return gramos
    def buscarSaboresPorTipo(self,tipo):
        nomsabores=[]
        for helado in self.__helados:
            if tipo==helado.getGramos():
                sabores=helado.getSabores()
                for sabor in sabores:
                    nombre=sabor.getNombre()
                    if(not(nombre in nomsabores)):
                        nomsabores.append(nombre)
        return nomsabores
    def test(self,manejadorSa):
        print("Test:")
        manejador2=ManejadorHelados()
        helado1=Helado(100)
        helado2=Helado(500)
        helado1.añadirSabor(manejadorSa.retornaSabor(1))
        helado1.añadirSabor(manejadorSa.retornaSabor(2))
        helado1.añadirSabor(manejadorSa.retornaSabor(3))
        helado2.añadirSabor(manejadorSa.retornaSabor(1))
        helado2.añadirSabor(manejadorSa.retornaSabor(2))
        helado2.añadirSabor(manejadorSa.retornaSabor(4))
        manejador2.agregarHelado(helado1)
        manejador2.agregarHelado(helado2)
        maspedidos=manejador2.buscarSaboresMasPedidos(manejadorSa.retornaNumerosSabores())
        print("Sabores mas pedidos:")
        for sabor in maspedidos:
            nombre=manejadorSa.retornaSabor(sabor[0])
            print(nombre.getNombre(),"con:",sabor[1])
        gramos=manejador2.estimarGramosVendidos(1)
        print("Gramos de sabor 1 vendidos:",gramos) 
        print("Sabores vendidos en helado de 100gr")
        sabores=manejador2.buscarSaboresPorTipo(100)
        for sabor in sabores:
            print(sabor)