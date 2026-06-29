# Tu código aquí 👇
def minutos_a_horas(minutos):
    print(f"Su tiempo en horas es: {minutos//60} horas y {minutos%60} minutos")
minutos = int(input("Ingrese una cantidad de minutos: "))
minutos_a_horas(minutos)