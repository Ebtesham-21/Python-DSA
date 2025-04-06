class Node:
    def __init__(self, data): 
        self.data = data
        self.next = None

class LinkedList: 
    def __init__(self):
        self.head = None #emplty list initially

    def append(self, data):
        new_node = Node(data)

        if self.head is None:
            self.head = new_node
            return
        
        last = self.head
        while last.next:
            last = last.next

        last.next = new_node

    def display(self):
        current = self.head
        while current:
            print(current.data, end=" -> ")
            current = current.next
        print("None")

    def search(self, key):
        current = self.head
        index = 0
        while current:
            if current.data == key:
                return f"Found {key} at index {index}"
            current = current.next
            index += 1
        return f"{key} not found in the list"

li = LinkedList()
li.append(10)
li.append(20)
li.append(30)

li.display()

print(li.search(20))
print(li.search(40))