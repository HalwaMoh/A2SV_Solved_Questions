# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def pathSum(self, root, targetSum):
        prefix = {0: 1}
        count = [0]
        
        def dfs(node, curr_sum):
            if not node:
                return
            
            curr_sum += node.val
            
            count[0] += prefix.get(curr_sum - targetSum, 0)
            
            prefix[curr_sum] = prefix.get(curr_sum, 0) + 1
            
            dfs(node.left, curr_sum)
            dfs(node.right, curr_sum)
            
            prefix[curr_sum] -= 1  
        
        dfs(root, 0)
        return count[0]
        
        