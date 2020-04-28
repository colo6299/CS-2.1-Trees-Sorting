#!python
from sorting_iterative import insertion_sort, bubble_sort

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
    `[low...high]` by choosing a pivot (TODO: document your method here) from
    that range, moving pivot into index `p`, items less than pivot into range
    `[low...p-1]`, and items greater than pivot into range `[p+1...high]`.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Choose a pivot any way and document your method in docstring above
    # TODO: Loop through all items in range [low...high]
    # TODO: Move items less than pivot into front of range [low...p-1]
    # TODO: Move items greater than pivot into back of range [p+1...high]
    # TODO: Move pivot item into final position [p] and return index p

def quick_sort(items, low=None, high=None):
    """Sort given items in place by partitioning items in range `[low...high]`
    around a pivot item and recursively sorting each remaining sublist range.
    TODO: Best case running time: ??? Why and under what conditions?
    TODO: Worst case running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Check if high and low range bounds have default values (not given)
    # TODO: Check if list or range is so small it's already sorted (base case)
    # TODO: Partition items in-place around a pivot and get index of pivot
    # TODO: Sort each sublist range by recursively calling quick sort

if __name__ == "__main__":
    ls = [1, 5, 6, 2, 3, 4]
    
    print('\nlist is: ' + str(split_sort_merge(ls)))