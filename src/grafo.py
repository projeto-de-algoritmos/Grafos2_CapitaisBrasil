from math import inf


class Grafo(object):
    """ Implementação da estrutura de um grafo. """

    def __init__(self, nodes, lista_adj):
        self.vertices = nodes
        self.grafo = self.monta_grafo(nodes, lista_adj)

    def monta_grafo(self, nodes, lista_adj):
        """
        Constrói a estrutura do grafo, com base nos vértices e a
        lista de adjacências.
        """

        grafo = {}
        for node in nodes:
            grafo[node] = {}

        grafo.update(lista_adj)

        # garantindo que a aresta terá o mesmo peso nos dois sentidos
        for node, arestas in grafo.items():
            for node_vizinho, peso in arestas.items():
                if not grafo[node_vizinho].get(node, False):
                    grafo[node_vizinho][node] = peso

        return grafo

    def get_vertices(self):
        """ Retorna os nós do grafo. """
        return self.vertices

    def get_vizinhos(self, node):
        """ Retorna os vizinhos de um nó. """

        vizinhos = []
        for node_vizinho in self.vertices:
            if self.grafo[node].get(node_vizinho, False) != False:
                vizinhos.append(node_vizinho)
        return vizinhos

    def peso_aresta(self, node1, node2):
        """ Retorna o valor de uma aresta entre dois nós. """
        return self.grafo[node1][node2]


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


def mensagem(nos_do_caminho, menor_caminho, estado_partida, estado_chegada):
    estados = {
        'AC': 'Acre', 'AL': 'Alagoas', 'AM': 'Amazonas', 'AP': 'Amapá',
        'BA': 'Bahia', 'CE': 'Ceará', 'DF': 'Distrito Federal', 'ES': 'Espírito Santo',
        'GO': 'Goiás', 'MA': 'Maranhão', 'MG': 'Minas Gerais', 'MS': 'Mato Grosso do Sul',
        'MT': 'Mato Grosso', 'PA': 'Pará', 'PB': 'Paraíba', 'PE': 'Pernambuco', 'PI': 'Piauí',
        'PR': 'Paraná', 'RJ': 'Rio de Janeiro', 'RN': 'Rio Grande do Norte', 'RO': 'Rondônia',
        'RR': 'Roraima', 'RS': 'Rio Grande do Sul', 'SC': 'Santa Catarina', 'SE': 'Sergipe',
        'SP': 'São Paulo', 'TO': 'Tocantins'
    }

    caminho = []
    node = estado_chegada
    while node != estado_partida:
        caminho.append(node)
        node = nos_do_caminho[node]

    # Adicionando o nó (estado) inicial manualmente ao final da lista
    caminho.append(estado_partida)

    estado = [estados[i] for i in caminho]
    print(f"A menor distância entre as capitais de {estado[-1]} e {estado[0]} é: {menor_caminho[estado_chegada]} km.")
    print(" -> ".join(reversed(estado)))


if __name__ == '__main__':

    adjacencias = {
        "AC": {"AM": 2, "RO": 3},
        "AM": {"RO": 9, "MT": 6},
        "RO": {"AM": 5, "MT": 1, "AC": 4, "PR": 5},
        "MT": {"TO": 5, "RO": 4, "GO": 2, "PA": 1, "MA": 8, "MS": 1},
        "MA": {"TO": 5, "PA": 3, "PI": 1, "PR": 4},
        "PR": {"SP": 1, "SC": 2, "MS": 4},
        "RR": {"AM": 5, "PA": 1},
        "RN": {"CE": 2, "PB": 2},
        "SC": {"RS": 3, "PR": 2},
        "RS": {"SC": 5},
    }

    estados = ['AC', 'AM', 'RO', 'RR', 'PA', 'AP', 'TO', 'MA', 'PI', 'BA', 'CE', 'RN', 'PB', 'PE', 'AL', 'SE', 'MT',
    'GO', 'MS', 'DF', 'MG', 'ES', 'SP', 'RJ', 'PR', 'SC', 'RS']

    grafo = Grafo(estados, adjacencias)

    estados_do_caminho, menor_caminho = dijkstra(grafo=grafo, estado_partida="AC")

    mensagem(estados_do_caminho, menor_caminho, estado_partida="AC", estado_chegada="MS")
