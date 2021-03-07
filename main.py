from pprint import pprint
c = []
class name:
    def __init__(self, filename):
        self.filename = filename

    def count_lines(self):
        i = 0
        d = []
        a = []
        with open(self.filename) as f:
            for line in f:
                i+=1
                x = line.strip('\n').strip()
                a.append(x)
            d.append(i)
            d.append(self.filename)
            d.append(a)
            c.append(d)














first = name('1.txt')
second =  name('2.txt')
third = name('3.txt')
first.count_lines()

second.count_lines()

third.count_lines()

#pprint(c)
pprint(sorted(c,  reverse=True))





