import DataStream as Stream
import SymbolTable

class Lexer:
    def __init__(self, filename):
        self.delims = [' ', '\n', '\t', '\r', ';']
        self.table = SymbolTable.SymbolTable("ReservedSymbols.txt")
        self.state = None
        self.filename = filename
        self.stream = Stream.Source(self.filename)
        while self.state != "EOF":
            if self.state == "IDENT" or "STATIC":


    def getNextChar(self):
        char = self.stream.nextChar()
        if char == '': self.state = "EOF"
        elif self.state == "STRING" and ord(char) == 126:
            self.state = "TILDE"
            return
        elif self.state == "TILDE":
            self.state = "STRING"
            return char
        elif self.state == "STRING" and ord(char) != 34: return char# we're inside a string, this doesn't go anywhere
        elif ord(char) == 34 and self.state == "STRING": # this is the ending quotes for a string we've traversed
            self.state = None
            self.getNextChar()
        elif ord(char) == 34 and self.state != "STRING": self.state = "STRING"
        elif ord(char) in range(97,122) and self.state != "STATIC": self.state = "IDENT"
        elif ord(char) in range(97,122) and self.state == "STATIC": self.state = "STATIC"
        elif ord(char) in range(65, 90): self.state = "STATIC"
        elif ord(char) in range(48,57): self.state = "INT"
        elif char in self.delims: self.state = "DELIM"
        return char

l = Lexer("test.txt")