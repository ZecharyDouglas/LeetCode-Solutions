class Solution:
    def countComponents(self, n: int, edges: List[List[int]]) -> int:
        node_map={i:[] for i in range(n)}
        answer=0
        
        for x , y in edges: 
            node_map[x].append(y)
            node_map[y].append(x)
            
        
        seen=set()
        def dfs(node):
            if node not in seen:
                seen.add(node)
                for neighbor in node_map[node]:
                    dfs(neighbor)
                
        for i in range(n):
            if i not in seen:
                dfs(i)
                answer += 1
                
        return answer