class Aglist:
    '''
    Boolean numeric aggregator list
    '''

    def __init__(self, length, items=None):
        self.items = [False] * length
        
    def insert(self, item):
        self.items[item] = True

    def remove(self, item):
        self.items[item] = False
    
    def __len__(self):
        pass

