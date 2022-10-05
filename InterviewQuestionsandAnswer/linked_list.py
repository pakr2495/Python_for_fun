class Node():
    def __init__(self, data=None, next=None) -> None:
        self.data = data
        self.next = next

class Linkedlist():
    def __init__(self) -> None:
        self.head = None

    def insert_value_begining(self,data):
        self.head = Node(data=data, next=self.head)

    def display(self):
        if self.head == None:
            print("empty list")
            return
        op = ""
        temp = self.head
        while temp:
            op = op + str(temp.data) +'----->'
            temp = temp.next
        print(op)
        return 

    def insert_end(self,data):
        if self.head is None:
            self.head = Node(data=data,next=None)
            return
        node = self.head
        while node.next:
            node = node.next
        node.next = Node(data=data,next=None)

    def length_linkedlist(self):
        if self.head is None:
            return 0
        node = self.head
        count = 0
        while node:
            count = count + 1
            node = node.next
        return count

    def remove(self,index):
        if index<0 or index>=(self.length_linkedlist()):
            return "Error"
        if index == 0:
            node = self.head
            self.head = node.next
        else:
            count = 0
            node = self.head
            while node.next:
                if count == index - 1:
                    node.next = node.next.next
                    break
                node = node.next
                count = count + 1


if __name__ == "__main__":
    ll = Linkedlist()
    ll.display()
    print(ll.length_linkedlist())
    ll.insert_end(5)
    ll.insert_end(3)
    ll.insert_end(2)
    ll.insert_end(4)
    ll.display()
    print(ll.length_linkedlist())
    ll.remove(0)
    ll.display()
