class Solution:
    def pivotInteger(self, n: int) -> int:
        lefts,left=1,1
        rights,right=n,n
        while left<=right:
            if lefts==rights:
                if left==right:
                    return left
                left+=1
                right-=1
                lefts+=left
                rights+=right
            elif lefts<rights:
                left+=1
                lefts+=left
            else:
                right-=1
                rights+=right
        return -1
