class menu:
    __Switch=None
    def __init__(self):
        self.__Switch={
            1:self.Opcion1,
            2:self.Opcion2,
            3:self.Opcion3,
            0:self.Salir
        }
    def Opciones(self,Op,MF,MR):
        fun=self.__Switch.get(Op,lambda :print("Opcion Incorrecta, ingrese otro valor."))
        if Op==1 or Op==2 or Op==3 or Op==0:
            fun(MF,MR)
        else:
            fun()
    def Opcion1(self,MF,MR):
        Tam=int(input("Ingrese el tamaño del ramo 1_Chico 2_Mediano 3_Grande\n"))
        if(Tam==1 or Tam==2 or Tam==3):
            MR.CrearRamo(MF,Tam)
        else:
            print("Valor incorrecto")
    def Opcion2(self,MF,MR):
        MF.MostrarTop5()
    def Opcion3(self,MF,MR):
        Num=int(input("Ingrese el tamaño de un ramo: 1_Chico 2_Mediano 3_Grande\n"))
        MR.MostrarRamo(Num)
    def Salir(self,MF,MR):
        print("Se salio correctamente.")
