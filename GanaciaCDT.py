cantidad = float(input("Cantidad de dinero invertido"))
porcentajeIntereses = float(input("Cual es el porcentaje de los intereses"))
porcentajeIntereses2 = porcentajeIntereses/100
periodo = float(input("Por cuanto tiempo es el CDT"))

valorIntereses = (cantidad * porcentajeIntereses2 * periodo)/360
valorDescuento = valorIntereses * 0.07
valorTotal = cantidad + valorIntereses - valorDescuento

print(f"El valor del interes es de: {valorIntereses}")
print(f"El valor del descuento es: {valorDescuento}")
print(f"El valor neto a recibir es: {valorTotal}")
