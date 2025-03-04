#Given the roots of two binary trees p and q, return true if the trees are equivalent, otherwise return false.
#Two binary trees are considered equivalent if they share the exact same structure and the nodes have the same values.

# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
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

