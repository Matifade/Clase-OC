# Tu código aquí 👇
def es_par(numero):
    if (numero%2) == 0:
        return True
    else:
        return False
numero=float(input("Ingrese un número: "))
print(es_par(numero))