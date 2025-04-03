from collections import deque

def bfs(graph, start):
    """
    Realiza a busca em largura (BFS) em um grafo a partir do nó inicial.

    Parâmetros:
    - graph: dicionário que representa a lista de adjacência do grafo.
    - start: nó inicial para iniciar a BFS.

    Retorna:
    - Uma lista com a ordem em que os nós foram visitados.
    """
    visited = set()           # Conjunto para rastrear nós visitados
    order = []                # Lista para armazenar a ordem de visita
    queue = deque([start])    # Fila para gerenciar os nós a serem visitados

    visited.add(start)
    
    while queue:
        vertex = queue.popleft()
        order.append(vertex)
        
        # Percorre todos os vizinhos do nó atual
        for neighbor in graph.get(vertex, []):
            if neighbor not in visited:
                visited.add(neighbor)
                queue.append(neighbor)
                
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
    
    ordem_visita = bfs(grafo, 'A')
    print("Ordem de visita usando BFS:", ordem_visita)
