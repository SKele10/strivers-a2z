def nStarTriangle(n: int) -> None:
    for row in range(n):
        print((row+1)*"*")
    
    for row in range(n-2, -1, -1):
        print((row+1)*"*")
        
nStarTriangle(3)