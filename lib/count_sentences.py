class MyString:
    
    def __init__(self, value=''):
        self._value = value
    
    @property
    def value(self):
        return self._value

    @value.setter
    def value(self, stringVal):
        if (type(stringVal) == str):
            self._value = stringVal
        else:
            print("The value must be a string.")

    def is_sentence(self):
        return self.value.endswith(".")

    def is_question(self):
        return self.value.endswith("?")

    def is_exclamation(self):
        return self.value.endswith("!")
    
    def count_sentences(self):
      sentences = [sentence.strip() for sentence in self.value.split(".?!")]
      sentences = [sentence for sentence in sentences if sentence]
      return len(sentences)

  
my_string = MyString("This is a sentence. This one has an exclamation mark! And this is a question?")
print(my_string.value) 
