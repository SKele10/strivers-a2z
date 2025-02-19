class Solution:
    def sumOfSeries(self,n):
        if n ==0: return 0
        return self.sumOfSeries(n-1) + pow(n,3)


solution = Solution()
print(solution.sumOfSeries(5))