# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def binaryTreePaths(self, root: Optional[TreeNode]) -> List[str]:
        paths = []
        current_path = ''

        def traverse(root, current_path):
            if not root:
                return 
            
            current_path += str(root.val)+'->'
            
            if not root.left and not root.right:
                current_path = current_path[:-2]
                paths.append(current_path)
                
            if root.left: 
                traverse(root.left, current_path)
            if root.right:
                traverse(root.right, current_path)
                                    
        traverse(root, current_path)
        return paths
