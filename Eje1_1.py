import random
import time

pc_num = random.randint(0, 100)
intentos = 0
current_intent = 1
user_num = 0

def ingresar_intentos():
    while(1):
        try:
            intentos = int(input("Ingrese el numero de intentos: "))
        except Exception as e:
            print(f"El valor ingresado no es un numero! [{e}]")
        else:
            print(f"El numero ingresado es {intentos}.")
            break
    return intentos

def number_user():
    while(1):    
        try:
            user_num = int(input("Ingrese un numero: "))
            break
        except Exception as e:
            print(f"El valor ingresado no es un numero! [{e}]")
    return user_num

def Adivina():
    global pc_num,current_intent
    print(f"{pc_num}")
    global user_num 

    while current_intent <= intentos:      
        print(f"Numero de Intentos {current_intent}")  
        user_num = number_user()

        if user_num != pc_num:
            if user_num < pc_num:
                print("El número ingresado es MENOR.!")
            elif user_num > pc_num:
                print("El número ingresado es MAYOR.!")
            current_intent += 1
        else:      
            print(f"Adivino el numero con {intentos - current_intent} de sobra.")
            break


intentos = ingresar_intentos()

print(f"{current_intent} and {intentos}")
Adivina()
print(f"GAME OVER.")