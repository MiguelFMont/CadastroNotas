import os
import time

listaAlunos = []
while True: 
    print(f'''Opções:
        1. Cadatrar alunos e notas
        2. Boletins
        3. Filtro de Boletim por aluno
        4. Alunos com maior Média Final
        5. Aluno com menor Média Final
        6. Pencentual de alunos com Média Final maior que 5.0
        ''')
    opcaoSelecionada = input(f'--> ')

    if opcaoSelecionada == '1':

        qtdCadastro = int(input(f'Dígite a quantidade de alunos que deseja cadastrar: '))

        contadorCadastro = 0

        while contadorCadastro < qtdCadastro:

            listaAluno = []
            listaNotaPratica = []
            listaNotaTeorica = []
            listaMediaPraticaTeorica = []

            nomeAluno = input(f'Dígite o nome completo do {contadorCadastro + 1}º aluno: ')

            print('Notas:')
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

            listaNotaTeorica.append(f'|  Notas das provas teóricas: ')
            listaNotaTeorica.append(f'T1: {notaTeorica1}  ')
            listaNotaTeorica.append(f'T2: {notaTeorica2}  |  \n')
            listaNotaPratica.append(f'|  Notas das provas práticas: ')
            listaNotaPratica.append(f'P1: {notaPratica1}  ')
            listaNotaPratica.append(f'P2: {notaPratica2}  |  \n')
            listaMediaPraticaTeorica.append(f'|  Média prática: {mediaPratica  }  |  \n')
            listaMediaPraticaTeorica.append(f'|  Média teórica: {mediaTeorica  }  |  \n')
            listaAluno.append(f'|  Nome: {nomeAluno}  |\n')
            listaAluno.append(listaNotaTeorica)
            listaAluno.append(listaNotaPratica)
            listaAluno.append(listaMediaPraticaTeorica)
            listaAluno.append(f'|  Média final: {mediaFinal}  |  ')
            listaAlunos.append(listaAluno)
            contadorCadastro += 1

    if opcaoSelecionada == '2':
        os.system('cls')
        print(f'Gerando Boletins..')

        for i in listaAlunos:
            for k in i:
                for j in k:
                        print(f'{j}', end='')
    print(f'\n')
    input('Tecle enter para voltar!')
           