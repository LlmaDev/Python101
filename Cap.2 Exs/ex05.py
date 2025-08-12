
while True:
    numero = input("Digite um número entre 1000 e 9999: ").strip()
    if numero.isdigit() and 1000 <= int(numero) <= 9999:
        break
    print("Entrada inválida! Digite um número de 4 dígitos.")

milhar = numero[0]
centena = numero[1]
dezena = numero[2]
unidade = numero[3]

print(f"Milhar: {milhar}")
print(f"Centena: {centena}")
print(f"Dezena: {dezena}")
print(f"Unidade: {unidade}")
