class LinkedList:


    class Node:


        def __init__(self, data, after=None):
            self.data = data
            self.after = after


    def __init__(self):
        self.head = None

    def append(self, data):
        prev = None
        curr = self.head;
        while curr is not None:
            prev = curr
            curr = curr.after
        if (prev is None):
            self.head = self.Node(data)
        else:
            prev.after = self.Node(data)

    def __str__(self):
        string = "["
        curr = self.head
        while curr is not None:
            string += str(curr.data)
            curr = curr.after
        string += "]"
        return string


if __name__ == "__main__":
    ll = LinkedList()
    for i in range(1, 4):
        ll.append(i)
    print(ll)
