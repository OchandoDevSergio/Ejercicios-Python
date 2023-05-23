# Programar una función que sume los términos de una sucesión hasta el número que se le pase como parámetro, esto es, si ejecutamos sucesion(2) el resultado será 1+2, si ejecutamos sucesion(5), el resultado será 1+2+3+4+5. Utilizarla para calcular los valores generados por cada uno de los 7 números proporcionados en el enunciado y sumarlos, multiplicando la suma obtenida por el logaritmo en la base propuesta del número proporcionado en el enunciado (importar para ello el paquete math y usar la función help para ver cómo usar la función logaritmo). El resultado a obtener será del tipo (sucesion(num1)+sucesion(num2)+..+sucesion(num7))*logbasej(numerologaritmo)
# Lista de 7 números para los que calcular cada una de las sucesiones: [ 412, 595, 342, 792, 427, 482, 332]
# Número del que calcular el logaritmo: 3486784401
# Base para el logaritmo: 9

import math
lista = [412, 595, 342, 792, 427, 482, 332]
total = 0
for valor in lista:
    for numero in range(0, (valor+1)):
        total += numero
total *= math.log(3486784401, 9)
print(total)

