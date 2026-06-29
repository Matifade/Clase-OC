# Tu código aquí 👇
def crear_email(nombre, apellido):
    mail = nombre+apellido+"@ipm.com"
    return mail.lower()
nombre = str(input("Ingrese su nombre: "))
apellido = str(input("Ingrese su apellido: "))
print(f"Tu email es: {crear_email(nombre, apellido)}")