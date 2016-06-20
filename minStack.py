class MinStack(object):

    def __init__(self):
        self.data = []
        self.minS = []

    def push(self, num):
        self.data.append(num)
        if not self.minS or num <= self.minS[-1]:
            self.minS.append(num)

    def pop(self):
        res = self.data.pop()
        if res == self.minS[-1]:
            self.minS.pop()
        return res

    def min(self):
        return self.minS[-1]