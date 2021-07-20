import random

Min = 1
Max = 6

print(" Instrucciones de juego")
print(" Los dados se van a tirar automaticamente")
print(" Vas a poder tirar cuantas veces quieras")
print(" Para volver a jugar escribe si")
print("A por todas juagador suerte")
print("                                                                            ")
print("                                                                            ")
roll_again = "yes"

while roll_again == "yes" or roll_again == "si":
    print("Los dados estan en el aire...")

    var1 = random.randint(Min, Max)
    var2 = random.randint(Min, Max)
    var3 = random.randint(Min, Max)
    res = var1 + var2 + var3
    print(f"Los dados han dado {res}")

    if res == 2:
        print("Tu puntuacion es de 2 puntos vuelve a tirar a ver si hay mas suerte")
    elif res == 3:
        print("Los dados han decidido que tu puntion es de un 3 vuelve a tirar")
    elif res == 4:
        print("Tu puntuacion es de 4 puntos no es muy buena puntuacion vuelve probar")
    elif res == 5:
        print("Tu puntuacion es de 5 puntos podria estar mejor vuelve a tirar")
    elif res == 6:
        print("Not bad sigue probando para llegar a la puntuacion mas alta")
    elif res == 7:
        print("Un siete wow seguro que no es tu primera tirada")
    elif res == 8:
        print("Australopitecus afarensis un 8 Felicidades")
    elif res == 9:
        print("Por las conchas de neptuno un 9")
    elif res == 10:
        print("No se seras tu el ganador de la loteria no poruqe sacar un 10 muy dificil")
    elif res == 11:
        print("Te ha bajado dios ver has sacado 11 puntos los felicidades champion")
    elif res == 12:
        print("Literalmente tienes mis respetos")
    elif res == 13:
        print(" Creo que estas haciendo trampas")
    elif res == 14:
        print(" El FBI esta en la puerta")
    elif res == 15:
        print("Quieres tambien a la interpool")
    elif res == 16:
        print("Nada estas tonto que no sigas que es imposible sacar la puntuacion maxima")
    elif res == 17:
        print("Las Puertas del cielo estan abiertas para ti adelante")
    else:
        print(" No se que esto porque no sale ningun numero encima xDD")
    roll_again = input("Roll the dices again?: ")
print("Bueno si no quieres juagr solo tenias que decirlo")
