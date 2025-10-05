
import os
os.system("cls")

class Coches:

    #Atributos o propiedades (variables)
    #Caracteristicas del coche
    #valores iniciales es posible declarar al principio de una clase
    def __init__(self,marca,color,modelo,velocidad,caballaje,plazas):
        self.__marca=marca
        self.__color=color
        self.__modelo=modelo
        self.__velocidad=velocidad
        self.__caballaje=caballaje
        self.__plazas=plazas
    
        


    #Crear los metodos setters y getters. estos metodos son importantes y necesarios en todas las clases para que
    #programador interactue con los valores de los atributos a traves de estos metodos, digamos que es la manera
    #mas adecuada y recomendada para solicitar un valor (get) y/o para ingresar o cambiar un valor (set) a un 
    #atributo en particular de la clase a traves de un objeto 

    #en teoria se deberia craer un metodo getter y setter por cada atributo que contenga la clase

    #los metodos get siempre regresan valor es decir el valor de la propiedad a traves de un return por otro lado
    #el metodo set siempre recibe parametros para cambiar o modificar el valor del atributo o prpiedad 


    #pongo self antes del atributo para hacer referencia a los atrubutos de la clase


    #forma con get y set
    def getMarca(self):
        return self.__marca
    
    def setMarca(self,marca):
        self.__marca=marca

    #forma con decoradores
    @property
    def marca2(self):
        return self.__marca
    
    @marca2.setter
    def marca2(self,marca):
        self.__marca=marca


    
    def getColor(self):
        return self.__color
    
    def setColor(self,color):
        self.__color=color

    def getModelo(self):
        return self.__modelo
    
    def setModelo(self,modelo):
        self.__modelo=modelo

    def getVelocidad(self):
        return self.__velocidad
    
    def setVelocidad(self,velocidad):
        self.__velocidad=velocidad

    def getCaballaje(self):
        return self.__caballaje
    
    def setCaballaje(self,caballaje):
        self.__caballaje=caballaje

    def getPlazas(self):
        return self.__plazas
    
    def setPlazas(self,plazas):
        self.__plazas=plazas

    #Metodos o acciones o funciones que hace el objeto 

    def acelerar(self):
        return "estas acelerando"
    def frenar(self):
        return "estas frenando" 

#Fin definir clase

