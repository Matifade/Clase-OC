# Tu código aquí 👇
try:
    peso = float(input("Ingrese su peso: "))
    altura = float(input("Ingrese su altura: "))
    IMC = peso / (altura * altura)
    print (f"Su IMC es de: {IMC}")
except Exception:
    print("Ingrese valores válido")