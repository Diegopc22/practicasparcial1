# Hacer un programa que lea 10 numeros
# Y los alamcene en un arreglo

a = [0,0,0,0,0,0,0,0,0,0]
#Pafa formatear el dato pones un f antes de cadena y al final orchetes
"""for i in range[0:10]:
    a[i] = int(input(f'Escribe un numero'{i+1}))"""
for i in range(0,10):
    a[i] = int(input('Escribe un numero: \n'))
for i in a:
    print(i)
