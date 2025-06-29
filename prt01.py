'''
Author FP
v0.01 - 29/06/2025 FP: Creación - "Calculadora" de módulo para tres ejes (x,y,z) - Álgebra I (Elementos de Álgebra y Geometria).
                       Test de subida a GitHub.
'''

lista = []      #Almacena los valores ingresados por el usuario.
listae = []     #Almacena los valores exponenciados.
modulo = []     #Almacena la raiz del módulo.

def abcde(lista):
    nro = 0
    af1 = 0
    print("--Se le solicitará el ingreso de 3 valores decimales--")     #Ingeso de tres valores, uno por eje x,y,z.
    for i in range(3):
        nro += 1
        entrada = float(input(f"Ingrese valor {nro}: "))
        lista.append(entrada)
    
    for j in range(len(lista)):                                         #Echo de cantidad de elementos almacenados
        af1 += 1                                                        #Defino variable (i genera conflictos)
        vexp = lista[af1-1] ** 2                                        #Valor exponencial al cuadrado a cada item de la lista
        listae.append(vexp)                                             #Almaceno lo exponenciado en la lista "listae"

    sumaejes = listae[0] + listae[1] + listae[2]                        #Suma los tres valores exponenciados
    raizmodu = sumaejes ** 0.5                                          #Realiza la raiz cuadrada de la sumatoria
    modulo.append(raizmodu)                                             #Almacena el valor en la lista "modulo".

    print(f"\nLista: {lista} \nLista exponencial: {listae} \nMódulo: {modulo} \n")

abcde(lista)
