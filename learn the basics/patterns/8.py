def nStarTriangle(n: int) -> None:
    for row in range(n):
        for col in range(n):
            if(row > col):
                print(' ', end="")
            else:
                print('*', end="")
        print((n-row-1)*'*', end="")
        print("\n", end="")
        
        
nStarTriangle(3)