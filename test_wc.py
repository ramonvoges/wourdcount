"""Tests for Word_Count"""

import wc

def test_count_words():
    """Tests the basic functionality of Word_Count."""

    test = "Eins zwei eins drei"
    counted = wc.Word_Count(test)
    #  counted = counter.count(test)
    assert counted.dictionary == {"eins": 2, "zwei": 1, "drei": 1}

def test_multiple_lines():
    """Tests the processing of multiple lines."""

    test = "Eins zwei\ndrei eins"
    counted = wc.Word_Count(test)
    assert counted.dictionary == {"eins": 2, "zwei": 1, "drei": 1}

def test_replace_punctuation():
    """Tests the removing of punctuation."""

    test = "Eins, zwei, drei, eins!"
    counted = wc.Word_Count(test)
    assert counted.dictionary == {"eins": 2, "zwei": 1, "drei": 1}
