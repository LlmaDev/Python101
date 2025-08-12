"""
2) Crie dois conjuntos, um para cada loja. Identifique quais modelos de smartphones cada uma delas vendem. 
Em seguida, mostre quais modelos no total você terá opção de comprar se visitá-las e quais modelos no total 
você terá opção de comprar se visitá-las e quais modelos se encontram disponíveis em ambas as lojas;
"""

lojaSmartOne = {
    "Samsung Galaxy S24 Ultra",
    "Xiaomi 14 Pro",
    "Motorola Edge 50 Ultra",
    "OnePlus 12",
    "Google Pixel 8 Pro",
    "Oppo Find X7 Pro",
    "Asus ROG Phone 8",
     "iPhone 15 Pro",
    "iPhone 15 Plus",
    "iPhone 15"
}

lojaJunaCell = {
    "iPhone 15 Pro Max",
    "iPhone 15 Pro",
    "iPhone 15 Plus",
    "iPhone 15",
    "Xiaomi 14 Pro",
    "Motorola Edge 50 Ultra",
    "OnePlus 12",
    "Google Pixel 8 Pro",
    "iPhone 14 Pro Max",
    "iPhone 14 Pro",
    "iPhone 14 Plus",
    "iPhone 14",
    "iPhone SE (3ª geração)",
    "iPhone 13 Mini"
}

print("\n\nSe visitar ambas as lojas você terá ", len(lojaSmartOne)+len(lojaJunaCell), " modelos para comprar.")
print("\n Sendo os modelos da Loja Smart One: \n", lojaSmartOne)
print("\n E os modelos da loja Juna Cell: \n", lojaJunaCell)

print("\nSendo que os modelos: " , lojaSmartOne&lojaJunaCell, " ambas as lojas possuem.")
