"""
LABORATORIO BACTEREOLÓGICO
En un laboratorio de bacteriología, se tienen clasificados los tipos de análisis que se realizan en 27 
categorías. De cada categoría de análisis se conoce la cantidad de reactivos necesarios y de cada uno 
de ellos se tiene:
- Miligramos a usar
- Temperatura de fusión del mismo (entero).

Los valores de los datos se ingresarán desde teclado. Desarrollar un programa que permita procesar 
esos datos para obtener para cada categoría de análisis:
- El peso total de los materiales reactivos necesarios
- La cantidad de reactivos que requieren entre 10 y 20 mg
- El procentaje de reactivos que tienen una temperatura de fusión superior a los 50°C
Además, se desea conocer cuál categoría consume mayor cantidad de reactivos en mg y cuál es esa cantidad.

"""

############### Inicio del programa ###############
#Listas
categorias = []
reactivos = []
miligramos = []
temperaturas = []

#Variables
cantReactivos = int()

#Constantes
cantCategorias = 27


#### FUNCIONES - Ingreso de datos ####

def funcReactivos(i, reactivos):
    reactivos.append(i+1)

def funcMiligramos(i, miligramos):
    miligramo = float(input("Ingrese la cantidad de miligramos del reactivo "+ str(i+1) + ": "))
    while miligramo < 0:
        miligramo = float(input("Cantidad inválida. \nIngrese la cantidad de miligramos del reactivo "+ str(i+1) + ": "))
    miligramos.append(miligramo)

def funcTemperatura(i, temperaturas):
    temperatura = int(input("Ingrese la temperatura de fusión del reactivo "+ str(i+1) + ": "))
    temperaturas.append(temperatura)


#### FUNCIONES - Análisis de datos ####

def analisisPeso(miligramos, categorias, reactivos):
    sumapeso = float(0)
    mayorPeso = miligramos[0]
    indice = int()
    for j in range(len(miligramos)):
        sumapeso = sumapeso + miligramos[j]
        if miligramos[j] >= 10 and miligramos[j] <= 20:
            rangoPeso =+ 1
        if miligramos[j] > mayorPeso:
            mayorPeso = miligramos[j]
            indice = j
    print("Peso total de los materiales reactivos necesarios: " + str(sumapeso) + "mg.")
    print("Cantidad de reactivos entre 10 y 20mg.: " + str(rangoPeso))
    print("\nMayor cantidad de reactivos:")
    print("Categoría: " + str(categorias[indice]) + " Cant. Reactivo/s: " + str(reactivos[indice]) + " Peso: " + str(miligramos[indice]) + "mg.")

def analisisTemperaturas(temperaturas):
    rangoTemperatura = int(0)
    for j in range(len(temperaturas)):
        if temperaturas[j] > 50:
            rangoTemperatura =+ 1
    print("\nCantidad de reactivos con temp. de fusión superior a los 50°: " + str(rangoTemperatura)) 


#### Inicio interface ####

print("LABORATORIO BACTEREOLÓGICO")
for x in range(cantCategorias):
    print("Categoría n°:"+ str(x+1))
    cantReactivos = int(input("Ingrese la cantidad de reactivos pertenecientes a esta categoría: "))
    while cantReactivos < 1:
        cantReactivos = int(input("Valor inválido. \nIngrese la cantidad de reactivos pertenecientes a esta categoría: "))

    for i in range(cantReactivos):
        categorias.append(x+1)

        funcReactivos(i, reactivos)

        funcMiligramos(i, miligramos)
        
        funcTemperatura(i, temperaturas)

#Muestro resultados
print("\nRESULTADOS")
analisisPeso(miligramos, categorias, reactivos)
analisisTemperaturas(temperaturas)