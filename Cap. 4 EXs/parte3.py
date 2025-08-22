import pandas as pd

# Carregar dataset
df = pd.read_csv("missions.csv")

# 1. Porcentagem de missões que deram certo
sucesso = (df["Status Mission"] == "Success").mean() * 100
print(f"1) Porcentagem de sucesso: {sucesso:.2f}%")

# 2. Média de gastos
media_gastos = df[df["Rocket Cost"] > 0]["Rocket Cost"].mean()
print(f"2) Média de gastos: {media_gastos}")

# 3. Quantidade de missões dos EUA
missoes_usa = df[df["Location"].str.contains("USA", case=False)].shape[0]
print("3) Missões EUA:", missoes_usa)

# 4. Missão mais cara da SpaceX
mais_cara = df[df["Company Name"]=="SpaceX"].sort_values("Rocket Cost", ascending=False).head(1)
print("4) Missão mais cara da SpaceX:\n", mais_cara)

# 5. Empresas e quantidade de missões
empresas = df["Company Name"].value_counts()
print("5) Empresas e nº de missões:\n", empresas)
