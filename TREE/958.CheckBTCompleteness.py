class Solution(object):
    def isCompleteTree(self, root):
        if root == None:
            return True

        q = deque()
        q.append(root)

        foundNull = False

        while q:
            node = q.popleft()

            if node == None:
                foundNull = True
            else:
                if foundNull:
                    return False

                q.append(node.left)
                q.append(node.right)

        return True