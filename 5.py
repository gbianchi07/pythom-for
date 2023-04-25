from tkinter import N


alunos = int(input('informe a quantidade de alunos: '))
notas = int(input('informe a quantidade de notas: '))

for a in range(alunos):
    soma= 0 
    for b in range(notas):
        n = float(input('informe a nota: '))
        soma += n
    media = soma / notas
    print(f'media: {round(media, 2)}')