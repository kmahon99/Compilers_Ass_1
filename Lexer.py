import DataStream as Stream

class Lexer:
    def __init__(self, filename):
        self.delims = ['\n','\t','\r',' ','(',')',';']
        self.filename = filename
        self.stream = Stream.Source(self.filename)
        self.getAnalysis()

    def Driver(self):
        if self.stream == None:
            print("Error")
        else:
            c = self.stream.nextChar()
            return c

    def getAnalysis(self):
        c = self.Driver()
        while c != '':
            if ord(c) in range(97,122):
                item = self.checkIdentifier(c)
                print("Identifier: ",item)
            elif ord(c) in range(48,57):
                item = self.checkInt(c)
                print("Int: ",item)
            elif ord(c) == 34:
                item  = self.checkString(c)
                print("String: ",item)

            c = self.Driver()

    def checkIdentifier(self, start):
        item = start
        c = self.Driver()
        while(ord(c) in range(65,90) or ord(c) in range(97,122)): # collect until we get something other than a letter
            item += c
            c = self.Driver()
        return item

    def checkInt(self,start):
        item = start
        c = self.Driver()
        while(ord(c) in range(48,57)): # collect until we get something other than a number
            item += c
            c = self.Driver()
        return item

    def checkString(self,start):
        item = ""
        c = self.Driver()
        while(ord(c) != 34):
            if ord(c) == 126: # tilde adds next character regardless
                c = self.Driver()
            item += c
            c = self.Driver()
        return item


l = Lexer("test.txt")