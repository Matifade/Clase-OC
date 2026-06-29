# Tu código aquí 👇
def calcular_precio_final(precio, descuento):
    final = precio - (descuento * precio / 100)
    return final
precio = float(input("Ingrese el precio: "))
descuento = float(input("Ingrese el porcentaje de decuento: "))
print(f"El precio final es: {calcular_precio_final(precio, descuento)}")