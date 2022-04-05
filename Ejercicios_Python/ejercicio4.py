"""
PLANTA DE AUTOPARTES
Una planta que produce autopartes posee varias máquinas destinadas a la producción de determinadas piezas. 
Se dispone de una planilla que, durante la última semana, se ha completado manualmente. 

En la misma se anota:
- Número de identificación de la máquina (número entero)
- Tiempo de funcionamiento semanal (en horas, minutos y segundos)
- Cantidad de piezas producidas (número entero)

Se desconoce la cantidad de máquinas que se encuentran trabajando actualmente.

Se requiere procesar esta información tal que se determine:
- El rendimiento de cada máquina (cantidad de piezas/tiempo en segundos)
- La cantidad total de piezas producidas en la planta esa semana

"""

######### Inicio del programa #########
menu = 1
i = 0

#Tabla
identMaquina = []
horas = []
minutos = []
segundos = []
cantPiezas = []

while menu != 2:
    identMaquina.append(int(input("Ingrese el n° de identificación de la máquina\n")))
    while identMaquina[i] < 1 or identMaquina[i] > 999:
        identMaquina.pop()
        identMaquina.append(int(input("Valor inválido, ingrese el n° de la maquina nuevamente\n")))
    

    print("Ingrese el tiempo de funcionamiento semanal")

    horas.append(int(input("Horas: ")))
    while horas[i] < 0:
            horas.pop()
            horas.append(int(input("Ingrese un valor positivo. Horas: ")))

    minutos.append(int(input("Minutos: ")))
    while minutos[i] < 0 or  minutos[i] > 60:
            minutos.pop()
            minutos.append(int(input("Ingrese un valor entre 0 y 60. Minutos: ")))
  
    segundos.append(int(input("Segundos: ")))
    while segundos[i] < 0 or segundos[i] > 60:
            segundos.pop()
            segundos.append(int(input("Ingrese un valor entre 0 y 60. Segundos: ")))


    cantPiezas.append(int(input("Ingrese la cantidad de piezas producidas\n")))
    while cantPiezas [i] < 0:
        cantPiezas .pop()
        cantPiezas .append(int(input("Valor inválido, ingrese un número positivo\n")))

    menu = int(input("Desea ingresar otra máquina a la lista? 1 - Si || 2 - No\n"))
    while menu != 1 and menu != 2:
        menu = int(input("Valor invalido. Ingrese: 1 - Si || 2 - No\n"))
    
    if menu == 1: i += 1

#Rendimiento de cada máquina
i = 0

for j in range (len(identMaquina)):
    minutos[i] = minutos[i] + (horas[i] * 60)
    segundos[i] = segundos[i] + (minutos[i] * 60)

    maquinaXseg = 0
    maquinaXseg = segundos[i]/cantPiezas[i]

    print("La máquina", str(identMaquina[i]), "produjo una pieza cada {0:.2f} segundos".format(maquinaXseg))

    i += 1

piezasTotal = 0
for j in range(len(cantPiezas)):
    piezasTotal = piezasTotal + cantPiezas[j]

print("\nLas piezas totales producidas esta semana son: ", piezasTotal)