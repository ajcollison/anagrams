#!/usr/bin/env python3
"""Performance tests for anagrams functions."""

try:
    import numpy
except ImportError:
    pass
try:
    import matplotlib.pyplot as pyplot
except ImportError:
    pyplot = None
import timeit
from anagrams import collect_anagrams


def trimmed_source(source, max_count):
    """Trim the source to the specified length."""

    count = 0
    for item in source:
        count += 1
        if count > max_count:
            break

        yield item


def test_collect_anagrams(max_count):
    """Run the `anagrams.collect_anagrams` function on the source data."""

    source = open('/usr/share/dict/words')
    collect_anagrams(trimmed_source(source, max_count))
    source.close()


def _main():
    """Run the tests."""

    times = []
    counts = list(range(25000, 275000, 25000))
    repeat = 3

    for count in counts:
        times.append(timeit.timeit("test_collect_anagrams(%s)" % count,
                                   number=repeat,
                                   setup="from __main__ import test_collect_anagrams"))

    print("Word Count\t\tTime")
    for count, time in zip(counts, times):
        print("    {0:6}\t\t{1:2.2f}".format(count, time))

    if numpy:
        xcoord = numpy.array([count / 25000. for count in counts])
        ycoord = numpy.array(times)
        zcoord = numpy.polyfit(xcoord, ycoord, 1)

        print("Slope: {0:2.2f}, intercept: {1:2.2f}".format(zcoord[0], zcoord[1]))

        if pyplot:
            poly = numpy.poly1d(zcoord)
            plotx = numpy.linspace(0, xcoord[-1], 100)
            pyplot.xlabel("Multiples of 25,000 Words")
            pyplot.ylabel("Execution Time")
            pyplot.plot(xcoord, ycoord, '.', plotx, poly(plotx), '-')
            pyplot.show()


if __name__ == '__main__':

    _main()
