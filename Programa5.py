
arr = [0,0,0,0,0,0,0,0,0,0]
lis = []
c = 0
c2 = 0
while(True):
    a = input('Escriebe un dato o valor \n')
    c += 1
    if a.isdigit():
        arr[c-1] = int(a)
    elif a.isalpha():
        lis.append(a)
    if c >= 10:
        break

for i in arr:
    if i != 0:
        c2 += 1
print(f'El arreglo tiene {c2}')
print(f'La lista tiene {len(lis)}')
print(arr)
print(lis)