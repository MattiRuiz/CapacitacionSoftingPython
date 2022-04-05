"""
COMERCIO DE DIAMANTES
Una empresa dedicada al comercio de diamantes posee 15 talladores, identificados con el número del 1 al 15.
Un experto clasificador evalúa los diamantes de acuerdo a tres criterios: el peso en quilates (un número real),
la pureza (texto de 3 caracteres) y el color (una letra entre la D y la Z).

Semanalmente el experto clasifica los diamantes y vuelca esta información en una tabla ordenada 
por número de tallador, es decir, comienza por los diamantes del tallador 1, luego los del 2 y así 
sucesivamente hasta terminar con los 15 talladores. Se dispone de la cantidad de diamantes que tallo cada uno.
Realizar un ejemplo de la tabla y datos que puede contener en la que se vuelca la información. 

Luego realizar un algoritmo que recibiendo los datos de la tabla generada por el experto muestre:

Por cada tallador:
- La cantidad de diamantes cuyo color esté entre la D y la G
- El peso total de los diamantes tallados.

En general:
- La cantidad total de diamantes tallados

"""

############ Comienzo del programa ############

#Listas
tallador = []
pesosQuilates = []
purezas = []
colores = []

#Variables
peso = 0
numTallador = 0
cantDiamantes = 0
pureza = str()
color = str()
contadorColores = int()
pesoTotal = int()
diamantesTotal = int()

#### FUNCIONES ####

#Función peso
def funcPeso(peso, pesosQuilates):
    print("TALLADOR: " + str(x+1) + " DIAMANTE: " + str(i+1))
    peso = int(input("Ingrese el peso en quilate: "))
    while peso < 0:
        peso = int(input("Valor inválido. Ingrese el peso en quilates: "))

    pesosQuilates.append(peso)

#Funcion pureza
def funcPureza(pureza, purezas):
    pureza = str(input("Ingrese la pureza del diamante: "))
    while len(pureza) > 3:
        pureza = str(input("Valor inválido. La pureza solo puede tener 3 caracteres. \nIngrese la pureza del diamante: "))

    purezas.append(pureza)

#Funcion color
def funcColor(color, colores):
    color = str(input("Ingrese el color del diamante: "))
    color = color.upper()
    colorOrd = ord(color)
    while colorOrd < ord("D") or colorOrd > ord("Z"):
        color = str(input("Valor inválido. Pruebe con un valor entre D y Z. \nIngrese el color del diamante: "))
        color = color.upper()
        colorOrd = ord(color)

    colores.append(color)

#Funcion resultados
def funcResultados(colores, contadorColores, diamantesTotal, pesosQuilates, pesoTotal):
    for j in range(len(colores)):
        if ord(colores[j]) > ord("D") and ord(colores[j]) < ord("G"):
            contadorColores = contadorColores + 1
        
        pesoTotal = pesoTotal + pesosQuilates[j]

    diamantesTotal = len(pesosQuilates)

    print("RESULTADOS:")
    print("Candidad de diamantes cuyo color esté entre la D y la G: " + str(contadorColores))
    print("El peso total de los diamantes tallados: " + str(pesoTotal) + " quilates")
    print("Cantidad de diamantes tallados: " + str(diamantesTotal))


### INICIO DEL EJECUTABLE ###

print("COMERCIO DE DIAMANTES")
for x in range(2):
    cantDiamantes = int(input("Ingrese la cantidad de diamantes pertenecientes al tallador n°" + str(x+1) + ": "))
    while cantDiamantes < 0:
        cantDiamantes = int(input("Cantidad inválida. \nIngrese la cantidad de diamantes pertenecientes al tallador n°" + str(x+1) + ": "))

    for i in range(cantDiamantes):
        numTallador = x+1
        tallador.append(numTallador)

        funcPeso(peso, pesosQuilates)

        funcPureza(pureza, purezas)

        funcColor(color, colores)

funcResultados(colores, contadorColores, diamantesTotal, pesosQuilates, pesoTotal)
