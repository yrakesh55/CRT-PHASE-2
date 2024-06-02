class Node:
    def __init__(self, data):
        self.data = data 
        self.next = None 
 
def printLinkedList(head):
    currentNode = head 
    while currentNode != None:
        print(currentNode.data, end = " --> ")
        currentNode = currentNode.next
    print()
 
def deletetrailnode(head):
    if head == None:
        return None
    previous=None
    currentnode=head
 
    while currentnode.next != None:
        previous = currentnode
        currentnode=currentnode.next
    previous.next = None
    return head
 
 
nums = [10, 20, 30, 40, 50, 60, 70, 80, 90, 100]
head = None 
for ele in nums:
    head = deletetrailnode(head)
    printLinkedList(head)
print("Final linked list is:")
printLinkedList(head)