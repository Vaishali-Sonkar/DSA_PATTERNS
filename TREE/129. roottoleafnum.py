# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def ps(self,root,sm):
        if root==None:
            return
        sm=sm*10 + root.val
        if root.left==None and root.right==None:
            self.res+=sm
            return
        self.ps(root.left,sm)
        self.ps(root.right,sm)
    def sumNumbers(self, root):
        self.res=0
        self.ps(root,0)
        return self.res
        