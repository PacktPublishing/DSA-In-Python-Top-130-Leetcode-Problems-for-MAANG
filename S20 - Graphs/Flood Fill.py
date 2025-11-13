class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:
        if image[sr][sc] == color:
            return image

        self.dfs(image, sr, sc, image[sr][sc], color)
        return image

    def dfs(self, image, row, col, oldColor, newColor):
        if row < 0 or row >= len(image) or col < 0 or col >= len(image[0]) or image[row][col] != oldColor:
            return

        image[row][col] = newColor
        self.dfs(image, row - 1, col, oldColor, newColor)  # Up
        self.dfs(image, row + 1, col, oldColor, newColor)  # Down
        self.dfs(image, row, col - 1, oldColor, newColor)  # Left
        self.dfs(image, row, col + 1, oldColor, newColor)  # Right
