class Menu:
    __switcher=None
    def __init__(self):
        self.__switcher = { 1:self.opcion1,
                            2:self.opcion2,
                            3:self.opcion3,
                            4:self.opcion4,
                            5:self.opcion5,
                            6:self.salir
                         }
    def opcion(self,op,manejadorSa,manejadorHe):
        func=self.__switcher.get(op, lambda: print("Opción no válida"))
        func(manejadorSa,manejadorHe)
    def salir(self,manejadorSa,manejadorHe):
        print('Usted salio del programa')
    def opcion1(self,manejadorSa,manejadorHe):
        from Clase_helado import Helado
        opciones={1:100,2:150,3:250,4:500,5:1000,6:-1}
        opcion=0
        gr=None
        while(opcion>6 or opcion<1):
            print("Opciones:")
            print("1: 100 gr")
            print("2: 150 gr")
            print("3: 250 gr")
            print("4: 500 gr")
            print("5: 1000 gr")
            opcion=int(input("Ingrese la cantidad de gramos con 1-5 o 6 para salir:"))
            while(opcion>6 or opcion<1):
                print("Opción incorrecta")
                opcion=int(input("Ingrese la cantidad de gramos con 1-5 o 6 para salir:"))
            gr=opciones.get(opcion)
        if(gr!=-1):
            helado=Helado(gr)
            opcion=None
            while(opcion!="n"):
                manejadorSa.mostrarSabores()
                opcion=int(input("Ingresa el numero de sabor:"))
                numerosabores=manejadorSa.retornaNumerosSabores()
                while(opcion>numerosabores or opcion<1):
                    print("opción incorrecta")
                    opcion=int(input("Ingresa el numero de sabor:"))
                sabor=manejadorSa.retornaSabor(opcion)
                helado.añadirSabor(sabor)
                opcion=input("Desea añadir mas sabores, 's' para si o 'n' para no:")
                while(opcion!="s" and opcion!="n"):
                    opcion=input("Desea añadir mas sabores, 's' para si o 'n' para no:")
            manejadorHe.agregarHelado(helado)
    def opcion2(self,manejadorSa,manejadorHe):
        numeros=manejadorSa.retornaNumerosSabores()
        sabores=manejadorHe.buscarSaboresMasPedidos(numeros)
        print("Sabores mas elegidos:")
        for sabor in sabores:
            nombre=manejadorSa.retornaSabor(sabor[0])
            print(nombre.getNombre(),"cantidad: ",sabor[1])
    def opcion3(self,manejadorSa,manejadorHe):
        print("Sabores:")
        manejadorSa.mostrarSabores()
        numero=int(input("Ingrese numero:"))
        numerosabores=manejadorSa.retornaNumerosSabores()
        if(numero>numerosabores or numero<1):
            print("Numero incorrecto")
        else:
            gramos=manejadorHe.estimarGramosVendidos(numero)
            sabor=manejadorSa.retornaSabor(numero)
            print("Para el sabor {} la cantidad de gramos vendidos es: {:.2f}gr".format(sabor.getNombre(),gramos))
    def opcion4(self,manejadorSa,manejadorHe):
        opciones={1:100,2:150,3:250,4:500,5:1000}
        print("Opciones:")
        print("1: 100 gr")
        print("2: 150 gr")
        print("3: 250 gr")
        print("4: 500 gr")
        print("5: 1000 gr")
        opcion=int(input("Ingrese numero de helado:"))
        while(opcion>5 or opcion<1 ):
            print("Numero incorrecto de helado")
            opcion=int(input("Ingrese numero de helado:"))
        opcion=opciones.get(opcion)
        nombres=manejadorHe.buscarSaboresPorTipo(opcion)
        if (len(nombres)==0):
            print("No se vendio ningún helado del tipo ingresado")
        else:
            print("Sabores vendidos:")
            for nombre in nombres:
                print(nombre)
    def opcion5(self,manejadorSa,manejadorHe):
        manejadorHe.test(manejadorSa)