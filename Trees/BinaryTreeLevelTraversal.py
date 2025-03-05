#Given a binary tree root, return the level order traversal of it as a nested list,
#where each sublist contains the values of nodes at a particular level in the tree, from left to right.

# Definition for a binary tree node.
from typing import Optional, List
class TreeNode:
    def __init__(self, val=0, left=None, right=None):
        self.val = val
        self.left = left
        self.right = right

class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ret = []
        stack = []
        nextlayer = []
        layervals = []
        stack.append(root)

        while stack!=[]:
            node = stack.pop(0)
            if node!=None:
                layervals.append(node.val)
                nextlayer.append(node.left)
                nextlayer.append(node.right)
            if stack==[] and nextlayer!=[]:
                stack = nextlayer
                nextlayer = []
                ret.append(layervals)
                layervals = []
        return ret  