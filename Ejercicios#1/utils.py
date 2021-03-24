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
class Father:
    def __init__ (self, parametro, num1, num2):
        self.parametro = parametro
        self.num1 = num1
        self.num2 = num2

    def check (self):
        if self.parametro > self.num1 and self.parametro < self.num2:
            return True #utilice return asi no imprime nada en pantalla, para probar que funcione cambiarlo por un print()
        else:
            return False #utilice return asi no imprime nada en pantalla, para probar que funcione cambiarlo por un print()

checking = Father(7, 1, 6)
checking.check() #  --> Probando que funcione. En este caso arrojara un False dado que 7 no esta entre 1 y 6

checking2 = Father(2, 1, 3)
checking2.check() # --> Probando que funcione. En este caso arrojara un True dado que 2 si esta entre 1 y 6

#Valor1: parametro  
#Valor2: primer numero  
#Valor3: segundo numero



#Ejercicio 3:

'''
Dentro del mismo script, desarrollar una función que lea un valor ingresado por el usuario, intente convertirlo en número y, además,
lo valide utilizando la función anterior. En caso de que el valor no sea válido, debe devolver None. Además, debe permitir personalizar el 
mensaje en el que se le pide al usuario que ingrese un valor.
'''

class Main:
    def __init__ (self, num):
        self.num = num
        
    def conversor(self):
        print('Numero ingresado:', self.num, '. Su tipo de dato es:')
        print(type(self.num)) #chequeamos que es un str

        changer = int(self.num)
        print('\nNumero transformado a Int! Su tipo de dato ahora es:')
        print(type(changer)) #verificamos que el cambio fue correcto, de str a int :D

finalPrint = Main('10') #Ingresamos 10, el cual tiene valor Str inicialmente, pero terminara siendo Int
finalPrint.conversor()


class Son (Father, Main):
    def __init__(self, finalPrint):
        self.finalPrint = finalPrint

    def testing (self):
        if finalPrint > self.num1 and finalPrint < self.num2:
            print(True)
        else:
            print(None)    

endEx = Son(finalPrint) #ERROR: 'Son' object has no attribute 'num1' => A ver como lo solucionamos...
endEx.testing()
