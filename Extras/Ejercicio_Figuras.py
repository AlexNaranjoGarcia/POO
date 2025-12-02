from abc import ABC, abstractmethod

class Figura(ABC): # Hereda de ABC (Abstract Base Class)
    def __init__(self, x, y, visible=True):
        self._x = x
        self._y = y
        self._visible = visible

    @property
    def x(self):
        return self._x

    @x.setter
    def x(self, x):
        self._x = x

    @property
    def y(self):
        return self._y

    @y.setter
    def y(self, y):
        self._y = y

    @property
    def visible(self):
        return self._visible

    @visible.setter
    def visible(self, visible):
        self._visible = visible

    def estaVisible(self):
        return self._visible

    def mostrar(self):
        self._visible = True
        print(f"Figura en ({self._x},{self._y}) ahora visible.")

    def ocultar(self):
        self._visible = False
        print(f"Figura en ({self._x},{self._y}) ahora oculta.")

    def mover(self, dx, dy):
        self._x += dx
        self._y += dy
        print(f"Figura movida a ({self._x},{self._y}).")

    @abstractmethod
    def calcularArea(self):


class Rectangulo(Figura):
    def __init__(self, x, y, alto, ancho, visible=True):
        super().__init__(x, y, visible)
        self._alto = alto
        self._ancho = ancho

    @property
    def alto(self):
        return self._alto

    @alto.setter
    def alto(self, alto):
        self._alto = alto

    @property
    def ancho(self):
        return self._ancho

    @ancho.setter
    def ancho(self, ancho):
        self._ancho = ancho

    def calcularArea(self):
        return float(self._alto * self._ancho)

    def __str__(self): 
        return (f"Rectángulo (ID: {id(self)}) - Pos:({self.x},{self.y}) | "
                f"Alto:{self.alto} | Ancho:{self.ancho} | "
                f"Visible:{self.visible} | Área:{self.calcularArea():.2f}")
    
import math
class Circulo(Figura):
    def __init__(self, x, y, radio, visible=True):
        super().__init__(x, y, visible) 
        self._radio = radio

    @property
    def radio(self):
        return self._radio

    @radio.setter
    def radio(self, radio):
        self._radio = radio

    def calcularArea(self):
        return float(math.pi * (self._radio ** 2))

    def __str__(self): # Representación en cadena para facilitar la impresión
        return (f"Círculo (ID: {id(self)}) - Pos:({self.x},{self.y}) | "
                f"Radio:{self.radio} | Visible:{self.visible} | "
                f"Área:{self.calcularArea():.2f}")
    
