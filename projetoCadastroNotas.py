import os
import time

listaAlunos = []
listaNumeroVerificacao = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0', ',', '.']
listaQtdCadastroVerificacao = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
listaNomeVerificacao = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' '] 
menuOpcoes = True
while menuOpcoes == True: 
    print(f'''Opções:
    1. Cadastrar alunos e notas
    2. Boletins
    3. Filtro de boletim por aluno
    4. Alunos com maior média final
    5. Aluno com menor média final
    6. Percentual de alunos com média final maior que 5.0
    7. Excluir aluno cadastrado
    8. Sair
          
          >>> Use "-" para voltar ao menu principal <<<
    ''')
    opcaoSelecionada = input(f'--> ')
    os.system('cls')

    if opcaoSelecionada == '1':

        print(f'Opção "Cadastrar alunos e notas" selecionada!\n')
        verificador = False 
        while verificador == False:

            contNumInvalido = 0

            qtdCadastro = (input(f'Digite a quantidade de alunos que deseja cadastrar: '))
            if qtdCadastro == '-':
                os.system('cls')
                print(f'Voltando ao menu principal!\n')
                time.sleep(1)
                break
            if qtdCadastro == '':
                os.system('cls')
                print(f'Quantidade inválida, por favor, digite novamente!\n')
                continue
            else:
                # fazer a mesma verificação de números que foi feita com as notas
                for i in qtdCadastro:
                    if listaQtdCadastroVerificacao.count(i) == 0:
                        contNumInvalido += 1
                if contNumInvalido > 0:
                    os.system('cls')
                    print(f'Quantidade inválida, por favor, digite novamente!\n')
                    continue

                if qtdCadastro.count(',') >= 1 or qtdCadastro.count('.') >= 1:
                    os.system('cls')
                    print(f'Quantidade inválida, por favor, digite novamente!\n')
                    continue
                else:
                    qtdCadastro = int(qtdCadastro)
                    verificador = True
        os.system('cls')

        if qtdCadastro == '-':
                continue
        verificador = False
        contCadastro = 0
        
        while contCadastro < qtdCadastro:

            listaAluno = []
            listaNotaPratica = []
            listaNotaTeorica = []
            listaMediaPraticaTeorica = []
            
            verificador = False 
            # garante que todos os loopings de verificação continuem até que todas as verificações sejam verdadeiras

            while verificador == False:
                nomeAluno = input(f'Digite o nome completo do {contCadastro + 1}º aluno: ')
                nomeAluno = nomeAluno.title()
                contEspacosVazios = 0
                contAlunoNaoEncontrado = 0
                contNum = 0
                contInvalido = 0

                if nomeAluno == '-':
                    os.system('cls')
                    
                    break

                for l in nomeAluno.lower():
                    if listaNomeVerificacao.count(l) == 0:
                        contInvalido += 1

                if contInvalido > 0:
                    os.system('cls')
                    print(f'O nome não pode conter números ou caracteres especiais, por favor, digite novamente!\n')
                    continue

                if len(nomeAluno) < 15:
                    os.system('cls')
                    print(f'O nome não pode conter mais de 5 espaços nem conter menos que 10 caracteres!\n')
                    contEspacosVazios = 0
                    continue

                if nomeAluno == '':
                    os.system('cls')
                    print(f'O nome não pode conter somente espaços vazios, por favor, digite novamente!\n')
                    continue
      
                for i in nomeAluno:  
                    if i == ' ':
                        contEspacosVazios += 1

                if len(nomeAluno) == (contEspacosVazios):
                        os.system('cls')
                        print(f'O nome não pode conter somente espaços vazios, por favor, digite novamente!\n')
                        contEspacosVazios = 0
                        continue
                

                for i in listaAlunos:
                    if i[0].find(nomeAluno) != -1: 
                        os.system('cls')
                        print(f'O aluno {nomeAluno} já foi cadastrado, por favor, digite novamente!\n')
                        break
                    else:
                        contAlunoNaoEncontrado += 1
                if contAlunoNaoEncontrado == len(listaAlunos):    
                    verificador = True


            os.system('cls')
            if nomeAluno == '-':  
                break
            print(f'Iniciando o cadastro do aluno {nomeAluno.title()}...\n')
            print('Preencha os campos abaixo com as notas!\n')
            verificador = False

            while verificador == False:
                notaTeorica1 = (input(f'prímeira prova teórica: '))

                if notaTeorica1 == '-':
                    os.system('cls')
                    
                    break

                if notaTeorica1 == '':
                    os.system('cls')
                    print(f'Nota inválida, por favor, digite novamente!\n')
                    continue
                else:
                    contNumInvalido = 0

                    for n in notaTeorica1:
                        if listaNumeroVerificacao.count(n) == 0:
                            contNumInvalido += 1
                    if contNumInvalido > 0:
                        os.system('cls')
                        print(f'Nota inválida, por favor, digite novamente!\n')                    
                        continue

                    if notaTeorica1.count(',') > 1:
                        os.system('cls')
                        print(f'Nota inválida, por favor, digite novamente!\n')
                        continue
                    else:
                        notaTeorica1 = notaTeorica1.replace(',', '.')

                        notaTeorica1 = float(notaTeorica1)
                            
                        while notaTeorica1 < 0 or notaTeorica1 > 10:
                            os.system('cls')
                            print(f'A nota não pode ser maior que 10 ou menor que 0!\nDigite novamente.')
                            break
                        else:
                            verificador = True
                    
            os.system('cls')
            if notaTeorica1 == '-':
                break
            verificador = False

            while verificador == False:
                notaTeorica2 = (input(f'segunda prova teórica: '))

                if notaTeorica2 == '-':
                    os.system('cls')
                    
                    break

                if notaTeorica2 == '':
                    os.system('cls')
                    print(f'Nota inválida, por favor, digite novamente!\n')
                    continue
                else:
                    contNumInvalido = 0

                    for n in notaTeorica2:
                        if listaNumeroVerificacao.count(n) == 0:
                            contNumInvalido += 1
                    if contNumInvalido > 0:
                        os.system('cls')
                        print(f'Nota inválida, por favor, digite novamente!\n')                    
                        continue

                    if notaTeorica2.count(',') > 1:
                        os.system('cls')
                        print(f'Nota inválida, por favor, digite novamente!\n')
                        continue
                    else:
                        notaTeorica2 = notaTeorica2.replace(',', '.')

                        notaTeorica2 = float(notaTeorica2)
                            
                        while notaTeorica2 < 0 or notaTeorica2 > 10:
                            os.system('cls')
                            print(f'A nota não pode ser maior que 10 ou menor que 0!\nDigite novamente.')
                            break
                        else:
                            verificador = True

            os.system('cls')
            if notaTeorica2 == '-':
                break
            verificador = False
            while verificador == False:
                notaPratica1 = (input(f'primeira prova prática: '))

                if notaPratica1 == '-':
                    os.system('cls')
                    
                    break

                if notaPratica1 == '':
                    os.system('cls')
                    print(f'Nota inválida, por favor, digite novamente!\n')
                    continue
                else:
                    contNumInvalido = 0

                    for n in notaPratica1:
                        if listaNumeroVerificacao.count(n) == 0:
                            contNumInvalido += 1
                    if contNumInvalido > 0:
                        os.system('cls')
                        print(f'Nota inválida, por favor, digite novamente!\n')                    
                        continue

                    if notaPratica1.count(',') > 1:
                        os.system('cls')
                        print(f'Nota inválida, por favor, digite novamente!\n')
                        continue
                    else:
                        notaPratica1 = notaPratica1.replace(',', '.')

                        notaPratica1 = float(notaPratica1)
                            
                        while notaPratica1 < 0 or notaPratica1 > 10:
                            os.system('cls')
                            print(f'A nota não pode ser maior que 10 ou menor que 0!\nDigite novamente.')
                            break
                        else:
                            verificador = True

            os.system('cls')
            if notaPratica1 == '-':
                break
            verificador = False
            while verificador == False:
                notaPratica2 = (input(f'segunda prova prática: '))

                if notaPratica2 == '-':
                    os.system('cls')
                    
                    break

                if notaPratica2 == '':
                    os.system('cls')
                    print(f'Nota inválida, por favor, digite novamente!\n')
                    continue
                else:
                    contNumInvalido = 0

                    for n in notaPratica2:
                        if listaNumeroVerificacao.count(n) == 0:
                            contNumInvalido += 1
                    if contNumInvalido > 0:
                        os.system('cls')
                        print(f'Nota inválida, por favor, digite novamente!\n')                    
                        continue

                    if notaPratica2.count(',') > 1:
                        os.system('cls')
                        print(f'Nota inválida, por favor, digite novamente!\n')
                        continue
                    else:
                        notaPratica2 = notaPratica2.replace(',', '.')

                        notaPratica2 = float(notaPratica2)
                            
                        while notaPratica2 < 0 or notaPratica2 > 10:
                            os.system('cls')
                            print(f'A nota não pode ser maior que 10 ou menor que 0!\nDigite novamente.')
                            break
                        else:
                            verificador = True
            os.system('cls')
            if notaPratica2 == '-':
                break
            verificador = False

            mediaTeorica = (0.4 * notaTeorica1) + (0.6 * notaTeorica2)
            mediaPratica = (notaPratica1 + notaPratica2) / 2

            if mediaTeorica > 5 and mediaPratica > 5:
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
            listaAluno.append(f'|  Nome: {nomeAluno.title()}  |\n')
            listaAluno.append(listaNotaTeorica)
            listaAluno.append(listaNotaPratica)
            listaAluno.append(listaMediaPraticaTeorica)
            listaAluno.append(f'|  Média final: {mediaFinal:.2f}  |  \n\n')
            listaAlunos.append(listaAluno)
            contCadastro += 1
            print(f'Cadastro do aluno {nomeAluno.title()} concluído com sucesso!\n')
        
        input('Tecle Enter para voltar!\n')
        os.system('cls')

    if opcaoSelecionada == '2': 
        print(f'Opção "Boletins" selecionada!\n')  
        if listaAlunos == []:
            print(f'Nenhum aluno cadastrado, por favor, cadastre um aluno!\n')
            input('Tecle Enter para voltar!\n')
            os.system('cls')
        else:
            os.system('cls')
            print(f'Gerando Boletins..\n')

            for i in listaAlunos:
                for k in i:
                    for j in k:
                            print(f'{j}', end='')
            print(f'\n')
            input('Tecle Enter para voltar!\n')
            os.system('cls')

    if opcaoSelecionada == '3':
        print(f'Opção "Filtro de boletim por aluno" selecionada!\n')
        verificador = False
        while verificador == False:
            if listaAlunos == []:
                print(f'\nNenhum aluno cadastrado, por favor, cadastre um aluno!\n')
                input('Tecle Enter para voltar!\n')
                os.system('cls')
                break
            else:
                pesquisaAluno = input(f'Digite o nome do aluno: ')
                pesquisaAluno = pesquisaAluno.title()
                print(f'Gerando Boletim por aluno..\n\n')
                contAlunoNaoEncontrado = 0
                for i in listaAlunos:
                    if i[0].find(pesquisaAluno) != -1: 
                        for k in i:
                            for j in k:
                                print(f'{j}', end='')
                    else:
                        contAlunoNaoEncontrado += 1
                if contAlunoNaoEncontrado == len(listaAlunos):
                    print(f'Aluno não encontrado!\n')
                    continue
                else:
                    input('Tecle Enter para voltar!\n')
                    verificador = True
    os.system('cls')
    verificador = False

    if opcaoSelecionada == '4':
        print(f'Opção "Alunos com maior média final" selecionada\n')
        if listaAlunos == []:
            print('Nenhum aluno cadastrado, por favor, cadastre um aluno!\n')
            input('Tecle Enter para voltar!\n')
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

                    # Split foi utilizado para retirar o '\n' do nome do aluno
                    # Foi retirado do site https://docs.python.org/pt-br/3.6/library/stdtypes.html#text-sequence-type-str
                    # Do slide 7.Strings (Autorizado pela professora Lucia)

            print(f'Aluno com maior média final:\n--> {alunoMaiorMedia}  com média {maiorMedia:.2f}')
            input('Tecle Enter para voltar!\n')
            os.system('cls')

    if opcaoSelecionada == '5':
        print(f'Opção "Aluno com menor média final" selecionada!\n')
        if listaAlunos == []:
            print('Nenhum aluno cadastrado, por favor cadastre um aluno!\n')
            input('Tecle Enter para voltar!\n')
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

                    # Split foi utilizado para retirar o '\n' do nome do aluno
                    # Foi retirado do site https://docs.python.org/pt-br/3.6/library/stdtypes.html#text-sequence-type-str
                    # Do slide 7.Strings (Autorizado pela professora Lucia)

            print(f'Aluno com menor média final:\n--> {alunoMenorMedia}  com média {menorMedia:.2f}')
            input('Tecle Enter para voltar!\n')
            os.system('cls')

    if opcaoSelecionada == '6':
        print(f'Opção "Percentual de alunos com média maior que 5.0" selecionada!\n')
        if listaAlunos == []:
            print('\nNenhum aluno cadastrado, por favor cadastre um aluno!\n')
            input('Tecle Enter para voltar!\n')
            os.system('cls')
        else:
            os.system('cls')
            print(f'Gerando percentual de alunos com média maior que 5.0..\n')
            contPercentAlunos = 0
            for i in listaAlunos:
                mediaFinal = i[4].split(': ')[1]
                mediaFinal = float(mediaFinal.split(' | ')[0])
                if mediaFinal > 5:
                    contPercentAlunos += 1

            percentual = (contPercentAlunos / len(listaAlunos)) * 100
            print(f'--> {percentual:.1f}%')
            input('\nTecle Enter para voltar!')
            os.system('cls')

    if opcaoSelecionada == '7':
        print(f'Opção "Excluir alunos cadastrado" selecionada!\n')  
        while verificador == False:
            if listaAlunos == []:
                print('\nNenhum aluno cadastrado, por favor, cadastre um aluno!\n')
                input('Tecle Enter para voltar!\n')
                os.system('cls')
                break
            else:
                print(f'Gerando lista de alunos cadastrados..\n\n')
                for i in listaAlunos:
                    for k in i:
                        for j in k:
                            print(f'{j}', end='')
                            
                print(f'\n')
            
                contAlunoNaoEncontrado = 0
                nomeAlunoExcluir = input(f'Digite o nome do aluno que deseja excluir: ')

                if nomeAlunoExcluir == '-':
                    os.system('cls')
                    
                    break
                
                nomeAlunoExcluir = nomeAlunoExcluir.title()
                contNomes = 0
                listaNome = []
                for i in listaAlunos:
                # criar um contador para quando tiver mais de uma pessoa com o mesmo nome se o usuário não digirar o nome completo
                # e criar uma lista para armazenar o valor de i quando o usuário colocar o nome inteiro
                # se ele sempre digitasse o nome todo, não precisaria
                    if i[0].find(nomeAlunoExcluir) != -1:    
                        contNomes += 1
                        listaNome.append(i)
                    else:
                        contAlunoNaoEncontrado += 1
                if contAlunoNaoEncontrado == len(listaAlunos):
                    print(f'Aluno não encontrado!\n')
                    continue
                else:
                    if contNomes > 1:
                        os.system('cls')
                        print(f'Existem {contNomes} alunos com o nome {nomeAlunoExcluir}, por favor, digite o nome completo!\n')
                        input('Tecle Enter para voltar!\n')
                        os.system('cls')
                        continue
                    elif contNomes == 1:
                        os.system('cls')
                        listaAlunos.remove(listaNome[0])
                        print(f'Aluno {nomeAlunoExcluir} excluído com sucesso!\n')
                        input('Tecle Enter para voltar!\n')
                        os.system('cls')
                        verificador = True
        verificador = False

    if opcaoSelecionada == '-':
        os.system('cls')
        continue
        
    if opcaoSelecionada == '8':
        os.system('cls')
        print(f'Encerrando o programa!\n')
        menuOpcoes = False