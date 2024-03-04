class Solution:
    def bagOfTokensScore(self, tokens: List[int], power: int) -> int:
        tokens.sort()
        curr_power=power
        curr_score,max_score=0,0

        i,j=0,len(tokens)-1

        while(i<=j):
            if tokens[i]<=curr_power:
                curr_power-=tokens[i]
                curr_score+=1
                max_score=max(max_score,curr_score)
                i+=1
                
            elif curr_score>=1:
                curr_score-=1
                curr_power+=tokens[j]
                j-=1
            else:
                break

        return max_score




