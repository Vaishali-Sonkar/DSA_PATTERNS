class Solution(object):
    def dbt(self,root):
        if root==None:
            return 0
        left=self.dbt(root.left)
        right=self.dbt(root.right)
        sm=left+right
        self.res=max(sm,self.res)
        return 1+max(left,right)
        
    def diameterOfBinaryTree(self, root):
        self.res=0
        self.dbt(root)
        return self.res