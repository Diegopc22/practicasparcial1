
# Hacer un programa que lea una cadena y que muestre en pantalla
# cuantos numeros tiene, cuantas mayusculas, cuantas minuculas
# y cuantos espacios

def inicio():
    n = 0
    e = 0
    min = 0
    m = 0
    numeros = "0123456789"
    cadena = input('Ecribe una cadena: ')
    for i in cadena:
        if i in numeros:
            n += 1
        if i == ' ':
            e += 1
        if ord(i)>= 97 and ord(i) <= 122:
            min += 1
        if ord(i) >= 65 and ord(i) <= 90:
            m += 1
    print(f'Los numeros son: {m} \n y los espacios: {e} \n y las minusculas: {min} \n y las mayusculas: {m}')





if __name__ == '__main__':
    inicio()