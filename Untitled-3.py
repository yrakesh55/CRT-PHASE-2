def printlevelordertraversal(root):
    if root==None:
        return
    Q=[root]
    result=[]
    while len(Q)>0:
        n=len(Q)
        subresult=[]
        for i in range(n):
            currnode=Q.pop(0)
            subresult.append(currnode.data)
            if currnode.left!=None:
                Q.append(currnode.left)
            if currnode.right!=None:
                Q.append(currnode.right)
        result.append(subresult)
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
 
printlevelordertraversal(obj1)

