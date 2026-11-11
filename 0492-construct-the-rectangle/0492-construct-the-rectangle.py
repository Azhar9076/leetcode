import math
class Solution:
    def constructRectangle(self, area: int) -> list[int]:
        l = int(math.sqrt(area))

        while area % l != 0:
            l -= 1
        w = area // l

        return [w, l]    