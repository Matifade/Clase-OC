# Tu código aquí 👇
try:
    nota1 = float( input("Ingrese nota 1: "))
    nota2 = float( input("Ingrese nota 2: "))
    nota3 = float( input("Ingrese nota 3: "))
    prom = (nota1+nota2+nota3)/3
    print(f"Tu promedio es: {prom}")
except ValueError:
    print("Ingrese un valor válido")