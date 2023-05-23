# Cargar el fichero "Quijote.txt" del ejercicio del tema 7 con el código de caracteres correcto, crear una función que permita seleccionar el número de párrafo que se solicita más abajo (empezando a contar por 0 para el primer párrafo) como en el ejercicio del tema 7 y le aplique a ese párrafo una encriptación por desplazamiento de código (como la explicada en el tema 6) con el desplazamiento positivo indicado más abajo, devolviendo el párrafo encriptado y obteniendo a la vez el valor numérico del código del caracter que se encuentra en la posición del párrafo que se indica más abajo (empezando a contar por 0 para el primer caracter del párrafo). Guardar el párrafo encriptado en una variable y crear una función a la que pasarle el párrafo encriptado y el desplazamiento aplicado y que permita desencriptar el texto aplicando el mismo desplazamiento de código en sentido inverso (esta parte no se evalua).
# Número de párrafo: 0
# Desplazamiento del código de encriptación: 8
# Número de carácter dentro del párrafo: 409

archivo = open ('quijote.txt', 'r') # Para ejecutar en terminal de VSC (ANSI)
#archivo = open ('quijote.txt', 'r', encoding="utf-8") Para ejecutar en Spyder
texto=archivo.read()
parrafoEncriptado= ""
parrafoDesencriptado= ""
def encriptaParrafo():
    parrafos= texto.split('\n\n')
    global parrafoEncriptado
    for letra in parrafos[0]:
        parrafoEncriptado= parrafoEncriptado + chr (ord(letra)+8)
    print(ord(parrafoEncriptado[409]))
def desencriptaParrafo():
    global parrafoDesencriptado
    for letra in parrafoEncriptado:
        parrafoDesencriptado= parrafoDesencriptado + chr (ord(letra)-8)
    print(parrafoDesencriptado)
encriptaParrafo()
desencriptaParrafo()