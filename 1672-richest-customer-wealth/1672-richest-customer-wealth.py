class Solution:
    def maximumWealth(self, accounts: list[list[int]]) -> int:
        result = []
        for i in range(len(accounts)):
            result.append(sum(accounts[i]))
        return max(result)        