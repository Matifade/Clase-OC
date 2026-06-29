# Tu código aquí 👇
try:
    horas = float(input("Ingrese el total de horas trabajadas: "))
    tar = float(input("Ingrese el precio de su tarifa por hora: $"))
    sal = horas * tar
    print(f"Tu salario es de: ${sal}")
except ValueError:
    print("Ingrese un valor válido")