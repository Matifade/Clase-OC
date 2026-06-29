# Tu código aquí 👇
try:
    dias = int(input("Ingrese una cantidad de días "))
    seg = dias * 86400
    print(f"{dias} días en segundos son: {seg} seg")
except ValueError:
    print("Ingrese un valor válido")