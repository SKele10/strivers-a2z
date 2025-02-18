def getNumberPattern(n: int) -> None:
    for row in range(2*n -1):
        for col in range(2*n-1):
            top = row
            left = col
            right = 2*n -2 - col
            bottom = 2*n -2 - row
            print(n - min(top, left, right, bottom), end="")
        print()
            
                
getNumberPattern(4)
