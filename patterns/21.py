def getStarPattern(n: int) -> None:
    for row in range(n):
        for col in range(n):
            if row == 0 or col == 0 or row == n-1 or col == n-1:
                print("*", end="")
            else: 
                print(" ", end="")
        print()

getStarPattern(5)