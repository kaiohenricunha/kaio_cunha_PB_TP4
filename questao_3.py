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

def search_heap(heap, target, i=0):
    """
    Busca recursivamente por 'target' na heap.
    Utiliza a propriedade de min-heap para podar a busca: 
    se o elemento atual é maior que target, nenhum elemento da subárvore pode ser target.
    """
    if i >= len(heap):
        return False

    # Se o nó atual for maior que o target, a subárvore não pode conter target
    if heap[i] > target:
        return False

    # Se encontrou o target, retorna True
    if heap[i] == target:
        return True

    left = 2 * i + 1
    right = 2 * i + 2
    return search_heap(heap, target, left) or search_heap(heap, target, right)

# Exemplo de uso
if __name__ == '__main__':
    lista = [4, 10, 3, 5, 1]
    heap = build_heap(lista.copy())
    print("Heap:", heap)

    # Testando a busca
    valor = 5
    print(f"Elemento {valor} encontrado? {search_heap(heap, valor)}")

    valor = 7
    print(f"Elemento {valor} encontrado? {search_heap(heap, valor)}")
