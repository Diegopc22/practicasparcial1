# Hacer un programa que en una lista se introduzcan cadenas de caracteres con las siguientes restricciones: 
# 1.- las cadenas no deben tener espacio
# 2.- la cadena solo puede tener mayúscula la primera letra
# 3.- obligatoriamente debe de tener todas las vocales
# El programa no termina hasta que la lista tenga 5 elementos
# (EN) Program to input strings with these restrictions:
# 1.- No spaces
# 2.- Only the first letter can be uppercase
# 3.- Must contain all vowels
# Program ends when list has 5 elements

def vocales(v):  # (ES) Verifica que la cadena tenga todas las vocales | (EN) Checks if string contains all vowels
    va = False
    ve = False
    vi = False
    vo = False
    vu = False
    if 'a' in v or 'A' in v:
        va = True
    if 'e' in v or 'E' in v:
        ve = True
    if 'i' in v or 'I' in v:
        vi = True
    if 'o' in v or 'O' in v:
        vo = True
    if 'u' in v or 'U' in v:
        vu = True
    if va == True and ve == True and vi == True and vo == True and vu == True:  # (ES) Si todas las vocales están presentes | (EN) If all vowels are present
        lista.append(v)  # (ES) Agrega la cadena a la lista | (EN) Appends string to the list
        print(lista)  # (ES) Muestra la lista actual | (EN) Prints current list
    else:
        print('No contiene las vocales')  # (ES) Mensaje si no contiene todas las vocales | (EN) Message if string doesn't have all vowels


def minusculas(m):  # (ES) Verifica que todo, excepto la primera letra, sea minúscula | (EN) Checks that all except first letter are lowercase
    cm = 0  # (ES) Contador de minúsculas | (EN) Lowercase counter
    for i in m[1:]:  # (ES) Recorre desde la segunda letra | (EN) Iterate from second letter
        if ord(i) >= 97 and ord(i) <= 122:  # (ES) Es minúscula | (EN) Is lowercase
            cm += 1
    if cm == len(m)-1:  # (ES) Si todas son minúsculas menos la primera | (EN) If all lowercase except first
        print(f'Son minusculas, excepto la primera: {m}')
        vocales(m)  # (ES) Llama a la función de vocales | (EN) Calls vowel check function
    else:
        print('Se encontro más de una mayúscula')  # (ES) Si hay más de una mayúscula | (EN) More than one uppercase found


def pedir():  # (ES) Función principal para pedir cadenas | (EN) Main function to request strings
    while(len(lista) <= 4):  # (ES) Mientras la lista tenga menos de 5 elementos | (EN) While list has less than 5 elements
        ca = ""  # (ES) Variable para filtrar caracteres no deseados | (EN) Variable to filter unwanted characters
        cad = input('Ingresa una cadena \n')  # (ES) Solicita cadena al usuario | (EN) Ask user for string
        for i in cad:
            if i == " ":  # (ES) Detecta espacios | (EN) Detect spaces
                print('Error, espacio')  # (ES) Mensaje de error | (EN) Error message
        if cad.isalpha():  # (ES) Si solo hay letras | (EN) If only letters
            minusculas(cad)  # (ES) Revisa mayúscula/minúscula | (EN) Check uppercase/lowercase
        else:  # (ES) Si hay números u otros caracteres | (EN) If numbers or other characters
            for i in cad:
                if ord(i) >= 48 and ord(i) <= 57:  # (ES) Ignora números | (EN) Ignore numbers
                    pass
                else:
                    ca += i  # (ES) Agrega caracteres válidos | (EN) Append valid characters
            minusculas(ca)  # (ES) Revisa mayúscula/minúscula | (EN) Check uppercase/lowercase


lista = []  # (ES) Lista para almacenar cadenas válidas | (EN) List to store valid strings
if __name__ == '__main__':
    pedir()  # (ES) Llama a la función principal | (EN) Calls main function
