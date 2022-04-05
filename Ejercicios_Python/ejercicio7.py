"""
SALTO EN LARGO

En un torneo de salto en largo se pueden inscribir hasta 50 participantes. Cada participante está 
identificado con un número no necesariamente correlativo y realiza 3 saltos, de los cuales se registra 
el largo del mismo.
Se pide, primero realizar un bosquejo de los datos. Luego realizar un algoritmo que informe el ganador de 
la competencia (aquel que saltó más lejos en cualquiera de los 3 intentos), la distancia del salto ganador 
y cuántos participantes se inscribieron.

Desafio extra: suponer que un participante puede no realizar los 3 saltos y que en este caso se lo 
considera descalificado, por lo que no se lo tendrá en cuenta para elegir al ganador de la competencia. 
Modificar el algoritmo anterior para contemplar este caso.

------------------------------------

Proceso de inscripcion de participantes:
- ID y 3 saltos, el mejor queda guardado.

Proceso de datos de saltos
- Buscar el más largo y devolverlo.
- En caso de ingresar 0mts significa que no se realizo ese salto. Ese competidor se queda descalificado

Devolucion de datos:
- Primero devolver una tabla con: ID del atleta, salto 1, salto 2, salto 3 y salto más largo.
- Mostrar el ganador (salto más lejos) y la distancia saltada.
- Mostrar cant. de participantes.

"""

############## Inicio del programa ##############

#Listas
ids = []
salto1 = []
salto2 = []
salto3 = []
saltoResultado = []

#Variables
idcampeon = int()
saltoCampeon = float()
salir = 1
id = int()
salto = float()

print("SALTO EN LARGO")

#def ingresoDatos():
while len(ids) > 50 or salir == 1:

    id = int(input("Ingrese el ID de atleta n°" + str(len(ids)+1) + ":"))
    while id < 0 or id > 999:
        id = int(input("Valor inválido. Ingrese un número entre 0 y 999: "))

    ids.append(id)
    
    for i in range(3):
        salto = float(input("Ingrese la distancia del salto n°" + str(i+1) + " o 0 para descalificado:\n"))
        while salto < 0 or salto > 10:
            salto = float(input("Valor inválido.\nIngrese la distancia del salto n°" + str(i+1) + " o 0 para descalificado:\n"))
        if i == 0:
            salto1.append(salto)
        elif i == 1:
            salto2.append(salto)
        elif i == 2:
            salto3.append(salto)

    salir = int(input("Desea ingresar otro participante? 1) Si 2) No :"))
    while salir != 1 and salir != 2:
        salir = int(input("Valor inválido. Ingrese 1) Si 2) No :"))

if len(ids) > 50:
    print("Sólo se puede ingresar hasta 50 atletas.\n")


#def muestraDatos()
print("RESULTADOS")
saltoResultado = salto1

for i in range(len(ids)):
    
    print("ID:"+str(ids[i])+" | S1: "+str(salto1[i])+" | S2: "+str(salto2[i])+" | S3: "+str(salto3[i]))

    if salto1 == 0 or salto2 == 0 or salto3 == 0:
        saltoResultado = 0
    else:
        if salto2[i] > saltoResultado[i]:
            saltoResultado[i] = salto2[i]
        
        if salto3[i] > saltoResultado[i]:
            saltoResultado[i] = salto3[i]

    if saltoResultado[i] > saltoCampeon:
        saltoCampeon = saltoResultado[i]
        idcampeon = ids[i]

print("\nCAMPEÓN:\nID: "+str(idcampeon)+"\nDistancia: "+str(saltoCampeon))
print("Cantidad de participantes: "+str(len(ids)))
