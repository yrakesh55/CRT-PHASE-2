# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def deleteNode(self, root, key):
        if root == None:
            return None 
        elif root.val > key:
            # If root value is greater than node to be deleted
            root.left = self.deleteNode(root.left, key)
        elif root.val < key:
            # If root value is lesser than node to be deleted
            root.right = self.deleteNode(root.right, key)
        else:
            # If root value is equal to node to be deleted
 
            # category-1 (Node with 0 children)
            if root.left == None and root.right == None:
                return None
 
            # category-2 (Node with 1 children) 
            if root.left == None:
                return root.right 
            elif root.right == None:
                return root.left
 
            # category-3 (Node with 2 children)
            # Finding inorder successor 
            curr = root.right 
            while curr.left != None:
                curr = curr.left 
 
            # Once inorder successor is found, we need to replace the value 
            root.val = curr.val 
            root.right = self.deleteNode(root.right, curr.val)
        return root


 

