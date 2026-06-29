# Tu código aquí 👇
try:
    num = int (input ("Ingresá un número entero: "))
    if num%2 == 0:
        print("Es par")
    else:
        print ("No es par")
except ValueError:
    print("Ingrese valores válidos")