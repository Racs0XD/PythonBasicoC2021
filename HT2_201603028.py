#Ejercicio 1
from colorama import Fore, init
init()

print(Fore.WHITE+"==================================================")
h = int(input(Fore.YELLOW+"Ingrese un valor entero positivo para la altura del triangulo: "+Fore.WHITE))

for i in range(h): 
    for j in range(i+1):
        print(Fore.GREEN+"*", end="")
    print("")

#Ejercicio 2
print(Fore.WHITE+"==================================================")

x = int(input(Fore.YELLOW+"Ingrese un valor entero positivo para determinar si es primo: "+Fore.WHITE))

def esPrimo (num):

    contador = 0

    for i in range(1, num+1):
        if num % i == 0:
            contador += 1

    if contador == 2:
        print(Fore.GREEN+"Es primo")
    else:
        print(Fore.RED+"No es primo")
    
print(esPrimo(x))
