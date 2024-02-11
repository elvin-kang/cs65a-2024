class Loop():
    def __init__(self, start, end, count):
        self.start = start
        self.end = end
        self.count = count
    def forLoop(self):
        for i in range(self.start, self.end, self.count):
            print(i)


# some code..