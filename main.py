from ClassMenu import menu
from ManejadorRamo import ManR
from ManejadorFlores import ManF

if __name__=='__main__':
    NuevoM=menu()
    NuevoMF=ManF()
    NuevoMR=ManR()
    NuevoMF.CargarArchivo()
    Num=int(input("Seleccione una opcion:\n1_Registrar un ramo vendido.\n2_Mostrar el nombre de las 5 flores  más pedidas en un ramo\n3_Ingresar por teclado un tipo de ramo y mostrar las flores vendidas en ese tamaño\n0_Salir\n------------------------------------------\n"))
    NuevoM.Opciones(Num,NuevoMF,NuevoMR)
    while(Num!=0):
        Num=int(input("----------Seleccione una opcion:----------\n1_Registrar un ramo vendido.\n2_Mostrar el nombre de las 5 flores  más pedidas en un ramo\n3_Ingresar por teclado un tipo de ramo y mostrar las flores vendidas en ese tamaño\n0_Salir\n------------------------------------------\n"))
        NuevoM.Opciones(Num,NuevoMF,NuevoMR)
