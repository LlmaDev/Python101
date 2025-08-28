import numpy as np;
# =========================
# 4. Matriz qualquer
# =========================
matriz = np.random.randint(1, 10, (3,4))  # Exemplo 3x4
linhas, colunas = matriz.shape
num_elem = linhas * colunas

print("Matriz:\n", matriz)
print("Linhas:", linhas, "Colunas:", colunas)
print("Total elementos:", num_elem)
print("Par" if num_elem % 2 == 0 else "Ímpar")

# =========================
# 5. Matriz 4x4
# =========================
np.random.seed(10)
matriz2 = np.random.randint(1, 51, (4,4))
print("\nMatriz 4x4:\n", matriz2)

# a) médias
media_linhas = matriz2.mean(axis=1)
media_colunas = matriz2.mean(axis=0)
print("Média por linha:", media_linhas)
print("Média por coluna:", media_colunas)

# b) maior média
print("Maior média das linhas:", media_linhas.max())
print("Maior média das colunas:", media_colunas.max())

# c) contagem de aparições
unicos, contagem = np.unique(matriz2, return_counts=True)
print("Contagem de aparições:", dict(zip(unicos, contagem)))
print("Números que aparecem 2 vezes:", unicos[contagem==2])
