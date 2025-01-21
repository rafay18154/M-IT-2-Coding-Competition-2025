def count_valid_numbers(N):
    from collections import deque

    def is_valid(k):
        visited = set()
        queue = deque([k])
        while queue:
            num = queue.popleft()
            if num == 1:
                return True
            if num in visited:
                continue
            visited.add(num)
            for digit in str(num):
                d = int(digit)
                if d > 1 and num % d == 0:
                    queue.append(num // d)
        return False

    def count(N):
        count = 0
        queue = deque(range(1, 10))  
        while queue:
            num = queue.popleft()
            if num > N:
                continue
            count += 1
            for d in range(10):
                next_num = num * 10 + d
                if next_num <= N:
                    queue.append(next_num)
        return count

    # Handle small and large cases
    if N <= 10**5:
        return sum(1 for k in range(1, N + 1) if is_valid(k))
    else:
        return count(N)

num = int(input())
print(count_valid_numbers(num))

