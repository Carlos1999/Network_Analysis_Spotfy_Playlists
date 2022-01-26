# :notes:Estudo da Rede de Coocorrência de Playlists do Spotify 



## :mag: Introdução 

Tal postagem é referente ao trabalho da segunda unidade da disciplina de Análise de Redes (**IMD1155)** da Universidade Federal do Rio Grande do Norte.

Nesse repositório, estaremos realizando um estudo da rede de coocorrência formada por artistas presentes em playlists do Spotify, utilizando como base dados fornecidos em 2018 pelo próprio Spotify no [The Spotify Million Playlist Dataset Challenge](https://www.aicrowd.com/challenges/spotify-million-playlist-dataset-challenge).

![img](https://miro.medium.com/max/700/1*ekbwn2Eirwzyv6nuUB-KWA.png)

Esse *dataset* (Conjunto de dados) disponibilizava dados de um milhão de playlists, criadas por usuários, para que fossem desenvolvidos modelos de *machine learning* capazes de completar as playlists de forma automática.

No nosso caso, os dados foram utilizados para criar uma rede que tem como nós os artistas presentes nas playlists e as arestas são criadas observando quais artistas estão presentes na mesma playlist.

Por exemplo, imagine uma playlist com os seguintes artistas:

- Annita
- Annita
- Alok
- Justin Bieber

A rede formada a partir dela seria:



![img](https://miro.medium.com/max/487/1*h2pVRe5223i7blf1FCL60w.png)

Exemplo de grafo

Desse modo foi gerado o grafo utilizando uma parte do *dataset* (Com apenas 500 artistas) fornecido com o objetivo de realizar análises sobre a disposição da rede através de grandezas conhecidas, criando gráficos e exibindo os nós com valores mais importantes.

Algumas métricas foram utilizadas para a realização da análise. As métricas globais foram: *Eccentriciy, periphery, radius* e *Center.*

No que diz respeito ao ranqueamento dos nós (*Node Ranking*) as métricas estudadas foram: *Degree centrality, closeness centrality, Betweenness Centrality* e *EigenVector centrality.*

Além disso, foram feitas uma análise bivariada (PDF e CDF) , uma análise multivariada e uma análise da decomposição da rede.



Para ver a rede de forma interativa clique [aqui](https://carlos1999.github.io/Network_Analysis_Spotify_Playlists/network/).



## :hammer_and_wrench: As principais tecnologias utilizadas foram:

- Python;
- Google colaboratory;
- Networkx;
- Gephi.



## :large_blue_diamond: Passo a passo para reprodução



Caso queira modificar a amostra utilizada para a criação do grafo:

* Baixe o [DataSet](https://www.aicrowd.com/challenges/spotify-million-playlist-dataset-challenge/dataset_files) e extraia a pasta **data** para dentro do repositório; 

* abra o arquivo **Cria_grafo.py** e modifique a variável `pegar_quant_slices` para a quantidade de slices que você irá utilizar do dataframe, cada slice possui 1000 playlists;
* Execute o arquivo **Cria_grafo.py** e aguarde o termino da execução.

Caso queira utilizar os dados já gerados ou caso já tenha executado os passos anteriores basta executar as células do notebook **Análise Grafo Spotify.ipynb** na ordem, de cima pra baixa, para utilizar o grafo gerado anteriormente e visualizar o estudo.



## :man_technologist: Autores do Projeto

* Carlos Vinícius dos Santos ([@Carlos1999](https://github.com/carlos1999))

* Hugo Felipe dos Santos ([@hugofsantos](https://github.com/hugofsantos))

  

## :question: Sobre o Projeto

Projeto criado para a disciplina de Análise de Redes (IMD1155), ministrada pelo professor [@ivanovitchm](https://github.com/ivanovitchm), do **Instituto Metrópole Digital - UFRN**, curso de Bacharelado em Tecnologia da Informação.