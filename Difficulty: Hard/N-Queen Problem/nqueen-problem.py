class Solution:
    def nQueen(self, n):

        def issafe(row, col, board, n):
            r, c = row, col
            while r >= 0 and c >= 0:
                if board[r][c] == 'Q':
                    return False
                r -= 1
                c -= 1

            r, c = row, col
            while c >= 0:
                if board[r][c] == 'Q':
                    return False
                c -= 1

            r, c = row, col
            while r < n and c >= 0:
                if board[r][c] == 'Q':
                    return False
                r += 1
                c -= 1

            return True

        def solve(col, board, ans, n):
            if col == n:
                curr = []
                for i in range(n):
                    for j in range(n):
                        if board[i][j] == 'Q':
                            curr.append(j + 1)
                            break
                ans.append(curr)
                return

            for row in range(n):
                if issafe(row, col, board, n):
                    board[row][col] = 'Q'
                    solve(col + 1, board, ans, n)
                    board[row][col] = '.'

        ans = []
        board = [['.'] * n for _ in range(n)]
        solve(0, board, ans, n)
        return ans
