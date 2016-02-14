# Kevin Mahon 13379741

# a token class to store info obtained by the lexer
class Token:
    def __init__(self, type, attribute):
        if type == "(": self.type = "lpar"
        elif type == ")": self.type = "rpar"
        elif type == ";": self.type = "semicolon"
        else: self.type = type
        self.attribute = attribute

    def to_s(self):
        return self.type + " : " + str(self.attribute)