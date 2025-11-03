import funciones 
import getpass
from model.usuarios import usuariosOBJ,usuariosBD
from model.notas import notasOBJ,notasBD

class App:
    def __init__(self):
        self.main()

    def main(self):
        opcion=True
        while opcion:
            funciones.borrarPantalla()
            opcion=funciones.menu_usurios() 

            if opcion=="1" or opcion=="REGISTRO":
                funciones.borrarPantalla()
                print("\n \t ..:: Registro en el Sistema ::..")
                nombre=input("\t ¿Cual es tu nombre?: ").upper().strip()
                apellidos=input("\t ¿Cuales son tus apellidos?: ").upper().strip()
                email=input("\t Ingresa tu email: ").lower().strip()
                password=getpass.getpass("\t Ingresa tu contraseña: ").strip()
                
                objeto=usuariosOBJ.Usuarios(nombre,apellidos,email,password)
                resultado=usuariosBD.Usuarios.registrar(objeto.nombre,objeto.apellidos,objeto.email,objeto.password)
                if resultado:
                    print(f"\n\t{nombre} {apellidos} Se registro correctamente con el email: {email}")
                else:
                    print(f"\n\t ...Por favor intentelo de nuevo, no fue posible registrar al usuario")
                funciones.esperarTecla()  

            elif opcion=="2" or opcion=="LOGIN": 
                funciones.borrarPantalla()
                print("\n \t ..:: Inicio de Sesión ::.. ")     
                email=input("\t Ingresa tu E-mail: ").lower().strip()
                password=getpass.getpass("\t Ingresa tu contraseña: ").strip()

                registro=usuariosBD.Usuarios.iniciar_sesion(email,password)
                if registro:
                    usuario_id,nombre,apellidos,mail,password,fecha=registro
                    self.menu_notas(usuario_id,nombre,apellidos)
                else:
                    print("\n\t Email o contraseña incorrectas, vuelva a intentarlo")
                    funciones.esperarTecla()
            
            elif opcion=="3" or opcion=="SALIR": 
                print("\n\tTermino la Ejecución del Sistema")
                opcion=False
                funciones.esperarTecla()  
            else:
                print("\n\tOpcion no valida, vuela a intentarlo...")
                opcion=True
                funciones.esperarTecla()  



    def menu_notas(self,usuario_id,nombre,apellidos):
        while True:
            funciones.borrarPantalla()
            print(f"\n \t \t \t Bienvenido {nombre} {apellidos}, has iniciado sesión ...")
            opcion=funciones.menu_notas()

            if opcion == '1' or opcion=="CREAR":
                funciones.borrarPantalla()
                print(f"\n \t .:: Crear Nota ::. ")
                titulo=input("\tTitulo: ")
                descripcion=input("\tDescripción: ")

                objeto=notasOBJ.Notas(titulo,descripcion)
                resultado=notasBD.Notas.insertar(usuario_id,objeto.titulo,objeto.descripcion)
                if resultado:
                    print(f"\n\tLa nota {titulo} se registro correctamente")
                else:
                    print(f"\n\t ...Por favor intentelo de nuevo, no fue posible registrar la nota")
                funciones.esperarTecla()    



            elif opcion == '2' or opcion=="MOSTRAR":
                funciones.borrarPantalla()
                print(f"\n \t \t \t Tus notas {nombre} {apellidos} son:")
                resultado=notasBD.Notas.mostrar(usuario_id)
                if resultado:
                    print(F"\n\t Mostrar Notas\n")
                    print(f"{'NUM NOTA':<12}{'ID':<10}{'TITULO':<15}{'DESCRIPCION':<20}{'FECHA'}")
                    print(f"{'-'*70}")
                    cont=1
                    for i in resultado:
                        print(f"{cont:<12}{i[0]:<10}{i[2]:<15}{i[3]:<20}{i[4]}")
                        cont=cont+1
                else:
                    print(f"\n\t ...No exiten notas para mostrarte")
                funciones.esperarTecla()



            elif opcion=='3' or opcion=="CAMBIAR":
                funciones.borrarPantalla() 
                resultado=notasBD.Notas.mostrar(usuario_id)
                if resultado:
                    print(F"\n\t Mostrar Notas\n")
                    print(f"{'NUM NOTA':<12}{'ID':<10}{'TITULO':<15}{'DESCRIPCION':<20}{'FECHA'}")
                    print(f"{'-'*70}")
                    cont=1
                    for i in resultado:
                        print(f"{cont:<12}{i[0]:<10}{i[2]:<15}{i[3]:<20}{i[4]}")
                        cont=cont+1

                    print(f"\n \t .:: {nombre} {apellidos}, vamos a cambiar un Nota ::. \n")
                    id=input("\t \t ID de la nota a actualizar: ")
                    titulo=input("\t Nuevo título: ")
                    descripcion=input("\t Nueva descripción: ")
                    # crear otra vez el objeto y usar sus atributos?
                    check=notasBD.Notas.check(id)
                    if check:
                        op=input("¿De verdad quieres cambiar la nota? (si/no): ").lower().strip()
                        if op=="si":
                            resultado=notasBD.Notas.actualizar(titulo,descripcion,id)
                            if resultado:
                                print(f"\n\tLa nota {titulo} se actualizó correctamente")
                            else:
                                print(f"\n\tFallo al actualizar la nota")
                    else:
                        input(f"\n\tNo existe una nota con ese ID")
                    funciones.esperarTecla()
                else:
                    print(f"\n\t ...No exiten notas para mostrarte")
                    funciones.esperarTecla()


                
            elif opcion == '4' or opcion=="ELIMINAR":
                funciones.borrarPantalla()
                resultado=notasBD.Notas.mostrar(usuario_id)
                if resultado:
                    print(F"\n\t Mostrar Notas\n")
                    print(f"{'NUM NOTA':<12}{'ID':<10}{'TITULO':<15}{'DESCRIPCION':<20}{'FECHA'}")
                    print(f"{'-'*70}")
                    cont=1
                    for i in resultado:
                        print(f"{cont:<12}{i[0]:<10}{i[2]:<15}{i[3]:<20}{i[4]}")
                        cont=cont+1

                    print(f"\n \t .:: {nombre} {apellidos}, vamos a borrar un Nota ::. \n")
                    id=input("\t \t ID de la nota a eliminar: ")
                    check=notasBD.Notas.check(id)
                    if check:
                        op=input("¿De verdad quieres cambiar la nota? (si/no): ").lower().strip()
                        if op=="si":
                            resultado=notasBD.Notas.eliminar(id)
                            if resultado:
                                print(f"\n\tLa nota {id} se elimino correctamente")
                            else:
                                print("Fallo al eliminar la nota")
                    else:
                        input(f"\n\tNo existe una nota con ese ID")
                    funciones.esperarTecla()
                else:
                    print(f"\n\t ...No exiten notas para mostrarte")
                    funciones.esperarTecla()

            elif opcion == '5' or opcion=="SALIR":
                input("\n\tRegresando al menu principal")
                break
            else:
                input("\n \t \t Opción no válida. Intenta de nuevo.")

if __name__ == "__main__":
    app=App()    

# crear otra vez el objeto y usar sus atributos?
# checar id primero luego pedri datos
# mensaje de correo ya existenet