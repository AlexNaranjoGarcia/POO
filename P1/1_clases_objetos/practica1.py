#Implementar paradigmas Estructurados VS POO

#Estructurado
def sum(base,altura):
    suma=base*altura
    return suma

base=float(input("Tamaño de la base: "))
altura=float(input("Tamaño de la altura: "))
area=sum(base,altura)
print(f"El area del rectangulo es: {area}")

#POO
class Rectangulos:
    def __init__(self,base,altura):
        self.base=base
        self.altura=altura
    def area(self):
        return self.base*self.altura
    


rect1=Rectangulos(5,3)
print(f"Area: {rect1.area()}")