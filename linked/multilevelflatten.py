https://www.geeksforgeeks.org/flatten-a-linked-list-with-next-and-child-pointers/


# A complete working Python program to find length of a
# Linked List iteratively

# Node class
class newNode:
    # Function to initialise the node object
    def __init__(self, data):
        self.data = data  # Assign data
        self.next = None  # Initialize next as null
        self.down = None


# Linked List class contains a Node object
class LinkedList:

    # Function to initialize head
    def __init__(self):
        self.root = None

    # This function is in LinkedList class. It inserts
    # a new node at the beginning of Linked List.
    # iteratively, given 'node' as starting node.


    def getCount(self,head):
        temp=head
        while temp.next!=None:
            temp=temp.next
        curr = head
        while curr!=temp:
            if curr.down:
                temp.next = curr.down
                while temp.next!=None:
                    temp=temp.next
            curr=curr.next
        while head!=None:
            print(head.data)
            head=head.next

# 1-2-3-4
#   |
#   7-8-10-12
#   | |  |
#   9 16 11
#   |  |
#   14 17-18-19-20
#   |            |
#   15-23        21
#       |
#       24

if __name__ == '__main__':
    head = newNode(10)
    head.next = newNode(5)
    head.next.next = newNode(12)
    head.next.next.next = newNode(7)
    head.next.next.next.next = newNode(11)
    head.down = newNode(4)
    head.down.next = newNode(20)
    head.down.next.next = newNode(13)
    head.down.next.down= newNode(2)
    head.down.next.next.down= newNode(16)
    head.down.next.next.down.down= newNode(3)
    head.next.next.next.down = newNode(17)
    head.next.next.next.down.down = newNode(9)
    head.next.next.next.down.down.down = newNode(19)
    head.next.next.next.down.next= newNode(6)
    head.next.next.next.down.down.next= newNode(8)
    head.next.next.next.down.down.down.next= newNode(15)
    # head.next.down.next.down.down.next.next.next.down= newNode(21)
    # head.next.down.next.next = newNode(10)
    # head.next.down.next.next.down = newNode(11)
    # head.next.down.next.next.next = newNode(12)
    llist = LinkedList()

print("Count of nodes is :", llist.getCount(head))

