# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxAncestorDiff(self, root: Optional[TreeNode]) -> int:
        # General idea
        ## every node needs to be compared to its children
        ## the max of the comparisons needs to be returned
        # Components
        #track the lowest number , the highest number  , and greatest absolute difference and pass it back up the tree
        ##return the max absolute difference
        # Implementation
        
        def dfs(node):
            if not node:
                return (float('inf'), float('-inf') , 0)
            
            left_min , left_max , left_abs = dfs(node.left)
            right_min , right_max  , right_abs = dfs(node.right)
            
            curr_max= max(left_max , right_max , node.val)
            curr_min= min(right_min , left_min , node.val)
            curr_abs= max(abs(node.val-curr_max) , abs(node.val-curr_min) , left_abs , right_abs)
            return (curr_min , curr_max , curr_abs)
            
        _min , _max , _abs = dfs(root)
        return _abs
            