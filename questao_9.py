def build_graph(edges, directed=False):
    """
    Constrói um grafo a partir de uma lista de arestas.
    
    Parâmetros:
    - edges: lista de tuplas representando as arestas, ex.: [("A", "B"), ("B", "C")].
    - directed: Booleano que indica se o grafo é direcionado. Padrão é False (não direcionado).
    
    Retorna:
    - Um dicionário representando a lista de adjacência do grafo.
    """
    graph = {}
    for u, v in edges:
        if u not in graph:
            graph[u] = []
        if v not in graph:
            graph[v] = []
        graph[u].append(v)
        if not directed:
            graph[v].append(u)
    return graph

# Exemplo de uso:
if __name__ == "__main__":
    arestas = [("A", "B"), ("A", "C"), ("B", "D"), ("C", "D"), ("D", "E")]
    
    # Constrói um grafo não-orientado
    grafo = build_graph(arestas, directed=False)
    print("Grafo (não-orientado) - Lista de adjacência:")
    for vertice, vizinhos in grafo.items():
        print(f"{vertice}: {vizinhos}")
    
    # Se preferir um grafo orientado, basta definir directed=True
    grafo_orientado = build_graph(arestas, directed=True)
    print("\nGrafo orientado - Lista de adjacência:")
    for vertice, vizinhos in grafo_orientado.items():
        print(f"{vertice}: {vizinhos}")
