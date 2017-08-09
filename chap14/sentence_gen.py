import re
import reprlib

RE_WORD = re.compile('\w+')

class Sentence:

  def __init__(self, text):
    self.text = text
    self.words = RE_WORD.findall(text)

  def __repr__(self):
    return 'Sentence({})'.format(reprlib.repr(self.text))

  def __iter__(self):
    for word in self.words:
      yield word
    # this return is not needed
    # there is no need to catch an exception. The generator function doesn't raise StopIteration
    #   it simply exits when it's done producing values
    return

s = Sentence("Hello again world. It's rainy today")
for i in s:
  print(i)


