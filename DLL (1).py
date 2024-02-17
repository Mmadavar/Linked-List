class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class DLL:
    def __init__(self):
        self.head = None
       
    
    def append(self, data):

        if self.head is None:
            new = Node(data)
            self.head = new
            new.prev = None
            
        else:
            new = Node(data)
            curr = self.head
            while curr.next:
                curr = curr.next
            curr.next = new
            new.prev = curr
            new.next = None

    def print(self):
        curr = self.head
        while curr != None:
            print(curr.data)
            curr = curr.next
    
    def reverse(self):
        
        curr = self.head
        temporary = None
        while curr:
            temporary = curr.prev
            curr.prev = curr.next
            curr.next = temporary
            curr = curr.prev
            
        if temporary:
            self.head = temporary.prev

    
    
d = DLL()
d.append(1)
d.append(4)
d.append(3)
d.append(9)
d.reverse()
d.print()

    
   
