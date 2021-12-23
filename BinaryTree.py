import sys

class Node:
    def __init__(self,data):
        self.right = self.left = None
        self.data = data
class BinaryTree:
    def insert(self,root,data):
        if root == None:
            return Node(data)
        else:
            if data <= root.data:
                cur = self.insert(root.left,data)
                root.left = cur
            else:
                cur = self.insert(root.right,data)
                root.right = cur
        return root

    def levelOrder(self, root):
        # Breadth First Search
        height = self.height(root)
     
        for level in range(height):
            self.print_level(root, level)
            
      
    def height(self, root):
        # height of the binary tree
        if not root:
            return 0
        l_height = self.height(root.left)
        r_height = self.height(root.right)
        
        return max(l_height, r_height) + 1
    
    def print_level(self, root, level):
        if root:
            if level == 0:
                print(root.data, end=' ')
            elif level > 0:
                self.print_level(root.left, level - 1)
                self.print_level(root.right, level - 1)
            

N = int(input()) # num of nodes
myTree = BinaryTree() # new tree
root = None
for i in range(N):
    data = int(input())
    root = myTree.insert(root,data)
myTree.levelOrder(root)
