# Instrucciones de entrada y salida                 # (ES) Notas sobre print y input | (EN) Notes about print and input
# print() o el print(f)                              # (ES) Cómo mostrar información en pantalla | (EN) How to display information
# print('Hola mundo')                                # (ES) Muestra un mensaje | (EN) Displays a message
# print(f'Hola mundo nuevo {10}')                    # (ES) Muestra un mensaje con formato y valores | (EN) Displays a formatted message with values

# input('Escribe un numero') #Solo introduce letras  # (ES) Entrada de datos | (EN) Input from user
# Casts para convertir a valores específicos         # (ES) Conversión de tipo | (EN) Type conversion
# f = 0.0
# f = float(input('Ingresa un numero con decimales'))  # (ES) Convierte a float | (EN) Converts to float
# a = 0
# a = int(input('Ingresa un numero entero'))          # (ES) Convierte a entero | (EN) Converts to integer
# c = 120
# print(str(c))                                       # (ES) Convierte a string | (EN) Converts to string
# v = ""
# v = str(c)                                         # (ES) Almacena el valor como string | (EN) Stores value as string
# Nota: solo las variables que no se introducen por teclado se obligan a inicializar | (EN) Note: only variables not entered by keyboard must be initialized

# Hacer un programa que lea nombre y precio de un producto,  # (ES) Pide nombre y precio de un producto | (EN) Requests product name and price
# el programa calculará el costo y precio de venta.          # (ES) Calcula costo (12%) y precio final con IVA (16%) | (EN) Calculates cost (12%) and final price with VAT (16%)

def costo():  # (ES) Función principal que calcula los precios | (EN) Main function that calculates prices
    while(True):  # (ES) Bucle infinito hasta que el usuario decida salir | (EN) Infinite loop until user decides to exit
        cos = 0  # (ES) Variable para el costo | (EN) Variable for cost
        iva = 0  # (ES) Variable para el precio final con IVA | (EN) Variable for final price with VAT
        nom = input('¿Cual es el nombre de tu producto? \n')  # (ES) Pide el nombre del producto | (EN) Asks for product name
        pre = float(input('¿Cual es el precio de tu producto? \n'))  # (ES) Pide el precio y convierte a float | (EN) Asks for price and converts to float
        cos = float(pre * 0.12 + pre)  # (ES) Calcula el costo sumando 12% | (EN) Calculates cost adding 12%
        iva = float(pre * 0.16)  # (ES) Calcula el IVA 16% sobre el precio original | (EN) Calculates 16% VAT on original price
        iva = iva + cos  # (ES) Precio final sumando IVA al costo | (EN) Final price adding VAT to cost
        print(f'El precio final de {nom} es ${cos:.2f}')  # (ES) Muestra el costo | (EN) Displays the cost
        print(f'El precio final de {nom} es ${iva:.2f}')  # (ES) Muestra el precio final con IVA | (EN) Displays final price with VAT
        res = input('Deseas terminar este programa (s/n) \n')  # (ES) Pregunta si desea terminar | (EN) Asks if user wants to exit
        if res == 's' or res == 'S':  # (ES) Si responde sí, rompe el bucle | (EN) If yes, breaks loop
            break

if __name__ == "__main__":  # (ES) Punto de entrada del programa | (EN) Program entry point
    costo()  # (ES) Llama a la función costo | (EN) Calls the cost function
