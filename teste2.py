listaNome = [['NOME: Miguel'], ['NOME: João']]
cont = 0
for i in listaNome:
    if i[0].find('João') != -1:
        print('Aluno já cadastrado')
    else:
        cont += 1
    if cont == len(listaNome):
        print('Cadastro de aluno iniciado')