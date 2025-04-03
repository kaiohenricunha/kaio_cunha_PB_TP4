def dfs(graph, start, visited=None, order=None):
    """
    Realiza a busca em profundidade (DFS) em um grafo a partir do nó inicial.

    Parâmetros:
    - graph: dicionário que representa a lista de adjacência do grafo.
    - start: nó inicial para iniciar a DFS.
    - visited: conjunto de nós já visitados (usado na recursão).
    - order: lista que armazena a ordem de visita dos nós.

    Retorna:
    - Uma lista com a ordem em que os nós foram visitados.
    """
    if visited is None:
        visited = set()
    if order is None:
        order = []
    
    visited.add(start)
    order.append(start)
    
    for neighbor in graph.get(start, []):
        if neighbor not in visited:
            dfs(graph, neighbor, visited, order)
    
    return order

# Exemplo de uso:
if __name__ == "__main__":
    # Define um grafo usando lista de adjacência
    grafo = {
        'A': ['B', 'C'],
        'B': ['A', 'D', 'E'],
        'C': ['A', 'F'],
        'D': ['B'],
        'E': ['B', 'F'],
        'F': ['C', 'E']
    }
    
    ordem_visita = dfs(grafo, 'A')
    print("Ordem de visita usando DFS:", ordem_visita)
