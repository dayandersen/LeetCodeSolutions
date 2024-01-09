# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []
        q = deque()
        q.append((0, root))
        temp_arr = []
        ret = []
        
        while (q):
            depth, node = q.popleft()
            
            if node.left:
                q.append((depth+1, node.left))
            if node.right:
                q.append((depth+1, node.right))
            
            if not temp_arr or (temp_arr and temp_arr[-1][0] == depth):
                temp_arr.append((depth, node.val))
            else:
                ret.append([v for depth,v in temp_arr])
                temp_arr = []
                temp_arr.append((depth, node.val))
        ret.append([v for depth,v in temp_arr])
        return ret
        