class Solution:
    def selfDividingNumbers(self, left: int, right: int) -> list[int]:
        def selfdiv (i):
            for d in str(i):
                if d == '0' or i % int(d) != 0:
                    return False
            return True
        result = []
        for i in range(left, right+1):
            if selfdiv(i):
                result.append(i)
        return result                  