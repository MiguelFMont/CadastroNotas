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