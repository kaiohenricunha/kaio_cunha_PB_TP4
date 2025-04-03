def build_heap(arr):
    """
    Transforma a lista 'arr' em uma min-heap in-place.
    """
    n = len(arr)
    # Começamos dos nós não-folha, que vão de n//2 - 1 até 0
    for i in range(n // 2 - 1, -1, -1):
        sift_down(arr, i, n)
    return arr

def sift_down(arr, i, n):
    """
    Ajusta o nó de índice 'i' para baixo, garantindo a propriedade de heap.
    """
    smallest = i
    left = 2 * i + 1
    right = 2 * i + 2

    # Se o filho da esquerda existir e for menor que o nó atual, atualiza
    if left < n and arr[left] < arr[smallest]:
        smallest = left
    # Se o filho da direita existir e for menor que o atual menor, atualiza
    if right < n and arr[right] < arr[smallest]:
        smallest = right

    # Se o menor não for o nó original, faz a troca e continua ajustando
    if smallest != i:
        arr[i], arr[smallest] = arr[smallest], arr[i]
        sift_down(arr, smallest, n)

def show_heap(heap):
    """
    Exibe a heap em formato de lista.
    """
    print(heap)

# Exemplo de uso
if __name__ == "__main__":
    lista = [4, 10, 3, 5, 1]
    heap = build_heap(lista.copy())  # Usamos copy() para preservar a lista original
    show_heap(heap)
