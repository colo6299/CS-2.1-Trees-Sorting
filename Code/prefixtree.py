#!python3

from trienode import PrefixTreeNode


class PrefixTree:
    """PrefixTree: A multi-way prefix tree that stores strings with efficient
    methods to insert a string into the tree, check if it contains a matching
    string, and retrieve all strings that start with a given prefix string.
    Time complexity of these methods depends only on the number of strings
    retrieved and their maximum length (size and height of subtree searched),
    but is independent of the number of strings stored in the prefix tree, as
    its height depends only on the length of the longest string stored in it.
    This makes a prefix tree effective for spell-checking and autocompletion.
    Each string is stored as a sequence of characters along a path from the
    tree's root node to a terminal node that marks the end of the string."""

    # Constant for the start character stored in the prefix tree's root node
    START_CHARACTER = ''

    def __init__(self, strings=None):
        """Initialize this prefix tree and insert the given strings, if any."""
        # Create a new root node with the start character
        self.root = PrefixTreeNode(PrefixTree.START_CHARACTER)
        # Count the number of strings inserted into the tree
        self.size = 0
        # Insert each string, if any were given
        if strings is not None:
            for string in strings:
                self.insert(string)

    def __repr__(self):
        """Return a string representation of this prefix tree."""
        return f'PrefixTree({self.strings()!r})'

    def is_empty(self):
        """Return True if this prefix tree is empty (contains no strings)."""
        if self.root.num_children() == 0:
            return True
        else:
            return False

    def contains(self, string):
        """Return True if this prefix tree contains the given string."""
        return self.contains_recursive(self.root, string)
        
    # watch for recursion depth!!!  long word bad >:(
    def contains_recursive(self, node, tail):
        if node.has_child(tail[0]):
            if len(tail) == 1:
                if node.get_child(tail[0]).terminal is True:
                    return True
                else:
                    return False
            next_node = node.get_child(tail[0])
            return self.contains_recursive(next_node, tail[1:]) 
        else:
            return False

    def insert(self, string):
        """Insert the given string into this prefix tree."""
        self.insert_recursive(self.root, string)
        
    def insert_recursive(self, node, tail):
        string = tail
        first_char = string[0]
        if not node.has_child(first_char):
            if len(tail) == 1:
                node.add_child(first_char, PrefixTreeNode(first_char, True))
                self.size += 1
                return
            else:
                next_node = PrefixTreeNode(first_char)
                node.add_child(first_char, next_node)
                self.insert_recursive(next_node, tail[1:])
        else:
            next_node = node.get_child(first_char)
            if len(string) == 1:
                if next_node.terminal is not True:
                    next_node.terminal = True
                    self.size += 1
            else:
                self.insert_recursive(next_node, tail[1:])

    def _find_node(self, string):
        """Return a pair containing the deepest node in this prefix tree that
        matches the longest prefix of the given string and the node's depth.
        The depth returned is equal to the number of prefix characters matched.
        Search is done iteratively with a loop starting from the root node."""
        # Match the empty string
        if len(string) == 0:
            return self.root, 0
        # Start with the root node
        node = self.root
        # TODO

    def complete(self, prefix):
        """Return a list of all strings stored in this prefix tree that start
        with the given prefix string."""
        # Create a list of completions in prefix tree
        completions = []
        # TODO

    def strings(self):
        """Return a list of all strings stored in this prefix tree."""
        # Create a list of all strings in prefix tree
        all_strings = []
        charlists = []
        self._strings_recursive(self.root, [], charlists)
        for charlist in charlists:
            all_strings.append(''.join(charlist)) # I don't remember if that's how you do it lol
        return all_strings                        # UDPATE: It wasn't.
            
    def _strings_recursive(self, node, charlist, outlist):
        charlist.append(node.character)
        if node.terminal:
            outlist.append(list(charlist))
        for child in node.get_children():  # I had a thing for all the extra lists made, but I deleted it
            self._strings_recursive(child, list(charlist), outlist)

    def _traverse(self, node, prefix, visit):
        """Traverse this prefix tree with recursive depth-first traversal.
        Start at the given node with the given prefix representing its path in
        this prefix tree and visit each node with the given visit function."""
        # TODO


def create_prefix_tree(strings):
    print(f'strings: {strings}')

    tree = PrefixTree()
    print(f'\ntree: {tree}')
    print(f'root: {tree.root}')
    print(f'strings: {tree.strings()}')

    print('\nInserting strings:')
    for string in strings:
        tree.insert(string)
        print(f'insert({string!r}), size: {tree.size}')

    print(f'\ntree: {tree}')
    print(f'root: {tree.root}')

    print('\nSearching for strings in tree:')
    for string in sorted(set(strings)):
        result = tree.contains(string)
        print(f'contains({string!r}): {result}')

    print('\nSearching for strings not in tree:')
    prefixes = sorted(set(string[:len(string)//2] for string in strings))
    for prefix in prefixes:
        if len(prefix) == 0 or prefix in strings:
            continue
        result = tree.contains(prefix)
        print(f'contains({prefix!r}): {result}')

    print('\nCompleting prefixes in tree:')
    for prefix in prefixes:
        completions = tree.complete(prefix)
        print(f'complete({prefix!r}): {completions}')

    print('\nRetrieving all strings:')
    retrieved_strings = tree.strings()
    print(f'strings: {retrieved_strings}')
    matches = set(retrieved_strings) == set(strings)
    print(f'matches? {matches}')


if __name__ == '__main__':
    # Create a dictionary of tongue-twisters with similar words to test with
    tongue_twisters = {
        'Seashells': 'Shelly sells seashells by the sea shore'.split(),
        # 'Peppers': 'Peter Piper picked a peck of pickled peppers'.split(),
        # 'Woodchuck': ('How much wood would a wood chuck chuck'
        #                ' if a wood chuck could chuck wood').split()
    }
    # Create a prefix tree with the similar words in each tongue-twister
    for name, strings in tongue_twisters.items():
        print('\n' + '='*80 + '\n')
        print(f'{name} tongue-twister:')
        create_prefix_tree(strings)
