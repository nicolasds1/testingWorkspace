Consignas:

1) Crear un script utils.py y, en él, desarrollar una función que, dado un valor parcial y un total, retorne el porcentaje que el valor parcial 
representa sobre el total. Es decir, si se le pasan como parámetro 10 y 200, debería retornar 5. Si recibe como parámetro 100 y 20, debería retornar 500.
Al ejecutar el script, nada debería suceder.

2) Dentro del mismo script, escribir una función que determine si un valor está entre otros dos valores. 
Es decir, si la función recibe como parámetro 0, 1 y 5, debería devolver False puesto que 0 no está entre 1 y 5. 
Si recibe como parámetro 2, 1 y 3, debería devolver True porque 2 está entre 1 y 3.

3) Dentro del mismo script, desarrollar una función que lea un valor ingresado por el usuario, intente convertirlo en número y, además,
 lo valide utilizando la función anterior. En caso de que el valor no sea válido, debe devolver None. Además, debe permitir personalizar el 
 mensaje en el que se le pide al usuario que ingrese un valor.

4) Crear un nuevo script board.py y, en él, escribir una función que, dado un tamaño, inicialice una matriz de ese tamaño 
(tanto en ancho como en alto), conteniendo valores aleatorios que pueden ser 0 y 1, y retorne la matriz en cuestión.

5) Dentro del mismo script, desarrollar una función que imprima una matriz que sea suministrada por parámetro, con la siguiente salvedad: 
en caso de que el valor de la matriz sea menor a 2, debe mostrar un guión. Si el valor es mayor a 1, debe restarle 2 y mostrarlo.

6) Dentro del mismo script, desarrollar una función que, dada una matriz, una coordenada "x" y una coordenada "y", le sume 2 al valor
 si el mismo es menor que 2, y guarde el resultado en el mismo casillero de la matriz. 
 De poder realizarse, la función debe devolver True, caso contrario, False.

7) Dentro del mismo script, desarrollar una función que, dada una matriz y un valor, cuente la cantidad de elementos iguales que la matriz contiene
 y retorne ese total.

8) Crear un script main.py y, en él, desarrollar un juego utilizando las funciones definidas en las consignas anteriores.
    8.a) Se le debe solicitar al usuario que ingrese un tamaño de matriz. El tamaño no puede ser menor que 2 ni mayor que 10.
    8.b) Tras crear la matriz con el tamaño elegido por el usuario, deberá pedírsele ahora al mismo que ingrese una coordenada X y una coordenada Y, 
         y hacer visible ese valor en el tablero.
    8.c) Repetir la acción del punto anterior tantas veces como casilleros tenga el tablero a lo ancho
        (es decir, para un tablero de 3x3, hay que repetir el punto 8.b 3 veces). 
        Si se ingresa un valor inválido o una coordenada que ya había sido revelada, no cuenta como una de esas veces.
    8.d) Solicitar al usuario que intente adivinar el porcentaje de "1" que hay en el tablero, con un margen de error de +/- 5%. 

Comentarle al usuario si adivinó o no, y mostrar el tablero completamente descubierto.