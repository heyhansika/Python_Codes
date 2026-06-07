class Solution:
    def exist(self, board, word):
        rows = len(board)
        cols = len(board[0])

        def dfs(i, j, index):

            # If all characters are matched
            if index == len(word):
                return True

            # Boundary check + character mismatch
            if (i < 0 or j < 0 or
                i >= rows or j >= cols or
                board[i][j] != word[index]):
                return False

            # Mark cell as visited
            temp = board[i][j]
            board[i][j] = '#'

            # Explore 4 directions
            found = (dfs(i + 1, j, index + 1) or
                     dfs(i - 1, j, index + 1) or
                     dfs(i, j + 1, index + 1) or
                     dfs(i, j - 1, index + 1))

            # Backtrack
            board[i][j] = temp

            return found

        # Try every cell as starting point
        for i in range(rows):
            for j in range(cols):
                if dfs(i, j, 0):
                    return True

        return False
