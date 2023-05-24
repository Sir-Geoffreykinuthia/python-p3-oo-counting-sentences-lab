#!/usr/bin/env python3

# using regular expression for the search pattern
import re

class MyString:
    def __init__(self, value=""):
        self._value = value

    #  using getter method for the value property
    @property
    def value(self):
        return self._value
    
  #  using setter method for the value of the property
    @value.setter
    def value(self, new_value):
        if not isinstance(new_value, str):
            print("The value must be a string.")
        else:
            self._value = new_value
  # confirming if the str ends with a period
    def is_sentence(self):
        return self._value.endswith('.')
    
  # checking if the string ends with a question mark
    def is_question(self):
        return self._value.endswith('?')
    
  # confirming if the str ends with the exclamation mark
    def is_exclamation(self):
        return self._value.endswith('!')
    
  # counting number of sentenses in the string
  # splitting strings based on the ending marks and 
  # using regular expression to match the punctuation marks
    def count_sentences(self):
        sentences = re.split(r'[.?!]+', self._value)
        return len(sentences) - 1
    
    

