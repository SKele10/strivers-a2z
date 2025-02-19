def alphaTriangle(n: int):
    num = n - 1
    for row in range(n):
        for col in range(row+1):
            print(chr(65+num), end=" ")
            num -= 1
        num = n - 1
        print()
        
        
alphaTriangle(3)

