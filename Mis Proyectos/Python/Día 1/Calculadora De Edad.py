anio_actual = 2026

aniodenac = int (input ("¿En qué año naciste?"))

edad = anio_actual - aniodenac

if edad >= 18:
    print("Puedes pasar, eres mayor de edad")
else:
    print("No puedes pasar, eres menor de edad")