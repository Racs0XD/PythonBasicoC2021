from colorama import Fore, init
init()

print(Fore.WHITE+"==================================================")
print(Fore.WHITE+"======" + Fore.RED , "Bienvenido a calculo de masa corporal" + Fore.WHITE, "=====")
print(Fore.WHITE+"==================================================")

pesoKg = input(Fore.YELLOW+"Por favor ingreso su peso en kg: "+Fore.WHITE)

estaturaM = input(Fore.YELLOW+"Por favor ingreso su estatura en m: "+Fore.WHITE)

print(Fore.WHITE+"===================" + Fore.RED , "CALCULANDO" + Fore.WHITE, "===================")

imc = round(float(pesoKg) / (float(estaturaM) * float(estaturaM)),2)

print(Fore.GREEN+"Tu índici de masa corporal (IMC) es:  " +Fore.WHITE,  imc  ,Fore.WHITE+"Kg/m\u00B2")

print(Fore.WHITE+"==================================================")

print(Fore.WHITE+"==================" + Fore.RED , "HASTA PRONTO" + Fore.WHITE, "==================")

print(Fore.WHITE+"================================================== ")