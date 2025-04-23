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
    os.system('cls')

    if opcaoSelecionada == '1':

        qtdCadastro = (input(f'Dígite a quantidade de alunos que deseja cadastrar: '))
        
        while qtdCadastro == '' or qtdCadastro < '0' or qtdCadastro > '9':
            os.system('cls')
            print(f'Quantidade inválida, por favor digite novamente!')
            qtdCadastro = (input(f'Dígite a quantidade de alunos que deseja cadastrar: '))
        else:
            for i in qtdCadastro:
                if qtdCadastro.count(',') >= 1:
                    os.system('cls')
                    print(f'Quantidade inválida, por favor digite novamente!')
                    qtdCadastro = (input(f'Dígite a quantidade de alunos que deseja cadastrar: '))
            qtdCadastro = int(qtdCadastro)

        contadorCadastro = 0

        while contadorCadastro < qtdCadastro:

            listaAluno = []
            listaNotaPratica = []
            listaNotaTeorica = []
            listaMediaPraticaTeorica = []
            listaNumeroVerificacao = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']

            verificador = False
            verificador2 = False
            contEspacosVazios = 0

            nomeAluno = input(f'Dígite o nome completo do {contadorCadastro + 1}º aluno: ')
            
            while verificador == False:
                contNum = 0
                while verificador2 == False:
                    for n in listaNumeroVerificacao:
                        if nomeAluno.count(n) > 0:
                            contNum += 1
                        if contNum > 0:
                            os.system('cls')
                            print(f'O nome não pode conter números, por favor digite novamente!')
                            nomeAluno = input(f'Dígite o nome completo do {contadorCadastro + 1}º aluno: ')
                            contNum = 0
                            break
                        elif contNum == 0:
                            verificador2 = True
                            break

                verificador2 = False
                
                for aluno in listaAlunos:
                    if aluno[0].find(nomeAluno) != -1:
                        os.system('cls')
                        print(f'O nome já está cadastrado, por favor digite novamente!')
                        nomeAluno = input(f'Dígite o nome completo do {contadorCadastro + 1}º aluno: ')
                        continue

                for i in nomeAluno:

                    if i == ' ':
                        contEspacosVazios += 1

                if nomeAluno == '':
                    os.system('cls')
                    print(f'O nome não pode conter somente espaços vazio, por favor digite novamente!')
                    nomeAluno = input(f'Dígite o nome completo do {contadorCadastro + 1}º aluno: ')

                if len(nomeAluno) == (contEspacosVazios):
                        os.system('cls')
                        print(f'O nome não pode conter somente espaços vazio, por favor digite novamente!')
                        nomeAluno = input(f'Dígite o nome completo do {contadorCadastro + 1}º aluno: ')
                        contEspacosVazios = 0
                        continue
                else:
                    verificador = True
            
            os.system('cls')
            print(f'Iniciando o cadastro do aluno {nomeAluno}...\n')
            print('Preencha os campos abaixo com as notas!')

            notaTeorica1 = (input(f'prímeira prova teórica: '))

            while notaTeorica1 == '' or notaTeorica1 < '0' or notaTeorica1 > '9':
                os.system('cls')
                print(f'Nota inválida, por favor digite novamente!')
                notaTeorica1 = (input(f'prímeira prova teórica: '))
            else:
                
                for i in notaTeorica1:

                    if notaTeorica1.count(',') > 1:
                        os.system('cls')
                        print(f'Nota inválida, por favor digite novamente!')
                        notaTeorica1 = (input(f'prímeira prova teórica: '))
                        continue

                    else:
                        notaTeorica1 = notaTeorica1.replace(',', '.')
                        break

                notaTeorica1 = float(notaTeorica1)
                while notaTeorica1 < 0 or notaTeorica1 > 10:
                    os.system('cls')
                    print(f'A nota não pode ser maior que 10 ou menor que 0!')
                    notaTeorica1 = float(input(f'prímeira prova teórica: '))
                os.system('cls')

            notaTeorica2 = (input(f'segunda prova teórica: '))

            while notaTeorica2 == '' or notaTeorica2 < '0' or notaTeorica2 > '9':
                os.system('cls')
                print(f'Nota inválida, por favor digite novamente!')
                notaTeorica2 = (input(f'segunda prova teórica: '))
            else:
                 
                for i in notaTeorica2:
                    if notaTeorica2.count(',') > 1:
                        os.system('cls')
                        print(f'Nota inválida, por favor digite novamente!')
                        notaTeorica2 = (input(f'segunda prova teórica: '))
                        continue
                    else:
                        notaTeorica2 = notaTeorica2.replace(',', '.')
                        break

                notaTeorica2 = float(notaTeorica2)
                while notaTeorica2 < 0 or notaTeorica2 > 10:
                    os.system('cls')
                    print(f'A nota não pode ser maior que 10 ou menor que 0!')
                    notaTeorica2 = float(input(f'segunda prova teórica: '))
                os.system('cls')

            notaPratica1 = (input(f'primeiro projeto prático: '))

            while notaPratica1 == '' or notaPratica1 < '0' or notaPratica1 > '9':
                os.system('cls')
                print(f'Nota inválida, por favor digite novamente!')
                notaPratica1 = (input(f'primeiro projeto prático: '))
            else:
                for i in notaPratica1:
                    if notaPratica1.count(',') > 1:
                        os.system('cls')
                        print(f'Nota inválida, por favor digite novamente!')
                        notaPratica1 = (input(f'primeiro projeto prático: '))
                        continue
                    else:
                        notaPratica1 = notaPratica1.replace(',', '.')
                        break
                   
                notaPratica1 = float(notaPratica1)
                while notaPratica1 < 0 or notaPratica1 > 10:
                    os.system('cls')
                    print(f'A nota não pode ser maior que 10 ou menor que 0!')
                    notaPratica1 = float(input(f'primeiro projeto prático: '))
                os.system('cls')

            notaPratica2 = (input(f'segundo projeto prático: '))

            while notaPratica2 == '' or notaPratica2 < '0' or notaPratica2 > '9':
                os.system('cls')
                print(f'Nota inválida, por favor digite novamente!')
                notaPratica2 = (input(f'segundo projeto prático: '))
            else:

                for i in notaPratica2:
                    if notaPratica2.count(',') > 1:
                        os.system('cls')
                        print(f'Nota inválida, por favor digite novamente!')
                        notaPratica2 = (input(f'segundo projeto prático: '))
                        continue
                    else:
                        notaPratica2 = notaPratica2.replace(',', '.')
                        break
                    
                notaPratica2 = float(notaPratica2)
                while notaPratica2 < 0 or notaPratica2 > 10:
                    os.system('cls')
                    print(f'A nota não pode ser maior que 10 ou menor que 0!')
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
            listaMediaPraticaTeorica.append(f'|  Média prática: {mediaPratica  :.2f}  |  \n')
            listaMediaPraticaTeorica.append(f'|  Média teórica: {mediaTeorica  :.2f}  |  \n')
            listaAluno.append(f'|  Nome: {nomeAluno}  |\n')
            listaAluno.append(listaNotaTeorica)
            listaAluno.append(listaNotaPratica)
            listaAluno.append(listaMediaPraticaTeorica)
            listaAluno.append(f'|  Média final: {mediaFinal:.2f}  |  \n\n')
            listaAlunos.append(listaAluno)
            contadorCadastro += 1
            print(f'Cadastro do aluno {nomeAluno} concluído com sucesso!\n')
        
        input('Tecle enter para voltar!')
        os.system('cls')

    if opcaoSelecionada == '2':
        if listaAlunos == []:
            print('\nNenhum aluno cadastrado, por favor cadastre um aluno!\n')
            input('Tecle enter para voltar!')
            os.system('cls')
        else:
            os.system('cls')
            print(f'\nGerando Boletins..\n')

            for i in listaAlunos:
                for k in i:
                    for j in k:
                            print(f'{j}', end='')
            print(f'\n')
            input('Tecle enter para voltar!')
            os.system('cls')

    if opcaoSelecionada == '3':
        pesquisaAluno = input(f'Dígite o nome do aluno: ')
        pesquisaAluno = pesquisaAluno.title()
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
        if listaAlunos == []:
            print('\nNenhum aluno cadastrado, por favor cadastre um aluno!\n')
            input('Tecle enter para voltar!')
            os.system('cls')
        else:
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
        if listaAlunos == []:
            print('\nNenhum aluno cadastrado, por favor cadastre um aluno!\n')
            input('Tecle enter para voltar!')
            os.system('cls')
        else:
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
        if listaAlunos == []:
            print('\nNenhum aluno cadastrado, por favor cadastre um aluno!\n')
            input('Tecle enter para voltar!')
            os.system('cls')
        else:
            os.system('cls')
            print(f'Gerando percentual de alunos com média maior que 5.0..')
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