aluno = {}
aluno['nome'] = input('Nome: ')
aluno['media'] = float(input(f'Média de {aluno["nome"]}: '))
print(f'Nome é igual a {aluno["nome"]}\nMédia é igual a {aluno["media"]}')
if aluno['media'] >= 7:
    print('Situação é igual a Aprovado')
else:
    print('Situação é igual a Reprovado')
