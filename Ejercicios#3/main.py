#Ejercicio 1:
class BasePorAltura:
    def __init__ (self, base, altura):
        self.base = base
        self.altura = altura

    def calcBasePorAltura(self):
        res = self.base * self.altura
        print("Resultado Ejercicio 1:", res)

resultadoEjercicio1 = BasePorAltura(10, 5)
resultadoEjercicio1.calcBasePorAltura()       

#Ejercico 2:
class Rectangulo:
    def __init__ (self, base, altura):
        self.base = base 
        self.altura = altura

    def calcularBasePorAltura (self):
        resultado = self.base * self.altura
        print("Resultado Ejercicio 2:", resultado)

resultadoEjercicio2 = Rectangulo(10, 9)
resultadoEjercicio2.calcularBasePorAltura()                   

#Ejercicio 3:
class calcularAreaTrianguloRectangulo:
    def __init__ (self, base, altura):
        self.base = base
        self.altura = altura

    def calcAreaTrianguloRectangulo(self):
        area = (self.base * self.altura) / 2
        print("Resultado Ejercicio 3:", area)

resultadoEjercicio3 = calcularAreaTrianguloRectangulo(7, 4)
resultadoEjercicio3.calcAreaTrianguloRectangulo()

