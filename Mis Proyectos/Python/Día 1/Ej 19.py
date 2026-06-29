# Tu código aquí 👇
pied= "Piedra"
usuario = input("Elige: Piedra, Papel o Tijera: ")
if (usuario == "Piedra"):
    print ("Empate")
elif (usuario == "Papel"):
    print("¡Ganaste! Papel envuelve a Piedra")
elif (usuario == "Tijera"):
    print("Perdiste. Piedra rompe Tijera")
else:
    print("Ingrese una respuesta válida")