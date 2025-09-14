# Hacer un programa que lea 10 numeros   # (ES) Programa que lee 10 números | (EN) Program that reads 10 numbers
# Y los alamcene en una lista            # (ES) Los guarda en una lista | (EN) Stores them in a list

a = []  # (ES) Se inicializa la lista vacía | (EN) The empty list is initialized
suma = 0  # (ES) Variable para acumular la suma de los números | (EN) Variable to accumulate the sum of numbers
n = 0  # (ES) Contador para controlar cuántos números se han introducido | (EN) Counter to control how many numbers have been entered
numeros = "0,1,2,3,4,5,6,7,8,9";  # (ES) Cadena usada para validar que se ingresen solo dígitos | (EN) String used to validate only digits are entered

while(n <= 9):  # (ES) Bucle que se repite hasta que se ingresen 10 números | (EN) Loop repeats until 10 numbers are entered
    b = input('Escibre un numero: ')  # (ES) Pide al usuario un número como texto | (EN) Asks the user for a number as text
    x = 0  # (ES) Contador para validar si todos los caracteres son números | (EN) Counter to check if all characters are digits
    for i in b:  # (ES) Recorre cada caracter del valor ingresado | (EN) Iterates through each character of the entered value
        #if(ord(i) >= 48 and ord(i) <= 57):  # (ES) Opción: validar usando el código ASCII de los números | (EN) Option: validate using ASCII code of digits
        if i in numeros:  # (ES) Valida si el caracter está en la cadena de números | (EN) Validates if the character is in the string of digits
            x += 1  # (ES) Si es número, incrementa el contador | (EN) If it's a digit, increment the counter
    if len(b) == x:  # (ES) Si la cantidad de dígitos coincide con la longitud del texto ingresado, es válido | (EN) If digit count matches length of input, it's valid
        a.append(int(b))  # (ES) Convierte el texto a entero y lo guarda en la lista | (EN) Converts text to integer and stores it in the list
        n += 1  # (ES) Aumenta el contador porque se ingresó un número válido | (EN) Increases counter because a valid number was entered
    else:
        print('El valor no es un numero')  # (ES) Mensaje si lo ingresado no es válido | (EN) Message if the input is not valid

for i in a:  # (ES) Recorre la lista con los números ingresados | (EN) Iterates through the list with the entered numbers
    print(i)  # (ES) Imprime cada número | (EN) Prints each number
    suma += i  # (ES) Suma cada número a la variable suma | (EN) Adds each number to the sum variable

print(f'La suma es: {suma}')  # (ES) Imprime el total de la suma | (EN) Prints the total sum
