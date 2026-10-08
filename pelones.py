def binary_to_decimal():
    binario = input("Pon un número en binario: ")
    
    decimal = 0
    posicion = 0
    que_se_suma = []
    
    # Al voltear el texto, la primera posición es 2^0, la segunda 2^1, etc.
    for digito in reversed(binario):
        if digito == '1':
            valor = 2 ** posicion
            decimal = decimal + valor
            que_se_suma.append(valor)
            
        posicion = posicion + 1  # Pasamos a la siguiente potencia (0, 1, 2, 3...)

    print("Valores que se suman:", que_se_suma)
    print("Número entero (decimal):", decimal)