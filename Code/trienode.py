#!python3


class PrefixTreeNode:

    CHILDREN_TYPE = list
    def __init__(self, character=None, terminal=False, size=26):
        """Initialize this prefix tree node with the given character value, an
        empty structure of children nodes, and a boolean terminal property."""
        # Character that this node represents
        self.character = character
        # Data structure to associate character keys to children node values
        self.children = [None] * size
        # Marks if this node terminates a string in the prefix tree
        self.terminal = terminal

    def is_terminal(self):
        return self.terminal 

    def num_children(self):
        count = 0
        for space in self.children:
            if space is not None:
                count += 1
        return count

    def has_child(self, character):
        alpha_ordinal = ord(character) - 65
        if self.children[alpha_ordinal] is not None:
            return True
        else:
            return False

    def get_child(self, character):
        """Return this prefix tree node's child node that represents the given
        character if it is amongst its children, or raise ValueError if not."""
        if self.has_child(character):
            alpha_ordinal = ord(character) - 65
            return self.children[alpha_ordinal]
        else:
            raise ValueError(f'No child exists for character {character!r}')

    def get_children(self):
        retlist = []
        for space in self.children:
            if space is not None:
                retlist.append(space)
        return retlist

    def add_child(self, character, child_node):
        """Add the given character and child node as a child of this node, or
        raise ValueError if given character is amongst this node's children."""
        if not self.has_child(character):
            alpha_ordinal = ord(character) - 65
            self.children[alpha_ordinal] = child_node
        else:
            raise ValueError(f'Child exists for character {character!r}')

    def __repr__(self):
        """Return a code representation of this prefix tree node."""
        return f'PrefixTreeNode({self.character!r})'

    def __str__(self):
        """Return a string view of this prefix tree node."""
        return f'({self.character})'
