'''
Questão 1
Faça um slicing no dataset para mostrar apenas o País (Country), Região
(Region), População (Population) e Area (Area (sq. mi.)) dos países contidos
nele;
Questão 2
Conte e em seguida mostre quais são as diferentes Regiões do planeta segundo
este dataset;
Questão 3
Mostre qual a taxa média de alfabetização (Literacy (%)) do planeta segundo
este dataset;
Questão 4
Conte quantos países são da América do Norte (NORTHERN AMERICA)
segundo este dataset;
Questão 5
Encontre qual país da América do Sul e Caribe (LATIN AMER. & CARIB)
possui a maior renda per capita (GDP ($ per capita));
'''

import numpy as np;

##Slicing the csv

df = np.loadtxt("paises.csv", delimiter = ';', dtype=str, encoding='utf-8');
print("Dados sliced: \n");
print(df, "\n");

##Regioes
print("Regiãããããão: ");
regions = df[:, 1];
print(regions, "\n");

##Literacy mean
LiteraMean = df[1:,9].astype(float);
##LiteraMean = LiteraMean.astype(float);
print("Media Alfabetizados: ",LiteraMean.mean(),"\n")

##Behind the Wall Country
northAmercia = (df[1:,1]);
print(np.sum(northAmercia == "NORTHERN AMERICA                   "));
# print(northAmercia);

##América do Sul e Caribe (LATIN AMER. & CARIB)
foodAndBeachesCountries = (df[1:,1]=="LATIN AMER. & CARIB    ");
foodAndBeachesCountriesGDP = (df[1:,8].astype(float))
print(foodAndBeachesCountriesGDP.max());
print(foodAndBeachesCountries == "LATIN AMER. & CARIB    " and foodAndBeachesCountriesGDP.max() );
print(foodAndBeachesCountries)
# possui a maior renda per capita (GDP ($ per capita));


