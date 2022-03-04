__author__ = "Brendon Taylor"
__docformat__ = 'reStructuredText'
__since__ = '05/06/2020'
__modified__ = '07/06/2020'

from typing import TypeVar, Generic
from list import SortedLinkList
K = TypeVar('K')
I = TypeVar('I')
from stack import ArrayStack


class BinarySearchListTreeNode(Generic[K, I]):
    """ Implementation of a BST List Node

    Attributes:
         key (K): the key to be stored in the node
         items (SortedLinkList[I]): the sorted list of items in the node
         left (BinarySearchListTreeNode[K, I]): pointer to left child
         right (BinarySearchListTreeNode[K, I]): pointer to right child
    """

    def __init__(self, key: K, item: I = None) -> None:
        self.key = key
        self.items = SortedLinkList()
        self.items.append(item)
        self.left = None
        self.right = None

    def __str__(self):
        """Key and associated data items"""
        return " (" + str(self.key) + ", " + str(self.items) + " ) "


class BinarySearchListTree(Generic[K, I]):
    """ Implementation of a BST using a sorted list for the item.

    Attributes:
         root (BinarySearchListTreeNode): reference to the root of the BST
    """
    def __init__(self) -> None:
        self.root = None

    def aux_getitem(self, key: K, curr: BinarySearchListTreeNode) -> SortedLinkList[I]:
        if curr is None:
            raise KeyError
        elif curr.key == key:
            return self.items
        elif key < curr.key:
            return self.aux_getitem(key, curr.left)
        else:
            return self.aux_getitem(key, curr.right)

    def __getitem__(self, key: K) -> SortedLinkList[I]:
        current = self.root
        return self.aux_getitem(key, current)

    def aux_setitem(self, new: BinarySearchListTreeNode, current: BinarySearchListTreeNode) -> None:
        if current is None:
            current = new
        elif new.key < current.key:
            if current.left == None:
                current.left = new
            else:
                self.aux_setitem(new, current.left)
        elif new.key > current.key:
            if current.right == None:
                current.right = new
            else:
                self.aux_setitem(new, current.right)


    def __setitem__(self, key: K, item: I) -> None:
        try:
            linked_lst = self.__getitem__(key)
            if not linked_lst.__contains__(item):
                linked_lst.insert(item)
        except KeyError:
            new_node = BinarySearchListTreeNode(key, item)
            current = self.root
            self.aux_setitem(new_node, current)

    def __iter__(self) -> BinarySearchListTreeIterator:
        return BinarySearchListTreeIterator(self.head)


class BinarySearchListTreeIterator:
    def __init__(self, node: BinarySearchListTreeNode) -> None:
        self.stack = ArrayStack(1000)
        self.current = node
        self.start = node

    def __iter__(self):
        return self

    def __next__(self) -> SortedLinkList:
        while self.current is not None:
            self.stack.push(self.current)
            self.current = self.current.left
        if self.stack:
            self.current = self.stack.pop()
            item = self.current
            self.current = self.current.right
            return item
        else:
            raise StopIteration

    def reset(self) -> None:
        self.__init__(self.start)

    def has_next(self) -> bool:
        if not stack and self.current is None:
            return False
        else:
            return True

    def peek(self) -> SortedLinkList:
        return self.current.items