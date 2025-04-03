class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """Insere uma palavra no Trie caractere por caractere."""
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True

    def search(self, word):
        """Retorna True se a palavra foi inserida no Trie, False caso contrário."""
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end

    def autocomplete(self, prefix):
        """
        Retorna todas as palavras do Trie que começam com o prefixo fornecido.
        """
        node = self.root
        for char in prefix:
            if char not in node.children:
                return []
            node = node.children[char]
        palavras = []
        self._dfs(node, prefix, palavras)
        return palavras

    def _dfs(self, node, prefix, palavras):
        if node.is_end:
            palavras.append(prefix)
        for char, child in node.children.items():
            self._dfs(child, prefix + char, palavras)

    def remove(self, word):
        """
        Remove a palavra do Trie e remove nós que se tornem desnecessários.
        """
        self._remove(self.root, word, 0)

    def _remove(self, node, word, index):
        """
        Método recursivo auxiliar para remoção.
        Retorna True se o nó atual puder ser removido (ou seja, não é final de outra palavra e não possui outros filhos).
        """
        if index == len(word):
            # Palavra não existe se o nó não marca fim de palavra
            if not node.is_end:
                return False
            # Desmarca o fim de palavra
            node.is_end = False
            # Se o nó não tiver filhos, pode ser removido
            return len(node.children) == 0

        char = word[index]
        if char not in node.children:
            return False  # Palavra não encontrada

        should_delete_child = self._remove(node.children[char], word, index + 1)

        # Se o nó filho pode ser removido, deleta-o do dicionário
        if should_delete_child:
            del node.children[char]
            # Retorna True se o nó atual não é fim de outra palavra e não possui outros filhos
            return not node.is_end and len(node.children) == 0

        return False

# Exemplo de uso:
if __name__ == "__main__":
    trie = Trie()
    palavras = ["casa", "casamento", "casulo", "cachorro"]
    for palavra in palavras:
        trie.insert(palavra)

    print("Antes da remoção:")
    print("Busca 'casa':", trie.search("casa"))
    print("Autocomplete 'cas':", trie.autocomplete("cas"))

    # Removendo a palavra "casa"
    trie.remove("casa")

    print("\nApós a remoção de 'casa':")
    print("Busca 'casa':", trie.search("casa"))
    print("Autocomplete 'cas':", trie.autocomplete("cas"))
