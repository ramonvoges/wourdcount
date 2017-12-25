import re

class Word_Count(object):
    """Blueprint for the object Word_Count"""

    def __init__(self, text):
        self.text = text
        self.dictionary = {}
        self.count()

    def count(self):
        """Counts words in a given text.

        :returns: dictionary with words and counts

        """
        #  text = text.split(' ')
        text = self.text.replace('\n', ' ')
        #  text = text.replace(r'  +', ' ')
        for word in text.split(' '):
            word = word.casefold()
            word = word.strip(',.!;?#')
            if self.dictionary.get(word):
                self.dictionary[word] += 1
            else:
                self.dictionary[word] = 1

        if self.dictionary.get(''):
            del self.dictionary['']
        return self.dictionary

if __name__ == "__main__":
    counter = Word_Count("Eins zwei eins drei")
    print(counter.dictionary)
