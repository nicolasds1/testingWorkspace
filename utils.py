'''
1) Crear un script utils.py y, en él, desarrollar una función que, dado un valor parcial y un total, retorne el porcentaje que el valor parcial 
representa sobre el total. Es decir, si se le pasan como parámetro 10 y 200, debería retornar 5. Si recibe como parámetro 100 y 20, debería retornar 500.
Al ejecutar el script, nada debería suceder.
'''
#Ejercicio1:

def function (x, y):
    while x and y > 0:
        res = x / y
        end = res * 100
        return end

# print(function(10, 200)) --> probando que funcione
# print(function(100, 20)) --> probando que funcione
