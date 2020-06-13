
n = int(input('Ingrese numero a revisar: '))
i=2
flag=0

while i < n:
    if n % i == 0:
        print(f'{n} no es primo')
        flag = 1
        break
    i += 1
if flag == 0:
    print(f'{n} si es primo')