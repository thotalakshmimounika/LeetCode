class Solution:
    def customSortString(self, order: str, s: str) -> str:
        d={}
        for char in s:
            d[char]=d.get(char,0)+1
        ans=[]
        for char in order:
            if char in d:
                ans+=char*d[char]
                del d[char]
        for key,feq in d.items():
            ans+=key*feq
        return ''.join(ans)
            

        