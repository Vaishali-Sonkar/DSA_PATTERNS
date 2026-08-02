class Solution(object):
    def func(self,postorder,low,high):
        if low>high:
            return None
        value = postorder[self.idx]
        node=TreeNode(value)
        self.idx-=1

        idd=self.hsh[node.val]
        node.right=self.func(postorder,idd+1,high)
        node.left=self.func(postorder,low,idd-1)

        return node


    def buildTree(self, inorder,postorder):
        self.hsh={}
        self.idx=len(postorder)-1
        for i in range(0,len(inorder)):
            self.hsh[inorder[i]]=i
        return self.func(postorder,0,len(inorder)-1)
        