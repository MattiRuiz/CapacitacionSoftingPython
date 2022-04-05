vertices = []
grados = []

def multigrafo_conexo (vertices, grados):
    print("ingrese la cantidad de vertices que tiene el multigrafo conexo")
    cantVertices = int(input())

    for x in range(cantVertices):
        print("ingrese el nombre del vertice " + str(x+1) + ": ")
        nombreVertice = input()
        while nombreVertice in vertices:
            nombreVertice = input("Nombre de vertice repetido, ingrese nuevamente:")
        vertices.append(nombreVertice)

        print("ingrese el grado del vertice " + str(x+1) + ":")
        grado = int(input())
        grados.append(grado)


def analisisDatos(vertices, grados):
    bandera = 0
    impar = 0
    for x in range(len(vertices)):
        if grados[x]%2 == 0:
            bandera = bandera + 1
        else:
            print("El vertice" + vertices[x] + " tiene grado impar")
            impar = impar + 1

    print("Bandera:"+str(bandera))
    print("Impar:"+str(impar))
    if bandera == vertices:
        print("Contiene un circuito eulereano")
    elif impar == 2:
        print("Contiene un recorrido eulereano")
    else:
        print("No contiene circuito ni recorrido eulereano")

#### Inicio ejecución ####

multigrafo_conexo (vertices, grados)
analisisDatos(vertices, grados)