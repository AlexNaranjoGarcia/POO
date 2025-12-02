from coches import * #es como copiar y pegar en este archivo  
#import coches agarro todo el archivo
#coche1=coches.Coches("VW","Blanco","2022",220,150,5)



#solicitar los datos que posteriormente seran los atributos del objeto




coche1=Coches("VW","Rojo","2020",200,160,4)
print(coche1.color, coche1.acelerar())

camion1=Camiones("VW","Blanco","2020",210,170,4,2,2500)
print(camion1.color, camion1.acelerar())

camioneta1=Camionetas("VW","Azul","2020",220,180,4,"delantera",True)
print(camioneta1.color, camioneta1.acelerar())



'''num_coches=int(input("Cuantos coches tienes: "))

for i in range(0,num_coches,1):
    print(f"\n\t...Datos del automovil {i+1} ...")
    marca=input("Ingresa la marca: ").upper()
    color=input("Ingresa el color: ").upper()
    modelo=input("Ingresa el modelo del auto: ").upper()
    velocidad=int(input("Ingresa la velocidad: "))
    potencia=int(input("Ingresa la potencia: "))
    plazas=int(input("Ingresa las plazas: "))

    coche1=Coches(marca,color,modelo,velocidad,potencia,plazas)
    print(f"\n\tDatos del Coche: \n Marca:{coche1.marca} \n Color: {coche1.color} \n Modelo: {coche1.modelo} \n Velocidad: {coche1.velocidad} \n Caballaje: {coche1.caballaje} \n Plazas: {coche1.plazas} ")

# se separa la clase de la implementacion y se usan for con un solo objeto'''










'''#Crear un objetos o instanciar la clase

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
print(f"Datos del Vehiculo: \n Marca: {coche4.marca2}")'''

