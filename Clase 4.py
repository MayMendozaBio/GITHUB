
#Clases
#commmit
#MAY
class Persona:
    def __init__(self, nombre='', cedula=0, genero=''):
        self.__nombre = nombre
        self.__cedula = cedula
        self.__genero = genero

    # Getters
    def getNombre(self):
        return self.__nombre

    def getCedula(self):
        return self.__cedula

    def getGenero(self):
        return self.__genero

    # Setters
    def setNombre(self, nombre):
        self.__nombre = nombre

    def setCedula(self, cedula):
        self.__cedula = cedula

    def setGenero(self, genero):
        self.__genero = genero
    
class Paciente(Persona):
    def __init__(self,servicio=""):
        Persona.__init__(self)
        self.__servicio = servicio

    def setServicio(self, servicio):
        self.__servicio = servicio

    def getServicio(self):
        return self.__servicio
        
class Empleado_Hospital(Persona):
    def __init__(self,turno=""):
        Persona.__init__(self)
        self.__turno = turno

    def setturno(self, turno):
        self.__turno = turno

    def getturno(self):
        return self.__turno   
    
class enfermera(Empleado_Hospital): 
    def __init__(self):
        super().__init__()
        self.__rango = ""

    def setrango(self, rango):
        self.__rango = rango

    def getrango(self):
        return self.__rango

class medico(Empleado_Hospital):
    def __init__(self):
        super().__init__()
        Empleado_Hospital.__init__(self)
        
        self.__especialidad = ''
    
    def setespecialidad(self, especialidad):
        self.__especialidad = especialidad
    def getespecialidad(self):
        return self.__especialidad


objetos = []
enfermeras=[]
medicos=[]

while True:
    menu=input('''
    Ingrese la opcion que necesite del menú
    1. Ingresar los datos del paciente
    2. Buscar paciente
    3.Ingresar enfermera
    4.Buscar enfermera
    5.Ingresar médico
    6.Buscar médico
    7. Salir''')

    if menu=="1":
        nombre=str(input("Ingrese el nombre del paciente"))
        cedula=int(input("Ingrese la cedula del paciente"))
        genero=str(input("Ingrese el genero del paciente"))
        servicio=str(input("Ingrese el servicio donde se encuentra el paciente"))

        paciente=Paciente() #para que se genere cada ciclo
        paciente.setNombre(nombre)
        paciente.setCedula(cedula)
        paciente.setGenero(genero)
        paciente.setServicio(servicio)
        objetos.append(paciente)


    elif menu=="2":
        CC=int(input("INGRESE LA CEDULA DEL PACIENTE QUE DESEA BUSCAR: "))
        for i in objetos: #para cada paciente en la lista de objetos
            if CC==i.getCedula():
                print(f'''
Nombre: {i.getNombre()}
CC: {i.getCedula()}
Género: {i.getGenero()}
Servicio: {i.getServicio()}

''')
                break
        else:
            print("No existe el apciente en la abse de datos")

    elif menu=="3":
        nombre=str(input("Ingrese el nombre de la enfermera"))
        cedula=int(input("Ingrese la cedula de la enefermera"))
        genero=str(input("Ingrese el genero de la enfermera"))
        turno=str(input("Ingrese turno "))
        rango=str(input("Ingrese rango"))

        enf=enfermera() 
        enf.setNombre(nombre)
        enf.setCedula(cedula)
        enf.setGenero(genero)
        enf.setturno(turno)
        enf.setrango(rango)

        enfermeras.append(enf)

    elif menu=="4":
        CC=int(input("INGRESE LA CEDULA DE LA ENFERMERA QUE DESEA BUSCAR: "))
        for i in enfermeras: 
            if CC==i.getCedula():
                print(f'''
Nombre: {i.getNombre()}
CC: {i.getCedula()}
Género: {i.getGenero()}
Turno: {i.getturno()}
Rango: {i.getrango()}

''')
                break
        else:
            print("No existe la enfermera en la abse de datos")

    elif menu=="5":
        nombre=str(input("Ingrese el nombre del médico"))
        cedula=int(input("Ingrese la cedula del médico"))
        genero=str(input("Ingrese el genero del médico"))
        turno=str(input("Ingrese turno "))
        especialidad=str(input("Ingrese especialidad"))

        m=medico() 
        m.setNombre(nombre)
        m.setCedula(cedula)
        m.setGenero(genero)
        m.setturno(turno)
        m.setespecialidad(especialidad)

        medicos.append(m)
    
    elif menu=="6":
        CC=int(input("INGRESE LA CEDULA DEL MÉDICO QUE DESEA BUSCAR: "))
        for i in medicos: 
            if CC==i.getCedula():
                print(f'''
Nombre: {i.getNombre()}
CC: {i.getCedula()}
Género: {i.getGenero()}
Turno: {i.getturno()}
Especialidad: {i.getespecialidad()}

''')
                break
        else:
            print("No existe el médico en la abse de datos")

    elif menu=="7":
        break
    else:
        print("Ingresa un digito válido")


