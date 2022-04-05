"""
TEMPERATURAS DIARIAS
A lo largo de un día se ha registrado la temperatura de un determinado ambiente a intervalos de media hora 
comenzando a las 00:00hs. Se desea conocer:
- La cantidad de veces que la temperatura superó los 25°C.
- La temperatura máxima y la mínima, con la hora correspondiente.

"""

############ Inicio del programa ############

#Variables
horas = 0
minutos = 0
temperatura = 0

#Contadores y guardadores de datos
tempMax = -10
horasMax = 0
minMax = 0

tempMin = 55
horasMin = 0
minMin = 0

tempSup25 = 0

print("TEMPERATURAS DIARIAS")

for i in range (47):
    
    print ("HORA: " + "{:02d}".format(horas) + ":" + "{:02d}".format(minutos))
    temperatura = int(input("Ingrese la temperatura correspondiente: "))
    while temperatura < -10 or temperatura > 55:
        temperatura = int(input("Valor inválido. Ingrese una temperatura entre -10 y 55 grados: "))

    if temperatura > 25:
        tempSup25 += 1
    
    if temperatura > tempMax:
        tempMax = temperatura
        horasMax = horas
        minMax = minutos
    elif temperatura < tempMin:
        tempMin = temperatura
        horasMin = horas
        minMin = minutos    

    #Reloj
    if minutos == 00:
        minutos = 30
    else:
        minutos = 00
        horas +=1

    
print("\nCantidad de veces que la temperatura supero los 25°:", tempSup25)
print("\nLa temperatura mínima fué de", tempMin, "° en el horario: "+ "{:02d}".format(horasMin) + ":" + "{:02d}".format(minMin) )
print("La temperatura máxima fué de", tempMax, "° en el horario: "+ "{:02d}".format(horasMax) + ":" + "{:02d}".format(minMax) )