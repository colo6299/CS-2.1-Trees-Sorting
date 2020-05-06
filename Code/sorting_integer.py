#!python


def counting_sort(numbers):
    """Sort given numbers (integers) by counting occurrences of each number,
    then looping over counts and copying that many numbers into output list.

    Running time: O(n) or O(nlog(k)) where k is unique integers, depending
    on the particular implimentation (dict/tree)

    Memory usage: Approx. O(klog(n)) where where k is unique integers, 
                  though the log(n) is basically a formality"""
    # TODO: Find range of given numbers (minimum and maximum integer values)
    # TODO: Create list of counts with a slot for each number in input range
    # TODO: Loop over given numbers and increment each number's count
    # TODO: Loop over counts and append that many numbers into output list
    # FIXME: Improve this to mutate input instead of creating new output list


def bucket_sort(numbers, num_buckets=10):
    """Sort given numbers by distributing into buckets representing subranges,
    then sorting each bucket and concatenating all buckets in sorted order.
    Running time: O((n/b)^2), at n=b it is equivalant to an O(n) counting sort
    Memory usage: O(n) add'l space"""
    # TODO: Find range of given numbers (minimum and maximum values)
    # TODO: Create list of buckets to store numbers in subranges of input range
    # TODO: Loop over given numbers and place each item in appropriate bucket
    # TODO: Sort each bucket using any sorting algorithm (recursive or another)
    # TODO: Loop over buckets and append each bucket's numbers into output list
    # FIXME: Improve this to mutate input instead of creating new output list
