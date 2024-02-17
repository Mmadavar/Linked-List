class Node:
    def __init__(self, coefficient, exponent):
        self.coefficient = coefficient
        self.exponent = exponent
        self.next = None

class Polynomial:
    def __init__(self):
        self.head = None
    
    def insert(self, coefficient, exponent):
        # Create a new node
        newNode = Node(coefficient, exponent)
        # If the list is empty, or the exponent is greater than the head's exponent
        if self.head is None or exponent > self.head.exponent:
            newNode.next = self.head
            self.head = newNode
        else:
            # Traverse the list to find the right position
            current = self.head
            while current.next and current.next.exponent >= exponent:
                current = current.next
            # Insert the new node
            newNode.next = current.next
            current.next = newNode
    
    def add(self, other):
        # Create a new polynomial to store the result
        result = Polynomial()
        p1 = self.head
        p2 = other.head
        
        while p1 and p2:
            if p1.exponent == p2.exponent:
                result.insert(p1.coefficient + p2.coefficient, p1.exponent)
                p1 = p1.next
                p2 = p2.next
            elif p1.exponent > p2.exponent:
                result.insert(p1.coefficient, p1.exponent)
                p1 = p1.next
            else:
                result.insert(p2.coefficient, p2.exponent)
                p2 = p2.next
        
        # Append remaining terms
        while p1:
            result.insert(p1.coefficient, p1.exponent)
            p1 = p1.next
        while p2:
            result.insert(p2.coefficient, p2.exponent)
            p2 = p2.next
        
        return result
    
    def display(self):
        current = self.head
        while current:
            print(f"{current.coefficient}x^{current.exponent}", end=" ")
            if current.next:
                print("+", end=" ")
            current = current.next
        print()

# Example usage
poly1 = Polynomial()
poly1.insert(3, 2)
poly1.insert(5, 1)
poly1.insert(6, 0)

poly2 = Polynomial()
poly2.insert(2, 1)
poly2.insert(4, 0)

print("Polynomial 1:")
poly1.display()
print("Polynomial 2:")
poly2.display()

result = poly1.add(poly2)
print("Result of Addition:")
result.display()
