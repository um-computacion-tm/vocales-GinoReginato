from Contador_de_vocales import contar_vocales

while True:
    palabra = input('Ingresar alguna palabra o "salir" para terminar: ')
    if palabra.lower() == 'salir':
        break
    print(contar_vocales(palabra))