def symmetry(n: int):
    for row in range(2 * n):
        if row < n:
            for col in range(2 * n):
                if col < n:
                    if row < (n - col):
                        print("*", end=" ")
                    else:
                        print(" ", end=" ")
                else:
                    if row <= (col - n):
                        print("*", end=" ")
                    else:
                        print(" ", end=" ")
            print()
        else:
            for col in range(2 * n):
                if col < n:
                    if (row - col) >= n:
                        print("*", end=" ")
                    else:
                        print(" ", end=" ")
                else:
                    if (2*n - row - 1) <= (col - n):
                        print("*", end=" ")
                    else:
                        print(" ", end=" ")
            print()
            
def symmetry1(n: int):
    # Update n with 2*n

    n = 2*n

    # For loop ‘row’ in range 0 to N-1.
    for row in range(n):
        # For loop ‘col’ in range 0 to N-1.
        for col in range(n):
            # Condition for first half of the rows.
            if (row < n//2 and (col < (n//2 - row) or col >= (n//2 + row))):
                print('*', end=" ")
            # Condition for the second half of the rows.
            if (row >= n//2 and (col <= (row-n//2) or col >= (n-row+n//2-1))):
                print('*', end=" ")
            if (row < n//2 and not (col < (n//2 - row) or col >= (n//2 + row))):
                print(" ", end=" ")
            if (row >= n//2 and not (col <= (row-n//2) or col >= (n-row+n//2-1))):
                print(" ", end=" ")
        print()


symmetry(3)
