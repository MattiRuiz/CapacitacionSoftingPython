"""
CONTROL DE EMPLEADOS
Del reloj de marcación del personal de una empresa se obtienen los siguientes datos: número de día, 
ID del empleado y cantidad de horas extras que trabajó. (Número entero)

Estos datos se vuelcan a una planilla donde están ordenados por día. Se sabe que todos los días que 
la empresa abrió hubo algún trabajador que hizo horas extras, y que en un mismo día no hubo dos empleados 
con igual cantidad de horas extras.

Se requiere procesar esta informacion para obtener:
Para cada día:
- El ID del empleado que trabajó la mayor cantidad de horas extras
- El promedio de horas extras trabajadas (cantidad total de horas extras / cantidad total de personas 
que trabajaron extras)
Para todo el periodo en estudio:
- La cantidad de días que se trabajó


"""

######### Inicio del programa #########

#Tabla
calendario = []
identificacion = []
horasExtras = []

#Variables
validez = ""
bandera = int()

#Constantes
validadores = ('si', 'no')


print("CONTROL DE EMPLEADOS")

tam = int(input("Cuantos dias tiene el mes a ingresar?: "))
while tam < 2 or tam > 31:      #Setear los valores entre 28 a 31 dias que puede llegar a tener el mes. Fueron cambiados para probar los resultados
    tam = int(input("Tamaño inválido. Ingrese cuandos dias tiene el mes a ingresar?: "))

print("Ingrese los empleados, ordenados por día, ID y cantidad de horas extras.")

for i in range(tam):
    dia = i+1
    validez = 'si'

    while validez != 'no':
        print("DIA ", dia)
        calendario.append(dia)

        id = int(input("Ingrese el número de identificación del empleado\n"))
        while id < 0: id = int(input("Valor inválido, ingrese un número positivo\n"))
        

        if len(identificacion) > 0:
            bandera = 0
            while bandera != 1:
                bandera = 1
                for j in range(len(identificacion)):
                    if calendario[j] == i+1 and identificacion[j] == id:
                        id = int(input("Identificador ya utilizado para este día. Ingrese uno diferente: "))
                        bandera = 0
    
        identificacion.append(id)

        extras = int(input("Ingrese la cantidad de horas extra que el empleado hizo este día: "))
        while extras < 0 or extras > 8:
            extras = int(input("Cantidad de horas extras erroneo. Ingrese un valor entre 0 y 8: "))
        
        if len(horasExtras) > 0:
            bandera = 0
            while bandera != 1:
                bandera = 1
                for j in range(len(horasExtras)):
                    if calendario[j] == i+1 and horasExtras[j] == extras and extras != 0:
                        print("Cant. de horas extras ingresada. No se pueden repetir cant. de horas un mismo día (con excepcion del 0)")
                        extras = int(input("Intente nuevamente: "))
                        while extras < 0 or extras > 8:
                            extras = int(input("Cantidad de horas extras erroneo. Ingrese un valor entre 0 y 8: "))
                        bandera = 0

        horasExtras.append(extras)

        print("Desea registrar otro empleado para el día ", dia, "?")
        validez = input("Ingrese: si - no: ")
        if validez not in validadores:
            validez = input("Valor inválido. Ingrese: si - no: ")

#Fin del ciclo / inicio de resultados

#Nuevas variables a utilizar
sumador = int()
mayor = 0
indice = int()
cantEmpleados = []
extrasTotal = int()
cantDias = []

for i in range(len(identificacion)):

    #Calcula el empleado con mayor cant. de horas extras
    sumador = 0
    for j in range(len(identificacion)):
        if identificacion[i] == identificacion[j]:
            sumador = sumador + horasExtras[j]

    if sumador > mayor:
        mayor = sumador
        indice = i    

    #Calcula la cantidad de empleados y el total de horas extra
    if horasExtras[i] > 0:  
        extrasTotal = extrasTotal + horasExtras[i]  
        if identificacion[i] not in cantEmpleados:
            cantEmpleados.append(identificacion[i])

    #Calcula la cantidad de dias trabajados
    if calendario[i] not in cantDias:
        cantDias.append(calendario[i])
    

print("El vendedor que hizo más horas extras fue ID:", identificacion[indice], "con ", mayor, " horas extras")
print("El promedio de horas extras trabajadas fue de: ", extrasTotal / len(cantEmpleados))
print("Los días trabajados fueron ", len(cantDias), ": \n", cantDias)

