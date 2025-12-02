class Usuarios:
    def __init__(self,nombre,apellidos,email,password):
        self._nombre=nombre
        self._apellidos=apellidos
        self._email=email
        self._password=password

    @property
    def nombre(self):
        return self._nombre
    @nombre.setter
    def nombre(self,otro):
        self._nombre=otro

    @property
    def apellidos(self):
        return self._apellidos
    @apellidos.setter
    def apellidos(self,otro):
        self._apellidos=otro

    @property
    def email(self):
        return self._email
    @email.setter
    def email(self,otro):
        self._email=otro

    @property
    def password(self):
        return self._password
    @password.setter
    def password(self,otro):
        self._password=otro