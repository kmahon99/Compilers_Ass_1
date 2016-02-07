import DataStream as Stream

class Lexer:
    def __init__(self, filename):
        self.filename = filename

    def Driver(self):
        stream = Stream.Source(self.filename)
        if stream == None:
            print("Error")
        else:
            c = stream.nextChar()
            while c != "END":
                print(c)
                c = stream.nextChar()

