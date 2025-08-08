numero = int(input("Digite o número que deseja ver a tabuada: "))

inicio = int(input("Digite o início do intervalo: "))
fim = int(input("Digite o fim do intervalo: "))

print(f"\n📌 Tabuada do {numero} de {inicio} até {fim}:\n")

for i in range(inicio, fim + 1):
    print(f"{numero} x {i} = {numero * i}")
