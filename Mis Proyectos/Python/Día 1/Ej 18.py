# Tu código aquí 👇
try:
    num=7
    usuario = int (input("Elige un número del 1 al 10: "))
    if (num==usuario):
        print("¡Ganaste!")
    else:
        print("Intentá de nuevo")
except ValueError:
    print("Ingrese un valor válido")