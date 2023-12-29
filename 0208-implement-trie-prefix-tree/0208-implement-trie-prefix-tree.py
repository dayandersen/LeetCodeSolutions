class Trie:
    class Node:
        def __init__(self, letter, mapping, is_full_word):
            self.letter = letter
            self.mapping = mapping
            self.is_full_word = is_full_word

    def __init__(self):
        self.root_node = self.Node(letter=" ", mapping={}, is_full_word=False)

    def insert(self, word: str) -> None:
        letters = list(word)
        node = self.root_node
        for letter in letters:
            if letter in node.mapping:
                node = node.mapping[letter]
            else:
                node.mapping[letter] = self.Node(letter, mapping={}, is_full_word=False)
                node = node.mapping[letter]
        node.is_full_word = True

    def search(self, word: str) -> bool:
        letters = list(word)
        node = self.root_node
        if letters[0] in node.mapping:
            node = node.mapping[letters[0]]
            for letter in letters[1:]:
                if letter in node.mapping:
                    node = node.mapping[letter]
                else:
                    return False
            return node.is_full_word
        else:
            return False
        

    def startsWith(self, prefix: str) -> bool:
        letters = list(prefix)
        node = self.root_node
        if letters[0] in node.mapping:
            node = node.mapping[letters[0]]
            for letter in letters[1:]:
                if letter in node.mapping:
                    node = node.mapping[letter]
                else:
                    return False
            return True
        else:
            return False