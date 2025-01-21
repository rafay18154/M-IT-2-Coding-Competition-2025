from bisect import bisect_left

def longest_increasing_subsequence(seq):
    lis = []
    for value in seq:
        pos = bisect_left(lis, value)
        if pos == len(lis):
            lis.append(value)
        else:
            lis[pos] = value
    return len(lis)

# Function to evaluate each test case
def solve_case(N, K, permutation):
    for i in range(N - K + 1):
        subseq = permutation[i:i + K]
        # Calculate LIS of the subsequence
        lis_length = longest_increasing_subsequence(subseq)
        
        # We want the LIS length to be <= K + 1
        if lis_length <= K + 1:
            return "YES", subseq
    return "NO", []

# Main function to solve the problem
def solve():
    test_cases = [
        (4, 5, [4, 2, 1, 3]),
        (7, 3, [3, 1, 4, 5, 7, 2, 6]),
        (8, 8, [4, 5, 6, 7, 8, 1, 2, 3]),
        (6, 4, [5, 2, 4, 3, 1, 6]),
        (9, 8, [1, 3, 2, 4, 6, 5, 7, 9, 8]),
        (9, 7, [1, 3, 2, 4, 6, 5, 7, 9, 8]),
        (9, 5, [1, 6, 8, 9, 2, 5, 3, 4, 7]),
        (3, 2, [3, 2, 1]),
        (3, 2, [1, 2, 3]),
        (1, 1, [1])
    ]
    
    for N, K, permutation in test_cases:
        result, subseq = solve_case(N, K, permutation)
        
        if result == "YES":
            print(result)
            print(*subseq)
        else:
            print(result)

solve()
