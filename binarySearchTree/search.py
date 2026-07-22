#leetcode 700. Search in a Binary Search Tree
class Solution(object):
    def fun(self,root,val):
        if not root:
            return 
        if root.val==val:
            self.ans=root
            return 
        #either go left or right
        if root.val<val:
            self.searchBST(root.right,val)   
        else:
            self.searchBST(root.left,val)
        return
    def searchBST(self, root, val):
        self.ans=None
        self.fun(root,val)
        return self.ans

            