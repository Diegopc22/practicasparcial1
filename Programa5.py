arr = [0,0,0,0,0,0,0,0,0,0]  # (ES) Arreglo con 10 ceros para guardar números | (EN) Array with 10 zeros to store numbers
lis = []  # (ES) Lista vacía para guardar letras/cadenas | (EN) Empty list to store letters/strings
c = 0  # (ES) Contador de entradas totales (hasta 10) | (EN) Counter of total inputs (up to 10)
c2 = 0  # (ES) Contador de números válidos en arr | (EN) Counter of valid numbers in arr

while(True):  # (ES) Bucle infinito que se detendrá con break | (EN) Infinite loop that stops with break
    a = input('Escriebe un dato o valor \n')  # (ES) Pide un dato al usuario | (EN) Asks the user for a value
    c += 1  # (ES) Incrementa el contador de entradas | (EN) Increases the input counter
    if a.isdigit():  # (ES) Valida si lo ingresado son solo dígitos (número entero positivo) | (EN) Checks if input is only digits (positive integer)
        arr[c-1] = int(a)  # (ES) Convierte el valor a entero y lo guarda en arr | (EN) Converts input to integer and stores it in arr
    elif a.isalpha():  # (ES) Valida si lo ingresado son solo letras | (EN) Checks if input is only letters
        lis.append(a)  # (ES) Agrega el texto a la lista lis | (EN) Appends the text to list lis
    if c >= 10:  # (ES) Si ya se ingresaron 10 datos, termina el bucle | (EN) If 10 values entered, stop the loop
        break

for i in arr:  # (ES) Recorre el arreglo arr | (EN) Iterates through array arr
    if i != 0:  # (ES) Cuenta solo los números distintos de 0 (los ingresados) | (EN) Counts only numbers different from 0 (the entered ones)
        c2 += 1  # (ES) Incrementa el contador de números válidos | (EN) Increases valid number counter

print(f'El arreglo tiene {c2}')  # (ES) Imprime cuántos números se guardaron | (EN) Prints how many numbers were stored
print(f'La lista tiene {len(lis)}')  # (ES) Imprime cuántas cadenas se guardaron | (EN) Prints how many strings were stored
print(arr)  # (ES) Imprime todo el arreglo de números | (EN) Prints the whole number array
print(lis)  # (ES) Imprime toda la lista de letras/cadenas | (EN) Prints the whole string list
