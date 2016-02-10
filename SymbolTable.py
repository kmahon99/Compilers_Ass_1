import Token

class SymbolTable:
    def __init__(self, reserved_file):
        self.reserved_file = open(reserved_file, "r")
        self.root = TrieNode(None, -1)
        self.current = self.root
        self.global_id = 0
        self.tokens = []
        for line in reserved_file:
            self.tokens.append(Token.Token(line, self.inputSymbol(line, False)))

    def inputSymbol(self, symbol, flag):
        self.current = self.root
        for char in symbol:
            node = TrieNode(char, -1)
            if flag == True: # static
                if node in self.current.children:
                    self.current = self.current.children[self.current.children.index(node)]
                else:
                    return -1
            else:
                if node in self.current.children:
                    self.current = self.current.children[self.current.children.index(node)]
                else:
                    self.current = self.current.addChild(node)
                    self.current = node
        self.tokens.append(Token.Token(self.current.value, self.current.id))
        if self.current.id == -1:
            self.current.id = self.global_id
            self.global_id += 1
        return self.current.id

class TrieNode:
    def __init__(self, value, id):
        self.value = value
        self.id = id
        self.children = []

    def addChild(self, node):
        self.children.append(node)

    def __eq__(self, other):
        return self.value == other.value

s = SymbolTable("ReservedSymbols.txt")
print(s.inputSymbol("test",False))