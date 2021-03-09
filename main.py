from pprint import pprint
text = []
class name:
    def __init__(self, filename):
        self.filename = filename

    def count_lines(self):
        i = 0
        text_filename = []
        text_in_file = []
        with open(self.filename) as f:
            for line in f:
                i+=1
                x = line.strip('\n').strip()
                text_in_file.append(x)
                res = ''.join(text_in_file)
            text_filename.append(i)
            text_filename.append(self.filename)
            text_filename.append(res)
            text.append(text_filename)

first = name('1.txt')
second = name('2.txt')
third = name('3.txt')
first.count_lines()
second.count_lines()
third.count_lines()

def sort():
    sort_text = sorted(text, reverse=True)
    for element in sort_text:
        for elem in element:
            pprint(elem)
pprint(sort())


