while verificador == False:
                nomeAluno = input(f'Digite o nome completo do {contCadastro + 1}º aluno: ')
                nomeAluno = nomeAluno.title()
                contEspacosVazios = 0
                contAlunoNaoEncontrado = 0
                contNum = 0

                for n in listaNumeroVerificacao:
                    if nomeAluno.count(n) > 0:
                        contNum += 1
                if contNum > 0:
                    os.system('cls')
                    print(f'O nome não pode conter números, por favor, digite novamente!\n')
                    contNum = 0
                    continue

                for i in nomeAluno:  
                    if i == ' ':
                        contEspacosVazios += 1

                if len(nomeAluno) < 15:
                    os.system('cls')
                    print(f'O nome não pode conter mais de 5 espaços nem conter menos que 10 caracteres!\n')
                    contEspacosVazios = 0
                    continue

                if nomeAluno == '':
                    os.system('cls')
                    print(f'O nome não pode conter somente espaços vazios, por favor, digite novamente!\n')
                    continue

                if len(nomeAluno) == (contEspacosVazios):
                        os.system('cls')
                        print(f'O nome não pode conter somente espaços vazios, por favor, digite novamente!\n')
                        contEspacosVazios = 0
                        continue
                for i in listaAlunos:
                    if i[0].find(nomeAluno) != -1: 
                        os.system('cls')
                        print(f'O aluno {nomeAluno} já foi cadastrado, por favor, digite novamente!\n')
                        continue
                    else:
                        contAlunoNaoEncontrado += 1
                if contAlunoNaoEncontrado == len(nomeAluno):    
                    verificador = True