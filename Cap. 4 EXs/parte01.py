import numpy as np

# =========================
# 1. Arrays unidimensionais
# =========================
arr1 = np.ones(8, dtype=int)
arr2 = np.random.randint(0, 10, 8)
arr3 = arr1 + arr2

print("Array 1:", arr1)
print("Array 2:", arr2)
print("Array Resultante:", arr3)
print("Soma:", arr3.sum())

if arr3.sum() >= 40:
    arr3 = arr3.reshape(4, 2)  # mais linhas que colunas
else:
    arr3 = arr3.reshape(2, 4)  # mais colunas que linhas

print("Array Remodelado:\n", arr3)

# =========================
# 2. Arrays pares
# =========================
arr4 = np.arange(0, 52, 2)
arr5 = np.arange(50, 101, 2)
arr_concat = np.concatenate((arr4, arr5))
arr_sorted = np.sort(arr_concat)

print("Concatenado:", arr_concat)
print("Ordenado:", arr_sorted)

# =========================
# 3. Mini Campo Minado
# =========================
campo = np.zeros((2,2), dtype=int)

# adiciona um 1 em posição aleatória
linha, coluna = np.random.randint(0,2), np.random.randint(0,2)
campo[linha, coluna] = 1

tentativas = 0
achou = False

while tentativas < 3 and not achou:
    print("\nCampo Atual:\n", campo)
    x = int(input("Digite a linha (0 ou 1): "))
    y = int(input("Digite a coluna (0 ou 1): "))
    tentativas += 1

    if campo[x,y] == 1:
        print("💥 Game Over! Você achou a bomba!")
        achou = True

if not achou:
    print("🎉 Congratulations! You beat the game!")
