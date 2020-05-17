import sorting_iterative as SortIter
import sorting_recursive as SortRecur
import sorting_integer as SortInt
from unittest import TestCase
from random import randint


def _generate_testcase(length=10, rnge=None):
    
    if rnge is None:
        rnge = (0, length*10)

    random_list = []
    for _ in range(length):
        random_list.append(randint(rnge[0], rnge[1]))

    sorted_list = sorted(random_list)

    return random_list, sorted_list



class RandomSortTest(TestCase):
    
    def test_bubble_sort(self):
        for _ in range(100):
            random_and_sorted = _generate_testcase()
            SortIter.bubble_sort(random_and_sorted[0])
            assert random_and_sorted[0] == random_and_sorted[1]

    def test_selection_sort(self):
        for _ in range(100):
            random_and_sorted = _generate_testcase()
            SortIter.selection_sort(random_and_sorted[0])
            assert random_and_sorted[0] == random_and_sorted[1]

    def test_insertion_sort(self):
        for _ in range(100):
            random_and_sorted = _generate_testcase()
            SortIter.insertion_sort(random_and_sorted[0])
            assert random_and_sorted[0] == random_and_sorted[1]

    def test_merge_sort(self):
        for _ in range(100):
            random_and_sorted = _generate_testcase()
            SortRecur.merge_sort(random_and_sorted[0])
            assert random_and_sorted[0] == random_and_sorted[1]

    def test_counting_sort(self):
        for _ in range(100):
            random_and_sorted = _generate_testcase()
            SortInt.counting_sort(random_and_sorted[0])
            assert random_and_sorted[0] == random_and_sorted[1]  

    def test_bucket_sort(self):
        for _ in range(100):
            random_and_sorted = _generate_testcase()
            SortInt.bucket_sort(random_and_sorted[0])
            assert random_and_sorted[0] == random_and_sorted[1]  










