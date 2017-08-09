import re
import reprlib

# lazy implementation
# This uses less memory. re.match loads all matches into a list. re.finditer only produces the next match on demand

RE_WORD = re.compile('\w+')

class Sentence:

  def __init__(self, text):
    self.text = text

  def __repr__(self):
    return 'Sentence({})'.format(reprlib.repr(self.text))

  def __iter__(self):
    for match in RE_WORD.finditer(self.text):
      yield match.group()

s = Sentence("Hello world. Just another day in paradise")
for i in s:
  print(i)

