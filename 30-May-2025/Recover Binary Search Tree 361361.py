# Problem: Recover Binary Search Tree - https://leetcode.com/problems/recover-binary-search-tree/description/

# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverTree(self, root: Optional[TreeNode]) -> None:
        """
        Do not return anything, modify root in-place instead.
        """
        myFNode = None
        mySNode = None
        myPNode = None

        def helper(root):
            nonlocal myFNode, mySNode, myPNode
            if root is None:
                return
            
            helper(root.left)

            if myPNode !=None and root.val < myPNode.val and myFNode == None:
                myFNode = myPNode

            if myPNode !=None and root.val < myPNode.val and myFNode != None:
                mySNode = root

            myPNode = root

            helper(root.right)

        helper(root)

        if myFNode != None and mySNode != None:
            myFNode.val, mySNode.val = mySNode.val, myFNode.val