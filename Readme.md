# README

### AUTOR

#### Gino Reginato

## Descripcion 
Este codigo python define una funcion llamada 'contar_vocales con el cual cuenta la cantidada de vocales (a,e,i,o,u) que tiene una palabra

Cada método dentro de la clase TestContarVocales representa una prueba individual y verifica un escenario específico del comportamiento esperado de la función contar_vocales. Estos escenarios incluyen:

    test_nada: Verifica que cuando se pasa una cadena sin vocales, el resultado es un diccionario vacío.
    test_contar_a: Verifica que cuando se pasa una cadena con una vocal 'a', el resultado sea un diccionario con una ocurrencia de la vocal 'a'.
    test_contar_aa: Verifica que cuando se pasa una cadena con dos vocales 'a', el resultado sea un diccionario con dos ocurrencias de la vocal 'a'.
    test_contar_bese: Verifica que cuando se pasa una cadena con dos vocales 'e', el resultado sea un diccionario con dos ocurrencias de la vocal 'e'.
    test_contar_besa: Verifica que cuando se pasa una cadena con una vocal 'a' y una vocal 'e', el resultado sea un diccionario con una ocurrencia de 'a' y una ocurrencia de 'e'.
    test_contar_casanova: Verifica que cuando se pasa una cadena con tres vocales 'a' y una vocal 'o', el resultado sea un diccionario con tres ocurrencias de 'a' y una ocurrencia de 'o'.
    test_contar_mUrciElago: Verifica que cuando se pasa una cadena con una vocal de cada tipo ('a', 'e', 'i', 'o', 'u'), el resultado sea un diccionario con una ocurrencia de cada vocal.

Finalmente, unittest.main() se utiliza para ejecutar todas las pruebas definidas en la clase TestContarVocales. Si todas las pruebas pasan, significa que la función contar_vocales funciona como se esperaba para los escenarios definidos.