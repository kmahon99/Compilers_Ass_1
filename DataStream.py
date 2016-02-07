#a class to hold the data loaded from a file
class Source:

    def __init__(self, filename):
        try:
            self.file = open(filename, "r")
        except FileNotFoundError:
            return None

    def nextChar(self):
        char = self.file.read(1)
        if char == '':
            char = "END"
        elif char == '\n':
            char = "NEWLINE"
        elif char == ' ':
            char = "SPACE"
        elif char == '\t':
            char = "TAB"
        elif char == '\r':
            char == "RETURN"
        return char

    def __del__(self):
        self.file.close()


s = Source("test.txt")

c = s.nextChar()

while c != "END":
    c = s.nextChar()
    print(c)