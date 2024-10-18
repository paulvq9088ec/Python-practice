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
# class Animal:
#     def __init__(self, especie, nombre):
#         self.especie = especie.lower()
#         self.nombre = nombre
#     def hablar(self):
#         if (self.especie == 'perro'): 
#             print('guau')
#         elif (self.especie == 'gato'):
#             print('miau')
#         else:
#             print('No reconocemos esta especie')

# animal1 = Animal('Gato', 'Sparkol')
# animal1.hablar()

'''Ejercicio 77
Crear una clase llamada persona. 
Con los atributos: nombre, edad
**Un constructor donde los datos pueden estar vacios
*Los setters y getters
para cada uno de los atributos.
*mostrar(): muestra los datos de la persona.
*esMayorDeEdad(): devuelve un valor lógico indicando si es mayor de edad
'''
# class Persona:
#     def __init__(self, nombre=None, edad=None):
#         self._nombre = nombre
#         self._edad = edad
    
#     @property
#     def nombre(self):
#         return self._nombre
    
#     @nombre.setter
#     def nombre(self, nuevo_nombre):
#         self._nombre = nuevo_nombre

#     @property
#     def edad(self):
#         return self.edad
    
#     @edad.setter
#     def edad(self, nueva_edad):
#         self.edad = nueva_edad
    
#     def mostrar(self):
#         print(self.__dict__)
#         print(f'El nombre es: {self._nombre}')
#         print(f'Su edad es: {self._edad}')
    
#     def esMayorDeEdad (self):
#         if self._edad >= 18:
#             print(f'La persona tiene "{self._edad}" por lo tanto es mayor de edad')
#         else:
#             print(f'La personas tiene "{self._edad}" así que es menor de edad')

# persona1 = Persona('Jose', 25)
# persona1.mostrar()
# persona1.esMayorDeEdad()

'''Ejercicio 78
Crear una clase persona y otra clase estudiante
La clase persona tiene el atributo:     nombre
y el método:     mostrar_nombre()
La clase estudiante debe heredar de la clase persona y utilizar el método mostrar_nombre() de la clase persona
'''
# class Persona:
#     def __init__(self, nombre):
#         self.nombre = nombre
    
#     def mostrar_nombre(self):
#         print(f'El nombre es: {self.nombre}')

# class Estudiante(Persona):
#     def __init__(self, nombre):
#         super().__init__(nombre)

#     def mostrar(self):
#         return super().mostrar_nombre()

# estudiante1 = Estudiante('Juanito Alimaña')
# estudiante1.mostrar()    

'''Ejercicio 79
Representa una cuenta bancaria con depósito y retiro
debe haber un titular y una saldo
Utiliza POO
'''
# class Cuenta:
#     def __init__(self, titular, saldo):
#         self.titular = titular
#         self.saldo = saldo

#     def depositar(self, cantidad):
#         self.saldo += cantidad
#         print(f'Se depositó: {cantidad} y el saldo actual es: {self.saldo}')

#     def retirar(self, cantidad):
#         if self.saldo < cantidad:
#             print('Lo sentimos pero no tiene saldo suficiente para realizar la transacción')
#         else:
#             self.saldo -= cantidad
#             print(f'Se retiró "{cantidad}" y su saldo actual es: {self.saldo}')
    
#     def mostrar(self):
#         print(f'El nombre del titular es: {self.titular}')
#         print(f'Su saldo actual es: {self.saldo}')

# cuenta1 = Cuenta('Carlitos', 500)
# cuenta1.depositar(200)
# cuenta1.retirar(400)
# cuenta1.mostrar()
# cuenta1.retirar(400)

'''Ejercicio 80
Obten la cantidad de memoria ram en mi computadora o laptop
pip install psutil
'''
# import psutil

# def obtener_ram():
#     memoria = psutil.virtual_memory()
#     memoria_total = memoria.total / (1024 ** 3)
#     return memoria_total

# memoria = obtener_ram()
# print('Total de ram: ', memoria, 'GB')

'''Ejercicio 81
Elevar al cuadrado una lista de nuemeros utilizando map()
'''
# import random
# listaNumeros = []
# def crearLista():
#     for i in range(1,21):
#         x = random.randint(1,50)
#         listaNumeros.append(x)
#     print(listaNumeros)
# crearLista()

# def calcularCuadrado():
#     def cuadrado(x):
#         return x ** 2
#     cuadrados = list(map(cuadrado,listaNumeros))
#     print(cuadrados)
# calcularCuadrado()

'''Ejercicio 82
Convertir una lista de cadenas que sean números a enteros utilizando map()
'''
# def convertir(elemento):
#     return int(elemento)

# cadena = ['1','2','3','4']

# nuevaCadena = list(map(convertir, cadena))
# print(nuevaCadena)

'''Ejercicio 83
Calcular la longitud que tiene cada palabra dentro de una lista de palabras utilizando map
'''
# palabra = ['HOla', 'gato', 'perro']

# def calLong(e):
#     return len(e)
# longitud = list(map(calLong, palabra))
# print(longitud)

'''Ejercicio 84
Obtener el cuadrado de la suma de dos listas de números utilizando map
'''
#import random

# lista1 = []
# lista2 = []

# def agregarNum(x):
#     for i in range(1,11):
#         aleatorio = random.randint(1,100)
#         x.append(aleatorio)

# agregarNum(lista1)
# agregarNum(lista2)

# print(lista1)
# print(lista2)

#Opción laaaaaaaaarga
# x=0
# suma = []
# for i in lista1:
#     suma.append(lista1[x] + lista2[x])
#     x += 1

# print('La suma es: ',suma)
# x=0
# cuadrado = []
# for i in suma:
#     cuadrado.append(suma[x]** 2)
#     x += 1

# print('El cuadrado es: ',cuadrado)

#Opción corta
# def suma_cuadrado(a,b):
#     return (a + b) ** 2

# resultado = list(map(suma_cuadrado,lista1,lista2))
# print('El resultado más fácil y corto: ',resultado)

'''Ejercicio 85
Contar el número de vocales en una lista de palabras utilizando map
'''
#palabras = ['Hola que hace mi gente. Hoy vamos a aplicar lo aprendido']
#separado = palabras

# def contar(palabra):
#     return sum(1 for letra in palabra if letra.lower() in 'aeiou')

#palabras = ['paranguricutirimicuaro', 'esternocleidomastoideos','veintimilla']
# conteo = list(map(contar, palabras))
# print(conteo)

# conteo = list(map(lambda palabra : sum(1 for letra in palabra if letra.lower() in 'aeiou'), palabras))
# print(conteo)

'''Ejericio 86
Elevar un número al cuadrado utilizando lambda
'''
# cuadrado = lambda x : x ** 2
# print(cuadrado(5))

'''Ejercicio 87
Sumar dos número utilizando lambda
'''
# suma = lambda x,y : x + y
# print(suma(5,8))

'''Ejercicio 88
Verificar si un número es par usando lambda
'''
# verificar = lambda x: x % 2 == 0
# print(verificar(1097))

'''Ejercicio 89
Comprobar si una palabra es palíndromo usando lambda
'''
# palindromo = lambda palabra : palabra == palabra[::-1]
# print(palindromo('radar'))
# print(palindromo('iluminati'))

'''Ejercicio 90
Duplicar cada elemento de una lista usando map y lambda
'''
# import random

# listaNum = []
# for x in range(1,6):
#     num = random.randint(1,100)
#     listaNum.append(num)
# print(listaNum)

# duplicado = list(map(lambda num : num * 2, listaNum))
# print(duplicado)

'''Ejercicio 91
Filtrar números pares de una lista utilizando filter
'''
import random
listaNum = []

for x in range(1,11):
    num = random.randint(1,100)
    listaNum.append(num)
print(listaNum)

pares = list(filter(lambda x : x%2 == 0, listaNum))
print(pares)