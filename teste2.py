nome = '|  Nome: Miguel Fernandes Monteiro  |\n'

separadorNome = nome.split(': ')[1]
separadorNome = separadorNome.split('  |')[0]
print(f'''
{separadorNome}

''')