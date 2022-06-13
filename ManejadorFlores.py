import csv
from ClaseFlor import Flor
import numpy as np

class ManF:
    __Dim=0
    __Cant=0
    __Inc=1

    def __init__(self):
        self.__Dim=ManF.CalDim()
        self.__Arr=np.empty(self.__Dim,dtype=Flor)

    def CargarArchivo(self):
        Archivo=open("Flores.csv","r",encoding="utf-8")
        Reader=csv.reader(Archivo,delimiter=";")
        for fila in Reader:
            if self.__Dim== self.__Cant:
                self.__Dim=self.__Inc+self.__Dim
                self.__Arr.resize(self.__Dim)
            NuevaFlor=Flor(int(fila[0]),fila[1],fila[2],fila[3])
            self.__Arr[self.__Cant]=NuevaFlor
            self.__Cant=self.__Cant+1
        Archivo.close()

    def MostrarFlores(self):
        for i in range(len(self.__Arr)):
            print(self.__Arr[i])

    def Buscar(self,ID):
        Num=-1
        for i in range(len(self.__Arr)):
            if self.__Arr[i].GetId()==ID:
                Num=self.__Arr[i]
        return Num

    def MostrarTop5(self):
        ListAux=[]
        for i in range(len(self.__Arr)):
            ListAux.append(self.__Arr[i])
        ListAux.sort(key= lambda  x: x.GetCont(),reverse=True)
        print("Lista del top 5 flores mas vendidas en cada ramo")
        for i in range(5):
            print(ListAux[i])

    @classmethod
    def CalDim(cls):
        Archi=open("Flores.csv","r",encoding="utf-8")
        Reader=csv.reader(Archi,delimiter=";")
        Cont=0
        for fila in Reader:
            Cont=Cont+1
        return Cont
