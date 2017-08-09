import re
import reprlib

RE_WORD = re.compile('\w+')

# iterables have an __iter__ method that instatiates a new iterator every time
# Iterators implement a __next__ method that returns individual items and an __iter__ method that returns self
# iterators are also iterable, but iterables are nto iterators

# to support multiple traversals it must be possible to obtain multiple indepenced interators from the same
#   iterable instance, and each iterator must keep its own internal state.
# therefore, do not implement __next__ on an iterable

class Sentence:

  def __init__(self, text):
    self.text = text
    self.words = RE_WORD.findall(text)

  def __repr__(self):
    return 'Sentence({})'.format(reprlib.repr(self.text))

  def __iter__(self):
    return SentenceIterator(self.words)


class SentenceIterator:

  def __init__(self, words):
    self.words = words
    self.index = 0

  def __next__(self):
    try:
      word = self.words[self.index]
    except IndexError:
      raise StopIteration()
    self.index += 1
    return word

  # it is not necessary for __iter__ to be defined for this to work
  # however, iterators are supposed to implement both __next__ and __iter__
  def __iter__(self):
    return self

s = Sentence("hello world. it's sunny outside today")
for i in s:
  print(i)
