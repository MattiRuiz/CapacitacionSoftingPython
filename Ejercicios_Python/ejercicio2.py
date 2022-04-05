'''
Ejercicio 2 – Central telefónica

Una central telefónica registra la duración de cada llamada, expresada en segundos.
A partir de esta información se quiere convertir la duración de cada llamada a:
horas, minutos y segundos y mostrarla.

Luego, al finalizar el ingreso de datos y el proceso de conversión, determinar:

    La cantidad de llamadas que superaron los 10 minutos.
    El promedio de duración de las llamadas (en segundos).
    La mínima duración de llamada (en segundos).

    No se sabe cuántas llamadas se han registrado, proponer un fin de datos.

''' 

# Datos: duración llamada en segundos.
# Estructura de control: while.
# Convetir a horas, minutos y segundos
# Contar llamadas.
# Sumar --> luego hacer el promedio.
# Buscar el minimo.
# Mostrar resultados.

###########  Programa principal  ###########

print("BIENVENIDOS A LA CALCULADORA DE TELECOM")

#Inicializador de valores estáticos
minimo = 9999999999
sumador = 0
minMayor10 = 0
cantLlamadas = 0

#Valor para ingrese al while
segundos = 1

while segundos!=0:

    #Inicializador de valores dinámicos
    horas = 0
    minutos = 0
    segundos = 0

    #ingreso de la cantidad de segundos
    print("Ingrese la duración de la llamada en segundos")
    print("Ingrese 0 para mostrar los resultados y terminar")
    segundos = int(input())

    #validador de tiempo negativo
    while segundos < 0:
        print("Valor inválido. Ingrese la duración de la llamada en segundos")
        print("O ingrese 0 para mostrar los resultados y terminar")
        segundos = int(input())

    #opcion 0: sale del programa
    if segundos == 0:
        break
    
    #Guarda el valor minimo
    if(segundos < minimo):
        minimo = segundos

    #Acumulador de segundos
    sumador = sumador + segundos

    #Conversor a horas/minutos/segundos
    while segundos > 60:
        segundos = segundos - 60
        minutos += 1
        while minutos > 60:
            minutos = minutos - 60
            horas += 1

    #Cuenta las llamadas que superaron los 10 min
    if minutos > 10:
        minMayor10 = minMayor10 + 1

    #Muestra en pantalla horas/minutos/segundos
    print("La llamada duró horas:" + str(horas) + " minutos:" + str(minutos) + " segundos:" + str(segundos))
    print("\n")

    #Contador de llamadas
    cantLlamadas = cantLlamadas + 1

#En caso de no ingresar valores no se muestra el resumen
if cantLlamadas > 0:
    print("------------------")
    print("RESUMEN")

    #Muestra las llamadas que superaron los 10 min
    print("En total de las "+ str(cantLlamadas) + " llamadas, " + str(minMayor10) + " superaron los 10 minutos.")

    #Muestra el promedio de las llamadas
    promedio = sumador / cantLlamadas
    print("El promedio de las llamadas fué de " + str(promedio) + " segundos.")

    #Muestra la llamada minima
    print("La llamada más corta duró " + str(minimo) + " segundos.")

print("\n")
print("Gracias por utilizar nuestros servicios, que tenga un buen día.")
input()



    


