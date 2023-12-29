class Solution:
    class Node:
        def __init__(self, val):
            self.val = val
            self.parent = self
        
        def union(self, node):
            node.find().parent = self.find()

        def find(self):
            if self != self.parent:
                self.parent = self.parent.find()
                return self.parent
            else:
                return self

        def __str__(self):
            return f'self.val: {self.val}, self.parent: {self.find().val}' 

    def findRedundantConnection(self, edges: List[List[int]]) -> List[int]:
        
        g = {}
        redundant = []
        for edge in edges:
            n1, n2 = None,None
            if edge[0] in g:
                n1 = g[edge[0]]
            if edge[1] in g:
                n2 = g[edge[1]]
            
            if n1 == None:
                n1 = Solution.Node(edge[0])
            if n2 == None:
                n2 = Solution.Node(edge[1])
        
            if n1.find() != n2.find():
                g[edge[0]] = n1
                g[edge[1]] = n2
                n1.union(n2)
            else:
                redundant = edge
        
        return redundant