def solve():
    N, K = map(int, input().split())
    screenshots = [list(map(int, input().split())) for _ in range(N)]

    indexed_screenshots = [(i + 1, screenshots[i]) for i in range(N)]

    indexed_screenshots.sort(key=lambda x: x[1])

    for i in range(1, N):
        for j in range(K):
            if indexed_screenshots[i][1][j] < indexed_screenshots[i-1][1][j]:
                print("NO")
                return

    # If we reached here, it means we have a valid order
    print("YES")
    print(" ".join(str(x[0]) for x in indexed_screenshots))

# Call the function
solve()
