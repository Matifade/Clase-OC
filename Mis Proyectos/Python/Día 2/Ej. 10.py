# Tu código aquí 👇
contra = "secreto"
usuario = ""
while usuario != "secreto":
    usuario = str(input("Ingrese la contraseña:"))
    if usuario == contra:
        print("Bienvenido")
    else:
        print("Inténtalo de nuevo")