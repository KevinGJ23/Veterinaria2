class Medicamento:
    def __init__(self):
        self.__nombre = "" 
        self.__dosis = 0 

    def verNombre(self):
        return self.__nombre 
    def verDosis(self):
        return self.__dosis 

    def asignarNombre(self,med):
        self.__nombre = med 
    def asignarDosis(self,med):
        self.__dosis = med 

class Mascota:

    def __init__(self):
        self.__nombre= " "
        self.__historia=0
        self.__tipo=" "
        self.__peso=" "
        self.__fecha_ingreso=" "
        self.__lista_medicamentos=[]

    def verNombre(self):
        return self.__nombre
    def verHistoria(self):
        return self.__historia
    def verTipo(self):
        return self.__tipo
    def verPeso(self):
        return self.__peso
    def verFecha(self):
        return self.__fecha_ingreso
    def verLista_Medicamentos(self):
        return self.__lista_medicamentos 

    def asignarNombre(self,n):
        self.__nombre=n
    def asignarHistoria(self,nh):
        self.__historia=nh
    def asignarTipo(self,t):
        self.__tipo=t
    def asignarPeso(self,p):
        self.__peso=p
    def asignarFecha(self,f):
        self.__fecha_ingreso=f
    def asignarLista_Medicamentos(self,n):
        self.__lista_medicamentos = n 
    def verificar(self,v):
        p=False
        for j in self.__lista_medicamentos:
            if v == j.verNombre():
                p=True
        return p

class sistemaV:
    def __init__(self):
        self.__lista_perros={}
        self.__lista_gatos={}
    def verificarExiste(self,historia):
        r=False
        for m in self.__lista_perros.values():
            if historia == m.verHistoria():
                r=True
        for j in self.__lista_gatos.values():
            if historia == j.verHistoria():
                r=True
        return r
    def verNumeroMascotas(self, t):
        if t == "felino":
            return len(self.__lista_gatos) 
        elif t == "canino":
            return len(self.__lista_gatos) 
        else:
            return len(self.__lista_gatos)+len(self.__lista_perros)
        
    def ingresarMascota(self,mascota,t):
        if t == "felino":
            self.__lista_gatos[mascota.verHistoria()]= mascota
        else:
            self.__lista_perros[mascota.verHistoria()]= mascota

    def verFechaIngreso(self,historia):
        #busco la mascota y devuelvo el atributo solicitado
       
               
        for m in self.__lista_perros.values():
            if historia == m.verHistoria():
                 return m.verFecha() 
        for j in self.__lista_gatos.values():
            if historia == j.verHistoria():
                 return j.verFecha() 
        return None

    def verMedicamento(self,historia):
        #busco la mascota y devuelvo el atributo solicitado
                
        for m in self.__lista_perros.values():
            if historia == m.verHistoria():
                return m.verLista_Medicamentos() 
        for j in self.__lista_gatos.values():
            if historia == j.verHistoria():
                 return j.verLista_Medicamentos() 
        return None

    def eliminarMascota(self, historia):
        
                
        for m in self.__lista_perros.values():
            if historia == m.verHistoria():
                del self.__lista_perros[historia]  #opcion con el pop
                return True  #eliminado con exito
        for j in self.__lista_gatos.values():
            if historia == j.verHistoria():
                del self.__lista_gatos[historia]  #opcion con el pop
                return True  #eliminado con exito
        return False 
    def eliminarmedicamento(self,historia,med):
        p= "No se elimino"
        for m in self.__lista_perros.values():
            if historia == m.verHistoria():
                for i in m.verLista_Medicamentos():
                    if i.verNombre() == med:
                        p="eliminado"

        for j in self.__lista_gatos.values():
            if historia == j.verHistoria():
                for i in j.verLista_Medicamentos():
                    if i.verNombre() == med:
                        p="eliminado"
        return p  #eliminado con exito 
        

def main():
    servicio_hospitalario = sistemaV()
    # sistma=sistemaV()
    while True:
        menu=int(input('''\nIngrese una opción: 
                       \n1- Ingresar una mascota 
                       \n2- Ver fecha de ingreso 
                       \n3- Ver número de mascotas en el servicio 
                       \n4- Ver medicamentos que se están administrando
                       \n5- Eliminar mascota 
                       \n6- Eliminar medicamento 
                       \n7- Salir 
                       \nUsted ingresó la opción: ''' ))
        if menu==1: # Ingresar una mascota 
        
            historia=int(input("Ingrese la historia clínica de la mascota: "))
            #   verificacion=servicio_hospitalario.verDatosPaciente(historia)
            if servicio_hospitalario.verificarExiste(historia) == False:
                while True:
                    tipo=input("""Ingrese el tipo de mascota 
                            1. felino 
                            2. canino """)
                    if tipo =="1":
                        tip="felino"
                        break
                    elif tipo =="2":
                        tip="canino"
                        break
                    else:
                        print("Opción invalida")
                        pass
                if servicio_hospitalario.verNumeroMascotas(tip) >= 10:
                        print("No hay espacio ...") 
                else:
                    nombre=input("Ingrese el nombre de la mascota: ")
                    peso=int(input("Ingrese el peso de la mascota: "))
                    print("fecha de ingreso de la mascota")
                    while True:
                        d=int(input("Dia  00: "))
                        m=int(input("Mes 00: "))
                        a=int(input("Año 0000: "))
                        if d >31 or m >12 or a<2023 :
                            print("ingresaste mal la fecha, intenta nuevamente")
                            pass
                        else:
                            fecha=(str(d) + "/" + str(m) +"/" + str(a))
                            print(fecha)
                            break
                    nm=int(input("Ingrese cantidad de medicamentos: "))
                    lista_med=[]
                    mas= Mascota()
                    for i in range(0,nm):
                        while True: 
                            nombre_medicamentos = input("Ingrese el nombre del medicamento : ")
                            m=mas.verificar(nombre_medicamentos)
                            if m == True:
                                print("Existe el medicamento")
                            else:
                                dosis =int(input("Ingrese la dosis : "))
                                medicamento = Medicamento()
                                medicamento.asignarNombre(nombre_medicamentos)
                                medicamento.asignarDosis(dosis)
                                lista_med.append(medicamento)
                                mas.asignarLista_Medicamentos(lista_med)
                                break
                    mas.asignarNombre(nombre)
                    mas.asignarHistoria(historia)
                    mas.asignarPeso(peso)
                    mas.asignarTipo(tipo)
                    mas.asignarFecha(fecha)
                    servicio_hospitalario.ingresarMascota(mas,tip)

            else:
                print("Ya existe la mascota con el numero de histoira clinica")

        elif menu==2: # Ver fecha de ingreso
            q = int(input("Ingrese la historia clínica de la mascota: "))
            fecha = servicio_hospitalario.verFechaIngreso(q)
            # if servicio_hospitalario.verificarExiste == True
            if fecha != None:
                print("La fecha de ingreso de la mascota es: " + fecha)
            else:
                print("La historia clínica ingresada no corresponde con ninguna mascota en el sistema.")

        elif menu==3: # Ver número de mascotas en el servicio 
            numero=servicio_hospitalario.verNumeroMascotas("d")
            print("El número de pacientes en el sistema es: " + str(numero))

        elif menu==4: # Ver medicamentos que se están administrando
            q = int(input("Ingrese la historia clínica de la mascota: "))
            medicamento = servicio_hospitalario.verMedicamento(q) 
            if medicamento != None: 
                print("Los medicamentos suministrados son: ")
                for m in medicamento:   
                    print(f"\n- {m.verNombre()}")
            else:
                print("La historia clínica ingresada no corresponde con ninguna mascota en el sistema.")


        elif menu == 5: # Eliminar mascota
            q = int(input("Ingrese la historia clínica de la mascota: "))
            resultado_operacion = servicio_hospitalario.eliminarMascota(q) 
            if resultado_operacion == True:
                print("Mascota eliminada del sistema con exito")
            else:
                print("No se ha podido eliminar la mascota")
        elif menu==6:
            q = int(input("Ingrese la historia clínica de la mascota: "))
            nombre_medicamentos = input("Ingrese el nombre del medicamento: ")
            resultado_operacion = servicio_hospitalario.eliminarmedicamento(q,nombre_medicamentos)
            print(resultado_operacion)

        elif menu==7:
            print("Usted ha salido del sistema de servicio de hospitalización...")
            break

        else:
            print("Usted ingresó una opción no válida, intentelo nuevamente...")

if __name__=='__main__':
    main()# V2
