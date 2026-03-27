# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def constructFromPrePost(self, preorder, postorder):
        if not preorder :
            return
        root=TreeNode(preorder[0])
        if len(preorder)==1:
            return root
        index_=postorder.index(preorder[1])
        root.left= self.constructFromPrePost(preorder[1:index_+2],postorder[:index_+1])
        root.right= self.constructFromPrePost(preorder[index_+2: ],postorder[index_+1:-1])
        return root  
        