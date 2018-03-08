#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Simple word count implementation in Python. """


import collections
import string

from sys import argv
from stop_words import get_stop_words


class Wordcount(object):

    """Counting every occurrence of all the tokens in a given text file."""

    def __init__(self, file_to_process):
        """Creates Wordcount object. """
        self.file_to_process = file_to_process
        self.text = self.read_file()
        self.words_cleaned = self.pre_process()
        self.words_counted = self.count_words()

    def read_file(self):
        """Reads the file to process.

        :returns: text

        """
        with open(self.file_to_process) as file_to_read:
            text = file_to_read.read()

        return text

    def pre_process(self):
        """Converting to lowercase and removing stopwords.
        :returns: text_cleaned

        """
        text_to_lower = self.text.casefold()
        words = [w.strip(string.punctuation) for w in text_to_lower.split()]

        blacklist = get_stop_words('english')

        return [word for word in words if word not in blacklist]

    def count_words(self):
        """Counts the occurrences of all the tokens.
        :returns: words_counted

        """

        return collections.Counter(self.words_cleaned)


def main():
    """Starts the program from the command line.
    :returns: TODO

    """
    for filename in argv[2:]:
        word_count = Wordcount(filename)
        print(f"The text in {word_count.file_to_process} consists of",
              len(word_count.words_counted), "tokens.")
        print(f"These are the {argv[1]} most common.")
        print(word_count.words_counted.most_common(int(argv[1])))


if __name__ == '__main__':
    main()
