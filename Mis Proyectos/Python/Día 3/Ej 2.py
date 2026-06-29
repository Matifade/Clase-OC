# Tu código aquí 👇
def cuadrado(numero):
    resultado = numero * numero
    return resultado
try:
    numero = float(input("Ingrese un número: "))
    print(cuadrado(numero))
except ValueError:
    print("Ingrese un número válido")