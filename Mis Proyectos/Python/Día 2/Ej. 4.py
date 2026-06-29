# Tu código aquí 👇
cont=0
frase=input("Ingrese una frase: ")
for letras in frase:
    if letras in "AaEeIiOoUu":
        cont=cont+1
print(f"El total de vocales es de: {cont}")