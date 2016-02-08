import DataStream as Stream

class Lexer:
    def __init__(self, filename):
        self.filename = filename
        self.stream = Stream.Source(self.filename)

    def Driver(self):
        if self.stream == None:
            print("Error")
        else:
            c = self.stream.nextChar()
            return c


    def GetAnalysis(self):
        c = self.Driver()
        while c != "END":
            if ord(c) >= 65 and ord(c) <= 90:
                self.checkStatic(c)

    def checkStatic(self, startchar):
        item = startchar
        c = self.Driver()
        while (ord(c) >= 48 and ord(c) <= 57) and (ord(c) != )

l = Lexer("test.txt")
l.Driver()