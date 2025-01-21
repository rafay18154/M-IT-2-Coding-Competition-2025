def is_repetitive_string(s):
    n = len(s)
    i = 0
    
    # The string must start with 'M'
    if i < n and s[i] == 'M':
        i += 1
    else:
        return False
    
    # After 'M', there must be a sequence of 'IT' repeating
    while i < n:
        if i + 1 < n and s[i:i+2] == 'IT':
            i += 2
        else:
            return False
    
    # If we've processed the entire string, it's valid
    return i == n

def main():
    t = int(input())  # Number of test cases
    results = []
    
    # Process each test case
    for _ in range(t):
        n = int(input())  # Length of the string (not actually needed)
        s = input().strip()  # The input string
        
        # Check if the string follows the repetitive pattern
        if is_repetitive_string(s):
            results.append("YES")
        else:
            results.append("NO")
    
    # Output all results
    print("\n".join(results))

if __name__ == "__main__":
    main()
