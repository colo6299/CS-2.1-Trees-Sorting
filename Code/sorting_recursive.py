#!python
from sorting_iterative import insertion_sort, bubble_sort
from random import random

def merge(items1, items2):
    """Merge given lists of items, each assumed to already be in sorted order,
    and return a new list containing all items in sorted order.
    TODO: Running time: O(n+m) where the variables correspond to the lengths of the lists.
    TODO: Memory usage: O(n) add'l space in this case"""
    retlist = []
    ndx1 = 0
    ndx2 = 0
    while ndx1 is not len(items1) and ndx2 is not len(items2):
        if items1[ndx1] > items2[ndx2]:
            retlist.append(items2[ndx2])
            ndx2 += 1
        else:
            retlist.append(items1[ndx1])
            ndx1 += 1
    if ndx1 == len(items1):
        retlist.extend(items2[ndx2:])
    if ndx2 == len(items2):
        retlist.extend(items1[ndx1:])
    return retlist


def split_sort_merge(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each with an iterative sorting algorithm, and merging results into
    a list in sorted order.
    TODO: Running time: O(n) when sorted, O(n^2) average and worst(reverse sort)
    TODO: Memory usage: O(n) add'l space"""
    center = len(items) // 2
    items1 = items[:center]
    items2 = items[center:]

    insertion_sort(items1)
    insertion_sort(items2)

    items.clear()
    items.extend(merge(items1, items2))


def merge_sort(items):
    """Sort given items by splitting list into two approximately equal halves,
    sorting each recursively, and merging results into a list in sorted order.
    TODO: Running time: O(nlog(n)) average/worst
    TODO: Memory usage: lots and lots. Will fix shortly."""

    items2 = _merge_sort_helper(items)
    items.clear()
    items.extend(items2)

def _merge_sort_helper(items):

    if items is None:
        return []

    if len(items) <= 3:
        bubble_sort(items)
        return items

    center = len(items) // 2
    items1 = items[:center]
    items2 = items[center:]

    return merge(_merge_sort_helper(items1), _merge_sort_helper(items2))


def partition(items, low, high):  
    """Return index `p` after in-place partitioning given items in range
    `[low...high]` by choosing a pivot (centerpoint with small random offset) from
    that range, moving pivot into index `p`, items less than pivot into range
    `[low...p-1]`, and items greater than pivot into range `[p+1...high]`.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""

    pivot = items[(high + low) // 2]  # do the randy bits
    back = low
    p_index = 0
    for front in range(low, high):
        p_index = front
        if items[front] > pivot: 
            if back <= front:    
                back = front     
            while back < high and not items[back] < pivot:
                back += 1
            if back == high:
                return p_index
            items[front], items[back] = items[back], items[front]
    return p_index + 1


def quick_sort(items, low=None, high=None):
    """Sort given items in place by partitioning items in range `[low...high]`
    around a pivot item and recursively sorting each remaining sublist range.
    TODO: Best case running time: ??? Why and under what conditions?
    TODO: Worst case running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    if low is None:
        low = 0
    if high is None:
        high = len(items)
    #print(high-low)
    if (high - low) <= 1:
        return
    mid = partition(items, low, high)
    quick_sort(items, low, mid)
    quick_sort(items, mid, high)
    


# NOTE: NOT MY CODE, USING FOR LEARNING PURPOSES
def slow_sort(list_in, i=0, j=None):
    n = len(list_in)
    if n == 1:
        return list_in
    mid = n // 2
    mx = max(slow_sort(list_in[:mid])[-1], slow_sort(list_in[mid:])[-1])
    list_in.remove(mx)
    return slow_sort(list_in) + [mx]

if __name__ == "__main__":
    ls = [4, 2]
    print('\np_index: ' + str(partition(ls, 0, len(ls))))
   # print('\np_index: ' + str(quick_sort(ls)))
    print(ls)