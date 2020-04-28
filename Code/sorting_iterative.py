#!python


def is_sorted(list_in):
    for index, item in enumerate(list_in):
        if index == len(list_in) - 1:
            return True
        if list_in[index + 1] is not None:
            if item > list_in[index + 1]:
                return False
    return True

def bubble_sort(items, descending=False, comparison=lambda a, b: a > b):
    """Sort given items by swapping adjacent items that are out of order, and
    repeating until all items are in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""

    finished = False
    while finished is False:
        has_swapped = False
        for index, item in enumerate(items):
            if index is 0:
                continue
            if descending:
                if comparison(item, items[index-1]):  # What does DRY stand for, anyway?
                    items[index] = items[index-1]
                    items[index-1] = item
                    has_swapped = True
            else:
                if comparison(items[index-1], item):  # What does DRY stand for, anyway?
                    items[index] = items[index-1]
                    items[index-1] = item
                    has_swapped = True
        if has_swapped is False:
            finished = True

def cocktail_shaker_sort(items, descending=False, comparison=lambda a, b: a > b):
    """Sort given items by shaking the list really hard.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""

    finished = False
    while finished is False:
        has_swapped = False
        for index, item in enumerate(items):
            if index is 0:
                continue
            if descending:
                if comparison(item, items[index-1]):   # What does DRY stand for, anyway?
                    items[index] = items[index-1]
                    items[index-1] = item
                    has_swapped = True
            else:
                if comparison(items[index-1], item):   # What does DRY stand for, anyway?
                    items[index] = items[index-1]
                    items[index-1] = item
                    has_swapped = True

        for index in range(len(items) -1, -1, -1):
            item = items[index]
            if index is 0:
                continue
            if descending:
                if comparison(item, items[index-1]):   # What does DRY stand for, anyway?
                    items[index] = items[index-1]
                    items[index-1] = item
                    has_swapped = True
            else:
                if comparison(items[index-1], item):   # What does DRY stand for, anyway?
                    items[index] = items[index-1]
                    items[index-1] = item
                    has_swapped = True

        if has_swapped is False:
            finished = True

def selection_sort(items, descending=False, comparison=lambda a, b: a > b):
    """Sort given items by finding minimum item, swapping it with first
    unsorted item, and repeating until all items are in sorted order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""

    if descending:  # What does DRY stand for, anyway?
        for index in range(len(items)):
            maximum_ndx = index
            for p_index in range(index+1, len(items)):
                if comparison(items[p_index], items[maximum_ndx]):
                    maximum_ndx = p_index
            items[index], items[maximum_ndx] = items[maximum_ndx], items[index]

    else:          # What does DRY stand for, anyway?
        for index in range(len(items)):
            minimum_ndx = index
            for p_index in range(index+1, len(items)):
                if comparison(items[minimum_ndx], items[p_index]):
                    minimum_ndx = p_index
            items[index], items[minimum_ndx] = items[minimum_ndx], items[index]

def insertion_sort(items, descending=False, comparison=lambda a, b: a > b):
    """Sort given items by taking first unsorted item, inserting it in sorted
    order in front of items, and repeating until all items are in order.
    TODO: Running time: ??? Why and under what conditions?
    TODO: Memory usage: ??? Why and under what conditions?"""
    
    for index in range(1, len(items)):
        _insertion_helper(items, index, items[index], descending, comparison)

def _insertion_helper(list_in, sublist_index, item, descending=False, comparison=lambda a, b: a > b):
    '''
    Handles insertion into sorted sublist during insertion sort. 

    sublist_index should equal working index.
    '''
    insert_index = _binary_locator(list_in, 0, sublist_index, item, descending, comparison)
    slide_index = sublist_index
    while slide_index is not insert_index and slide_index is not 0:
        list_in[slide_index] = list_in[slide_index-1]
        slide_index -= 1
    list_in[insert_index] = item


def _binary_locator(list_in, lower_index, upper_index, item, descending=False, comparison=lambda a, b: a > b):
    '''
    Helper helper... recursive binary search for index

    definitely going to need tweaking
    '''
    if upper_index == lower_index:
        return upper_index

    if descending:
        center = (lower_index + upper_index) // 2  # stable for descending
        if comparison(item, list_in[center]):  # What does DRY stand for, anyway?
            upper_index = center - 1
        elif comparison(list_in[center], item):
            lower_index = center
        else:
            return center     

    else:
        center = (lower_index + upper_index) // 2  # not stable for ascending, make it round up
        if comparison(list_in[center], item):  # What does DRY stand for, anyway?
            upper_index = center
        elif list_in[center] == item:  
            return center
        else:
            lower_index = center + 1    

    return _binary_locator(list_in, lower_index, upper_index, item, descending)
