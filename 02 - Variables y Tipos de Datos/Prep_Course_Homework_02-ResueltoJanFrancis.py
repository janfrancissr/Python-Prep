#Ejercicios para practicar y resolver
#github_user: janfrancissr

## Variables

#1) Crear una variable que contenga un elemento del conjunto de números enteros y luego imprimir por pantalla
a = 7
print(a)

#2) Imprimir el tipo de dato de la constante 8.5
k = 8.5
print(type(8.5))

#3) Imprimir el tipo de dato de la variable creada en el punto 1
print(type(a))

#4) Crear una variable que contenga tu nombre
my_name = "Jan Francis Arroyo"
print(my_name)

#5) Crear una variable que contenga un número complejo
n_complejo = 7 + 7j
print(n_complejo)

#6) Mostrar el tipo de dato de la variable crada en el punto 5
print(type(n_complejo))

#7) Crear una variable que contenga el valor del número Pi redondeado a 4 decimales
import math

var_pi = math.pi
print(var_pi)

#8) Crear una variable que contenga el valor 'True' y otra que contenga el valor True. ¿Se trata de lo mismo?
b = True
c = True

print("b is "+str(b)+" and c is "+str(c)+" too")

#9) Imprimir el tipo de dato correspondientes a las variables creadas en el punto 8
#print("b is "+str(type(b)))
#print("c is "+str(type(c)))

print("b is ", type(b), "and c is ", type(c))

#10) Asignar a una variable, la suma de un número entero y otro decimal
s = 10 + 9.5

print(s)

#11) Realizar una operación de suma de números complejos
a = 4 + 4j
b = 5 + 5j
print(a + b)

#12) Realizar una operación de suma de un número real y otro complejo
c = a + 40.4
print(c)

#13) Realizar una operación de multiplicación
print(5*8)

#14) Mostrar el resultado de elevar 2 a la octava potencia
print(2**8)

#15) Obtener el cociente de la división de 27 entre 4 en una variable y luego mostrarla
d = 27/4
print(d)

#16) De la división anterior solamente mostrar la parte entera
print (27 // 4)

#17) De la división de 27 entre 4 mostrar solamente el resto
print(27 % 4)

#18) Utilizando como operandos el número 4 y los resultados obtenidos en los puntos 16 y 17. Obtener 27 como resultado
print(4*6 + 3) 

#19) Utilizar el operador "+" en una operación donde intervengan solo variables alfanuméricas
var1 = "My name is "
var2 = 'Jan Francis'
print(var1 + var2)

#20) Evaluar si "2" es igual a 2. ¿Por qué ocurre eso?
print("2" == 2)
#Sale FALSO porque una variable es string y la otra variable es un número entero


#21) Utilizar las funciones de cambio de tipo de dato, para que la validación del punto 20 resulte verdadera
print(int("2") == 2)

#22) ¿Por qué arroja error el siguiente cambio de tipo de datos? a = float('3,8')
#Porque 3,8 estando entre comillas es una Cadena o String, y no se puede convertir una cadena a un numero flotante,
#sino solo al revés
#a = float('3,8')
#print(a)

b = str(3.8)
print(b)

#23) Crear una variable con el valor 3, y utilizar el operador '-=' para modificar su contenido
x = 10
x -= 4
print(x)

#24) Realizar la operacion 1 << 2 ¿Por qué da ese resultado? ¿Qué es el sistema de numeración binario?
a = 1 << 2
print(a)

#25) Realizar la operación 2 + '2' ¿Por qué no está permitido? ¿Si los dos operandos serían del mismo tipo, siempre arrojaría el mismo resultado?
print(int(2) + int('2'))
print(str(2) + str('2'))
print(float(2) + float('2'))

#26) Realizar una operación válida entre valores de tipo entero y string
var1 = 'Este texto se repite '
var2 = 4
print(var1*var2 + str(var2) + " veces")

