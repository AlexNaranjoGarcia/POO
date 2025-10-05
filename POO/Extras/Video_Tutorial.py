class Pais:
    def __init__(self, nombre, presidente):
        self.nombre = nombre
        self.presidente = presidente

    def __str__(self):
        return f"Pais: {self.nombre}, Presidente: {self.presidente}"
    
pais1 = Pais("Mexico", "Claudia Sheinbaum")
print(pais1)

class Ciudad:
    def __init__(self, nombre, habitantes, pais):
        self.nombre = nombre
        self.habitantes = habitantes
        self.pais = pais

    def __str__(self):
        return f"Ciudad: {self.nombre} - Habitantes: {self.habitantes} ({self.pais})"


ciudad1 = Ciudad("Durango", 10000000, pais1)
print(ciudad1)

class Urbanizacion:
    def __init__(self, nombre, ciudad):
        self.nombre = nombre
        self.ciudad = ciudad
    
    def __str__(self):
        return f"Urbanizacion: {self.nombre} ({self.ciudad})"
    
urb1 = Urbanizacion("Residencial del Bosque", ciudad1)
print(urb1)