class UnionFind:
    def __init__(self, n):

        self.pai = list(range(n))
        self.rank = [0] * n

    def find(self, x):
        # Busca
        if self.pai[x] != x:
            self.pai[x] = self.find(self.pai[x])
        return self.pai[x]

    def union(self, a, b):
        # União dos conjuntos
        raiz_a = self.find(a)
        raiz_b = self.find(b)

        if raiz_a == raiz_b:
            return False

        if self.rank[raiz_a] < self.rank[raiz_b]:
            self.pai[raiz_a] = raiz_b
        elif self.rank[raiz_a] > self.rank[raiz_b]:
            self.pai[raiz_b] = raiz_a
        else:
            self.pai[raiz_b] = raiz_a
            self.rank[raiz_a] += 1

        return True



while True:
    # Entrada
    n, m = map(int, input().split())

    if n == 0 and m == 0:
        break

    # Modelagem da lista de adjacência
    lista_adjacencia = [[] for i in range(n)]

    # Lista de arestas
    arestas = []

    for i in range(m):
        u, v, peso = map(int, input().split())

        # Grafo não direcionado
        lista_adjacencia[u].append((v, peso))
        lista_adjacencia[v].append((u, peso))

        # Aresta no formato
        arestas.append((peso, u, v))


    arestas.sort()

    uf = UnionFind(n)
    pesadas = []

    for peso, u, v in arestas:
        # Se não conseguir unir, forma ciclo
        if uf.union(u, v) == False:
            pesadas.append(peso)

    if len(pesadas) == 0:
        print("forest")
    else:
        print(" ".join(map(str, pesadas)))