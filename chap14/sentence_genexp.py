import re
import reprlib

RE_WORD = re.compile('\w+')

class Sentence:

  def __init__(self, text):
    self.text = text

  def __repr__(self):
    return 'Sentence({})'.format(reprlib.repr(self.text))

  def __iter__(self):
    return (match.group() for match in RE_WORD.finditer(self.text))

s = Sentence('hello again world. today is coming to an end')

for i in s:
  print(i)
