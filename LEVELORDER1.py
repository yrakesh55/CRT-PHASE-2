class Node:
    def __init__(self, data):
        self.data = data 
        self.left = None 
        self.right = None
def printLevelOrderTraversal(root):
    if root == None:
        return 
    Q = [root]
    result = []
    while len(Q) > 0:
        n = len(Q)
        subResult = []
        for i in range(n):
            currNode = Q.pop(0)
            subResult.append(currNode.data)
            if currNode.left != None:
                Q.append(currNode.left)
            if currNode.right != None:
                Q.append(currNode.right)
 
        result.append(subResult)    
 
    print(result)
 
obj1 = Node(12)
obj2 = Node(5)
obj3 = Node(8)
obj4 = Node(-1)
obj5 = Node(2)
obj6 = Node(89)
obj1.left = obj2
obj1.right = obj3 
obj2.left = obj4
obj2.right = obj5
obj3.right = obj6
 
printLevelOrderTraversal(obj1)