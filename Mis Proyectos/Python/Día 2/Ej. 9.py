# Tu código aquí 👇
precios = {
    "Manzana" : 100,
    "Banana" : 50,
    "Naranja" : 80
}
try:
    fruta = input("Ingrese la fruta que desea comprar: ")
    kilos = float( input( "Ingrese la cantidad de kilos que desea comprar: "))
    precio = precios.get(fruta, 0) * kilos
    if precio == 0:
        print("ERROR. Ingrese un peso y una fruta válidos")
    else:
        print(f"El precio final es: ${precio}")
except ValueError:
    print("Ingrese valores válidos")



