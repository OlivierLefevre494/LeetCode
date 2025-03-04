# Given the roots of two binary trees root and subRoot, 
# return true if there is a subtree of root with the same structure and node values of subRoot and false otherwise.
# A subtree of a binary tree tree is a tree that consists of a node in tree and 
# all of this node's descendants. The tree tree could also be considered as a subtree of itself.
#SOLUTION TIME COMPELXITY O(M*N) M NUM OF NODES IN ROOT AND N NUM OF NODES IN SUBROOT
# SOLUTION SPACE COMPLEXITY O(M+N) M NUM OF NODES IN ROOT AND N NUM OF NODES IN SUBROOT
from typing import Optional

# Definition for a binary tree node.
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:   
    def isSubtree(self, root: Optional[TreeNode], subRoot: Optional[TreeNode]) -> bool:
        if root==None and subRoot==None:
            return True
        stack=[]
        visited = set()
        stack.append(root)
        while stack != []:
            node = stack.pop()
            if node not in visited:
                visited.add(node)
                if node.left!=None:
                    stack.append(node.left)
                if node.right!=None:
                    stack.append(node.right)
                if self.isSameTree(node, subRoot)==True:
                    return True
        return False

            
        

    def isSameTree(self, p: Optional[TreeNode], q: Optional[TreeNode]) -> bool:
        pstack = []
        qstack = []
        if p != None:
            pstack.append(p.val)
        if q != None:
            qstack.append(q.val)
        self.bfs(p, pstack)
        self.bfs(q,qstack)
        return (pstack==qstack)

    def bfs(self, p, stack):
        if p==None: return 0
        if p.left != None:
            stack.append(p.left.val)
        else:
            stack.append(None)
        if p.right != None:
            stack.append(p.right.val)
        else:
            stack.append(None)
        self.bfs(p.left, stack)
        self.bfs(p.right, stack)