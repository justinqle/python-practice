from linked_list import LinkedList
from empty_list import EmptyList

class NonEmptyList(LinkedList):

    def __init__(self):
        self.next = EmptyList()

    def add(value):
        return self.next = 

    def __iter__(self):
        return self

    def __next__(self):
        return self.next
