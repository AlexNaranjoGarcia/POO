class Notas:
    def __init__(self,titulo,descripcion):
        self._titulo=titulo
        self._descripcion=descripcion

    @property
    def titulo(self):
        return self._titulo
    @titulo.setter
    def titulo(self,otro):
        self._titulo=otro

    @property
    def descripcion(self):
        return self._descripcion
    @descripcion.setter
    def descripcion(self,otro):
        self._descripcion=otro