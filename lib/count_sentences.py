#!/usr/bin/env python3

class MyString:
  def __init__(self, value = ""):
    self.value = value

  @property
  def value(self):
      """The value property"""
      return self._value

  @value.setter
  def value(self, value):
      if isinstance(value, str):
          self._value = value
      else:
          print("The value must be a string.")

  def is_sentence(self):
      return self._value.endswith(".")
  
  def is_question(self):
      return self._value.endswith("?")

  def is_exclamation(self):
      return self._value.endswith("!")
  
  def count_sentences(self):
      count = 0
      for i in range(len(self._value)):
          if self._value[i] in ".!?" and (i == 0 or self._value[i - 1] not in ".!?"):
              count += 1
      return count