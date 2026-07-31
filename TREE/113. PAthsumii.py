# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def ps(self,root,sm,target,path):
        if root==None:
            return
        sm+=root.val
        path.append(root.val)
        if root.left==None and root.right==None:
            if sm==target:
                self.ans.append(path[:])
        self.ps(root.left,sm,target,path)
        self.ps(root.right,sm,target,path)
        path.pop()
    def pathSum(self, root, targetSum):
        self.ans=[]
        self.ps(root,0,targetSum,[])
        return self.ans
        