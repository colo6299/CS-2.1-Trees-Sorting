#!python


def is_sorted(list_in):
    for index, item in enumerate(list_in):
        if index == len(list_in) - 1:
            return True
        if list_in[index + 1] is not None:
            if item > list_in[index + 1]:
                return False
    return True

def bubble_sort(items, descending=False):
    """Sort given items by swapping adjacent items that are out of order, and
    repeating until all items are in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    
    finished = False
    while finished is False:
        has_swapped = False
        for index, item in enumerate(item):
            if index is 0:
                continue
            if descending:
                if item > items[index-1]:
                    items[index] = items[index-1]
                    items[index-1] = item
                    has_swapped = True
            else:
                if item < items[index-1]:
                    items[index] = items[index-1]
                    items[index-1] = item
                    has_swapped = True
        if has_swapped is False:
            finished = True

def selection_sort(items, descending=False):
    """Sort given items by finding minimum item, swapping it with first
    unsorted item, and repeating until all items are in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""

    if descending:  # What does DRY stand for, anyway?
        for index in range(len(items)):
            maximum_ndx = index
            for p_index in range(index+1, len(items)):
                if items[p_index] > items[maximum_ndx]:
                    maximum_ndx = p_index
            items[index], items[maximum_ndx] = items[maximum_ndx], items[index]

    else:          # What does DRY stand for, anyway?
        for index in range(len(items)):
            minimum_ndx = index
            for p_index in range(index+1, len(items)):
                if items[p_index] < items[minimum_ndx]:
                    minimum_ndx = p_index
            items[index], items[minimum_ndx] = items[minimum_ndx], items[index]


def insertion_sort(items):
    """Sort given items by taking first unsorted item, inserting it in sorted
    order in front of items, and repeating until all items are in order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    # TODO: Repeat until all items are in sorted order
    # TODO: Take first unsorted item
    # TODO: Insert it in sorted order in front of items
