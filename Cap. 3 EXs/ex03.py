"""
3) Faça um programa que leia o nome e a média de um aluno e guarde-os em um dicionário. Em seguida, a partir da média 
(para ser aprovado deve ter média >=50), gere a situação final do aluno ('AP' ou 'RP'), que também deve ser guardada neste 
dicionário. No final, mostre todo o conteúdo deste dicionário;
"""

nome = input("Escreva seu nome: ")
media = int(input("Entre sua média: "))

alunos = {'nome':nome, 'media': media}

if media >=50:
    alunos = {'nome':nome, 'media': media, 'situation': 'AP'}
else:
    alunos = {'nome':nome, 'media': media, 'situation': 'RP'}

print("Dicionário com todos os alunos: ", alunos)