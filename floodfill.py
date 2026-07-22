class Solution:
    def floodFill(self, image, sr, sc, color):

        original = image[sr][sc]

        if original == color:
            return image

        rows = len(image)
        cols = len(image[0])

        def dfs(r, c):

            if (r < 0 or c < 0 or
                r >= rows or c >= cols or
                image[r][c] != original):
                return

            image[r][c] = color

            dfs(r + 1, c)
            dfs(r - 1, c)
            dfs(r, c + 1)
            dfs(r, c - 1)

        dfs(sr, sc)

        return image
