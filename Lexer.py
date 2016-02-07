

class Lexer:
    def __init__(self, filename):
        self.filename = filename

    def Driver(self):
        with open(self.filename) as file:
            while True:
                char = file.read(1)
                if not char:
                    print("End")
                    break


l = Lexer("test.txt")
l.Driver()