from linked_list import LinkedList
from non_empty_list import NonEmptyList

class EmptyList(LinkedList):

    def __init__(self):
        pass

    def add(self, value):
        return NonEmptyList(value)

    def __iter__(self):
        return self

    def __next__(self):
        raise StopIteration
