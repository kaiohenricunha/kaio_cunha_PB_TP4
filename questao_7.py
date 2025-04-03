class TrieNode:
    def __init__(self):
        self.children = {}
        self.is_end = False

class Trie:
    def __init__(self):
        self.root = TrieNode()

    def insert(self, word):
        """Insere uma palavra no Trie, caractere por caractere."""
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True

    def search(self, word):
        """Verifica se uma palavra está presente no Trie."""
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
        # Percorre o Trie seguindo o prefixo
        for char in prefix:
            if char not in node.children:
                # Se o prefixo não existe, retorna lista vazia
                return []
            node = node.children[char]
        
        # A partir do nó atual, coleta todas as palavras com o prefixo dado
        palavras = []
        self._dfs(node, prefix, palavras)
        return palavras

    def _dfs(self, node, prefix, palavras):
        """
        Percorre o Trie em profundidade (DFS) para coletar as palavras que iniciam com 'prefix'.
        """
        if node.is_end:
            palavras.append(prefix)
        for char, child in node.children.items():
            self._dfs(child, prefix + char, palavras)

# Exemplo de uso:
if __name__ == "__main__":
    trie = Trie()
    lista_de_palavras = ["casa", "carro", "cadeira", "computador", "cachorro", "casamento", "casual"]
    
    for palavra in lista_de_palavras:
        trie.insert(palavra)
    
    prefixo = "ca"
    print("Palavras que começam com '{}':".format(prefixo), trie.autocomplete(prefixo))
