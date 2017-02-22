class Node:
    def __init__(self, data = None, children = None):
        self.data = data
        if children is None:
            self.children = {}
    def addChild(self, data):
        if data not in self.children:
            new_node = Node(data)
            self.children[data] = new_node

class Trie(object):
    def __init__(self, root = None):
        self.root = root
        if root is None:
            self.root = Node('*')
    def addWord(self, word):
        current = self.root
        while True:
            if len(word) == 0:
                # all characters added to Trie
                # append end sign to the word
                if '*' not in current.children:
                    current.children['*'] = None
                return
            current.addChild(word[0])
            current = current.children[word[0]]
            word = word[1:]
    def isWord(self, word):
        current = self.root
        while True:
            if len(word) == 0:
                # all characters checked
                # need to check end sign
                if '*' in current.children:
                    return True
                else:
                    return False
            if word[0] in current.children:
                # next character in Trie
                # keep checking
                current = current.children[word[0]]
                word = word[1:]
            else:
                # next character not in Trie
                return False
    def isPrefix(self, word):
        current = self.root
        while True:
            if len(word) == 0:
                # all characters in Trie
                return True
            if word[0] in current.children:
                # same as isWord method
                current = current.children[word[0]]
                word = word[1:]
            else:
                return False
