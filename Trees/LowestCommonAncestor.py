#Given a binary search tree (BST) where all node values are unique, and two nodes from the tree p and q, return the lowest common ancestor (LCA) of the two nodes.
#The lowest common ancestor between two nodes p and q is the lowest node in a tree T such that both p and q as descendants. The ancestor is allowed to be a descendant of itself.
# Definition for a binary tree node.
from typing import Optional
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def lowestCommonAncestor(self, root: TreeNode, p: TreeNode, q: TreeNode) -> TreeNode:
        ppath = []
        qpath = []
        ppath = self.dfs(root, [], p)
        qpath = self.dfs(root, [], q)
        a = root
        i = 0
        while i<min(len(ppath), len(qpath)):
            if ppath[i].val==qpath[i].val:
                a = ppath[i]
            else:
                break
            i = i+1
        return a
        
    def dfs(self, node, path, num):
        if node != None:
            newpath = path.copy()
            newpath.append(node)
            if node.val==num.val:
                return newpath
            else:
                a = self.dfs(node.left, newpath, num)
                b = self.dfs(node.right, newpath, num)
                if a!=None:
                    return a
                elif b!= None:
                    return b
                else:
                    return None
        return None