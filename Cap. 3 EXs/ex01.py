"""
1) Crie uma lista preenchida com os 5 primeiros colocados de um campeonato de futebol, na ordem de colocação. Depois mostre:
   a) Apenas os 3 primeiros colocados;
   b) Os ultimos 2 colocados;
   c) Uma lista com os times em ordem alfabética;
   d) Em que posição da tabela se encontra o Barcelona 
"""

colocados =['Ponte De Ferro', 'Pousão', 'Barcelona', 'Unai Club', 'Three Hearts', 'Awesome FC']

print("Os 3 primeiros colocados: ")

for i in range(3):
    print(i+1,":",colocados[i])

print("\nOs dois ultimos colocados: ")

for i in range(len(colocados) - 1, len(colocados) - 3, -1):
    print(i+1,":",colocados[i])

print("\nEm ordem alfabética: ")
colocados.sort()
print(colocados)

try:
    print("\nBarcelona está na ", colocados.index('Barcelona')+1,"° posição")
except ValueError:
    print("\nO Barcelona não esta na tabela.")