
#a class to hold the data loaded from a file
class Source:

    def __init__(self, filename):
        self.file = open(filename, "r")

    def nextChar(self):
        char = self.file.read(1)
        return char

    def __del__(self):
        try:
            self.file.close()
        except AttributeError:
            pass