import re
class Solution:
    def mostCommonWord(self, paragraph: str, banned: list[str]) -> str:
        paragraph = re.sub(r'[^a-zA-Z\s]', ' ', paragraph)
        para = paragraph.lower().split()
        banned = set(banned)
        hashdict = {}        

        for word in para:
            if word not in banned:
                hashdict[word] = hashdict.get(word, 0) + 1   
        return max(hashdict, key=hashdict.get)    


        
