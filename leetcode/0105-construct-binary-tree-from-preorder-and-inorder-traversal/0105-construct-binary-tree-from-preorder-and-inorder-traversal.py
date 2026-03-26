# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def buildTree(self, preorder, inorder):
        if not preorder :
            return
        root=TreeNode(preorder[0])
        if len(preorder)==1:
            return root
        index_=inorder.index(root.val)
        root.left= self.buildTree(preorder[1:1+index_],inorder[:index_])
        root.right= self.buildTree(preorder[1+index_: ],inorder[index_+1:])
        return root    
        

        