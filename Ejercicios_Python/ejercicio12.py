'''
El sector de ensamble de una línea productiva de una empresa está dotada de 15 operadores 
los cuales están distribuidos en 3 turnos. Los operadores están identificados con un número del 1 al 15. 
Del 1 al 5 están en el primer turno, del 6 al 10 en el segundo y del 11 al 15 en el tercero.
Cada un determinado período de tiempo (se desconoce la cantidad de días transcurridos hasta esa fecha), 
el Gerente de Producción necesita evaluar distintos indicadores asociados con sus objetivos anuales. 
Para realizar esto extrae los siguientes datos del sistema de gestión: día y mes de la producción, 
costo unitario de cada unidad ensamblada ese día y cantidad de productos ensamblados.
-----------------
Realizar los siguientes algoritmos:
Algoritmo A:
- ¿Cuál es el costo total de producción por las unidades de cada día?
- Determinar el promedio de productos por colaboradores del turno 2 ensamblados en cada día.
- Calcular la cantidad de ausencias por turno en todo el período
Algoritmo B:
- Determinar la jornada (día y mes) de mayor ensamble en todo el período. Considerar que hay una sola
- Determinar el promedio diario de productos ensamblados del mes 6
- Informar a medida que se vayam ingresando los datos mediante el texto "Alerta de ensamble" si, 
en ese día, la cantidad de producutos ensamblados no superó las 400 unidades o superó las 1700.
Algoritmo C:
- Determinar la cantidad total de productos ensamblados en cada turno en el período evaluado.
- Determinar el mes en el cuál se produjo el mayor costo unitario y cuál fue ese mismo.
'''

#Listas
dias = []
meses = []
costosUnit = []
operador1 = []
operador2 = []
operador3 = []
operador4 = []
operador5 = []
operador6 = []
operador7 = []
operador8 = []
operador9 = []
operador10 = []
operador11= []
operador12 = []
operador13 = []
operador14 = []
operador15 = []

#Variables 
dia = int()
mes = int()
costo = float()
cantProductos = int()
controlador = int()

#Constantes
cantEmpleados = 15

############## Funciones ##############

def controladorDiaMes():
    mes = int(input("Ingrese el número del mes a cargar: "))
    while mes < 1 or mes > 12:
        mes = int(input("Valor ingresado incorrecto, ingrese el número del mes nuevamente: "))
    meses.append(mes)
    
    dia = int(input("Ingrese la fecha del día a cargar: "))
    while dia < 1 or dia > 31:
        dia = int(input("Fecha inválida, ingrese nuevamente: "))
    dias.append(dia)

    print("Desea ingresar otro día para el mes %d ?", format(mes))
    controlador = int(input("1) Si  2) No : "))
    while controlador < 1 or controlador > 2:
        print("Valor ingresado incorrecto, intente nuevamente")
        controlador = int(input("1) Si  2) No : "))



############## Inicio del programa ##############
