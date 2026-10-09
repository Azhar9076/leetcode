class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        result = []
        for i in range(len(accounts)):
            for j in range (len(accounts[0])):
                result.append(sum(accounts[i]))
        return max(result)        