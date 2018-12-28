from linked_list import LinkedList
from empty_list import EmptyList
from non_empty_list import NonEmptyList

li = EmptyList()
for i in range(1, 4):
    li.add(i)
for elem in li:
    print(elem)
