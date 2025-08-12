'''
4) Faça um programa que leia o nome e peso de 3 pessoas e no final mostre o nome da pessoa mais pesada e a mais leve;
'''
pessoas = [ ]

for i in range(3):
    nome = input("Escreva seu nome: ")
    peso = float(input("Entre seu peso: "))
    pessoas.append({'nome':nome, 'peso': peso})

maior = pessoas[0];
menor = pessoas[0];

for pessoa in pessoas:
    if pessoas['peso'] > maior['peso']:
        maior = pessoas
    if pessoas['peso'] < menor['peso']:
        menor = pessoas

print("Maior peso: ", maior)
print("Menor peso: ", menor)