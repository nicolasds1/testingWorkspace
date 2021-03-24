#Ejercicio 1
print('Ejercicio 1:')

def calcSuperficieRectangulo (base, altura):
    area = base * altura
    return print('La superficie del rectangulo es:', area)

calcSuperficieRectangulo(4, 6) #El 4 representa la base y el 6 la altura


#Ejercicio 2
print('\nEjercicio 2:')

def calcSuperficieTrianguloRectangulo (base, altura):
    area = (base * altura) / 2
    return print('La superficie del triangulo rectangulo es:', area)

calcSuperficieTrianguloRectangulo(10, 5) #El 10 representa la base y el 5 la altura


#Ejercicio 3
print('\nEjercicio 3:')

def calcNumPrimo(numero):
    if numero == 0 or numero == 1 or numero == 4:
        return False
    for x in range(2, int(numero/2)):
        if numero % x == 0:
            return False
    return True

# Probando que sea primo
numero = int(input("Ingrese un numero para validar: "))
es_primo = calcNumPrimo(numero)

if es_primo:
	print("Si es primo")
else:
	print("No es primo")


#Ejercicio 4
print('\nEjercicio 4:')

def seRepite ():
    quote = 'No nececitas ser un experto, para ser un gran artista - Art Atack'
    se_repite = quote.count('s') #Nos fijamos cuantas veces aparece el caracter 's'
    #se_repite2 = quote.count('un') #Nos fijamos cuantas veces aparece la palabra 'un'
    return print('El caracter "s" aparece en total', se_repite, 'veces')
    #return print('La palabra "un" aparece en total', se_repite2, 'veces')

print('"No necesitas ser un experto, para ser un gran artista - Art Atack"')
seRepite()


#Ejercicio 5
print('\nEjercicio 5:')

def esCapicua (cadenaDeCaracteres):
    if cadenaDeCaracteres == cadenaDeCaracteres[::-1]:
        print('La cadena de caracteres es Capicua')
    else:
        print('La cadena de caracteres no es Capicua')    

esCapicua('1991') #Probando si es capicua o no (Con Int)
esCapicua('2000') #Probando si es capicua o no (Con Int)
esCapicua('S.A.S') #Probando si es capicua o no (Con Str)
esCapicua('Hola Mundo') #Probando si es capicua o no (Con Str)


#Ejercicio 6: Quedo pendiente, no supe como realizarlo