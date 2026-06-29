# Tu código aquí 👇
try:
    num = float (input("Ingresa un número: "))
    for mult in range(1,11):
        multfin = num*mult
        print(f"{num}*{mult}={multfin}")
except ValueError:
    print("Ingrese un número válido")