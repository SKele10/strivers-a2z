def seeding(n: int) -> None:
    for i in range(n, 0, -1):
        for col in range(i):
            print('* ', end="")
        print('\n', end="")
    
seeding(3)