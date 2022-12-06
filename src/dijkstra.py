from math import inf
from src.grafo import Grafo


def dijkstra(grafo: Grafo, estado_partida):
    vertices_nao_visitados = list(grafo.get_vertices())

    menor_caminho = {}
    estados_do_caminho = {}

    # Inicializa todos os nós não visitados com valor infinito.
    for node in vertices_nao_visitados:
        menor_caminho[node] = inf
    # O nó inicial começa com o valor 0
    menor_caminho[estado_partida] = 0

    while vertices_nao_visitados:
        menor_vertice_atual = None
        # Encontrar o vértice com o menor peso
        for node in vertices_nao_visitados:
            if menor_vertice_atual is None:
                menor_vertice_atual = node
            elif menor_caminho[node] < menor_caminho[menor_vertice_atual]:
                menor_vertice_atual = node

        # Atualiza os valores das distâncias entre um nó e outro
        vizinhos_vertice_atual = grafo.get_vizinhos(menor_vertice_atual)
        for vizinho in vizinhos_vertice_atual:
            peso_temporario = menor_caminho[menor_vertice_atual] + grafo.peso_aresta(menor_vertice_atual, vizinho)
            if peso_temporario < menor_caminho[vizinho]:
                menor_caminho[vizinho] = peso_temporario
                # Atualiza o melhor caminho para o nó sendo visitado
                estados_do_caminho[vizinho] = menor_vertice_atual

        vertices_nao_visitados.remove(menor_vertice_atual)
    return estados_do_caminho, menor_caminho
