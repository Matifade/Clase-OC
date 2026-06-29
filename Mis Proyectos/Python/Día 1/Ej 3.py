# Tu código aquí 👇
dolar = 1400
try:
    usuario = float(input("Ingresá una cantidad de dólares: "))
    pesos = dolar * usuario
    print(f"Tu dinero en pesos es: {pesos}")
except ValueError:
    print("Ingrese un valor válido")