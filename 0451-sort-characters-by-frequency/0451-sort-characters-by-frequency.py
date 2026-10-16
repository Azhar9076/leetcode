class Solution:
    def frequencySort(self, s: str) -> str:
        hash = {}
        for key , value in enumerate(s):
            hash[value] = hash.get(value, 0) + 1
        hash = dict(sorted(hash.items(), key = lambda x:x[1], reverse = True))

        string = ''
        for key , value in hash.items():
            string += key * value
        return string    