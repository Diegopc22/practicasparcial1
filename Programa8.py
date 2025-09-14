# Hacer un programa que lea una cadena y que muestre en pantalla          # (ES) Programa que lee una cadena | (EN) Program that reads a string
# cuantos numeros tiene, cuantas mayusculas, cuantas minuculas            # (ES) Cuenta números, mayúsculas, minúsculas | (EN) Counts numbers, uppercase, lowercase
# y cuantos espacios                                                      # (ES) Y también cuenta los espacios | (EN) And also counts spaces

def inicio():  # (ES) Función principal | (EN) Main function
    n = 0  # (ES) Contador de números | (EN) Counter for numbers
    e = 0  # (ES) Contador de espacios | (EN) Counter for spaces
    min = 0  # (ES) Contador de minúsculas | (EN) Counter for lowercase
    m = 0  # (ES) Contador de mayúsculas | (EN) Counter for uppercase
    numeros = "0123456789"  # (ES) Cadena usada para validar números | (EN) String used to validate numbers
    cadena = input('Ecribe una cadena: ')  # (ES) Pide una cadena al usuario | (EN) Asks the user for a string
    for i in cadena:  # (ES) Recorre cada caracter de la cadena | (EN) Iterates through each character of the string
        if i in numeros:  # (ES) Si el caracter está en "0123456789" es número | (EN) If character is in "0123456789", it's a number
            n += 1
        if i == ' ':  # (ES) Si el caracter es un espacio | (EN) If the character is a space
            e += 1
        if ord(i) >= 97 and ord(i) <= 122:  # (ES) Si está entre 'a' (97) y 'z' (122) es minúscula | (EN) If between 'a' (97) and 'z' (122), it's lowercase
            min += 1
        if ord(i) >= 65 and ord(i) <= 90:  # (ES) Si está entre 'A' (65) y 'Z' (90) es mayúscula | (EN) If between 'A' (65) and 'Z' (90), it's uppercase
            m += 1
    
    print(f'Los numeros son: {n} \nLos espacios: {e} \nLas minusculas: {min} \nLas mayusculas: {m}')
    # (ES) Muestra el total de números, espacios, minúsculas y mayúsculas | (EN) Displays totals of numbers, spaces, lowercase and uppercase

if __name__ == '__main__':  # (ES) Punto de entrada del programa | (EN) Entry point of the program
    inicio()  # (ES) Ejecuta la función inicio | (EN) Runs the inicio function
