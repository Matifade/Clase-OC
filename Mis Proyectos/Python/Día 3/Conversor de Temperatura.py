# Define tu función aquí
def celsius_a_fahrenheit(temperatura_hoy):
    fah = (temperatura_hoy * 9/5)+32
    return fah


# Prueba tu función aquí
temperatura_hoy = -32
resultado = celsius_a_fahrenheit(temperatura_hoy)
print(f"{temperatura_hoy}°C son {resultado}°F")