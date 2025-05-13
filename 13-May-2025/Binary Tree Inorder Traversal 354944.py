# Problem: Binary Tree Inorder Traversal - https://leetcode.com/problems/binary-tree-inorder-traversal/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def inorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        res = []
        def traverse(curr_node):
            if curr_node.left:
                traverse(curr_node.left)
            res.append(curr_node.val)

            if curr_node.right:
                traverse(curr_node.right)
        if root:
            traverse(root)
        return res