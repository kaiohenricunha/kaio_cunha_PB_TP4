from collections import deque

def find_path_bfs(graph, start, end):
    """
    Encontra um caminho entre 'start' e 'end' usando Breadth-First Search (BFS).

    Parâmetros:
    - graph: dicionário representando a lista de adjacência do grafo.
    - start: nó de partida.
    - end: nó de destino.

    Retorna:
    - Uma lista com o caminho encontrado de 'start' até 'end', ou None se não existir.
    """
    # Inicializa a fila com uma tupla contendo o nó de partida e o caminho até ele (inicialmente, só [start])
    queue = deque([(start, [start])])
    visited = {start}  # Conjunto para rastrear os nós já visitados

    while queue:
        current, path = queue.popleft()
        
        # Se o nó atual for o destino, retorna o caminho percorrido
        if current == end:
            return path
        
        # Explora os vizinhos do nó atual
        for neighbor in graph.get(current, []):
            if neighbor not in visited:
                visited.add(neighbor)
                # Adiciona o vizinho na fila com o caminho atualizado
                queue.append((neighbor, path + [neighbor]))
                
    return None  # Retorna None se nenhum caminho for encontrado

# Exemplo de uso:
if __name__ == "__main__":
    # Define um grafo não-orientado usando lista de adjacência
    graph = {
        'A': ['B', 'C'],
        'B': ['A', 'D'],
        'C': ['A', 'D'],
        'D': ['B', 'C', 'E'],
        'E': ['D']
    }
    
    start_node = 'A'
    end_node = 'E'
    path = find_path_bfs(graph, start_node, end_node)
    
    if path:
        print("Caminho encontrado de {} até {}:".format(start_node, end_node), " -> ".join(path))
    else:
        print("Nenhum caminho encontrado entre {} e {}".format(start_node, end_node))
