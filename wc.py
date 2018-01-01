#!/usr/bin/env python3.6
# -*- coding: utf-8 -*-

"""Simple word count implementation in Python."""

import collections
#  import fileinput
from sys import argv
from stop_words import get_stop_words


class Wordcount(object):
    """Blueprint for the object Word_Count"""

    def __init__(self):
        self.dictionary = {}

    @staticmethod
    def pre_process_text(text):
        """Replaces line endings and splits the text into an array.

        :text: the given text input
        :returns: text as an array to process

        """
        text = text.replace('\n', ' ')
        word_list = text.split(' ')
        return word_list

    @staticmethod
    def pre_process_word(word):
        """Normalizes the given word and strips off all punctuation.

        :word: TODO
        :returns: TODO

        """
        normalized_word = word.casefold()
        stripped_word = normalized_word.strip('\",.!;?#')
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


def main():
    """Starts the program if run from the command line.
    """
    wc = Wordcount()
    for filename in argv[1:]:
        file_to_read = open(filename)
        text_to_count = file_to_read.read()
        print(collections.Counter(wc.count(text_to_count)).most_common(15))


if __name__ == "__main__":
    """If run from the command line, then accept files etc. as input.
    """
    main()
