class Solution:
    def findJudge(self, n: int, trust: list[list[int]]) -> int: 
        # Basically we need to find the node with no outgoing edges
        outdegree = [0] * (n+1)
        indegree = [0] * (n+1)

        for i,j in trust:
            outdegree[i] +=1
            indegree[j] +=1

        # print(f"{outdegree[1:]=}")
        for ot in range(1,len(outdegree)):
            if outdegree[ot] == 0 and indegree[ot]==n-1:
                return ot
        return -1