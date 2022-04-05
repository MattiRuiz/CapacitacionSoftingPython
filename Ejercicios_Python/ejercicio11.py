"""
EMPRESA EMPLEADOS
Una empresa está dividida en 15 secciones. De cada sección se tiene: número que la identifica, 
cantidad de empleados que trabajan en ella. Durante un determinado período se registró en cada 
sección de la empresa los siguientes datos de cada uno de sus empleados: Número de identificación 
del empleado, turno en el que trabajó (M: Mañana; T: Tarde) y cantidad de horas que trabajó.

Se desea procesar esta información para poder saber:
- El promedio de horas que se trabajó en cada sección
- Para toda la empresa, si hubo o no un turno en el que se trabajó más cantidad de horas, 
y en caso afirmativo en cuánto se superó al otro

"""

# Constantes
secciones = 15
tipoTurno = ('M', 'T')

# Listas
IDSecciones = []
tipoSeccion = []
IDEmpleados = []
turnos = []
cantHoras = []

# Variables
seccion = int()
numEmpleados = int()
empleado = int()
turno = str()
horas = int()
horasManana = int()
horasTarde = int()
diferenciaTurnos = int()

######## Funciones ########

def ingresoDatos(x):
    print("----------------------------------------------------")
    seccion = int(input("Ingrese el ID de la sección "+ str(x+1) + " : "))
    while seccion in IDSecciones:
        seccion = int(input("ID de sección ya registrada. Ingrese un ID nuevo: "))
    while seccion not in tipoSeccion:
        tipoSeccion.append(seccion)

    numEmpleados = int(input("Ingrese la cantidad de empleados correspondiente a la seccion " + str(seccion) + " : "))

    ingresoEmpleados(seccion, numEmpleados)


def ingresoEmpleados(seccion, numEmpleados):
    for i in range(numEmpleados):
        empleado = int(input("Ingrese el ID del empleado " + str(i+1) + " de la sección " + str(seccion) + " : "))
        while empleado in IDEmpleados:
            empleado = int(input("ID de empleado ya registrado. Ingrese un ID nuevo : "))

        IDSecciones.append(seccion)
        IDEmpleados.append(empleado)

        print("En que turno trabajó el empleado " + str(empleado) + " ? ")
        turno = str(input("M) Mañana; T) Tarde : "))
        turno = turno.upper()
        while turno not in tipoTurno:
            print("Valor ingresado inválido. Ingrese. ")
            turno = str(input("M) Mañana; T) Tarde : "))
        
        turnos.append(turno)

        horas = int(input("Ingrese la cantidad de horas trabajadas por el empleado " + str(empleado) + " : "))

        cantHoras.append(horas)

def horasSeccion():
    for x in range(len(tipoSeccion)):
        sumaHoras = int(0)
        for i in range(len(IDSecciones)):
            if tipoSeccion[x] == IDSecciones[i]:
                sumaHoras = sumaHoras + cantHoras[i]
        print("En la sección " + str(tipoSeccion[x]) + " se trabajó " + str(sumaHoras) + " horas")
    
def horasTurno(horasTarde, horasManana):
    for x in range(len(turnos)):
        if turnos[x] == "M":
            horasManana = horasManana + cantHoras[x]
        elif turnos[x] == "T":
            horasTarde = horasTarde + cantHoras[x]
    
    if horasManana > horasTarde:
        diferenciaTurnos = horasManana - horasTarde
        print("En el turno MAÑANA se trabajó " + str(diferenciaTurnos) + " horas más que en el turno TARDE")
    elif horasTarde > horasManana:
        diferenciaTurnos = horasTarde - horasManana
        print("En el turno TARDE se trabajó " + str(diferenciaTurnos) + " horas más que en el turno MAÑANA")
    else:
        print("En ambos turnos se trabajó " + str(horasManana) + " horas")


######## Inicio del programa ########

for x in range(secciones):
    ingresoDatos(x)

print("\n-----------------------------------------")
print("RESULTADOS")
print("\nAnálisis de horas por sección: ")

horasSeccion()

print("\nAnálisis de horas por turnos:")

horasTurno(horasTarde, horasManana)

print("\n")