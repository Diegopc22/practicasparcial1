def vocales(cad):
    # (ES) Flags para comprobar cada vocal | (EN) Flags to check each vowel
    a = False
    e = False
    i = False
    o = False
    u = False
    # (ES) Validamos que la cadena contenga todas las vocales (mayus o minus) | (EN) Check if string contains all vowels (upper or lower)
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
    # (ES) Si todas son True, agregamos la cadena a la lista | (EN) If all are True, append the string to the list
    if a == True and e == True and i == True and o == True and u == True:
        lista.append(cad)
        print(lista)
    else:
        print('Error: la cadena no tiene todas las vocales')


def minusculas(m):
    cm = 0  # (ES) Contador de minúsculas | (EN) Lowercase counter
    print(m)
    # (ES) Recorre desde el segundo caracter en adelante | (EN) Iterate from second character onwards
    for i in m[1:]:
        if ord(i) >= 97 and ord(i) <= 122:  # (ES) Verifica si es minúscula | (EN) Check if lowercase
            cm += 1
    # (ES) Si todas (menos la primera) son minúsculas | (EN) If all (except the first) are lowercase
    if cm == len(m) - 1:
        print(f'La cadena son minúsculas excepto la primera ({cm})')
        vocales(m)
    else:
        print('Error: la cadena no cumple con el formato de minúsculas')


def leer():
    ce = 0  # (ES) Contador de caracteres diferentes de espacio | (EN) Counter of non-space characters
    nc = ""  # (ES) Nueva cadena filtrada si hay números | (EN) New filtered string if numbers exist
    c = input('Ingresa una cadena \n')
    # (ES) Contamos los caracteres distintos a espacio | (EN) Count non-space characters
    for i in c:
        if ord(i) != 32:
            ce += 1
    # (ES) Validamos que no haya espacios | (EN) Validate that there are no spaces
    if ce == len(c):
        if c.isalpha():  # (ES) Solo letras | (EN) Only letters
            minusculas(c)
        else:
            # (ES) Si hay números, los filtramos | (EN) If numbers exist, filter them out
            for i in c:
                if ord(i) >= 48 and ord(i) <= 57:  # (ES) Es número | (EN) It's a number
                    pass
                else:
                    nc += i
            print(nc)
            minusculas(nc)
    else:
        print('Error: la cadena no cumple (tiene espacios)')


lista = []  # (ES) Lista para guardar cadenas válidas | (EN) List to store valid strings
if __name__ == '__main__':
    while True:  # (ES) Se repite hasta que tengamos 5 cadenas válidas | (EN) Repeat until we have 5 valid strings
        leer()
        if len(lista) >= 5:
            break
