# Tu código aquí 👇
try:
    num = float(input("Ingrese un número "))
    if num>0:
        print("Positivo")
    elif num<0:
        print("Negativo")
    else:
        print("Cero")
except ValueError:
    print("Ingrese un valor válido")