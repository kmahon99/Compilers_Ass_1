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

    def processChar(self, char, flag): # set flag to true for dynamic
        node = TrieNode(char, -1)
        if node.value == None: # end of input, send id back to caller and reset to root
            if id == -1 and flag == True:
                self.current.modID(self.global_id)
                self.global_id += 1
            id = self.current.value
            self.current = self.root
            return id
        if node in self.current.children:
            self.current = self.current.children[self.current.children.index(node)]
            return None
        else:
            if flag == True:
                self.current.addChild(node)
                self.current = node
                return None


class TrieNode:
    def __init__(self, value, id):
        self.value = value
        self.id = id
        self.children = []

    def addChild(self, node):
        self.children.append(node)

    def modID(self, id): self.id = id

    def __eq__(self, other):
        return self.value == other.value

s = SymbolTable("ReservedSymbols.txt")
print(s.inputSymbol("test",False))