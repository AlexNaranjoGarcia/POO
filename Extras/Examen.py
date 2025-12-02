class Fabrica:
    def __init__(self, llantas, color, precio):
        self._llantas = llantas
        self._color = color
        self._precio = precio
    
    @property
    def llantas(self):
        return self._llantas
    
    @llantas.setter
    def llantas(self, llantas):
        self._llantas = llantas
    
    @property
    def color(self):
        return self._color
    
    @color.setter
    def color(self, color):
        self._color = color
    
    @property
    def precio(self):
        return self._precio
    
    @precio.setter
    def precio(self, precio):
        self._precio = precio

class Moto(Fabrica):
    def __init__(self, llantas, color, precio, tipoMoto):
        super().__init__(llantas, color, precio)
        self._tipoMoto = tipoMoto

    @property
    def tipoMoto(self):
        return self._tipoMoto
    
    @tipoMoto.setter
    def tipoMoto(self, tipoMoto):
        self._tipoMoto = tipoMoto

class Carro(Fabrica):
    def __init__(self, llantas, color, precio, tipoCarro):
        super().__init__(llantas, color, precio)
        self._tipoCarro = tipoCarro
    
    @property
    def tipoCarro(self):
        return self._tipoCarro
    
    @tipoCarro.setter
    def tipoCarro(self, tipoCarro):
        self._tipoCarro = tipoCarro

moto1 = Moto(2, "Rojo", 12000, "Deportiva")
carro1 = Carro(4, "Azul", 100000, "Sedan")

print(moto1.color, moto1.llantas, moto1.tipoMoto)
print(carro1.color, carro1.llantas, carro1.tipoCarro)