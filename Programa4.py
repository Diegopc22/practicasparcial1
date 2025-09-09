# Hacer un programa que lea 10 numeros
# Y los alamcene en una lista

a = [] #se inicialisa lalista
suma = 0
n = 0
numeros = "0,1,2,3,4,5,6,7,8,9"; #forma de validar que introduciendo lo que tu necesitas
while(n <= 9): #El while permite que indiques hasta que se cumpla lo que neseitas si no se repite hasta que termine
    b = input('Escibre un numero: ')
    x = 0
    for i in b:
        #if(ord(i) >= 48 and ord(i) <= 57): #El ord se utiliza para optener el ascci de algun caracter
        if i in numeros: #validacion por medio de lo que tu necesitas 
            x += 1
    if len(b) == x: #si lo que se introducio en b es igual a x se cumple la condicion 
        a.append(int(b)) #Se hace el castin de que b es un entero
        n += 1 #Si si son numeros se sumara uno para que se cumple la condicion del while  
    else:
        print('El valor no es un numero')
for i in a:
    print(i) #Se imprime la lista de numeros 
    suma += i #Se suma cada numero que esta en la variable i
print(f'La suma es: {suma}') #Se imprime el resultado de la suma
