'''
Ejercicio 1 – Socios Clubes

Luego de recabar datos de los socios en cada uno de los 17 clubes más importantes de la ciudad
se quiere determinar, para cada una de ellos, entre los censados mayores de edad (tienen 18 años o más)
quienes son más numerosos, los que son temporales (código 1) o los que son permanentes (código 2).
Para resolver esto se dispone, por cada socio de cada uno de los clubes, su código de asociado 
(1 para temporal, 2 para permanente) y la edad. Ver ejemplo.
Un código de asociado 0 (cero) indica que no hay más datos de ese club.
Valide el código entre 0, 1 y 2; no permita otros valores.
Validar la edad que no sea negativa y reconfirme si es mayor a 100.

'''

# Datos a ingresar codigo, edad
# for i in range(1,18):     para manejar los clubes
# while (codigo != 0):      while anidado dentro de for
# validar el codigo 0,1,2
# Chequear la edad la validez de la edad con un while para verificar no sea < 0 y > 100
# Reconfirme si es > 100
# Contadores para tipos de asociados


########   Programa Principal   #########

print("Calculadora de socios para clubes")
for i in range (1, 18):
    print("CLUB N°: " + str(i))

    #seteo de valores
    contadorPermanente = int(0)
    contadorTemporal = int(0)
    codigo = int(1)

    while (codigo != 0):
        #codigo de socio
        print("Elija una de las siguientes opciones")
        print("1 - Socio temporal || 2 - Socio premanente || 0 - Pasar al siguiente club")
        codigo = int(input())
        print("Usted eligio: " + str(codigo))

        #validacion del codigo
        while(codigo!=1 and codigo!=2 and codigo!=0):
            print("Valor invalido, ingrese nuevamente")
            print("1 - Socio temporal || 2 - Socio premanente || 0 - Pasar al siguiente club")
            codigo = int(input())

        #opcion 0: muestra del total de socios y paso al siguiente club
        if(codigo==0):
            print("\n")
            print("De los socios del club N°" + str(i) + " hay:")
            print("Socios permanentes: " + str(contadorPermanente) + " || Socios Temporales: "+ str(contadorTemporal))
            print("-----------------------")
            break

        #Ingreso de edad y validacion
        print("Ingrese la edad del socio:")
        edad = int(input())
        while(edad < 0):
            print("La edad ingresada es inválida, pruebe nuevamente")
            print("Ingrese la edad del socio:")
            edad = int(input())

        #Reconfirmacion si es mayor a 100 años
        if (edad > 100):
            print("Ustéd ingresó que el socio tiene: " + str(edad) + " años")
            confirmacion = input("¿Es correcto? si - no: ")

            #validacion de la confirmacion
            while (confirmacion!='si' and confirmacion!='no'):
                print("Valor inválido, ingrese nuevamente:")
                print("Ustéd ingresó que el socio tiene: " + str(edad) + " años")
                confirmacion = input("¿Es correcto? si - no: ")

            #resultado de la validacion
            if (confirmacion=='si'):
                print("Edad confirmada")
            elif (confirmacion=='no'):
                edad = 1
                print("Usuario anulado")  

        #suma de socios
        if(edad >= 18):
            if (codigo==1):
                contadorTemporal = contadorTemporal + 1
            elif (codigo==2):
                contadorPermanente = contadorPermanente + 1

#Fin del programa
print("Gracias por utilizar la calculadora de clubes, que tenga un buen día")


