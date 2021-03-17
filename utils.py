#Ejercicio1:

'''
1) Crear un script utils.py y, en él, desarrollar una función que, dado un valor parcial y un total, retorne el porcentaje que el valor parcial 
representa sobre el total. Es decir, si se le pasan como parámetro 10 y 200, debería retornar 5. Si recibe como parámetro 100 y 20, debería retornar 500.
Al ejecutar el script, nada debería suceder.
'''

def function (x, y):
    while x and y > 0:
        res = x / y
        end = res * 100
        return end

# print(function(10, 200)) --> probando que funcione
# print(function(100, 20)) --> probando que funcione



#Ejercicio 2:

'''
Dentro del mismo script, escribir una función que determine si un valor está entre otros dos valores. 
Es decir, si la función recibe como parámetro 0, 1 y 5, debería devolver False puesto que 0 no está entre 1 y 5. 
Si recibe como parámetro 2, 1 y 3, debería devolver True porque 2 está entre 1 y 3.
'''

def param (parametro, num1, num2):
    if parametro > num1 and parametro < num2:
        return True
    else:
        return False

# print(param(7, 1, 6))   --> Probando que funcione. En este caso arrojara un False dado que 7 no esta entre 1 y 6
# print(param(2, 1, 3))   --> Probando que funcione. En este caso arrojara un True dado que 2 si esta entre 1 y 6

#Valor1: parametro  
#Valor2: primer numero  
#Valor3: segundo numero