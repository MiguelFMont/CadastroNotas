import os

listaAlunos = []

qtdCadastro = int(input(f'Dígite a quantidade de alunos que deseja cadastrar: '))

contadorCadastro = 0

while contadorCadastro < qtdCadastro:

    listaAluno = []
    listaNotaPratica = []
    listaNotaTeorica = []
    listaMediaPraticaTeorica = []

    nomeAluno = input(f'Dígite o nome completo do {contadorCadastro + 1}º aluno: ')

    print('Dígite a nota da:')
    notaTeorica1 = float(input(f'prímeira prova teórica: '))
    notaTeorica2 = float(input(f'segunda prova teórica: '))
    notaPratica1 = float(input(f'primeiro projeto prático: '))
    notaPratica2 = float(input(f'segundo projeto prático: '))
    os.system('cls')

    mediaTeorica = (0.4 * notaTeorica1) + (0.6 * notaTeorica2)
    mediaPratica = (notaPratica1 + notaPratica2) / 2

    if mediaTeorica and mediaPratica > 5:
        mediaFinal = (0.3 * mediaPratica) + (0.7 * mediaTeorica)
    else:
        if mediaTeorica < mediaPratica:
            mediaFinal = mediaTeorica
        else:
            mediaFinal = mediaPratica

    listaNotaTeorica.append(f'Notas das provas teóricas: ')
    listaNotaTeorica.append(notaTeorica1)
    listaNotaTeorica.append(notaTeorica2)
    listaNotaPratica.append(f'Notas das provas práticas: ')
    listaNotaPratica.append(notaPratica1)
    listaNotaPratica.append(notaPratica2)
    listaMediaPraticaTeorica.append(f'Média prática: {mediaPratica}' )
    listaMediaPraticaTeorica.append(f'Média teórica: {mediaTeorica}')
    listaAluno.append(nomeAluno)
    listaAluno.append(listaNotaTeorica)
    listaAluno.append(listaNotaPratica)
    listaAluno.append(listaMediaPraticaTeorica)
    listaAluno.append(f'Média final: {mediaFinal}')
    listaAlunos.append(listaAluno)
    contadorCadastro += 1

print(listaAlunos)
