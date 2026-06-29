# Tu código aquí 👇
def puede_votar(edad):
    if edad >= 18:
        return "Puede votar"
    else:
        return "Aún no puede votar"
edad = int(input("Igrese su edad: "))
print(puede_votar(edad))