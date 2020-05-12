
class KVHolder:

    def __init__(self, key, value):
        self.key = key
        self.value = value

    def __gt__(self, value):
        return self.key > value

    def __lt__(self, value):
        return self.key < value

    def __eq__(self, value):
        return self.key == value
