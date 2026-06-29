# Tu código aquí 👇
try:
    base = float(input("¿Cuánto es tu base? "))
    altu = float(input("¿Cuánto es tu altura? "))
    area = base * altu
    print (f"Tu área es de: {area}")
except ValueError:
    print("Ingrese un valor válido")