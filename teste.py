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
            contEspacosVazios = 0

            nomeAluno = input(f'Dígite o nome completo do {contadorCadastro + 1}º aluno: ')

            while verificador == False:

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

                for i in nomeAluno:
                    if listaNumeroVerificacao.count(i) >= 1:
                        os.system('cls')
                        print(f'O nome não pode conter números, por favor digite novamente!')
                        nomeAluno = input(f'Dígite o nome completo do {contadorCadastro + 1}º aluno: ')
                        break
                    else:
                        verificador = True


            os.system('cls')
            print(f'Iniciando o cadastro do aluno {nomeAluno}...\n')
            print('Preencha os campos abaixo com as notas!')