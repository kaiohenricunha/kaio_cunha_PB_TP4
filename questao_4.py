def sift_down(heap, i, n):
    """Ajusta o nó de índice 'i' para baixo na heap."""
    smallest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and heap[left] < heap[smallest]:
        smallest = left
    if right < n and heap[right] < heap[smallest]:
        smallest = right

    if smallest != i:
        heap[i], heap[smallest] = heap[smallest], heap[i]
        sift_down(heap, smallest, n)

def build_heap(arr):
    """Transforma a lista 'arr' em uma min-heap in-place."""
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        sift_down(arr, i, n)
    return arr

def sift_up(heap, i):
    """Ajusta o nó de índice 'i' para cima na heap, mantendo a propriedade de min-heap."""
    while i > 0:
        parent = (i - 1) // 2
        if heap[i] < heap[parent]:
            heap[i], heap[parent] = heap[parent], heap[i]
            i = parent
        else:
            break

def insert_heap(heap, element):
    """Insere um novo elemento na heap, mantendo a propriedade de min-heap."""
    print("Heap antes da inserção:", heap)
    heap.append(element)
    sift_up(heap, len(heap) - 1)
    print("Heap após a inserção:", heap)
    return heap

def remove_min(heap):
    """
    Remove o elemento raiz (menor elemento) da min-heap e reestrutura a heap.
    Exibe o estado da heap antes e depois da remoção.
    """
    if not heap:
        print("Heap vazia!")
        return None
    
    print("Heap antes da remoção:", heap)
    min_elem = heap[0]
    heap[0] = heap[-1]
    heap.pop()
    if heap:
        sift_down(heap, 0, len(heap))
    print("Heap após a remoção:", heap)
    return min_elem

# Exemplo de uso
if __name__ == "__main__":
    # Considere a lista inicial
    lista = [5, 2, 3, 7, 1]
    
    # 1. Cria a min-heap (a raiz será o menor elemento: 1)
    heap = build_heap(lista.copy())
    print("Heap construída:", heap)
    
    # 2. Insere o valor 0, que deve se tornar a nova raiz
    insert_heap(heap, 0)
    
    # 3. Busca o elemento 7 na heap
    def search_heap(heap, target, i=0):
        """
        Busca recursivamente por 'target' na heap utilizando a propriedade de min-heap.
        Se o nó atual for maior que target, a busca é podada nessa subárvore.
        """
        if i >= len(heap):
            return False
        if heap[i] > target:
            return False
        if heap[i] == target:
            return True
        return search_heap(heap, target, 2 * i + 1) or search_heap(heap, target, 2 * i + 2)
    
    print("Elemento 7 encontrado?", search_heap(heap, 7))
    
    # 4. Remove o menor elemento (0) e reestrutura a heap
    remove_min(heap)
