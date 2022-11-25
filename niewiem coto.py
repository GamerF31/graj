class Node:
    def __init__(self,data,next):
        self.data = data
        self.next = next

class List:
    head=None
    tail=None
    def printlist(self):
        print("list")
        a=self.head
        while a is not None:
                print(a.data)
                a=a.next

    def append(self, data):
        node = Node(data, None)
        if self.head is None:
            self.head = self.tail = node
        else:
            self.tail.next = node
        self.tail = node

p=List()
p.append(15)
p.append(25)
p.printlist()