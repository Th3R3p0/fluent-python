import re
import reprlib

RE_WORD = re.compile('\w+')

class Sentence:

    def __init__(self, text):
        self.text = text
        self.words = RE_WORD.findall(text)

    def __getitem__(self, index):
        return self.words[index]

    def __len__(self):
        return len(self.words)

    def __repr__(self):
        return 'Sentence({})'.format(reprlib.repr(self.text))

s = Sentence('"I wonder how this sentence class will work", said the student.')
print(s)
print(len(s))

for i in s:
    print(i)

# The __iter__ dunder function is not defined, however this funtion is iterable because the __getitem__ is defined
# Thus, all sequences (str, unicode, list, tuple, buffer, xrange) are iterable because they all have the __getitem__
#     function implemented
print(list(s))

s3 = Sentence('Pig and Pepper')
it = iter(s3)
print(it)

# next pops the zero index from the list
print(next(it))
print(next(it))
print(next(it))
# the next in the next line would through a StopIteration exception because there is no zero index
# next(it)

it = iter(s3)
print(next(it))
print(list(iter(it)))
# the next in the next line would through a StopIteration exception - ??? because it has run through all indexes ???
# print(next(it))

