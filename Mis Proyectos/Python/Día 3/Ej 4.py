# Tu código aquí 👇
def mayor_de_tres(n1, n2, n3):
    if n1 > n2 and n1 > n3:
        return n1
    elif n2 > n1 and n2 > n3:
        return n2
    else:
        return n3
n1= float(input("Ingrese un número: "))
n2= float(input("Ingrese un número: "))
n3= float(input("Ingrese un número: "))
print(f"El número más grande es: {mayor_de_tres(n1,n2,n3)}")