import pandas as pd

# Carregar dataset
df = pd.read_csv("space.csv")

# ===========================================
# 1) Porcentagem de missões que deram certo
# ===========================================
sucesso = (df["Status Mission"] == "Success").mean() * 100
print(f"1) Porcentagem de sucesso: {sucesso:.2f}%")

# ===========================================
# 2) Média de gastos (apenas missões com valor > 0)
# ===========================================
df["Cost"] = pd.to_numeric(df["Cost"], errors="coerce")  # garante que seja numérico
media_gastos = df.loc[df["Cost"] > 0, "Cost"].mean()
print(f"2) Média de gastos (missões com valor > 0): ${media_gastos:,.2f}")

# ===========================================
# 3) Quantidade de missões realizadas nos EUA
# ===========================================
missoes_usa = df[df["Location"].str.contains("USA", case=False, na=False)].shape[0]
print(f"3) Missões realizadas nos EUA: {missoes_usa}")

# ===========================================
# 4) Missão mais cara da SpaceX
# ===========================================
mais_cara = df[df["Company Name"]=="SpaceX"].sort_values("Cost", ascending=False).head(1)

if not mais_cara.empty:
    mission_name = mais_cara.iloc[0]["Detail"] if "Detail" in mais_cara.columns else "N/A"
    year = mais_cara.iloc[0]["Datum"] if "Datum" in mais_cara.columns else "N/A"
    cost = mais_cara.iloc[0]["Cost"]
    print("4) Missão mais cara da SpaceX:")
    print(f"   Nome: {mission_name}")
    print(f"   Ano: {year}")
    print(f"   Custo: ${cost:,.2f}")
else:
    print("4) Nenhuma missão da SpaceX encontrada.")

# ===========================================
# 5) Empresas e quantidade de missões
# ===========================================
empresas = df["Company Name"].value_counts()
print("5) Empresas e nº de missões:")
for empresa, qtd in empresas.items():
    print(f"   {empresa}: {qtd}")
