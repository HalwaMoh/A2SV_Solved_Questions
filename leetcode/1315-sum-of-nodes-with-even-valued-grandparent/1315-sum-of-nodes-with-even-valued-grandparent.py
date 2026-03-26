# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def sumEvenGrandparent(self, root):
        def solve(node,parent,gparent):
            if node is None:
                return 0
            ans = 0
            if gparent and gparent.val % 2 == 0:
                ans += node.val
            left_child=solve(node.left,node,parent)
            right_child=solve(node.right,node,parent)
            return ans+ left_child + right_child
        return solve(root, None, None)




