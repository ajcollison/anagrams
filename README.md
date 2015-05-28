# anagrams
Python program for consuming a list of words
and generating lists of anagrams.  Words consisting
of a single letter (and empty string) are ignored, 
and optionally the minimum length of words considered
can be specified - the default minimum length being 4.

NOTE: Written for python 3

TODO: More testing/better handling of non-ascii input files
TODO: Compare performance with trie/DAWG approach

Examples
--------

Find anagrams for words in the local dictionary file:

    $ cat /usr/share/dict/words | ./anagrams.py
    seam, mesa, asem, same
    gate, geta, geat, gaet
    duro, ordu, dour, roud
    reis, rise, sire, sier
    dree, reed, deer, rede, dere
    aper, pare, pear, rape, reap
    redo, roed, doer, rode
    odor, door, rood, oord
    duper, perdu, drupe, prude, pured
    ...

This will only consider words 4 characters or more in length
and will only return anagram lists with a length equal to or
greater than the word length.


Include words as small as two letters:

    $ cat /usr/share/dict/words | ./anagrams.py -l 2
    ado, dao, oda
    crena, rance, nacre, crane, caner
    tow, two, wot
    leat, teal, tale, late, tael, laet, atle
    seater, asteer, saeter, teaser, reseat, staree, easter
    align, linga, langi, liang, algin
    was, saw, swa
    detar, trade, rated, derat, drate, tread, dater
    pho, hop, poh
    mire, emir, reim, riem, rime
    awd, wad, daw
    id, di
    ...

Don't require the number of anagrams to be at least equal to
the number of letters in the words:

    $ cat /usr/share/dict/words | ./anagrams.py -m
    alliably, labially
    carlie, eclair, erical
    eral, earl, lear, real
    moor, room, moro
    anticlinorium, inclinatorium
    sultane, unslate
    tarn, natr, rant
    khat, kath
    patulent, petulant
    demal, medal
    glycerate, electragy
    undercase, uncreased
    sawish, siwash
    knob, bonk
    bocardo, cordoba
    pimola, lipoma
    resty, strey
    arrie, airer
    amination, animation
    aliunde, unideal
    cutup, upcut
    carabin, arbacin
    tala, lata
    amnionate, anamniote, emanation
    ...

The module can also be imported and used in other programs:

    >>> from anagrams import collect_anagrams, filter_anagrams
    >>> 
    >>> with open('/usr/share/dict/words') as wordfile:
    ...     anagrams = collect_anagrams(wordfile, min_word_length=4)
    ... 
    >>> filtered = filter_anagrams(anagrams)

etc.


Test Coverage
-------------

Some basic test coverage is included:

    $ python test_anagrams.py
    ...
    ----------------------------------------------------------------------
    Ran 3 tests in 0.001s

    OK

