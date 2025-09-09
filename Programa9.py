def vocales(cad):
    a = False
    e = False
    i = False
    o = False
    u = False
    #for i in cad:
    if 'a' in cad or 'A' in cad:
        a = True
    if 'e' in cad or 'E' in cad:
        e = True
    if 'i' in cad or 'I' in cad:
        i = True
    if 'o' in cad or 'O' in cad:
        o = True
    if 'u' in cad or 'U' in cad:
        u = True
    if a == True and e == True and i == True and o == True and u == True:
        lista.append(cad)
        print(lista)
    else:
        print('Erro')
    
def minusculas(m):
    cm = 0
    pass
    print(m)
    for i in m[1: ]:
        if ord(i) >= 97 and ord(i) <= 122:
            cm +=1
    if cm == len(m)-1:
        print(f'la cadena son minusculas esepto la primera{cm}')
        vocales(m)
    else:
        print('Error la cadena no cumple')

def leer():
    ce = 0
    nc = ""
    c = input('Ingresa una cadena \n')
    for i in c:
        if ord(i) != 32:
            ce += 1
    if ce == len(c):
        if c.isalpha():
            #revisamos que sea mayusculas
            minusculas(c)
        else:
            for i in c:
                if ord(i) >= 48 and ord(i) <= 57:
                    pass
                else:
                    nc += i
            print(nc)
            minusculas(nc)
    else:
        print('Error la cadena no comple')
        

lista = []
if __name__ == '__main__':
    while(True):
        leer()
        if len(lista) >= 5:
            break