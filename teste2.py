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

listaAlfabeto2 = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', ' ']

while True:
    nome = input('Digite seu nome: ')
    contInvalido = 0
    for l in nome:
            if listaAlfabeto2.count(l) == 0:
                contInvalido += 1

    if contInvalido > 0:
        print(f'O nome não pode conter números ou caracteres especiais, por favor, digite novamente!\n')
        continue
    else:
        print(f'Nome válido: {nome}')
        break
