#Hacer un programa que lea nombre, edad y sexo de 5 personas, 
#estos elementos tiene que estar dentro de una lista



def pedir():
    d = 0
    while(True):
        nombre = input('Cual es tu nombre: ')
        edad = input('Cual es tu edad: ')
        sexo = input('Cual es tu genero M o H: ')
        lista.append("Nombre: "+nombre+", Edad: "+edad+", Sexo: "+sexo)
        d += 1
        if d >= 5:
            break
    resultado()

def resultado():
    print(lista)

lista = []
if __name__  == "__main__":
    pedir() 