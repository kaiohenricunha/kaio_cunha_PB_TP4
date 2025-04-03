def sift_down(arr, i, n):
    """Ajusta o nó de índice 'i' para baixo na heap."""
    smallest = i
    left = 2 * i + 1
    right = 2 * i + 2

    if left < n and arr[left] < arr[smallest]:
        smallest = left
    if right < n and arr[right] < arr[smallest]:
        smallest = right

    if smallest != i:
        arr[i], arr[smallest] = arr[smallest], arr[i]
        sift_down(arr, smallest, n)

def build_heap(arr):
    """Transforma a lista 'arr' em uma min-heap in-place."""
    n = len(arr)
    for i in range(n // 2 - 1, -1, -1):
        sift_down(arr, i, n)
    return arr

def sift_up(heap, i):
    """Realiza o ajuste para cima (sift-up) para manter a propriedade da heap."""
    while i > 0:
        parent = (i - 1) // 2
        if heap[i] < heap[parent]:
            heap[i], heap[parent] = heap[parent], heap[i]
            i = parent
        else:
            break

def insert_heap(heap, element):
    """
    Insere um novo elemento na heap, mantendo a propriedade de min-heap.
    """
    # Mostra o estado da heap antes da inserção
    print("Heap antes da inserção:", heap)
    
    heap.append(element)
    sift_up(heap, len(heap) - 1)
    
    # Mostra o estado da heap após a inserção
    print("Heap após a inserção:", heap)
    return heap

# Exemplo de uso
if __name__ == "__main__":
    lista = [4, 10, 3, 5, 1]
    # Constrói a heap a partir da lista
    heap = build_heap(lista.copy())
    # Insere um novo elemento, por exemplo, o número 2
    insert_heap(heap, 2)
