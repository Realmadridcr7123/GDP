from matplotlib import pyplot as plt
import pandas as pd
import seaborn as sns

# 1- Ladda ner ett eller flera dataset som visar BNP, BNP per capita och förväntad livslängd.
# Läs in den första CSV-filen
df1 = pd.read_csv('gdp.csv')

# Läs in den andra CSV-filen
df2 = pd.read_csv('Life-Expectancy-Data.csv')

# Kombinera de två dataframes baserat på gemensamma kolumner
merged_df = pd.merge(df1, df2, left_on=['Country Name', 'Year'], right_on=['Country', 'Year'])

# Ta bort den överflödiga kolumnen 'Country' efter sammanslagningen
merged_df.drop(columns=['Country'], inplace=True)

# Byt namn på kolumnen 'Value' till 'GDP'
merged_df.rename(columns={'Value': 'GDP'}, inplace=True)

# Extrahera önskade kolumner
extracted_df = merged_df[['Country Name', 'Year', 'GDP', 'GDP_per_capita', 'Life_expectancy']]

# Spara den extraherade dataframen till en ny CSV-fil
extracted_df.to_csv('extracted_data.csv', index=False)

# 2- Visa förhållandet mellan förväntad livslängd och BNP per capita
plt.figure(figsize=(10, 6))
sns.scatterplot(data=extracted_df, x='GDP_per_capita', y='Life_expectancy', hue='Year', palette='viridis', alpha=0.8)
plt.title('Förväntad livslängd vs BNP per capita')
plt.xlabel('BNP per capita (USD)')
plt.ylabel('Förväntad livslängd (år)')
plt.legend(title='År', bbox_to_anchor=(1.05, 1), loc='upper left')
plt.grid(True)
plt.tight_layout()
plt.show()

# 3- Resonera kort om resultaten och överväga bakgrunden till resultaten.
"""
Resultaten av visualiseringen visar ett förväntat samband mellan BNP per capita och förväntad livslängd, 
vilket stämmer överens med förväntningarna och tidigare forskning inom området. Generellt sett tenderar länder med 
högre BNP per capita att ha högre förväntad livslängd.

Det finns flera skäl till detta samband:

1. **Bättre tillgång till sjukvård**: Länder med högre BNP per capita har vanligtvis bättre utvecklade 
sjukvårdssystem, vilket leder till förbättrad tillgänglighet till medicinsk vård, vaccinationer och behandling av sjukdomar.

2. **Bättre levnadsstandard**: En högre BNP per capita kan indikera en högre levnadsstandard för invånarna 
i ett land, inklusive bättre bostäder, tillgång till rent vatten och sanitet, vilket minskar risken för sjukdom 
och förbättrar hälsan.

3. **Bättre utbildning och kunskap**: Länder med högre BNP per capita har vanligtvis bättre utbildningssystem 
och tillgång till kunskap och information om hälsosamma levnadsvanor, vilket kan leda till längre och friskare liv.

Det är dock viktigt att komma ihåg att sambandet mellan BNP per capita och förväntad livslängd inte är helt orsakssamband 
och att det finns många andra faktorer som kan påverka hälsoutkomster i ett land, som sociala 
och ekonomiska ojämlikheter, tillgång till rent vatten och sanitet samt miljöfaktorer.
"""

# 4- Gjorde du någon datarengöring? Förklara vad du har gjort och varför.
"""
Dataintegration:
Jag hade två dataset - ett om BNP och ett om förväntad livslängd. För att förstå båda sammanslog jag dem 
baserat på gemensamma faktorer som land och år.

Borttagning av redundans:
Efter sammanslagningen märkte jag att ett dataset hade en överflödig kolumn som hette 'Country'. Jag tog bort den 
eftersom den bara tog upp plats.

Standardisering av kolumnnamn:
I ett dataset fanns en kolumn som hette 'Value', vilket inte var särskilt beskrivande. Så, jag ändrade dess namn 
till 'GDP' för att tydliggöra vad den representerar.

Val av funktion:
Inte varje kolumn var nödvändig för vad jag ville analysera. Jag behöll bara de viktiga som landets namn, år, BNP, 
BNP per capita och förväntad livslängd. Mindre röra, bättre fokus!

Datapreservation:
Slutligen sparade jag det rena datasetet som 'extracted_data.csv' så att vi enkelt kan hänvisa till det senare.

Varje av dessa steg bidrar till att säkerställa att data är korrekt formatterad, konsistent och redo för analys,
vilket i slutändan förbättrar tillförlitligheten och noggrannheten hos de insikter som dras från den.
"""

# 5- Vilka länder har en förväntad livslängd en standardavvikelse över medelvärdet?

# Beräkna medelvärdet och standardavvikelsen för förväntad livslängd
mean_life_expectancy = extracted_df['Life_expectancy'].mean()
std_dev_life_expectancy = extracted_df['Life_expectancy'].std()

# Hitta tröskeln för en standardavvikelse över medelvärdet
threshold = mean_life_expectancy + std_dev_life_expectancy

# Filtrera länder med förväntad livslängd över tröskeln
countries_above_threshold = extracted_df[extracted_df['Life_expectancy'] > threshold]

# Ta bort dubbla länder för att säkerställa att varje land endast visas en gång
unique_countries = countries_above_threshold.drop_duplicates(subset=['Country Name'])

# Skriv ut länderna
print("Länder med en förväntad livslängd en standardavvikelse över medelvärdet:")
print(unique_countries['Country Name'])

# Visa plottarna
plt.show()
