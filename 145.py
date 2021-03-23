class TreeNode:
     def __init__(self, val=0, left=None, right=None):
            self.val = val
            self.left = left
            self.right = right
class Solution:
    def postorderTraversal(self, root: TreeNode) -> List[int]:
        if root is None:
            return []
        stack, output = [root, ], []
        while stack:
            root = stack.pop()
            output.append(root.val)
            if root.left is not None:
                stack.append(root.left)
            if root.right is not None:
                stack.append(root.right)
                
        return output[::-1]