#!/usr/bin/env python
# -*- coding: utf-8 -*-

""" Simple word count implementation in Python. """


import collections
import string

from sys import argv
from stop_words import get_stop_words


class Wordcount(object):

    """Counting every occurrence of all the tokens in a given text file."""

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
        text_to_lower = self.text.lower()

        for punctuation in string.punctuation:
            text_cleaned = text_to_lower.replace(punctuation, "")

        return text_cleaned

    def remove_stopwords(self):
        """Removes the stopwords.
        :returns: words_cleaned

        """
        words = self.text_cleaned.split()

        blacklist = get_stop_words('english')
        words_cleaned = [word for word in words if word not in blacklist]

        return words_cleaned

    def count_words(self):
        """Counts the occurrences of all the tokens.
        :returns: words_counted

        """
        tokens = set(self.words_cleaned)

        words_counted = {token: self.words_cleaned.count(token) for token in
                         tokens}

        return words_counted

    def __init__(self, file_to_process):
        """Creates Wordcount object. """
        self.file_to_process = file_to_process
        self.text = self.read_file()
        self.text_cleaned = self.pre_process()
        self.words_cleaned = self.remove_stopwords()
        self.words_counted = self.count_words()


def main():
    """Starts the program from the command line.
    :returns: TODO

    """
    for filename in argv[2:]:
        word_count = Wordcount(filename)
        print(f"The text in {word_count.file_to_process} consists of",
              len(word_count.words_counted), "tokens.")
        print(f"These are the {argv[1]} most common.")
        print(collections.Counter(word_count.words_counted).most_common(
            int(argv[1])))


if __name__ == '__main__':
    main()
