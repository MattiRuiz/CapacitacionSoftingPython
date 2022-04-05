"""
CLASIFICACIÓN DE PELÍCULAS
Realizar un sistema de clasificación de contenido de las peliculas por edades. 
El sistema dispone de la siguiente categoría:

G | Todas las audiencias | VERDE
P | Asistencia de padres recomendada | VERDE
M | Asistencia de padres muy recomendada | AMARILLO
R | Restringido | AMARILLO
N | Prohibida para menores ded 17 | ROJO

Para anticipar el contenido de la película o del avance, se creó una calificación especial 
con franjas de color.

Situación problemática:
Se solicita realizar un algoritmo en pseudocódigo que, entre otras tareas, muestre el color de fondo 
a partir del dato de la clasificación, partiendo de un listado de películas de diferentes países.
El listado contiene la siguiente información:
- Código de país (entero entre 1 y 30)
- Código de película (entero)
- Clasificación (carácter)

El listado está ordenado por código de país. Se sabe que en total son 30 países. No se sabe cuántas 
películas hay por cada país, pero un código de película igual a 0 indica el final.
El algoritmo deberá solicitar por cada película los tres datos. A partir del dato de clasificación, 
mostrar en pantalla el nombre del color correspondiente (VERDE, AMARILLO o ROJO). Además, se debe calcular 
por cada país el porcentaje de películas calificadas como G o P.
El algoritmo deberá mostrar también el código del país con mayor cantidad de películas y dicha cantidad.

"""

########### Inicio del programa ###########

#Listas
codPais = []
codPeliculas = []
calificaciones = []

#Constantes
cantPaises = 30
tipoCalificaciones = ('G', 'P', 'M', 'R', 'N')


#### FUNCIONES - Ingreso de datos ####

def ingresoDatos(x, codPeliculas):
    pelicula = 1
    while pelicula != 0:
        pelicula = int(input("Ingrese el código de la película o ingrese 0 para pasar al siguiente país: "))
        if pelicula > 0:
            codPeliculas.append(pelicula)
            codPais.append(x+1)

            ingresoCalificacion(tipoCalificaciones, calificaciones)

        elif pelicula == 0:
            print("-- Siguiente país --")
        else:
            print("Valor inválido, intente nuevamente")
            

def ingresoCalificacion(tipoCalificaciones, calificaciones):
    calificacion = str(input("Ingrese la calificación de la película: "))
    calificacion = calificacion.upper()
    while calificacion not in tipoCalificaciones:
        print("Valor inválido, elija una de las siguientes calificaciones:")
        print(tipoCalificaciones)
        calificacion = str(input("Ingrese la calificación de la película: "))
        calificacion = calificacion.upper()

    calificaciones.append(calificacion)
    colores(calificacion)


#### FUNCIONES - Análisis de datos ####

def colores(calificacion):
    if calificacion == 'G' or calificacion == 'P':
        print("Color: VERDE")
    elif calificacion == 'M' or calificacion == 'R':
        print("Color: AMARILLO")
    elif calificacion == 'N':
        print("Color: ROJO")


def analisisDatos(calificaciones, codPais):
    peliculasMayor = 0
    for x in range(cantPaises):
        peliculasTotales = 0
        peliculasGyP = 0
        for j in range(len(codPais)):
            if codPais[j] == x+1:
                peliculasTotales = peliculasTotales + 1
                if calificaciones[j] == 'G' or calificaciones[j] == 'P':
                    peliculasGyP = peliculasGyP + 1
        if peliculasTotales > peliculasMayor:
            peliculasMayor = peliculasTotales
            indice = x+1

        peliculasCalculo = (peliculasGyP / peliculasTotales) * 100
        peliculasCalculo = int(peliculasCalculo)
        print("Pais n°: " + str(x+1) + " | Porcentaje de peliculas G y P: " + str(peliculasCalculo) + "%")

    print("\nEl pais con mayor cantidad de películas fué el n°: " + str(indice))
    print("Con: " + str(peliculasMayor) + " peliculas")


##### Inicio de la interface #####

print("CLASIFICACIÓN DE PELÍCULAS")
for x in range(cantPaises):
    print("Pais n°" + str(x+1) + ":")
    ingresoDatos(x, codPeliculas)

print("\nRESULTADOS")
analisisDatos(calificaciones, codPais)