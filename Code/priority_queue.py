from kv_holder import KVHolder
from binaryheap import BinaryMinHeap

class PriorityQueue:

    def __init__(self):
        self._heap = BinaryMinHeap()
        self._max_priority = 0
        self._min_priority = 0

    def _update_minmax(self, priority):
        if priority > self._max_priority:
            self._max_priority = priority
        if priority < self._min_priority:
            self._min_priority = priority

    @property
    def size(self):
        return self._heap.size

    @property
    def front(self):
        if self.is_empty() is False:
            return self._heap.get_min().value
        else:
            return None

    def dequeue(self):
        return self._heap.delete_min().value

    def enqueue(self, item):
        self.insert_back(item)

    def push_pop(self, item):
        self.insert_back(item)
        return self._heap.delete_min().value

    def is_empty(self):
        return self._heap.is_empty()

    def insert(self, item, priority):
        self._heap.insert(KVHolder(priority, item))
        self._update_minmax(priority)

    def insert_front(self, item):
        priority = self._min_priority - 1
        self.insert(item, priority)

    def insert_back(self, item):
        priority = self._max_priority + 1
        self.insert(item, priority)
