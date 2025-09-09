

# Instecciones de entrada y salida
# print() o el print(f)
# print('Hola mundo')
# print(f'Hola mundo nuevo {10}')
# # entrada de datos
# input('Escribe un numero') #Solo introduce letras
#Castis paracovertir a valres especificos
# f = 0.0
# f = float(input('Ingresa un numero con decimales'))
# a = 0
# a = int(input('Ingresa un numero entero'))
# c = 120
# print(str(c))
# v = ""
# v = str(c)
# Nota: solo las variables que no se introducen por teclado se obligana inicialisarlas.


# Hacer un programaque lea nombre y precio de un product, el programa calculara
# el costo y precio de venta.# el costo involucra el 12% y el IVA el 16

def costo():
    while(True):
        cos = 0
        iva = 0
        nom = input('¿Cual es el nombre de tu producto? \n')
        pre = float(input('¿Cual es el precio de tu producto? \n'))
        cos = float(pre * .12 + pre)
        iva = float(pre * .16)
        iva = iva + cos
        
        print(f'El precio final de {nom} es ${cos:.2f}')
        print(f'El precio final de {nom} es ${iva:.2f}')
        res = input('Deseas terminar este programa (s/n) \n')
        if res == 'n' or res == 'N':
            break

# def costo():
#     for i in range(1,5):
#         cos = 0
#         iva = 0
#         nom = input('¿Cual es el nombre de tu producto? \n')
#         pre = float(input('¿Cual es el precio de tu producto? \n'))
#         cos = float(pre * .12 + pre)
#         iva = float(pre * .16 + cos + pre)
        
#         print(f'El precio final de {nom} es ${cos:.2f}')
#         print(f'El precio final de {nom} es ${iva:.2f}')
#         res = input('Deseas terminar este programa (s/n) \n')
#         #if res == 'n' or res == 'N':
#         #    break

if __name__ == "__main__":
    costo()