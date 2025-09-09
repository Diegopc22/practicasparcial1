# Hacer un programa que en una lista se introdusca cadenas de caracteres con las siguinetes restriciones
# 1.- las cadenas no deven de tener espacio
# 2.- la cedena solo puede tener mayusculas la primer letra
# 3.- obligatoriamente debe de tener todas las bocales.
# El programa no termina hasta que la lista tenga 5 elementos
#Tarea 2
def vocales(v):
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
    if va == True and ve == True and vi == True and vo == True and vu == True:
        lista.append(v)
        print(lista)
    else:
        print('No contiene las vocales')


def minusculas(m):
    cm = 0
    for i in m[1:]:
        if ord(i) >= 97 and ord(i) <= 122:
            cm += 1
    if cm == len(m)-1:
        print(f'Son minusculas, exepto la primera: {m}')
        vocales(m)
    else:
        print('Se encontro más de una mayuscula')

def pedir():
    while(len(lista) <= 4):
        #d = 0
        ca = ""
        cad = input('Ingresa una cadena \n')
        for i in cad:
            if i == " ":
                print('Error, espcacio')
        if cad.isalpha():
            minusculas(cad)
        else:
            for i in cad:
                if ord(i) >= 48 and ord(i) <= 57:
                    pass
                else:
                    ca += i
            minusculas(ca)

                


lista = []
if __name__ == '__main__':
    pedir()