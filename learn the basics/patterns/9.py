def nStarDiamond(n: int) -> None:
    for row in range(n-1, -1, -1): 
        for col in range(n):
            if col < row:
                print("", end=" ")
            else:
                print("*", end="")
        print((n-1-row)*"*", end="")
        print()
    
    for row in range(n):
        for col in range(n):
            if col< row:
                print("", end=" ")
            else:
                print("*", end="")
        print((n-1-row)*"*", end="")
        print()
                
        
        
nStarDiamond(3)