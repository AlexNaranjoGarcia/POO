class Alumnos:
    def __init__(self,nombre,edad,matricula):
        self.__nombre=nombre
        self.__edad=edad
        self.__matricula=matricula

    def inscribirse(self):
        print(f"El alumno {self.__nombre} se inscribio")

    def estudiar(self):
        print(f"El alumno {self.__nombre} esta estudiando")


    def getNombre(self):
        return self.__nombre
    
    def setNombre(self,nuevo):
        self.__nombre=nuevo

    def getEdad(self):
        return self.__edad
    
    def setEdad(self,nuevo):
        self.__edad=nuevo

    def getMatricula(self):
        return self.__matricula
    
    def setMatricula(self,nuevo):
        self.__matricula=nuevo

class Cursos:
    def __init__(self,nombre,codigo,creditos):
        self.__nombre=nombre
        self.__codigo=codigo
        self.__creditos=creditos

    def asignar(self):
        print(f"Se asigno el curso de  {self.__nombre}")

    @property
    def nombre(self):
        return self.__nombre

    @nombre.setter
    def nombre(self,nuevo):
        self.__nombre=nuevo

    @property
    def codigo(self):
        return self.__codigo
    
    @codigo.setter
    def codigo(self,nuevo):
        self.__codigo=nuevo

    @property
    def creditos(self):
        return self.__creditos

    @creditos.setter
    def creditos(self,nuevo):
        self.__creditos=nuevo

class Profesores:
    def __init__(self,nombre,experiencia,num_profesor):
        self.__nombre=nombre
        self.__experiencia=experiencia
        self.__num_profesor=num_profesor
    def impartir(self):
        print(f"El profesor {self.__nombre} esta impartiendo un curso")
    def evaluar(self):
        print(f"El profesor {self.__nombre} esta evaluando")
    def getNombre(self):
        return self.__nombre
    def setNombre(self,nuevo):
        self.__nombre=nuevo
    def getExperiencia(self):
        return self.__experiencia
    def setExperiencia(self,nuevo):
        self.__experiencia=nuevo
    def getNum_Profesor(self):
        return self.__num_profesor
    def setNum_Profesor(self,nuevo):
        self.__num_profesor=nuevo

alumno1=Alumnos("Juan",19,3141240167)
alumno2=Alumnos("Diego",19,3141249632)
alumno1.inscribirse()
print(alumno1.getNombre())

curso1=Cursos("matematicas","hrte65",2)
curso2=Cursos("historia","hrup75",3)
curso1.asignar()

profesor1=Profesores("Antonio",8,1289167)
profesor2=Profesores("Omar",10,1289198)
profesor1.impartir()

