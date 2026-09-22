from typing import List

class Solution:
    def numOfUnplacedFruits(self, fruits: List[int], baskets: List[int]) -> int:
        unplaced = 0
        
        for fruit in fruits:
            placed = False
            for j in range(len(baskets)):
                if baskets[j] >= fruit:
                    baskets[j] = -1          
                    placed = True
                    break
            
            if not placed:
                unplaced += 1
        
        return unplaced