import random

# 1. Generar número secreto
secreto = random.randint(1, 100)
adivinado = False  # Esta variable nos sirve de "bandera" para el while

print("🤖 He pensado un número del 1 al 100. ¿Puedes adivinarlo?")

# 2. Bucle while (mientras no haya adivinado)
while adivinado == False:
    
    # Tu código aquí:
    # a. Pedir número al usuario (input e int)
    usuario = int (input("Ingrese un número del 1 al 100: "))    
    # b. Comparar (if / elif / else)
    if usuario == secreto:
        print("¡Ganaste!")
        adivinado = True
    #    - Si es igual: Imprimir "Ganaste" y cambiar adivinado = True
    #    - Si es menor: Imprimir "Es más grande"
    elif usuario < secreto:
        print ("Es más grande...")
    #    - Si es mayor: Imprimir "Es más chico"
    else:
        print ("Es más chico...")
     # Borra esto y escribe tu código