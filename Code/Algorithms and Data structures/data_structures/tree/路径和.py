# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, x):
#         self.val = x
#         self.left = None
#         self.right = None

class Solution(object):
    def Sum(self, root):
        """
        :type root: TreeNode
        :type sum: int
        :type: int
        """
        if not root:
            return 0
        else:
            return root.val + self.Sum(root.left) + self.Sum(root.right)

    def hasPathSum(self, root, sum: int) -> bool:
        # 给定一个二叉树和一个目标和，判断该树中是否存在根节点到叶子节点的路径，这条路径上所有节点值相加等于目标和。
        if not root: return False
        t = sum - root.val
        if not root.left and not root.right:
            return t == 0
        return self.hasPathSum(root.left, t) or self.hasPathSum(root.right, t)
        
    def PathSumSolution(self, root):
        val = [root.val]
        if root.left:
            val.append(root.left.val)
            root = root.left
        
        if not root.left and not root.right:
            return val
