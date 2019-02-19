lista_numeros = []
listaNumeroPar = []
listaNumeroImpar = []
novo_valor = True

while novo_valor:
    numero = int(input('Qual o valor? '))
    lista_numeros.append(numero)
    flag = input('Deseja entrar com mais valores (y/n)? ')
    if flag != 'y':
        novo_valor = False

for index_numero in lista_numeros:
    if (index_numero % 2) == 0:
        listaNumeroPar.append(index_numero)
    elif(index_numero % 2) != 0:
        listaNumeroImpar.append(index_numero)


print("A lista digitada foi {}".format(lista_numeros))
print("Os numeros pares desta lista são: {}".format(listaNumeroPar))
print("Os numeros impares desta lista são: {}".format(listaNumeroImpar))