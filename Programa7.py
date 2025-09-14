# Hacer un programa que lea nombre, edad y sexo de 5 personas,   # (ES) Programa que pide datos de 5 personas | (EN) Program that asks data from 5 people
# estos elementos tiene que estar dentro de una lista             # (ES) Los datos se guardan en una lista | (EN) The data must be stored in a list




def pedir():  # (ES) Función para pedir los datos | (EN) Function to request data
    d = 0  # (ES) Contador de personas registradas | (EN) Counter for registered people
    while(True):  # (ES) Bucle infinito que termina con break | (EN) Infinite loop that ends with break
        nombre = input('Cual es tu nombre: ')  # (ES) Pide el nombre | (EN) Asks for the name
        edad = input('Cual es tu edad: ')  # (ES) Pide la edad | (EN) Asks for the age
        sexo = input('Cual es tu genero M o H: ')  # (ES) Pide el sexo (M = mujer, H = hombre) | (EN) Asks for gender (M = female, H = male)
        lista.append("Nombre: "+nombre+", Edad: "+edad+", Sexo: "+sexo)  
        # (ES) Une los datos en un texto y los agrega a la lista | (EN) Joins the data in a string and appends it to the list
        d += 1  # (ES) Incrementa el contador de personas | (EN) Increases the people counter
        if d >= 5:  # (ES) Cuando ya se registraron 5 personas, termina el bucle | (EN) When 5 people have been registered, stops the loop
            break
    resultado()  # (ES) Llama a la función que muestra los resultados | (EN) Calls the function that shows results

def resultado():  # (ES) Función que imprime la lista de personas | (EN) Function that prints the people list
    print(lista)  # (ES) Muestra toda la lista | (EN) Displays the whole list

lista = []  # (ES) Lista vacía para guardar la información | (EN) Empty list to store the information

if __name__  == "__main__":  # (ES) Punto de entrada del programa | (EN) Entry point of the program
    pedir()  # (ES) Llama a la función pedir() | (EN) Calls the pedir() function