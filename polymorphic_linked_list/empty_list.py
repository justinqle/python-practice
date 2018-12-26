from linked_list import LinkedList

class EmptyList(LinkedList):

    def __init__(self):
        pass

    def add(value):
        return NonEmptyList(value)

    def __iter__(self):
        return self

    def __next__(self):
        raise StopIteration
