# Tu código aquí 👇
try:
    cels = float ( input("Ingresa tu temperatura en Celsius: "))
    farh = (cels * 9/5) + 32
    print (f"Tu temperatura en Farenheit es: {farh}")
except ValueError:
    print("Ingrese un valor válido")