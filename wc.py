#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

import collections
#  import fileinput
from stop_words import get_stop_words
from sys import argv

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

    def pre_process_word(self, word):
        """Normalizes the given word and strips off all punctuation.

        :word: TODO
        :returns: TODO

        """
        normalized_word = word.casefold()
        stripped_word = normalized_word.strip(',.!;?#')
        return stripped_word

    def post_process_dict(self):
        """Removes empty records and stop words.

        :returns: changed dictionary without empty records

        """
        if self.dictionary.get(''):
            del self.dictionary['']

        blacklist = get_stop_words('english')
        for word in blacklist:
            if self.dictionary.get(word):
                del self.dictionary[word]

        return self.dictionary

    def count(self, text):
        """Counts words in a given text.

        :returns: dictionary with words and counts

        """
        self.dictionary = {}
        word_list = self.pre_process_text(text)
        for word in word_list:
            #  word = word.casefold()
            processed_word = self.pre_process_word(word)
            if self.dictionary.get(processed_word):
                self.dictionary[processed_word] += 1
            else:
                self.dictionary[processed_word] = 1

        return self.post_process_dict()

if __name__ == "__main__":
    wc = Wordcount()
    #  print(wc.count("Eins, zwei, eins und drei!"))
    #  script, filename = argv
    for filename in argv[1:]:
        f = open(filename)
        text = f.read()
        print(collections.Counter(wc.count(text)).most_common(15))
