class Solution:
    def ratInMaze(self, maze):
        # code here
        
        n = len(maze)
        m = len(maze[0])
        i, j = 0, 0
        
        ans = []
        visited = [[0 for _ in range(m)] for _ in range(n)]
        move = ''
        
        def solve(i, j, visited, move):
            
            if i == n-1 and j == m-1:
                ans.append(move)
                return
            
            # Down
            if i+1 < n and visited[i+1][j] == 0 and maze[i+1][j] == 1:
                visited[i][j] = 1
                solve(i+1, j, visited, move + 'D')
                visited[i][j] = 0
            
            # Left
            if j-1 >= 0 and visited[i][j-1] == 0 and maze[i][j-1] == 1:
                visited[i][j] = 1
                solve(i, j-1, visited, move + 'L')
                visited[i][j] = 0
            
            # Right    
            if j+1 < m and visited[i][j+1] == 0 and maze[i][j+1] == 1:
                visited[i][j] = 1
                solve(i, j+1, visited, move + 'R')
                visited[i][j] = 0
                
            # Up
            if i-1 >= 0 and visited[i-1][j] == 0 and maze[i-1][j] == 1:
                visited[i][j] = 1
                solve(i-1, j, visited, move + 'U')
                visited[i][j] = 0
        
        if maze[0][0] == 1:
            solve(0, 0, visited, move)
        
        return ans
