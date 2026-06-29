# Tu código aquí 👇
try:
    num1= float(input("Ingrese un número "))
    num2= float(input("Ingrese un número "))
    if num1<num2:
        print(f"El número más grande es {num2}")
    elif num1>num2:
        print(f"El número mayor es {num1}")
    else:
        print("Los números son iguales")
except ValueError:
    print("Ingrese un valor válido")