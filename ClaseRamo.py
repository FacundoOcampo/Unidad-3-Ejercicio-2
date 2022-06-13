class Ramo:
    __Tam=None
    __ListF=[]
    def __init__(self,Cadena,flor):
        self.__Tam=Cadena
        self.__ListF=flor
    def GetTam(self):
        return self.__Tam
    def MostrarRamoEntero(self):
        print("Tamaño: {}".format(self.__Tam))
        for i in range(len(self.__ListF)):
            print(self.__ListF[i])
