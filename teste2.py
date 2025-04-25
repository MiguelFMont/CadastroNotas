'''
listaNome = [['NOME: Miguel'], ['NOME: João']]
cont = 0
for i in listaNome:
    if i[0].find('João') != -1:
        print('Aluno já cadastrado')
    else:
        cont += 1
    if cont == len(listaNome):
        print('Cadastro de aluno iniciado')
'''
'''
listaAlunos = [['NOME: Miguel'], ['NOME: João']]
listaNome = []
for i in listaAlunos:
    if i[0].find('João') != -1:
        print('Aluno já cadastrado')
    else:
        listaNome.append(i[0])
        cont = 0
        for i in listaNome:
            if i[0].find('João') != -1:
                print('Aluno já cadastrado')
            else:
                cont += 1
    listaNome.append(listaNome.count(i))
print(listaNome)
'''

num = (input('Digite um número: '))

if num not in '0123456789.':
    print('O número não pode conter letras ou caracteres especiais!')