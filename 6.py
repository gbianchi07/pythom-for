numero = int(input('informe o  numero: '))
menor = numero
maior = numero

for n in range(9):
    numero = int(input('informe o  numero: '))
    if numero > maior:
        maior = numero
    if numero < menor:
        menor = numero
print(f'maior: {maior}')
print(f'menor: {menor}')