class Fib():
    def __init__(self, max):
        self.n = 0
        self.prev = 0
        self.curr = 1
        self.max = max

    def __iter__(self):
        return self

    def __next__(self):
        if self.n < self.max:
            value = self.curr
            self.curr += self.prev
            self.prev=value

            self.n += 1
            return value
        else:
            raise StopIteration


f = Fib(5)
for i in range(5):
    print(next(f))






