class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        n = len(nums)
        ans=[]
        m=2
        while m!=0:
            for i in range(n):
                ans.append(nums[i])
            m=m-1 
        return ans

        