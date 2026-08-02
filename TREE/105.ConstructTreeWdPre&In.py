# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def func(self,preorder,low,high):
        if low>high:
            return None
        value = preorder[self.idx]
        node=TreeNode(value)
        self.idx+=1

        idd=self.hsh[node.val]
        node.left=self.func(preorder,low,idd-1)
        node.right=self.func(preorder,idd+1,high)

        return node


    def buildTree(self, preorder, inorder):
        self.hsh={}
        self.idx=0
        for i in range(0,len(inorder)):
            self.hsh[inorder[i]]=i
        return self.func(preorder,0,len(inorder)-1)
        