'''
5) Desenvolva um programa que leia o nome, idade e sexo de n pessoas. No final, mostre:

   a. A média de idade do grupo;

   b. Quantas mulheres têm menos de 20 anos.
'''
people = []
mediaIdade = 0
mulheresMenos20 = 0
n = int(input('Entre o numero de pessoas: '))

for i in range(n):
    nome = input("Entre com seu nome: ")
    idade = float(input("Entre com sua idade: "))
    sexo = input("Entre com seu sexo('M' ou 'F'): ").strip().upper()
    mediaIdade += idade
    
    if sexo == "F" and idade < 20:
        mulheresMenos20+=1
        
print("/nMedia de idade do grupo: ", mediaIdade/n)
print("Há ", mulheresMenos20, " mulheres com menos de 20 anos!")