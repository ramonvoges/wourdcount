#  import re

class Wordcount(object):
    """Blueprint for the object Word_Count"""

    def __init__(self):
        #  self.text = None
        self.dictionary = {}
        #  self.count()

    def count(self, text):
        """Counts words in a given text.

        :returns: dictionary with words and counts

        """
        #  self.text = text
        #  text = text.split(' ')
        text = text.replace('\n', ' ')
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
    wc = Wordcount()
    print(wc.count("Eins zwei eins drei"))
