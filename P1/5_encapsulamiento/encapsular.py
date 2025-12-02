import os
os.system("cls")

class Clase:
    atributo_publico="Soy un atributo publico"
    _atributo_protegido="Soy un atributo protegido"
    __atributo_privado="Soy un atributo privado"

    def __init__(self,color,tamano):
        self.__color=color
        self.__tamano=tamano


    def _getAtributoPrivado(self):
        return  self.__atributo_privado
    
    def _setAtributoPrivado(Self,atributo_privado):
        Self.__atributo_privado=atributo_privado

    '''def getAtributoPrivado2(Self):
        Self._getAtributoPrivado()''' #para llamar a metodos privados

    @property
    def color(self):
        return self.__color
    
    @color.setter
    def color(Self,color):
        Self.color=color


    @property
    def tamano(self):
        return self.__tamano
    
    @tamano.setter
    def tamano(Self,tamano):
        Self.__tamano=tamano

objeto=Clase("Rojo","Grande")
print(f"Mi objeto tiene los sigueintes atributos {objeto.color} y {objeto.tamano}")


#objeto.tamano="grande"
#crea un objeto sin atributos porque no tiene constructor hasta abajo donde se imprimen se agregan los atributos ode declaran

#Usar los atributos y metodos de acuerdo a su encapsulamiento
print(f"Soy el contenido del atributo publico: {objeto.atributo_publico}")
print(f"Soy el contenido del atributo protegido: {objeto._atributo_protegido}")

print(f"Soy el contenido del atributo privado: {objeto._getAtributoPrivado()}")
objeto._setAtributoPrivado("Se ha cambiado el valor del atributo privado")
print(f"Soy el contenido del atributo privado: {objeto._getAtributoPrivado()}")



#Para imprimir tengo que usar get y set
#En la clase todod los atributos son self

