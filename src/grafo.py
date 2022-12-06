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


# Distância entre as capitais em km/1000
adjacencias = {
    "AC": {"AM": 1.44, "RO": 0.54},
    "AM": {"RO": 0.9, "MT": 2.35, "PA": 5.29, "RR": 0.78},
    "RO": {"MT": 1.45},
    "RR": {"PA": 6.08},
    "PA": {"TO": 1.28, "MT": 2.94, "AP": 1.91, "MA": 0.8},
    "TO": {"PI": 1.4, "MT": 1.78, "BA": 1.45, "GO": 0.87, "MA": 1.38},
    "MA": {"PI": 0.44},
    "PI": {"PE": 1.13, "BA": 1.16, "CE": 0.63},
    "BA": {"PE": 0.83, "MG": 1.37, "GO": 1.64, "ES": 1.2, "SE": 0.35, "AL": 0.63},
    "CE": {"PE": 0.8, "PB": 0.68, "RN": 0.53},
    "RN": {"PB": 0.18},
    "PB": {"PE": 0.12},
    "PE": {"AL": 0.28},
    "AL": {"SE": 0.29},
    "SE": {},  # já teve todos os seus vizinhos anotados anteriormente
    "MT": {"GO": 0.93, "MS": 0.69},
    "GO": {"DF": 0.2, "MS": 0.93, "MG": 0.9},
    "DF": {"MG": 0.71},
    "MS": {"MG": 1.45, "SP": 1.01, "PR": 0.99},
    "MG": {"SP": 0.58, "ES": 0.52, "RJ": 0.43},
    "ES": {"RJ": 0.52},
    "RJ": {"SP": 0.42},
    "SP": {"PR": 0.40},
    "PR": {"SC": 0.70},
    "SC": {"RS": 0.47},
    "RS": {},  # já teve todos os seus vizinhos anotados anteriormente
}

siglas = ['AC', 'AM', 'RO', 'RR', 'PA', 'AP', 'TO', 'MA', 'PI', 'BA', 'CE', 'RN', 'PB',
          'PE', 'AL', 'SE', 'MT', 'GO', 'MS', 'DF', 'MG', 'ES', 'SP', 'RJ', 'PR', 'SC', 'RS']


if __name__ == '__main__':
    grafo = Grafo(siglas, adjacencias)

