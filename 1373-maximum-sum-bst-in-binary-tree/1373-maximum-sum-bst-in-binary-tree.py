# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:

        ans = 0
        
        def dfs(node):
            nonlocal ans
            
            if not node:
                return True, 0, float('inf'), float('-inf')
            
            l_ok, l_sum, l_min, l_max = dfs(node.left)
            r_ok, r_sum, r_min, r_max = dfs(node.right)
            if l_ok and r_ok and l_max < node.val < r_min:
                total = l_sum + r_sum + node.val
                ans = max(ans, total)
                
                return True, total, min(l_min, node.val), max(r_max, node.val)
            
            return False, 0, 0, 0
        
        dfs(root)
        return ans
        