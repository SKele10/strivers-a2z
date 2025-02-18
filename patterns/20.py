def symmetry(n: int):
    spaces = 2 * n - 2
    for row in range(1, 2 * n):
        stars = row
        if (row > n): 
            stars = (2 * n) - row 
        for star in range(stars):
            print("*", end="")
            
        for space in range(spaces):
            print(" ", end="")
        
        for star in range(stars):
            print("*", end="")
        
        if (row < n): 
            spaces -= 2
        else:
            spaces += 2
        print()
            

symmetry(5)