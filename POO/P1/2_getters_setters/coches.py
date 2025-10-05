
import os
os.system("cls")

class Coches:

    #Atributos o propiedades (variables)
    #Caracteristicas del coche
    #valores iniciales es posible declarar al principio de una clase
    marca=""
    color=""
    modelo=""
    velocidad=0
    caballaje=0
    plazas=0


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

coche1=Coches()
coche1.setMarca("VW")
coche1.setColor("Blanco")
coche1.setModelo("2022")
coche1.setVelocidad(220)
coche1.setCaballaje(150)
coche1.setPlazas(5)
'''coche1.marca="VW"
coche1.color="Blanco"
coche1.modelo="2022"
coche1.velocidad=220
coche1.caballaje=150
coche1.plazas=5'''

print(f"Datos del Vehiculo: \n Marca:{coche1.getMarca()} \n color: {coche1.getColor()} \n Modelo: {coche1.getModelo()} \n velocidad: {coche1.getVelocidad()} \n caballaje: {coche1.getCaballaje()} \n plazas: {coche1.getPlazas()} ")

coche2=Coches()

coche2.setMarca("Nissan")
coche2.setColor("Azul")
coche2.setModelo("2020")
coche2.setVelocidad(180)
coche2.setCaballaje(150)
coche2.setPlazas(6)

'''coche2.marca="Nissan"
coche2.color="Azul"
coche2.modelo="2020"
coche2.velocidad=180
coche2.caballaje=150
coche2.plazas=6'''

print(f"Datos del Vehiculo: \n Marca:{coche2.getMarca()} \n color: {coche2.getColor()} \n Modelo: {coche2.getModelo()} \n velocidad: {coche2.getVelocidad()} \n caballaje: {coche2.getCaballaje()} \n plazas: {coche2.getPlazas()} ")
#Segunda palabra de una funcion en mayusculas


#con decoradores
coche3=Coches()
coche3.marca2="Honda"
print(f"Marca del carro: {coche3.marca2}")
