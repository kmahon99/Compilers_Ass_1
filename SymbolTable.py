# Kevin Mahon 13379741

class SymbolTable:
    def __init__(self, statics_file):
        try:
            self.reserved_file = open(statics_file)
        except FileNotFoundError:
            print("Reserved symbols file not found")
        self.root = TrieNode(None, -1)
        self.current = self.root
        self.global_id = 0
        self.flag = False
        for line in self.reserved_file: # add reserved symbols to trie
            id = self.addString(line, True)
            #print("RESERVED:",line)
            #print("ID =",id)

    # add or check a character in the trie, set flag = True for adding, False for checking
    def processChar(self, char, flag):
        self.flag = flag
        node = TrieNode(char, -1)
        if node in self.current.children:
            self.current = self.current.children[self.current.children.index(node)]
        else:
            if flag == True:
                self.current.addChild(node)
                self.current = node

    # returns the ID of the current node and resets to root, use after word has been added
    def getID(self):
        if self.flag == True:
            if self.current.getID() == -1:
                self.current.setID(self.global_id)
                self.global_id += 1
        id = self.current.getID()
        self.current = self.root
        return id

    # using methods 1 and 2 to do easy string adding to trie
    def addString(self, string, flag):
        for c in string:
            self.processChar(c, flag)
        return self.getID()

class TrieNode:
    def __init__(self, value, id):
        self.value = value
        self.id = id
        self.children = []

    def getID(self): return self.id

    def setID(self, id): self.id = id

    def addChild(self, node):
        self.children.append(node)

    def __eq__(self, other):
        return self.value == other.value