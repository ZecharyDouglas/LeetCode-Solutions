from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        ##bfs 
        ## track state for order reversal
        ## if state ==1 go left to right  , if -1 then right to left
        # for each level add its values to an answer array based on the state
        #return the answer
        queue = deque([root])
        state=1
        ans=[]
        if not root:
            return []
        while queue:
            temp=[]
            nodes_in_current_level=len(queue)
            for _ in range(nodes_in_current_level):
                node=queue.popleft()
                temp.append(node.val)
                if node.left:
                    queue.append(node.left)
                if node.right:
                    queue.append(node.right)
            if state==1:
                ans.append(temp)
            if state==-1:
                ##really cool way to reverse a list  using ""array_name[::-1]"" syntax
                ans.append(temp[::-1])
            state*=-1
        return ans
                
                
                
                
                
                
                
                