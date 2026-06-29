# Tu código aquí 👇
suma_total = 0
num = 1
try:
    while num != 0:
        num = 0
        num = float(input("Ingrese un número: "))
        suma_total = suma_total + num
    print(f"La suma de todos los números ingresados es: {suma_total}")
except ValueError:
    print("Ingrese un número válido")