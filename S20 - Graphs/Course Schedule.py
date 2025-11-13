class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        self.adj = []
        self.state = { }
        self.flag = False
        for i in range(numCourses):
            self.adj.append([])
            self.state[i] = 'U'

        for req in prerequisites:
            fromNode = req[1]
            toNode = req[0]
            self.adj[fromNode].append(toNode)

        for i in range(numCourses):
            if (self.state[i] == 'U'):
                self.dfs(i)

            if (self.flag == True):
                return False
        return True


    def dfs(self, node):
        if (self.state[node] == 'U'):
            self.state[node] = 'V'
            for nei in self.adj[node]:
                self.dfs(nei)
            self.state[node] = 'P'
        elif (self.state[node] == 'V'):
            self.flag = True


