class Solution:
    def printNos(self, n):
        if n == 0:
            return
        print(n, end=" ")
        self.printNos(n-1)


solution = Solution()
solution.printNos(5)