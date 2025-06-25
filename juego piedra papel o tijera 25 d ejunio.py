import random
name=input("ingresa tu nombre o alias  ")
while name=="":
    print("error, no escribiste tu nombre")
    name=input("para continuar escribe tu nombre o alias ")
while True:
    opciones=["piedra","papel","tijera"]
    print("Bienvenido al juego de piedra papel o tijera")
    a=input("elige piedra, papel o tijera:  ")
    if a not in opciones:
        print("opción no válida, escribe de nuevo")
        continue
    eleccion_pc=random.choice(opciones)
    print("la pc ha elegido", eleccion_pc )
    if a==eleccion_pc:
        print("empates")
        r=input("¿Deseas jugar de nuevo? (si/no):  ")
        if r!="si":
            print("adios")
            break 
    elif (a=="piedra" and eleccion_pc=="papel")or(a=="papel" and eleccion_pc=="tijera") or (a=="tijera" and eleccion_pc=="piedra"):
        print("perdiste", name)
        r=input("¿Deseas jugar de nuevo? (si/no):  ")
        if r!="si":
            print("adios")
            break 
    else:
        print("felicidades, ganaste", name)
        r=input("¿Deseas jugar de nuevo? (si/no):  ")
        if r!="si":
            print("adios")
            break 
