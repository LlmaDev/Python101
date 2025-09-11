#!/usr/bin/env python3
import pandas as pd
import numpy as np

def main():
    seriesYear1 = pd.Series({"Java": 16.25, "C": 16.04, "Python": 9.85})
    seriesYear2 = pd.Series({"C": 16.21, "Python": 12.12, "Java": 11.68})

    print("\nYear1:\n", seriesYear1)
    print("\nYear2:\n", seriesYear2)
    print()

    print("No primeiro ano a porcentagem total que elas juntas representam no mercado: "
          f"{seriesYear1.sum():.2f}%")
    print("No segundo ano a porcentagem total que elas juntas representam no mercado: "
          f"{seriesYear2.sum():.2f}%")
    print()

    diff_pp = seriesYear2 - seriesYear1
    diff_rel = (seriesYear2 - seriesYear1) / seriesYear1 * 100

    for lang in diff_pp.index:
        print(f"{lang}: Δ (p.p.) = {diff_pp[lang]:.2f}  |  Δ (%) = {diff_rel[lang]:.2f}%")
    print()

    positive_growth = diff_pp[diff_pp > 0]
    print("Linguagens com crescimento (apenas valores positivos, em p.p.):")
    for lang, val in positive_growth.items():
        print(f"- {lang}: {val:.2f} p.p. ({diff_rel[lang]:.2f}%)")
    print()

    projected_year4 = seriesYear2 + 2 * diff_pp  

    print("Projeção se o mesmo Δ (p.p.) se mantiver pelos próximos 2 anos:")
    print(projected_year4.apply(lambda x: f"{x:.2f}%").to_string())
    most_popular_after_2 = projected_year4.nlargest(1)
    label = most_popular_after_2.index[0]
    value = most_popular_after_2.iloc[0]
    print(f"\nLinguagem mais popular após 2 anos (projeção): {label} com {value:.2f}%")
    print()

    df = pd.DataFrame({
        "X": [10, 25, 35, 20, 28],
        "Y": [5, 15, 25, 30, 40],
        "Z": [100, 80, 60, 40, 20]
    }, index=["A", "B", "C", "D", "E"])

    print("DataFrame de exemplo:\n", df, "\n")
    mean_x_lt_30 = df.loc[df["X"] < 30, "X"].mean()
    print(f"Q6) Média dos elementos da coluna X que são < 30: {mean_x_lt_30:.2f}")

    mean_row_D = df.loc["D"].mean()       
    sum_row_E = df.iloc[4].sum()          
    print(f"Q7) Média da linha D (loc): {mean_row_D:.2f}")
    print(f"Q7) Soma da linha E (iloc): {sum_row_E:.2f}")

    slice_ACE_XY = df.loc[["A", "C", "E"], ["X", "Y"]]
    sum_per_row = slice_ACE_XY.sum(axis=1)
    sum_per_col = slice_ACE_XY.sum(axis=0)

    print("\nQ8) Slice (linhas A, C, E e colunas X, Y):\n", slice_ACE_XY)
    print("\nSoma por linha:\n", sum_per_row.to_string(formatter=lambda x: f"{x:.2f}"))
    print("\nSoma por coluna:\n", sum_per_col.to_string(formatter=lambda x: f"{x:.2f}"))

if __name__ == "__main__":
    main()
