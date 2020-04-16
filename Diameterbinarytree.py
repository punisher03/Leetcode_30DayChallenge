# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution:

    def diameterOfBinaryTree(self, root: TreeNode) -> int:
        self.ans=0
        def func(node):
            if node is None:
                return 0
            else:
                l=func(node.left)
                r=func(node.right)
                self.ans=max(l+r,self.ans)
                return 1+max(l,r)
        func(root)
        return self.ans
