#Ejercicio 1
from colorama import Fore, init
init()
print(Fore.WHITE+"==================================================")
print(Fore.WHITE+"==============" + Fore.LIGHTBLUE_EX, "Bienvenido al Sistema" + Fore.WHITE, "=============")
print(Fore.WHITE+"==================================================")
x = str.lower(input(Fore.YELLOW+"Ingrese su contraseña: "+Fore.WHITE))
print(Fore.WHITE+"==================================================")
y = str.lower(input(Fore.YELLOW+"Ingrese su contraseña de nuevo para validar: "+Fore.WHITE))
if y == x :
    print(Fore.GREEN+"Contraseña validada")
else:
    print(Fore.RED+"Contraseña incorrecta")

#Ejercicio 2
print(Fore.WHITE+"==================================================")
print(Fore.WHITE+"===============" + Fore.LIGHTBLUE_EX, "Asignación de Grupo" + Fore.WHITE, "==============")
print(Fore.WHITE+"==================================================")
nombre = input(Fore.YELLOW+"Ingrese nombre completo: "+Fore.WHITE)
genero = input(Fore.YELLOW+"Ingrese su genero: "+Fore.WHITE)
print(Fore.WHITE+"==================================================")
if genero == "M":
    if nombre.lower() < "m":
        grupo = "A"
    else:
        grupo = "B"
else:
    if nombre.lower() > "n":
        grupo = "A"
    else:
        grupo = "B"
print(Fore.GREEN+"Tu grupo es: " +grupo)
print(Fore.WHITE+"==================================================")