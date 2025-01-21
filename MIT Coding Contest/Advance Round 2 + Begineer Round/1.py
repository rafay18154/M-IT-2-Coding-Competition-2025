def solve():
    powers_of_5 = []
    power = 5
    while power <= 10**9:
        powers_of_5.append(power)
        power *= 5
    
    T = int(input())
    
    # Process each test case
    for _ in range(T):
        N = int(input())
        
        if N <= 5:
            print("MIT time")
        else:
            for i in range(1, len(powers_of_5)):
                if N <= powers_of_5[i]:
                    print(f"MIT^{i+1} time")
                    break
solve()
