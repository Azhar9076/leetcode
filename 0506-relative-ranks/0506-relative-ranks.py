class Solution:
    def findRelativeRanks(self, score: list[int]) -> list[str]:
        scored = sorted(score, reverse = True)
        result = {}
        for i in range (len(scored)):
            if i == 0:
                result[scored[i]] = "Gold Medal"
            elif i == 1:
                result[scored[i]] = "Silver Medal"
            elif i == 2:
                result[scored[i]] = "Bronze Medal"
            else :
                result[scored[i]] = (str(i+1))   
        return [result[x] for x in score]