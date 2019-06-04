import numpy as np
import pandas as pd
import matplotlib.pyplot as plot
import seaborn as sns

# Extracción de datos

directorio = './smashito/'

personajes = pd.read_csv(directorio + 'personajes.csv')
personajes_SSB4 = pd.read_csv(directorio + 'personajes-ssb4.csv')

personajes_smashito = pd.DataFrame(personajes['SSB']).count()
personajes_smashito_melee = pd.DataFrame(personajes['Melee']).count()
personajes_smashito_brawl = pd.DataFrame(personajes['Brawl']).count()
personajes_smashito_4 = pd.DataFrame(personajes['SSB4']).count()
personajes_smashito_ultimate = pd.DataFrame(personajes['Ult.']).count()
aumento_personajes = (personajes_smashito_ultimate[0] - personajes_smashito[0])*personajes['Fighter'].count()/100

# Total de personajes 

print(f"A lo largo de los años, el numero de personajes a aumentado de {personajes['SSB'].count()} a {personajes['Ult.'].count()} personajes. Aumentando estos en un {aumento_personajes}%")

# Numero de personajes por juego

juegos = ['SSB', 'Melee', 'Brawl', 'SSB4', 'Ult.']
numero_personajes_por_juego = [personajes_smashito[0], personajes_smashito_melee[0], personajes_smashito_brawl[0], personajes_smashito_4[0], personajes_smashito_ultimate[0]]

plot.figure(1)
plot.bar(juegos, numero_personajes_por_juego)
plot.xticks(rotation=90)
plot.xlabel('Juegos')
plot.ylabel('No. de personajes por juego')
plot.title('Personajes por juego')

# Cantidad de personajes por universo

universos = personajes['Universe'].unique()
numero_personajes_por_universo = np.zeros(universos.size)

for indice, universo in enumerate(universos):
    numero_personajes_por_universo[indice] = personajes[personajes['Universe'] == universo].Fighter.count()

plot.figure(2)
plot.bar(universos, numero_personajes_por_universo)
plot.xticks(rotation=90)
plot.xlabel('Universos')
plot.ylabel('No. de personajes por universo')
plot.title('Personajes por universo')

# Porcentaje de personajes por genero

generos = personajes['Gender'].unique()
porcentaje_personajes_por_genero = np.zeros(generos.size)

for indice, genero in enumerate(generos):
    porcentaje_personajes_por_genero[indice] = (personajes[personajes['Gender'] == genero].Fighter.count()*personajes['Fighter'].count())/100

plot.figure(3)
plot.pie(porcentaje_personajes_por_genero, 
         labels = generos, 
         autopct="%1.2f%%")
plot.title('Porcentaje de personajes por genero')

# Aparicion de personajes

personajes['Count'] = personajes.count(axis=1) - 3 # Se resta 3 que corresponden a las columnas 'Fighter', 'Universe' y 'Gender'

print('Lista de personajes antiguos:')
personajes_antiguos = personajes.sort_values(ascending = False, by = 'Count').query('Count == 5')
print(personajes_antiguos.loc[:, ['Fighter']])

plot.figure(figsize = (11, 8))
# grafica_personajes_antiguos = sns.boxplot(x = 'Fighter', y = 'Count', data = personajes)

print('Lista de personajes nuevos:')
personajes_nuevos = personajes.sort_values(ascending = False, by = 'Count').query('Count == 1')
print(personajes_nuevos.loc[:, ['Fighter']])

# Ofensiva vs Defensiva de los personajes más usados 
plot.figure(figsize = (5, 5))
plot.xticks(rotation = 90)
sns.barplot(x = 'Characters', y = 'Defense', hue = 'Offense', data = personajes_SSB4[:20].groupby(['Characters', 'Offense']).sum().reset_index()).set_title('Defensiva vs Ofensiva')