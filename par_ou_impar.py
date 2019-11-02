n = int(input())
numeros_par = []
numeros_impar = []

for i in range(n):
    numero = int(input())
    if numero % 2 == 0:
        numeros_par.append(numero)
    else:
        numeros_impar.append(numero)
numeros_par.sort(reverse=True)'''Ordenando em Pilha'''
numeros_impar.sort(reverse=True)'''Ordenando em Pilha'''

print("Numeros pares:")
for par in numeros_par:
    print(par)

print("Numeros impares:")    
for impar in numeros_impar:
    print(impar)