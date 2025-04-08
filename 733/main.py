class Solution(object):
    def floodFill(self, image, sr, sc, color):
        """
        :type image: List[List[int]]
        :type sr: int
        :type sc: int
        :type color: int
        :rtype: List[List[int]]
        """
        original_color = image[sr][sc]  # Store the starting pixel's color
        if original_color == color:
            return image  # If the new color is the same, no changes needed

        def dfs(r, c):
            # Check if the pixel is within the image bounds AND if it's the original color
            if r < 0 or r >= len(image) or c < 0 or c >= len(image[0]) or image[r][c] != original_color:
                return  # Stop if out of bounds or wrong color

            image[r][c] = color  # Change the pixel's color

            # Recursively call dfs for the neighboring pixels
            dfs(r + 1, c)  # Down
            dfs(r - 1, c)  # Up
            dfs(r, c + 1)  # Right
            dfs(r, c - 1)  # Left

        dfs(sr, sc)  # Start the flood fill from the given starting point
        return image
        
    print(floodFill(image = [[1,1,1],[1,1,0],[1,0,1]], sr = 1, sc = 1, color = 2))