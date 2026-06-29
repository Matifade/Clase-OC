# Variables Globales
saldo = 1000

# 1. Definir funciones
def verificar_pin(pin_usuario):
    # Tu código aquí (return True o False)
    if pin_usuario == "1234":
        return True
    else:
        return False

def retirar(monto):
    global saldo # Necesario para modificar la variable de afuera
    # Tu código aquí (if monto > saldo...)
    if saldo >= monto:
        saldo = saldo - monto
        print(f"Éxito. Saldo restante: ${saldo}")
    else:
        print("Fondos Insuficientes")
    

# 2. Ejecución Principal
print("🏦 Bienvenido al Banco Python")

input_pin = input("Ingrese su PIN: ")

if verificar_pin(input_pin):
    print("Acceso concedido. Saldo actual:", saldo)
    
    try:
        monto_str = input("¿Cuánto desea retirar? ")
        monto = int(monto_str)

        # Llamar a la función de retirar
        retirar(monto)
        
    except ValueError:
        print("Error: Ingrese un número válido.")
else:
    print("PIN Incorrecto. Policía en camino.")