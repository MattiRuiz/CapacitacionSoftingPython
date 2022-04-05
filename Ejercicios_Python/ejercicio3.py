"""

En una fábrica de ventiladores se trabaja en 3 turnos: M, T y N, todos los dias laborables.

De un determinado mes, se conoce la cantidad de días laborables que hubo y de cada día laborable 
del mismo se tiene, sin orden alguno, las siguientes ternas de datos, numero del dia, turno y 
cantidad de ventiladores producidos.

Se pide procesar la informacion correspondiente a un determinado mes para conocer:
- En que dia y qué turno se produjeron más ventiladores
- En qué dia t en qué turno se hicieron menos ventiladores

Tener en cuenta que es necesario validar la consistencia del numero de día 
(valor entero entre 1 y 31) y la codificación del turno (M, T o N)


"""

###########  Programa principal  ###########
laborales = 0



print("FABRICA DE VENTILADORES PEPITO")

#Obtencion de los dias laborales
laborales = int(input("Ingrese la cantidad de dias laborales que hubo en este mes: "))
while laborales < 1 or laborales > 30:
    laborales = int(input("Valor inválido, ingrese un numero entre 1 a 30 días: "))

#Definimos la cantidad de turnos por dia
horasLaborales = laborales * 3

#Los elementos de la tabla
dias = []
turno = []
cantProductos = []

#Controladores de los valores ingresados
controlDias = []
tipoTurno = ("M", "T", "N")


print("Cantidad de turnos laborables ", horasLaborales)


for i in range (horasLaborales):
    bandera = 0

    #Ingreso del dia
    dias.append(int(input("Ingrese la fecha del día " + str(i+1) + ": ")))
    while dias[i] < 1 or dias[i] > 31:
        dias.pop()
        dias.append(int(input("Fecha inválida, ingrese un valor entre 1 y 31: ")))

    if dias[i] not in controlDias:
        controlDias.append(dias[i])

        if len(controlDias) > laborales:
            controlDias.pop()
            print("Usted ya asignó fecha a todos los dias laborales disponible")
            dias.pop()
            print("Elija un día de la siguiente lista:")
            print(controlDias)
            dias.append(int(input("Ingrese la fecha del día " + str(i+1) + ": ")))
            while dias[i] not in controlDias:
                dias.pop()
                print("Valor inválido. Elija un día de la siguiente lista:")
                print(controlDias)
                dias.append(int(input()))
        else:
            print("Los dias disponibles son:")
            print(controlDias)

    #Ingreso del turno
    while bandera != 1:
        turno.append(input("Ingrese el turno a cargar: M - Mañana || T - Tarde || N - Noche\n"))
        while turno[i] not in tipoTurno:
            turno.pop()
            turno.append(input("Valor inválido, intente nuevamente: M - Mañana || T - Tarde || N - Noche\n"))
        
        bandera = 0

        for j in range(len(turno)):
            if dias[i] == dias[j] and turno[i] == turno[j]:
                bandera = bandera + 1
                if bandera > 1:
                    print("El turno: " + turno[i] + " ya fue cargado para el día " + str(dias[i]) + ", intente nuevamente")
                    turno.pop()

    #Ingreso de la cantidad de productos
    cantProductos.append(int(input("Ingrese la cantidad de productos que se produjeron el día: " + str(dias[i]) + " Turno: " + turno[i] + "\n")))
    while cantProductos[i] < 1:
        cantProductos.pop()
        turno.append(int(input("Valor inválido, ingrese un número positivo: ")))

#Comparacion de cantidad y resultados finales
mayor = cantProductos[0]
menor = cantProductos[0]
indice = 0

for i in range (len(cantProductos)):
    if cantProductos[i] > mayor:
        mayor = cantProductos[i]
        indice = i
    
print("El dia que se produjo MÁS ventiladores fue el " + str(dias[indice]) + " en turno " + turno[indice])
print("Con una producción de " + str(cantProductos[indice]) + " ventiladores \n")

for i in range (len(cantProductos)):
    if cantProductos[i] < menor:
        menor = cantProductos[i]
        indice = i
    
print("El dia que se produjo MENOS ventiladores fue el " + str(dias[indice]) + " en turno " + turno[indice])
print("Con una producción de " + str(cantProductos[indice]) + " ventiladores \n")

