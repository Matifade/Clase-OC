# Tu código aquí 👇
try:
    nota = float(input("Ingrese un la nota "))
    if nota>=6:
        print("APROBADO")
    else:
        print("DESAPROBADO")
except ValueError:
    print("Ingrese una nota válida")