class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        d={}
        for num in nums1:
            if num in d:
                d[num]+=1
            else:
                d[num]=1
        ans=[]
        for num in nums2:
            if num in d:
                ans.append(num)
                del d[num]
        return ans
