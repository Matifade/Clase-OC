# Tu código aquí 👇
try:
    total= float( input("¿Cuánto pagaste?"))
    porcprop= float (input("¿Cuánto porcentaje de propina querés dejar?"))
    prop= (porcprop * total)/100
    totalpag = prop + total
    print(f"El total a pagar es de:{totalpag} y la propina es de {prop}")
except ValueError:
    print("Ingrese valores válidos")