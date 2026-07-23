# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):

    #assuming p.val<q.val for making the code simple and eaisly addaptable
    def fun(self,root,p,q):
        if root==None:
            return self.ans
        #self
        if root==p or root==q:
            self.ans=root
            return
        if root.val<p.val:
            self.fun(root.right,p,q)
        elif root.val>q.val:
            self.fun(root.left,p,q)
        #middle of the two nodes
        else:
            self.ans=root
            return
    def lowestCommonAncestor(self, root, p, q):

        self.ans=None
        #as p<q is not always true we need to check and call the function accordingly
        if p.val<q.val:     
            self.fun(root,p,q)
        #swapped the values of p and q to make p<q
        else:
            self.fun(root,q,p)
        return self.ans