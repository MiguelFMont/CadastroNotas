import os

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
        os.system('cls')

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

            if mediaFinal % 1 > 0.75:
                mediaFinal = int(mediaFinal) + 1
            elif mediaFinal % 1 < 0.25:
                mediaFinal = int(mediaFinal)

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
            listaAluno.append(f'|  Média final: {mediaFinal:.1f}  |  \n\n')
            listaAlunos.append(listaAluno)
            contadorCadastro += 1
        print(f'Cadastro realizado com sucesso!')

    if opcaoSelecionada == '2':
        os.system('cls')
        print(f'Gerando Boletins..\n')

        for i in listaAlunos:
            for k in i:
                for j in k:
                        print(f'{j}', end='')
        print(f'\n')
        input('Tecle enter para voltar!')
        os.system('cls')

    if opcaoSelecionada == '3':
        os.system('cls')
        pesquisaAluno = input(f'Dígite o nome do aluno: ')
        print(f'Gerando Boletins por aluno..\n\n')
        contAlunoNaoEncontrado = 0
        for i in listaAlunos:
            if i[0].find(pesquisaAluno) != -1: 
                for k in i:
                    for j in k:
                        print(f'{j}', end='')
            else:
                contAlunoNaoEncontrado += 1
        if contAlunoNaoEncontrado == len(listaAlunos):
            print(f'Aluno não encontrado!')

        print(f'\n')
        input('Tecle enter para voltar!')
        os.system('cls')

    if opcaoSelecionada == '4':
        os.system('cls')
        print(f'Gerando alunos com maior média final..\n\n')
        alunoMaiorMedia = ''
        maiorMedia = 0
        for i in listaAlunos:
            mediaFinal = i[4].split(': ')[1]
            mediaFinal = float(mediaFinal.split(' | ')[0])
            if mediaFinal > maiorMedia:
                maiorMedia = mediaFinal
                alunoMaiorMedia = i[0].split(': ')[1]
                alunoMaiorMedia = alunoMaiorMedia.split('\n')[0]

        print(f'Aluno com maior média final:\n--> {alunoMaiorMedia}  com média {maiorMedia:.2f}')
        input('Tecle enter para voltar!')
        os.system('cls')

    if opcaoSelecionada == '5':
        os.system('cls')
        print(f'Gerando alunos com menor média final..\n\n')
        alunoMenorMedia = ''
        menorMedia = 10
        for i in listaAlunos:
            mediaFinal = i[4].split(': ')[1]
            mediaFinal = float(mediaFinal.split(' | ')[0])
            if mediaFinal < menorMedia:
                menorMedia = mediaFinal
                alunoMenorMedia = i[0].split(': ')[1]
                alunoMenorMedia = alunoMenorMedia.split('\n')[0]

        print(f'Aluno com menor média final:\n--> {alunoMenorMedia}  com média {menorMedia:.2f}')
        input('Tecle enter para voltar!')
        os.system('cls')

    if opcaoSelecionada == '6':
        os.system('cls')
        print(f'Gerando percentual de alunos com média maior que 5.0..\n\n')
        contPercentAlunos = 0
        for i in listaAlunos:
            mediaFinal = i[4].split(': ')[1]
            mediaFinal = float(mediaFinal.split(' | ')[0])
            if mediaFinal > 5:
                contPercentAlunos += 1

        percentual = (contPercentAlunos / len(listaAlunos)) * 100
        print(f'Percentual de alunos com média maior que 5.0: {percentual:.1f}%')
        input('Tecle enter para voltar!')
        os.system('cls')

