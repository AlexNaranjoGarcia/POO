
import os
os.system("cls")

class Coches:

    #Atributos o propiedades (variables)
    #Caracteristicas del coche
    #valores iniciales es posible declarar al principio de una clase
    def __init__(self,marca,color,modelo,velocidad,caballaje,plazas):
        self._marca=marca
        self._color=color
        self._modelo=modelo
        self._velocidad=velocidad
        self._caballaje=caballaje
        self._plazas=plazas
    
        


    #Crear los metodos setters y getters. estos metodos son importantes y necesarios en todas las clases para que
    #programador interactue con los valores de los atributos a traves de estos metodos, digamos que es la manera
    #mas adecuada y recomendada para solicitar un valor (get) y/o para ingresar o cambiar un valor (set) a un 
    #atributo en particular de la clase a traves de un objeto 

    #en teoria se deberia craer un metodo getter y setter por cada atributo que contenga la clase

    #los metodos get siempre regresan valor es decir el valor de la propiedad a traves de un return por otro lado
    #el metodo set siempre recibe parametros para cambiar o modificar el valor del atributo o prpiedad 


    #pongo self antes del atributo para hacer referencia a los atrubutos de la clase



    #forma con decoradores
    @property
    def marca(self):
        return self._marca
    
    @marca.setter
    def marca(self,marca):
        self._marca=marca

    @property
    def color(self):
        return self._color
    
    @color.setter
    def color(self,color):
        self._color=color

    @property
    def modelo(self):
        return self._modelo
    
    @modelo.setter
    def modelo(self,modelo):
        self._modelo=modelo

    @property
    def velocidad(self):
        return self._velocidad
    
    @velocidad.setter
    def velocidad(self,velocidad):
        self._velocidad=velocidad

    @property
    def caballaje(self):
        return self._caballaje
    
    @caballaje.setter
    def caballaje(self,caballaje):
        self._caballaje=caballaje

    @property
    def plazas(self):
        return self._plazas
    
    @plazas.setter
    def plazas(self,plazas):
        self._plazas=plazas

    #Metodos o acciones o funciones que hace el objeto 

    def acelerar(self):
        return "estas acelerando un coche"
    def frenar(self):
        return "estas frenando un coche" 


class Camiones(Coches):
    def __init__(self, marca, color, modelo, velocidad, caballaje, plazas,eje,capacidadCarga):
        super().__init__(marca, color, modelo, velocidad, caballaje, plazas)
        self.__eje=eje
        self.__capacidadCarga=capacidadCarga

    @property
    def eje(self):
        return self.__eje
    
    @eje.setter
    def eje (self,eje):
        self.__eje=eje


    @property
    def capacidadCarga(self):
        return self.__capacidadCarga
    
    @capacidadCarga.setter
    def capacidadCarga (self,capacidadCarga):
        self.__capacidadCarga=capacidadCarga

    #simula la creacion de otro atributo
    def cargar(self,tipo_carga):
        self.tipo_carga=tipo_carga
        return self.tipo_carga

    def acelerar(self):
        return "estas acelerando un camion"
    def frenar(self):
        return "estas frenando un camion" 


class Camionetas(Coches):
    def __init__(self, marca, color, modelo, velocidad, caballaje, plazas,traccion,cerrada):
        super().__init__(marca, color, modelo, velocidad, caballaje, plazas)
        self.__traccion=traccion
        self.__cerrada=cerrada

    @property
    def traccion(self):
        return self.__traccion
    
    @traccion.setter
    def eje (self,traccion):
        self.__traccion=traccion


    @property
    def cerrada(self):
        return self.__cerrada
    
    @cerrada.setter
    def cerrada (self,cerrada):
        self.__cerrada=cerrada

    #simula la creacion de otro atributo
    def transportar(self,num_pasajeros):
        self.num_pasajeros=num_pasajeros
        return self.num_pasajeros

    def acelerar(self):
        return "estas acelerando una camioneta"
    def frenar(self):
        return "estas frenando una camioneta" 
    

#Fin definir clase

#poner los atributos de coches en portegido para que funcione la herencia y cambiar los set y get por property