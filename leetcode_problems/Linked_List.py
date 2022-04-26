class Node:
    def __init__(self, value):
        self.next = None
        self.prev = None
        self.value = value


class LinkList:
    def __init__(self) -> None:
        self.head = None
        self.tail = None
        self.size = 0

    def add(self, value):
        node = Node(value)
        if self.tail is None:
            self.head = node
            self.tail = node
            self.size += 1
        else:
            self.tail.next = node
            node.prev = self.head
            self.tail = node
            self.size += 1
    def __str__(self) -> str:
        vals = []
        node = self.head
        while node is not None:
            vals.append(node.value)
            node = node.next
        return f"[{','.join(str(val) for val in vals)}]"


mylist = LinkList()
mylist.add(1)
mylist.add(2)
mylist.add(3)


print(mylist)