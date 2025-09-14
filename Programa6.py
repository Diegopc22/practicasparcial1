def hola():  # (ES) Función principal que pide los datos | (EN) Main function that asks for the inputs
    c = 0  # (ES) Contador de entradas | (EN) Input counter
    while(True):  # (ES) Bucle infinito controlado por break | (EN) Infinite loop controlled by break
        a = input('Escriebe un dato o valor \n')  # (ES) Pide al usuario un valor | (EN) Asks the user for a value
        c += 1  # (ES) Incrementa el contador | (EN) Increments the counter
        if a.isdigit():  # (ES) Si lo ingresado son solo dígitos (número positivo) | (EN) If input is only digits (positive number)
            arr[c-1] = int(a)  # (ES) Convierte el dato a entero y lo guarda en el arreglo en la posición correspondiente | (EN) Converts input to integer and stores it in array at the right position
        elif a.isalpha():  # (ES) Si lo ingresado son solo letras | (EN) If input is only letters
            lis.append(a)  # (ES) Se agrega a la lista de cadenas | (EN) Appends it to the string list
        if c >= 10:  # (ES) Si ya se ingresaron 10 valores, se rompe el bucle | (EN) If 10 values are entered, break the loop
            break
    resultados()  # (ES) Llama a la función que muestra los resultados | (EN) Calls the function that shows results

def resultados():  # (ES) Función que imprime los resultados | (EN) Function that prints results
    c2 = 0  # (ES) Contador de números válidos en arr | (EN) Counter of valid numbers in arr
    for i in arr:  # (ES) Recorre el arreglo | (EN) Iterates through the array
        if i != 0:  # (ES) Si el valor es distinto de 0, significa que se ingresó un número | (EN) If value is not 0, it means a number was entered
            c2 += 1  # (ES) Incrementa el contador de números | (EN) Increments number counter
    print(f'El arreglo tiene {c2}')  # (ES) Imprime la cantidad de números guardados | (EN) Prints how many numbers were stored
    print(f'La lista tiene {len(lis)}')  # (ES) Imprime la cantidad de cadenas guardadas | (EN) Prints how many strings were stored
    print(arr)  # (ES) Imprime el arreglo completo | (EN) Prints the whole array
    print(lis)  # (ES) Imprime la lista completa | (EN) Prints the whole list

arr = [0,0,0,0,0,0,0,0,0,0]  # (ES) Arreglo de 10 posiciones inicializado en 0 | (EN) Array of 10 positions initialized at 0
lis = []  # (ES) Lista vacía para guardar cadenas | (EN) Empty list to store strings

if __name__ == "__main__":  # (ES) Punto de entrada del programa | (EN) Entry point of the program
    hola()  # (ES) Llama a la función principal | (EN) Calls the main function