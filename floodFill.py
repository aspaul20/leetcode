class Solution:
    def floodFill(self, image: List[List[int]], sr: int, sc: int, color: int) -> List[List[int]]:

        rows = len(image)
        cols = len(image[0])

        def flood(image, r, c):

            if image[r][c] == color:
                return 

            orig_color = image[r][c]
            image[r][c] = color 
            
            if c - 1 >= 0 and image[r][c-1] == orig_color:
                flood(image, r, c-1)
            if r - 1 >= 0 and image[r-1][c] == orig_color:
                flood(image, r-1, c)
            if c + 1 < cols and image[r][c+1] == orig_color:
                flood(image, r, c+1)
            if r + 1 < rows and image[r+1][c] == orig_color:
                flood(image, r+1, c)


        flood(image, sr, sc)

        return image
