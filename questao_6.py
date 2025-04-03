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
        """
        Busca simples em Trie.
        Retorna True se a palavra foi inserida no Trie, e False caso contrário.
        """
        node = self.root
        for char in word:
            if char not in node.children:
                return False
            node = node.children[char]
        return node.is_end

# Exemplo de uso:
if __name__ == "__main__":
    trie = Trie()
    palavras = ["casa", "carro", "cadeira", "computador", "cachorro"]
    
    # Insere as palavras no Trie
    for palavra in palavras:
        trie.insert(palavra)
    
    # Busca por palavras
    busca1 = "carro"
    busca2 = "caso"
    print(f"A palavra '{busca1}' foi encontrada?", trie.search(busca1))
    print(f"A palavra '{busca2}' foi encontrada?", trie.search(busca2))
