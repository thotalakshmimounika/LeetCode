import heapq as hq
class Solution:
    def furthestBuilding(self, heights: List[int], bricks: int, ladders: int) -> int:
        n=len(heights)
        hq=[]
        for i in range(n-1):
           diff=heights[i+1]-heights[i]
           if diff>0:
               heapq.heappush(hq,diff)
               if len(hq)>ladders:
                   x=heapq.heappop(hq)
                   bricks-=x
                   if bricks<0:
                       return i
        return n-1

                

            





        # [4,2,7,6,9,14,12]
        # [0,2,-5,1,-3,-5,2]
        # [-5,-5,-3,0,1,2,2]
        # heapq.heapify(diff)
        # for i in range(n):
        #     if diff[i]<0:
                # while heapq:
                #     x=-(heapq.heappop())
                #     if bricks and x>=bricks:
                #         if ladders:
                #             ladders-=1
                #         else:
                #             bricks-=x
        
        



        