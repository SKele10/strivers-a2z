def alphaHill(n: int):
    for row in range(n-1, -1, -1):
        for col in range(n):
            if(col >= row):
                print(chr(65+col-row), end=" ")
            else:
                print(" ", end=" ")
        for col in range(n-row-2, -1, -1):
            print(chr(65+col), end=" ")
        print()
                
alphaHill(3)
            
