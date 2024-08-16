"""
Este programa es un minijuego en el cual se ejecuta
la elecion de un numero aleatorio mediante una funcion
situada en la libreria random

by:Fernando Ferreyra

"""


from random import randint

def adivina(j): 
    pc_num = randint(0, 100)

    for i in range(0, j):
        us_num = int(input("Ingrese un número: "))
        if us_num < pc_num:
            print("El número ingresado es MENOR.!")
        elif us_num > pc_num:
            print("El número ingresado es MAYOR.!")
        else:
            print("Adivino el número.!")
            break
        print("Intento número "+str(i+1) + ".")

    if i+1 == j:
        print('Se quedo sin intentos.!')

    else:
        i = + 1
        Intentos_1 = j - i
        if Intentos_1 > 1:
            print('Con ' + str(Intentos_1) + ' intentos de sobra.!')
        else:
            print('Con ' + str(Intentos_1) + ' intento de sobra.!')

print("\t\tAdivinar un número del 0-100")


Intentos = int(input("Ingrese un número de intentos:"))
adivina(Intentos)