#!/usr/bin/env python3
"""Unit and functional tests for anagrams.py"""

from unittest import TestCase, main
from anagrams import hash_word, collect_anagrams, filter_anagrams


class BasicAnagramsTestCase(TestCase):
    """Some baseline tests for collecting lists of anagrams."""

    def setUp(self):
        self.snowman = b'a\xE2\x98\x83'.decode('utf-8', 'strict')
        self.raw_data = ['levo', 'mila', 'egol', 'Amil',
                         'align', 'vole', 'velo', 'amli',
                         'mail', 'loge', 'goel', 'love',
                         'mali', 'a', 'it', 'asteer', 'saeter',
                         'reseat', '', 'reclasp', 'clasper',
                         'scalper', 'mail',
                         self.snowman]

    def test_hash_word(self):
        """Is the hash key correct?"""

        self.assertEqual(hash_word('align'), 'agiln')
        self.assertEqual(hash_word('a'), 'a')
        self.assertEqual(hash_word(''), '')

    def test_collect_anagrams(self):
        """Are anagrams collected under one key?"""

        anagrams = collect_anagrams(self.raw_data, min_word_length=4)

        assert 'ailm' in anagrams
        alist = anagrams['ailm']
        self.assertEqual(len(alist), 5)

        assert 'it' not in anagrams

        anagrams = collect_anagrams(self.raw_data, min_word_length=2)
        assert 'it' in anagrams
        assert self.snowman in anagrams

        self.assertRaises(AssertionError,
                          collect_anagrams,
                          self.raw_data,
                          min_word_length=1)

    def test_filter_anagrams(self):
        """Does the anagram list get trimmed correctly?"""

        anagrams = collect_anagrams(self.raw_data, min_word_length=4)
        filtered = list(filter_anagrams(anagrams, match_word_length=True))

        self.assertEqual(len(filtered), 2)

        anagrams = collect_anagrams(self.raw_data, min_word_length=4)
        filtered = list(filter_anagrams(anagrams))

        self.assertEqual(len(filtered), 5)


if __name__ == '__main__':
    main()
