while True:
    sexo = input("Digite seu sexo (M/F): ").strip().upper()

    if sexo == "M":
        print("Você é homem.")
        break
    elif sexo == "F":
        print("Você é mulher.")
        break
    else:
        print("Entrada inválida! Digite apenas M ou F.")
