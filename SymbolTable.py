
class SymbolTable:
    def __init__(self, reserved_file):
        self.reserved_file = open(reserved_file, "r")
        self.root = TrieNode(None, -1)
        self.current = self.root
        self.global_id = 0

    def inputSymbol(self, symbol, flag):
        self.current = self.root
        for char in symbol:
            node = TrieNode(char, -1)
            if flag == True: # static
                if node in self.current.children:
                    self.current = self.current.children[node]
                else:
                    return -1
            else:
                if node in self.current.children:
                    self.current = self.current.children[node]
                else:
                    self.current = self.current.addChild(symbol, -1)
        if self.current.getID == -1:
            self.current.modID(self.global_id)
            self.global_id += 1
        return self.current.getID()

class TrieNode:
    def __init__(self, value, id):
        self.value = value
        self.id = id
        self.children = []

    def addChild(self, symbol, id):
        child = self.children.append(TrieNode(symbol,id))
        return child

    def modID(self, new_id):
        self.id = new_id

    def getID(self): return self.id

    def __eq__(self, other):
        return self.value == other.value

s = SymbolTable("ReservedSymbols.txt")
print(s.inputSymbol("test", False))