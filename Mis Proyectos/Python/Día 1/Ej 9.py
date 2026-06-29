# Tu código aquí 👇
try:
    precori = float(input("Ingrese el precio original $"))
    porcdesc = int(input("Ingrese el porcentaje de descuento %"))
    montodesc = porcdesc * precori / 100
    precfin = precori - montodesc
    print(f"El precio final es de ${precfin} con un descuento de ${montodesc}")
except ValueError:
    print("Ingrese un valor válido")