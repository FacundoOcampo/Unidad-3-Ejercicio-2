class Flor:
    __Num=None
    __Nom=None
    __Color=None
    __Des=None
    def __init__(self,Id,Nombre,Color,Descripcion):
        self.__Num=Id
        self.__Nom=Nombre
        self.__Color=Color
        self.__Des=Descripcion
        self.__Cont=0
    def __str__(self):
        return "{:4d} {:17}{:15}{:10}".format(self.__Num,self.__Nom,self.__Color,self.__Des)
    def GetId(self):
        return self.__Num
    def Cont(self):
        self.__Cont=self.__Cont+1
    def GetCont(self):
        return self.__Cont
