class TrieNode:
    def __init__(self):
        self.children = {}  # Dicionário para armazenar os nós filhos
        self.is_end = False  # Indica se é o fim de uma palavra

class Trie:
    def __init__(self):
        self.root = TrieNode()
    
    def insert(self, word):
        """
        Insere uma palavra no Trie, caractere por caractere.
        """
        node = self.root
        for char in word:
            if char not in node.children:
                node.children[char] = TrieNode()
            node = node.children[char]
        node.is_end = True
    
    def display(self):
        """
        Retorna uma lista com todas as palavras armazenadas no Trie.
        """
        palavras = []
        self._dfs(self.root, "", palavras)
        return palavras
    
    def _dfs(self, node, prefix, palavras):
        # Se o nó atual marca o fim de uma palavra, adiciona a palavra à lista.
        if node.is_end:
            palavras.append(prefix)
        # Percorre recursivamente os filhos
        for char, child in node.children.items():
            self._dfs(child, prefix + char, palavras)

# Exemplo de uso:
if __name__ == "__main__":
    trie = Trie()
    # Lista de palavras a serem inseridas manualmente
    lista_de_palavras = ["casa", "carro", "cadeira", "computador", "cachorro"]
    
    for palavra in lista_de_palavras:
        trie.insert(palavra)
    
    print("Palavras inseridas no Trie:", trie.display())
