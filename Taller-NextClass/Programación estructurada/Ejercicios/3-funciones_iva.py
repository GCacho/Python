#Escribir una función que calcule el total de una factura tras 
#Aplicarle el IVA. La función debe recibir la cantidad sin IVA 
#Y el porcentaje de IVA a aplicar, y devolver el total de la 
#Factura. Si se invoca la función sin pasarle el porcentaje de IVA, 
#Deberá aplicar un 21%.

def total():
    monto = float(input('Ingrese el valor del producto que estas pagando: \n---->'))
    iva = int(input("Ingrese el valor del IVA: \n---->"))
    if iva != 0:
        if iva > 0:
            totalPagar = ((monto * iva) / 100) + monto
            return totalPagar
        else:
            return "El monto de IVA es negativo. No podemor realizar la operacion"
    else: 
        totalPagar = (monto * 0.21) + monto
        return totalPagar



if __name__ == '__main__':
    print(f"El total de su monto es:{total()}")