#imports
import json
import pandas as pd
from tqdm import *
import pickle
import networkx as nx

# Extraindo dados dos json e colocando em dataframe pandas
contador = 0
lista_slices = []
# Quantidade de slices que serão utilizados, 1 slice são 1000 playlists
pegar_quant_slices = 1

while(True):

    with open("data\mpd.slice."+str(contador)+"-"+str(contador+999)+".json") as json_file:
        data = json.load(json_file)
        lista_slices.append(data)
    print("data\mpd.slice."+str(contador)+"-"+str(contador+999)+".json")
    contador += 1000
    if(contador == pegar_quant_slices*1000):
        break


df_resultado = pd.DataFrame()

# Extraindo dados de playlists, cada música terá uma linha no dataframe, contendo o nome do artista, o ID da playlist e a posição da música na playlist
lista_colunas = ['pid']

for slice in lista_slices:
    print("Coletando dados slice:",lista_slices.index(slice)+1)
    pbar = tqdm(total = len(slice["playlists"]))
    for playlist in slice["playlists"]:
        pbar.update(1)
        # dataframe com as musicas da playlist
        df_tracks = pd.DataFrame(playlist["tracks"])
        for coluna in lista_colunas:
            df_tracks[coluna] = playlist[coluna]
        df_resultado = pd.concat([df_resultado,df_tracks ], ignore_index=True)
    pbar.close()

df_resultado = df_resultado[["artist_name","pid","pos"]]
# Salvando dataframe em arquivo pickle
pickle.dump(df_resultado, open("df_resultado.p", "wb"))


# CRIANDO GRAFO -------------------------------------------------------------------------------------------------- 
# Caso já tenha salvo o dataframe df_resultado de uma execução anterior descomente a linha a seguir e comece daqui
# df_resultado = pickle.load( open( "df_resultado.p", "rb") )

# cria grafo
G = nx.Graph()

print("Adicionando nós")
# Adiciona Nodes
lista_artistas = df_resultado["artist_name"].unique()

pbar = tqdm(total = len(lista_artistas))
for nome_artista in lista_artistas:
    G.add_node(nome_artista)
    pbar.update(1)
pbar.close()

# Adiciona Arestas, demora um bom tempo
print("Adicionando arestas")
df_resultado.sort_values(by=['pid'], inplace=True)
lista_playlists_ids = df_resultado.pid.unique()

pbar = tqdm(total = len(lista_playlists_ids))
for pid in lista_playlists_ids:
    df_pid = df_resultado[df_resultado.pid == pid]
    df_pid = pd.merge(df_pid,df_pid,on='pid',how='outer')
    for index,row in df_pid.iterrows():
        if(row["pos_x"] == row["pos_y"] ):
            continue

        no1 = row['artist_name_x']
        no2 = row['artist_name_y']
        
        # O peso será incrementado caso aquela aresta já exista, caso não exista será criada com valor 1 para o peso
        if( G.has_edge(no1,no2)):
            G.edges[no1,no2]['weight']+=1
        else:
            G.add_edge(no1,no2,weight = 1)
      
    pbar.update(1)

pbar.close()

# Export to graphml
nx.write_graphml(G, 'spotfy.graphml')
print("sucesso!")
