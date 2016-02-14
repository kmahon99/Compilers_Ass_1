# Kevin Mahon 13379741

import DataStream as Stream
import SymbolTable
import Token

class Lexer:
    def __init__(self, filename):
        self.delims = [' ', '\n', '\t', '\r']
        self.singles = ['(',')',';']
        self.table = SymbolTable.SymbolTable("ReservedSymbols.txt")
        self.state = None
        self.filename = filename
        self.stream = Stream.Source(self.filename)
        self.tokens = []

    def Driver(self):
        ident = ""
        while self.state != "EOF":
            oldstate = self.state
            char = self.getNextChar()
            if char == None: return
            if oldstate == "SINGLE":
                self.tokens.append(Token.Token(ident,0))
                ident = ""
            elif oldstate != self.state:
                if oldstate == "STATIC" or oldstate == "IDENT": self.tokens.append(Token.Token("id",self.table.getID()))
                elif oldstate == "INT": self.tokens.append(Token.Token("int",self.getValidInt(ident)))
                elif oldstate == "STRING": self.tokens.append(Token.Token("string",ident))
                elif oldstate == "UNKNOWN": self.tokens.append(Token.Token("error",0))
                ident = ""
            if self.state == "IDENT": self.table.processChar(char, True)
            elif self.state == "STATIC": self.table.processChar(char, False)
            ident += char
        return self.tokens

    # gets the next character and changes the Lexer's state based on it's type
    def getNextChar(self):
        char = self.stream.nextChar()
        if char == '': self.state = "EOF"
        elif ord(char) == 126 and self.state == "STRING": char = self.stream.nextChar() # tilde in string
        elif ord(char) != 34 and self.state == "STRING": self.state == "STRING"
        elif ord(char) == 34 and self.state == "STRING":
            self.state = "STRING_END"
            char = self.stream.nextChar()
        elif ord(char) == 34 and self.state != "STRING":
            self.state = "STRING"
            char = self.stream.nextChar()
        elif ord(char) in range(65,91) and self.state != "IDENT": self.state = "STATIC"
        elif ord(char) in range(65,91) and self.state == "IDENT": self.state = "IDENT"
        elif ord(char) in range(97,123) and self.state != "STATIC": self.state = "IDENT"
        elif ord(char) in range(97,123) and self.state == "STATIC": self.state = "STATIC"
        elif ord(char) in range(48,58): self.state = "INT"
        elif char in self.delims: self.state = "DELIM"
        elif char in self.singles: self.state = "SINGLE"
        else: self.state = "UNKNOWN"
        return char

    # helper function to prevent oversized int values being created
    def getValidInt(self,string_value):
        max_int = "65535"
        if len(string_value) > 5: return -1
        elif len(string_value) == 5:
            for i in range(0,5):
                if int(string_value[i]) < int(max_int[i]): return int(string_value)
                elif int(string_value[i]) > int(max_int[i]): return -1
        return int(string_value)


l = Lexer("test.txt")
t = l.Driver()
for item in t:
    print(item.to_s())