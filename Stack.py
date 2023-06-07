


from numpy import delete


class Node:
    def __init__(self, data=None):
        self.value = data
        self.next = None


class LinkedList:
    def __init__(self):
        self.head = None
        self.tail = None

    def __str__(self):
        ret_str = '['
        temp = self.head
        while temp is not None:
            ret_str += str(temp.value) + ', '
            temp = temp.next

        ret_str = ret_str.rstrip(', ')
        ret_str += ']'
        return ret_str

    def createList(self, value):
        if self.head is None:
            self.head = Node(value)
            self.temp = self.head
            return

        self.temp.next = Node(value)
        self.temp = self.temp.next

    def gettail(self):
        while(self.temp.next is not None):
            self.tail = self.temp
            return

    def insertion(self, value):
        newNode = Node(value)
        index = int(input("Enter key on which you want to insert:  "))
        if(index == self.head.value):
            newNode.next = self.head
            self.head = newNode
            return
        self.temp = self.head
        while(self.temp is not None):

            if(self.temp.next.value == index):
                if(self.temp.next is None):
                    self.temp.next = newNode
                    self.temp = self.temp.next
                    return

            if(self.temp.next.value == index):
                newNode = Node(value)
                newNode.next = self.temp.next
                self.temp.next = newNode
                return

            self.temp = self.temp.next

    def deletion(self, value):
        index = int(input("Enter value to delete:  "))
        if(index == self.head.value):
            temp1 = self.head
            self.head = self.head.next
            temp1 = None
            return
        self.temp = self.head
        while(self.temp is not None):

            if(self.temp.next.value == index):
                if(self.temp.next is None):
                    self.temp.value = None
                    return

            if(self.temp.next.value == index):
                temp1 = self.temp.next
                self.temp.next = self.temp.next.next
                temp1 = None
                return

            self.temp = self.temp.next

    def push(self, value):
        if(self.head == None):
            self.head = Node(value)
            return
        
        temp1 = Node(value)
        temp1.next = self.head
        self.head = temp1

    def pop(self):
        delete = self.head
        self.head = self.head.next
        delete.value = None
        del delete


l1 = LinkedList()
l1.push(1)
l1.push(2)
l1.push(3)
l1.pop()
l1.push(4)
l1.push(5)

l1.pop()

print(l1)