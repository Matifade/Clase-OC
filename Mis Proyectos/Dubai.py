import random

def jugar_wordle():
    # Lista de palabras de ejemplo (podés agregar las que quieras, siempre de 5 letras)
    palabras = ["PLATO", "PERRO", "GATOO", "VERDE", "CABLE", "TRECE", "MANGO", "RADIO", "TIGRE", "PIANO"]
    palabra_oculta = random.choice(palabras).upper()
    
    intentos_maximos = 6
    
    # Códigos de color para la terminal
    VERDE = "\033[42m\033[30m"      # Fondo verde, texto negro
    AMARILLO = "\033[43m\033[30m"   # Fondo amarillo, texto negro
    GRIS = "\033[47m\033[30m"       # Fondo gris, texto negro
    RESET = "\033[0m"               # Resetear colores

    print("¡Bienvenido a Wordle en Python!")
    print("Tenés 6 intentos para adivinar una palabra de 5 letras.\n")

    for intento in range(1, intentos_maximos + 1):
        # Pedir la palabra al usuario y validarla
        while True:
            suposicion = input(f"Intento {intento}/{intentos_maximos}: ").upper()
            if len(suposicion) == 5 and suposicion.isalpha():
                break
            print("Por favor, ingresá una palabra válida de 5 letras.")

        # Procesar los colores del intento
        resultado_linea = ""
        # Hacemos una copia de las letras para manejar duplicados correctamente
        letras_restantes = list(palabra_oculta)

        # Primera pasada: Marcar los verdes (letras correctas en la posición correcta)
        colores = [""] * 5
        for i in range(5):
            if suposicion[i] == palabra_oculta[i]:
                colores[i] = VERDE
                letras_restantes[i] = None # Consumimos la letra

        # Segunda pasada: Marcar amarillos (está pero en otra posición) y grises
        for i in range(5):
            if colores[i] == "": # Si no fue verde
                if suposicion[i] in letras_restantes:
                    colores[i] = AMARILLO
                    # Consumimos la primera coincidencia encontrada
                    letras_restantes[letras_restantes.index(suposicion[i])] = None
                else:
                    colores[i] = GRIS

        # Armar la fila con los bloques de colores
        for i in range(5):
            resultado_linea += f"{colores[i]} {suposicion[i]} {RESET}"
        
        print(resultado_linea + "\n")

        # Condición de victoria
        if suposicion == palabra_oculta:
            print(f"¡Ganaste! Te tomó {intento} intentos. 🎉")
            return

    # Condición de derrota
    print(f"Te quedaste sin intentos. La palabra era: {palabra_oculta} 😢")

if __name__ == "__main__":
    jugar_wordle()
