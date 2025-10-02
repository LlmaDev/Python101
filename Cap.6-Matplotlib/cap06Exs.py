'''
Exercícios a serem resolvidos:

1. Por meio do dataset paises.csv, trace dois gráficos de linhas em um mesmo plano cartesiano, um mostrando a taxa de mortalidade (Deathrate) e outro a 
taxa de natalidade (Birthrate) dos países da América do Norte;
2. Por meio do dataset space.csv, trace um gráfico em barras mostrando quantas empresas espaciais diferentes os EUA e a CHINA possuem;
Dica: não se esqueça de retirar os resultados repetidos
3. Por meio do dataset space.csv, trace um gráfico em torta ilustrando a porcentagem de missões da empresa Roscosmos que deram certo e que deram errado;
'''

import matplotlib.pyplot as plt
import numpy as np
import pandas as pd

# ===== EXERCÍCIO 1 =====
# Gráfico de linhas com taxa de mortalidade e natalidade dos países da América do Norte

paisesDb = pd.read_csv('paises.csv', sep=";", engine="python", skiprows=0)

# Filtrar apenas países da América do Norte
paises_norte_america = paisesDb[paisesDb["Region"].str.contains("NORTHERN AMERICA", case=False, na=False)]

# Converter as taxas para float
deathRate = paises_norte_america["Deathrate"].astype(float)
birthRate = paises_norte_america["Birthrate"].astype(float)
paises_nomes = paises_norte_america["Country"].values

# Criar o gráfico
plt.figure(figsize=(12, 6))
x = np.arange(len(paises_nomes))

plt.plot(x, deathRate, 'r-o', label='Taxa de Mortalidade', linewidth=2)
plt.plot(x, birthRate, 'b--s', label='Taxa de Natalidade', linewidth=2)

plt.xlabel('Países', fontsize=12)
plt.ylabel('Taxa (por 1000 habitantes)', fontsize=12)
plt.title('Taxa de Mortalidade e Natalidade - América do Norte', fontsize=14, fontweight='bold')
plt.xticks(x, paises_nomes, rotation=45, ha='right')
plt.legend(fontsize=10)
plt.grid(True, alpha=0.3)
plt.tight_layout()
plt.show()


# ===== EXERCÍCIO 2 =====
# Gráfico de barras mostrando quantas empresas espaciais diferentes os EUA e a CHINA possuem

# Ler o arquivo space.csv com separador correto (;)
spaceDb = pd.read_csv('space.csv', sep=";", engine="python")

# Filtrar apenas EUA e China e remover duplicatas de empresas
usa_empresas = spaceDb[spaceDb["Location"].str.contains("USA", case=False, na=False)]["Company Name"].unique()
china_empresas = spaceDb[spaceDb["Location"].str.contains("China", case=False, na=False)]["Company Name"].unique()

# Contar empresas únicas
num_empresas = [len(usa_empresas), len(china_empresas)]
paises = ['EUA', 'China']

# Criar o gráfico de barras
plt.figure(figsize=(10, 6))
cores = ['#1f77b4', '#ff7f0e']
barras = plt.bar(paises, num_empresas, color=cores, alpha=0.8, edgecolor='black', linewidth=1.5)

# Adicionar valores nas barras
for barra in barras:
    altura = barra.get_height()
    plt.text(barra.get_x() + barra.get_width()/2., altura,
             f'{int(altura)}',
             ha='center', va='bottom', fontsize=14, fontweight='bold')

plt.xlabel('País', fontsize=12)
plt.ylabel('Número de Empresas Espaciais', fontsize=12)
plt.title('Quantidade de Empresas Espaciais Diferentes - EUA vs China', fontsize=14, fontweight='bold')
plt.grid(True, axis='y', alpha=0.3)
plt.tight_layout()
plt.show()


# ===== EXERCÍCIO 3 =====
# Gráfico de pizza mostrando porcentagem de missões da Roscosmos que deram certo e errado

# Filtrar apenas missões da Roscosmos
roscosmos_missoes = spaceDb[spaceDb["Company Name"].str.contains("Roscosmos", case=False, na=False)]

# Contar missões bem-sucedidas e falhas
status_counts = roscosmos_missoes["Status Mission"].value_counts()

# Criar o gráfico de pizza
plt.figure(figsize=(10, 8))
cores_status = ['#2ecc71', '#e74c3c', '#95a5a6', '#3498db']
explode = tuple([0.05] * len(status_counts))

plt.pie(status_counts.values, 
        labels=status_counts.index,
        autopct='%1.1f%%',
        startangle=90,
        colors=cores_status[:len(status_counts)],
        explode=explode,
        shadow=True,
        textprops={'fontsize': 12, 'fontweight': 'bold'})

plt.title('Status das Missões da Roscosmos', fontsize=14, fontweight='bold', pad=20)
plt.axis('equal')
plt.tight_layout()
plt.show()

print("\n===== ESTATÍSTICAS =====")
print(f"\nExercício 1: {len(paises_nomes)} países da América do Norte analisados")
print(f"\nExercício 2:")
print(f"  - EUA: {len(usa_empresas)} empresas espaciais")
print(f"  - China: {len(china_empresas)} empresas espaciais")
print(f"\nExercício 3: Total de missões da Roscosmos: {len(roscosmos_missoes)}")
print(f"  Distribuição: {status_counts.to_dict()}")