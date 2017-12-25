#  import re

class Wordcount(object):
    """Blueprint for the object Word_Count"""

    def __init__(self):
        self.dictionary = {}

    def pre_process_text(self, text):
        """Replaces line endings and splits the text into an array.

        :text: the given text input
        :returns: text as an array to process

        """
        text = text.replace('\n', ' ')
        word_list = text.split(' ')
        return word_list

    def count(self, text):
        """Counts words in a given text.

        :returns: dictionary with words and counts

        """
        self.dictionary = {}
        word_list = self.pre_process_text(text)
        #  self.text = text
        #  text = text.split(' ')
        for word in word_list:
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
