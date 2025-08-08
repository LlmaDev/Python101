nome_completo = input("Digite seu nome completo: ").strip()

print("Nome em maiúsculas:", nome_completo.upper())
print("Nome em minúsculas:", nome_completo.lower())

total_letras = len(nome_completo.replace(" ", ""))
print("Total de letras no nome:", total_letras)

partes_nome = nome_completo.split()
if len(partes_nome) > 1:
    partes_nome[-1] = "do Inatel"
    nome_inatel = " ".join(partes_nome)
else:
    nome_inatel = nome_completo + " do Inatel"

print("Nome modificado:", nome_inatel)
