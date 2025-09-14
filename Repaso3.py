
# def validar(a):
#     c = 0
#     d = 0.0
#     try:
#         c = int(a)
#         print('Es un valor numerico, sin decimales')
#     except ValueError:
#         print('No es valor numerico, sin decimales')


#     try:
#         d = float(a)
#         print('Es un valor numerico, con decimales')
#     except ValueError:
#         print('No es valor numerico, con decimales')


# def leer():
#     # ord que optiene el ascii del caracter
#     # isalpha para caracteres
#     # isdigit para numeros
#     # try except ValueError:
#     a = input('Escribe un dato o valor \n')
#     validar(a)


# if __name__ == "__main__":
#     leer()

    # Hacer un programa que leea un dato cual sea y que lo almacene en una lista, respetando su tipo de dato

def validar(dato):
    f = 0.0
    i = 0
    
    try:
        i = int(dato)
        print('Es un entero')
        return i
    except ValueError:
        print('No es un entero')
        
    try:
        f = float(dato)
        print('Es un flotante')
        return f
    except ValueError:
        print('No un flotante')
        print('Es un string')
    return dato

def leer():
    a = input('Ingrisa un dato \n')
    dat = validar(a)
    lista.append(dat)

lista = []
if __name__ == '__main__':
    while(True):
        leer()
        r = input('deas añadir un nuevo dato S/N \n')
        if r == 'N' or  r =='n':
            print(lista)
            break