class xptoClass:    def __iter__(self):        self.a = [0]        return self
def __next__(self):     self.a.append( \            self.a[-1] \            + self.a[-2] if len(self.a) > 1 else 1)     return self.a
xpto = xptoClass() xptoIter = iter(xpto)
for k in range(1,6):          print(next(xptoIter))