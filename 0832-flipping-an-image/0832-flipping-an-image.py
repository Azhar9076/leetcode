class Solution:
    def flipAndInvertImage(self, image: list[list[int]]) -> list[list[int]]:
        for row in image:
            row.reverse()
            for j in range (len(row)):
                row[j] = 1 - row[j]
        return image        