nombre = input('Por favor escriba su nombre: \r\n')# el \r\n es para un salto de linea

print(f'Hola {nombre}')

#Leer datos que sean numeros

edad = input('Cual es tu edad?')

#Convertir edad string a int
edad = int(edad)

if edad>= 18:
    print(f'{nombre}, podes votar')
else:
    print(f'{nombre}, no podes votar')

#Mezcarlo con operadores

numero = input('Agrega un numero para saber si es par o impar \r\n')
numero = int(numero)

if numero % 2 == 0:
    print(f'{numero} es un numero par!')
else:
    print(f'{numero} es un numero impar!')
