#Ejercicio 36
'''Pide un caracter y determina si es una vocal
'''
# letra = input('Ingresa una letra:')
# vocal = {'a','e','i','o','u'}

# if letra.lower() in vocal:
#     print(f'Positivo mi so "{letra}" es una vocal')
# else:
#     print(f'Negativo mi compa, "{letra}" no es una vocal')

#Ejercicio 37
'''Calcula es máximo de 3 números
Respuesta: se encuentra con la función "max()"
'''
# lista = []
# while len(lista) < 3:
#     num1 = int(input('Ingresa un número: '))
#     lista.append(num1)
# lista.sort()
# print(lista[-1])

#Ejercicio 38
'''Determina si un número es divisible entre 5 y 7
'''
# num = int(input('Ingresa un número: '))
# if num % 5 == 0 and num % 7 == 0:
#     print(f'Mijitrin este número "{num}" sí es divisible para 5 y 7')
# else:
#     print(f'No mi compa, el número "{num}" no es divisible para 5 y 7')

#Ejercicio 41
'''Imprime los número del 10 al 1 en orden descendente
    Respuesta: crear una variable llamado "contador" y asignarle el valor de 10. Con while hacer que se reduzca hasta 0 y así ir imprimiendo los valores
'''
# lista = []
# for x in range(1,11):
#     lista.append(x)
# x=0
# while x <= 10:
#     print(lista[-1])
#     x += 1
#     lista.pop()

#Ejercicio 42
''' Solicitar al usuario ingresar un número N y luego imprime la suma de todos los números de 1 hasta N
'''
# num = int(input('Ingresa un número: '))
# sumatoria = 0
# x = 1
# while x <= num:
#     sumatoria += x
#     x += 1
# print(sumatoria)

#Ejercicio 43
'''Solicitar al usuario ingresar un número N e imprime el factorial de ese número
5! = 5 x 4 x 3 x 2 x 1 = 120
'''
# num = int(input('Ingresa un número: '))
# contador = num
# resultado = 1
# x = 1
# while x <= num:
#     resultado  = resultado * contador
#     contador -= 1
#     x += 1
# print(f'El factorial es: {resultado}')

'''Ejercicio 44
Genera un número aleatorio entre 1 y 10. Luego, pide al usuario adivinar el número hasta que lo haga correctamente
'''
# import random
# aleatorio = random.randint(1,10)
# contador = 0
# num = int(input('Adivina el número aleatorio entre el 1 y el 10: '))
# num = 0
# while num != aleatorio:
#     num = int(input('Nel mi so, intentalo nuevamente: '))
#     contador += 1
#     if num == aleatorio:
#         break
# print(f'Lograste adivinar el número aleatorio que era "{aleatorio}" y solo te tomó: "{contador}" intentos')

'''Ejercicio 45
Imprime la tabla de multiplicar de un número ingresado por el usuario
'''
# num = int(input('Ingresa un número: '))
# i = 0
# while i <= 10:
#     resultado = num * i
#     print(f'{num} x {i} = {resultado}')
#     i += 1

'''Ejercicio 46
Solicita al usuario ingresar un número y cuenta cuántos dígitos tiene
'''
# num = int(input('Ingresa un número'))
# inicial = num
# contador = 0
# while num != 0:
#     num = num // 10
#     contador += 1
# print(f'El número de dígitos que tiene el número "{inicial}" es de: {contador}')

'''Ejercicio 47
Hacer un menú de opciones que incluya la opción de salir del programa
'''
# while True:
#     print('1 - Para decir "Hola"')
#     print('2 - Para decir "Adios"')
#     print('3 - Para decir "Salir"')
#     num = int(input('Elige una opcion: '))
#     if num == 1:
#         print('Hola mijitrin')
#     elif num == 2:
#         print('Adios mi so')
#     elif num == 3:
#         break
#     else:
#         print('No sea pendejo, y escriba una de las opciones indicadas')
# print('Muchas gracias por participar de nuestro experimento. Vuelva pronto')

'''Ejercicio 48
Simular un volado o lanzamiento de una moneda
'''
# import random
# while True:
#     opcion = random.randint(1,2)    
#     if opcion == 1:
#         print('La opción es "CARA" mi compa')
#     else:
#         print('La opción es "CRUZ" mi so')
#     jugar = input('Quieres juegar de nuevo? S/N')
#     if jugar.lower() == 'n':
#         break
# print('Gracias por juegar')

'''Ejercicio 49
Simula el lanzamiento de un dado hasta obtener un 6
'''
# import random
# contador = 1
# mensaje = input('¿Quieres probar tu suerte? S/N ')
# while mensaje.lower() != "n":
#     aleatorio = random.randint(1,6)
#     print(f'Haz lanzado un: {aleatorio}')
#     if aleatorio == 6:
#         print(f'Haz logrado tirar un "6" y tan solo te tomo: {contador} intentos')
#         print('Gracias por jugar con nosotros')
#         break
#     else:
#         mensaje = input('¿Quieres volver a intentar? S/N ')
#     contador += 1

'''Ejercicio 50
Mostrar los números del 1 al 100
Reemplaznado los múltiplos del 3 por "Fizz" y los múltiplos de 5 por "Buzz"
'''
# miLista = []
# i = 1
# while len(miLista) < 100:
#     if i % 3 == 0 and i % 5 == 0:
#         miLista.append('Fizz Buzz')
#     elif i % 3 == 0:
#         miLista.append('Fizz')
#     elif i % 5 == 0:
#         miLista.append('Buzz')
#     else:
#         miLista.append(i)
#     i += 1
# print(miLista)

'''Ejercicio 51
Imprimir los números del 1 al 5 con for
'''
# for i in range(1,6):
#     print(i)

'''Ejercicio 52
Sumar los números del 1 al 10 con for
'''
# suma = 0
# for i in range(1, 11):
#     suma += i
#     print(f'La sumatoria está en: {suma}')

'''Ejercicio 53
Imprimir los elementos de una lista dada
'''
# miLista = [1,3,4,5,6,3,3,1]
# indice = 0
# for i in miLista:
#     print(f'El elemento en el indice {indice} actual es: {i}')
#     indice += 1
# print(len(miLista))

'''Ejercicio 54
Imprimir los caracteres de una cadena utilizando el ciclo for
'''
# cadena = 'Pepito Perez'
# indice = 0
# for i in cadena:
#     print(f'El caracter en el índice {indice} es: {i}')
#     indice += 1

'''Ejercicio 55
Imprimir los números pares del 2 al 10 con el ciclo for
'''
# for num in range(2,11,2):
#     print(f'El numero es: {num}')

'''Ejercicio 56
Listar 10 número y calcular el cuadrado de cada uno e imprimirlos utilizando for
'''
# for i in range(1,11):
#     cuadrado = i ** 2
#     print(f'El número es "{i}" y su cuadrado es: {cuadrado}')

'''Ejercicio 57
Imprimir los números del 5 al 1 en orden descendente
'''
# num = 5
# while num > 0:
#     print('El número actual es:', num)
#     num -= 1
# for i in range(5,0,-1):
#     print('El número actual es:', i)

'''Ejercicio 58
Multiplicar todos los elementos de una lista por 2
'''
# miLista = []
# for i in range(1,11):
#     miLista.append(i)
#     print(f'El númeror es {i} y multiplicado por 2 es: {i * 2}')
# print(miLista)

'''Ejercicio 59
Pedir al usuario un número e imprimir la tabla de multiplicar del mismo
'''
# num = int(input('Ingresa un número: '))
# for i in range(1,11):
#     print(f'{num} x {i} = {num * i}')

'''Ejercicio 60
Imprimir la suma de los números pares del 1 al 10 utilizando el ciclo for
'''
# suma = 0
# for i in range(1,11):
#     if (i % 2 == 0):
#         suma += i
#         print('Suma', suma)
# print('La sumatoria es:', suma)

'''Ejercicio 61
Crea una función para sumar dos números
'''
# def sumar(num1, num2):
#     return num1 + num2
# print(sumar(89,243))

'''Ejercicio 62
Crea una función para calcular el área de un círculo
'''
# from math import pi
# def area(r):
#     return pi * r**2
# print(round(area(5),2))

'''Ejercicio 63
Escribe una función para imprimir un mensaje de saludo
'''
# def saludo(nombre):
#     print(f'Hola estimado {nombre}, cómo estás?')
# print(saludo(input('Ingresa tu nombre ')))

'''Ejercicio 64
Escribe una función para verificar si un número es par o impar
'''
# def par(num):
#     if num % 2 == 0:
#         print(f'El número "{num}" es PAR')
#     else:
#         print(f'El número "{num}" es IMPAR')
# print(par(int(input('Ingresa un número: '))))

'''Ejercicio 65
Escribe una función para convertir grados celcius a fahrenheit
'''
# def convertir():
#     while True:
#         print('Del siguiente menú ingresa el número que de la opción que deseas utilizar:')
#         print('1 - si deseas convertir grados Celcius a Fahrenheit.')
#         print('2 - para convertir grados Fahrenheit a Celcius.')
#         print('3 - para salir.')
#         consuta = int(input('¿Qué deseas hacer? '))
#         if (consuta == 1):
#             grado = float(input('Ingresa los grados Celcius que deseas convertir a Fahrenheit: '))
#             formula = round(((grado * 9/5) + 32),2)
#             print(f'"{grado}" grados Celcius son: "{formula}" grodos Fahrenheit')
#             print('')
#         elif (consuta == 2):
#             grado = float(input('Ingresa los grados Fahrenheit que deseas convertir a Celcius: '))
#             formula = round(((grado -32) * 5/9),2)
#             print(f'"{grado}" grados Fahrenheit son: "{formula}" grodos Celcius')
#             print('')
#         elif (consuta == 3):
#             print('Gracias por usar nuestros servisios mi soooo')
#             break
#         else:
#             print('La opción que ingresaste no corresponde a ninguna del menú. No seas animal y presiona bien')
#             print('')
# convertir()

'''Ejercicio 66
Escribe una función para calcular el promedio de una lista de números
'''
# def promedio(a,b):
#     resultado = round(((a + b) / 2),2)
#     print('El resultado es: ',resultado)
# a = float(input('Ingresa el primer número para realizar el promedio: '))
# b = float(input('Ingresa el segundo número para realizar el promedio: '))
# promedio(a,b)

#Otra forma

# import random
# def promedio(lista):
#     resultado = sum(lista) / len(lista)
#     print('El resultado es: ',resultado)
# conjunto = []
# for i in range(random.randint(1,20)):
#     conjunto.append(i)
# print(conjunto)
# promedio(conjunto)

'''Ejercicio 67
Escribe una función para calcular el volumen de un cilindro: V = pi * r ** 2h
'''
# from math import pi
# def volumCilindro(r, h):
#     calculo = round((pi * (r ** 2) * h),2)
#     print('El volumen de un cilindro es: ', calculo)
# radio = float(input('Ingresa el radio del cilindro: '))
# altura = float(input('Ingresa la altura del cilindro: '))
# volumCilindro(radio, altura)

'''Ejercicio 68
Escribir una función que pida por teclado la distancia y la velocidad para poder calcular el tiempo de viaje
'''
# def tiempoViaje():
#     distancia = int(input('Ingresa la distancia (km): '))
#     velocidad = int(input('Ingresa la velocidad (km/h): '))
#     respuesta = int(round((distancia / velocidad),0))
#     minutos = int(round((distancia % velocidad)/60,2)*100)
#     print(f'La distancia es "{distancia}" km y el "{velocidad}" km/h, nos da un resultado de: {respuesta} horas y {minutos} minutos')
# tiempoViaje()

'''Ejercicio 69
Escribe una función para calcular la tasa de desempleo
td = no_desempleados/fuerza_laboral x 100
'''
# def tasaDesempleo():
#     no_desempleados = int(input('Ingresa en número de desempleados: '))
#     fuerza_laboral = int(input('Ingresa en número de la fuerza laboral: '))
#     resultado = round(((no_desempleados / fuerza_laboral) * 100),2)
#     print(f'El número de desempleados es "{no_desempleados}" y la fuerza laboral es "{fuerza_laboral}" y el resultado nos da una tasa de desempleo de: {resultado} por ciento')
# tasaDesempleo()

''' Ejercicio 70
Escribe una función para clasificar si una sustancia es ácida, básica o neutra a partir de su PH
'''
# def clasificiacion(ph):
#     if ph < 7:
#         print(f'La sustancia tiene un PH de "{ph}" por lo tanto es una sustancia Ácida')
#     elif ph > 7:
#         print(f'La sustancia tiene un PH de "{ph}" por lo tanto es una sustancia Básica')
#     else:
#         print(f'La sustancia tiene un PH de "{ph}" por lo tanto es una sustancia Neutra')

# clasificiacion(float(input('Ingresa el ph de la sustancia: ')))

'''Ejercicio 71
Crear una clase rectángulo con los siguientes atributos
base : base de rectángulo
altura : altura del rectángulo

La clase debe tener los siguientes metodos:
** __int__(self, base, altura): inicializa los atributos de la clase
** calcular_area(self): calcula y devuelve el área del rectángulo
** calcular_perimetro(self): calcual y devuelve el perímetro del rectángulo
'''
# class Rectangulo:
#     def __init__(self, base, altura):
#         self.base = base
#         self.altura = altura
    
#     def calcular_area(self):
#         return self.base * self.altura

#     def calcular_perimetro(self):
#         return 2 * (self.base + self.altura)

# rec1 = Rectangulo(5, 3)
# print(f'La áreas es: {rec1.calcular_area()}')
# print(f'El perímetro es: {rec1.calcular_perimetro()}')

'''Ejercicio 72
Crea una clase círculo con los siguientes atributos:
* radio: radio del círculo
La clase debe tener los siguientes métodos:
* __init__(self,radio): inicializa los atributos de la clase
*calcular_area(self): calcula y devuelve el área del círculo
*calcular_perimetro(self): calcula y devuelve el perímetro del círculo
'''
# from math import pi
# class Circulo:
#     def __init__(self,radio):
#         self.radio = radio
    
#     def calcular_area(self):
#         resultado = round((pi * (self.radio ** 2)),2)
#         return resultado

#     def calcular_perimetro(self):
#         resultado = round((2 * pi * self.radio),2)
#         return resultado

# cir1 = Circulo(5)
# print('El área es: ',cir1.calcular_area())
# print('El perímetro es: ',cir1.calcular_perimetro())

'''Ejercicio 73
Crea una clase libro con los atributos:
título, autor, editorial, año de publicación
Métodos:
constructor para inicializar los atributos
'''
# class Libro:
#     def __init__(self,titulo, autor, editorial, year_publicacion):
#         self.titulo = titulo
#         self.autor = autor
#         self.editorial = editorial
#         self.year_publicacion = year_publicacion

# libro1 = Libro('La vida de Pepito Perez', 'Pepito Perez', 'Don mosquito', '2010')
# print(libro1.__dict__)

'''Ejercicio 74
Crear una clase Persona con los atributos:
*** nombre, edad, dni
Con los métodos:
init()
es_mayor_edad() este retorna True si es verdad
'''
# class Persona:
#     def __init__(self, nombre, edad, dni):
#         self.nombre = nombre
#         self.edad = edad
#         self.dni = dni
    
#     def es_mayor_edad(self):
#         if(self.edad >= 18):
#             return print('La persona es mayor de edad')
#         else:
#             return print('La persona es menor de edad compañero')

# persona1 = Persona('Pepito', 7, 1738393)
# #print(persona1.es_mayor_edad())
# persona1.es_mayor_edad()

'''Ejercicio 75
Crear una clase coche con los atributos:
marca, modelo, matrícula, km
Con los métodos:
init como constructor
avanzar(km) este aumenta
el valor de km en la cantidad
'''
# class Coche:
#     def __init__(self, marca, modelo, matricula, km):
#         self.marca = marca
#         self.modelo = modelo
#         self.matricula = matricula
#         self.km = km

#     def avanzar(self, km):
#         self.km = self.km + km

# coche1 = Coche('Nissan', 'Kicks', 'skd sdf', 5000)
# print(coche1.__dict__)
# coche1.avanzar(3000)
# print(coche1.km)


'''Ejercicio 76
Crear una clase animal con los atributos:
especie y nombre
La clase debe tener los métodos:
init y hablar()
El método hablar() nos retorna una palabra según la interpretación del sonido como un perro sería "guau"
'''
class Animal:
    def __init__(self, especie, nombre):
        self.especie = especie.lower()
        self.nombre = nombre
    def hablar(self):
        if (self.especie == 'perro'): 
            print('guau')
        elif (self.especie == 'gato'):
            print('miau')
        else:
            print('No reconocemos esta especie')

animal1 = Animal('Gato', 'Sparkol')
animal1.hablar()