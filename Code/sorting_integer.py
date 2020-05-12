#!python
from sorting_iterative import insertion_sort

def counting_sort(numbers):
    """Sort given numbers (integers) by counting occurrences of each number,
    then looping over counts and copying that many numbers into output list.

    Running time: O(n) or O(nlog(k)) where k is unique integers, depending
    on the particular implimentation (list/dict/tree)

    Memory usage: Approx. O(klog(n-k)) where where k is unique integers, 
                  though the log(n-k) is basically a formality"""
    min_value = 0 
    max_value = 0 

    for number in numbers:
        if number < min_value:
            min_value = number
        if number > max_value:
            max_value = number
    
    count_list = [0] * (max_value - min_value + 1)
    for number in numbers:
        count_list[number] += 1
    
    numbers.clear()
    for number, count in enumerate(count_list):
        numbers.extend([number]*count)


def bucket_sort(numbers, num_buckets=10):
    """Sort given numbers by distributing into buckets representing subranges,
    then sorting each bucket and concatenating all buckets in sorted order.
    Running time: O((n/b)^2), at n>=b it is equivalant to an O(n) counting sort
    Memory usage: O(n) add'l space"""
    min_value = 0
    max_value = 0
    bucket_list = []

    for number in numbers:
        if number < min_value:
            min_value = number
        if number > max_value:
            max_value = number
    
    bstep = (max_value - min_value) // num_buckets
    for _ in range(num_buckets):
        bucket_list.append([])
    
    for number in numbers:
        put_index = number//bstep
        if put_index >= len(bucket_list):
            put_index = len(bucket_list)-1
        bucket_list[put_index].append(number)

    for bucket in bucket_list:
        insertion_sort(bucket)

    numbers.clear()
    for bucket in bucket_list:
        numbers.extend(bucket)

    