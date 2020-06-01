from Manejador_helados import ManejadorHelados
from Manejador_sabores import ManejadorSabores
from Clase_menu import Menu 
if __name__=='__main__':
    manejadorHe=ManejadorHelados()
    manejadorSa=ManejadorSabores()
    menu=Menu()
    op=None
    error=manejadorSa.cargarSabores()
    if(error!=-100):
        print("Bienvenido al programa:")
        print("A continuación se debera cargar el primer Helado:")
        menu.opcion(1, manejadorSa, manejadorHe)
        while(op!=6):
            print("Ingrese 1 para cargar un helado")
            print("Ingrese 2 para conocer los 5 sabores mas populares")
            print("Ingrese 3 para conocer los gramos vendidos de un sabor ")
            print("Ingrese 4 para saber los sabores vendidos en un tipo de helado")
            print("Ingrese 5 para realizar un test")
            print("Ingrese 6 para salir")
            op=int(input("Ingrese opcion:"))
            menu.opcion(op, manejadorSa, manejadorHe)
    else:
        print("Ocurrio un error en el archivo, fin de ejecución")