
import os
os.system("cls")

class Coches:

    #Atributos o propiedades (variables)
    #Caracteristicas del coche
    #valores iniciales es posible declarar al principio de una clase
    def __init__(self,marca,color,modelo,velocidad,caballaje,plazas):
        self.marca=marca
        self.color=color
        self.modelo=modelo
        self.velocidad=velocidad
        self.caballaje=caballaje
        self.plazas=plazas
    
    #otro constructor
    def __init__(self):
        self.marca=""
        self.color=""
        self.modelo=""
        self.velocidad=0
        self.caballaje=0
        self.plazas=0
        


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
        return self.marca
    
    def setMarca(self,marca):
        self.marca=marca

    #forma con decoradores
    @property
    def marca2(self):
        return self.marca
    
    @marca2.setter
    def marca2(self,marca):
        self.marca=marca


    
    def getColor(self):
        return self.color
    
    def setColor(self,color):
        self.color=color

    def getModelo(self):
        return self.modelo
    
    def setModelo(self,modelo):
        self.modelo=modelo

    def getVelocidad(self):
        return self.velocidad
    
    def setVelocidad(self,velocidad):
        self.velocidad=velocidad

    def getCaballaje(self):
        return self.caballaje
    
    def setCaballaje(self,caballaje):
        self.caballaje=caballaje

    def getPlazas(self):
        return self.plazas
    
    def setPlazas(self,plazas):
        self.plazas=plazas

    #Metodos o acciones o funciones que hace el objeto 

    def acelerar(self):
        pass

    def frenar(self):
        pass  

#Fin definir clase

#Crear un objetos o instanciar la clase

coche1=Coches("VW","Blanco","2022",220,150,5)
coche1.num_serie=("hw78cwe") #se pueden agregar mas atributos que no esten en el init pero se tienen que llenar los campos del contructir antes
print(f"Datos del Vehiculo: \n Marca:{coche1.getMarca()} \n color: {coche1.getColor()} \n Modelo: {coche1.getModelo()} \n velocidad: {coche1.getVelocidad()} \n caballaje: {coche1.getCaballaje()} \n plazas: {coche1.getPlazas()} ")



coche2=Coches("Nissan","Azul","2020",180,150,6)
print(f"Datos del Vehiculo: \n Marca:{coche2.getMarca()} \n color: {coche2.getColor()} \n Modelo: {coche2.getModelo()} \n velocidad: {coche2.getVelocidad()} \n caballaje: {coche2.getCaballaje()} \n plazas: {coche2.getPlazas()} ")
#Segunda palabra de una funcion en mayusculas


#con decoradores
coche3=Coches("Honda","","",0,0,0)
print(f"Datos del Vehiculo: \n Marca: {coche3.marca2}")

coche4=Coches("Honda","","",0,0,0)
coche4.marca2="Volvo"
print(f"Datos del Vehiculo: \n Marca: {coche4.marca2}")