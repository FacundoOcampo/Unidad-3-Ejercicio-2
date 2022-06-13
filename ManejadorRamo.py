from ClaseRamo import Ramo
class ManR:
    __List=None
    def __init__(self):
        self.__List=[]
    def CrearRamo(self,MF,Tam):
        print("Ingrese el id la/s Flor/es. 0 para salir")
        MF.MostrarFlores()
        Num=0
        ListAux=[]
        while Num < Tam:
            Id=int(input())
            Aux=MF.Buscar(Id)
            if Aux ==-1:
                print("Id no valido, ingrese otro id")
            else:
                Aux.Cont()
                ListAux.append(Aux)
                Num=Num+1
        NuevoRamo=Ramo(Tam,ListAux)
        self.__List.append(NuevoRamo)

    def MostrarRamo(self,Num):
        for ramo in self.__List:
            if ramo.GetTam()==Num:
                ramo.MostrarRamoEntero()
