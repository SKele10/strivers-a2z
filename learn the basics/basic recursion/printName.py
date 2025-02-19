class Solution:
    def printName(self, n):
        if n==0: return
        print("SK", end=" ")
        self.printName(n-1)
        

solution = Solution()
solution.printName(5)