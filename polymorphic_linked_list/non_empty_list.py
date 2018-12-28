from linked_list import LinkedList
from empty_list import EmptyList

class NonEmptyList(LinkedList):

    def __init__(self, data):
        self.data = data
        self.next = None

    def add(value):
        self.next = self.next.add(value)

    def __iter__(self):
        return self

    def __next__(self):
        return self.next
