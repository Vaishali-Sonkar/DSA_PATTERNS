# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isb(self,root):
        if root==None:
            return 0
        left = self.isb(root.left)
        right=self.isb(root.right)
        if abs(left-right)>1:
            self.res=False
        return 1+max(left,right)
    def isBalanced(self, root):
        self.res=True
        self.isb(root)
        return self.res

        
        