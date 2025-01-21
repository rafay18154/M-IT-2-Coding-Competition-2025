def min_operations(S1, S2):
    if S1 == S2:
        return 0
    
    diff_AAB_BAA = 0
    diff_BBA_ABB = 0
    
    # Step 3: Check for mismatched substrings in S1 and S2.
    n = len(S1)
    
    for i in range(n - 2):
        # Check for "AAB" and "BAA" mismatch
        if S1[i:i+3] == "AAB" and S2[i:i+3] == "BAA":
            diff_AAB_BAA += 1
        elif S1[i:i+3] == "BAA" and S2[i:i+3] == "AAB":
            diff_AAB_BAA += 1
        # Check for "BBA" and "ABB" mismatch
        elif S1[i:i+3] == "BBA" and S2[i:i+3] == "ABB":
            diff_BBA_ABB += 1
        elif S1[i:i+3] == "ABB" and S2[i:i+3] == "BBA":
            diff_BBA_ABB += 1
    return max(diff_AAB_BAA, diff_BBA_ABB)

def main():
    T = int(input())  # Number of test cases
    for _ in range(T):
        S1, S2 = input().split()  # The two strings for each test case
        result = min_operations(S1, S2)
        print(result)

if __name__ == "__main__":
    main()
