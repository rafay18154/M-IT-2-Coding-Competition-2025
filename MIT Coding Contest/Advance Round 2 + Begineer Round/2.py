class SegmentTree:
    def __init__(self, n):
        self.n = n
        self.tree = [None] * (4 * n)
    
    def build(self, arr, node, start, end):
        if start == end:
            self.tree[node] = [0] * (self.n + 1)
            self.tree[node][arr[start]] = 1
        else:
            mid = (start + end) // 2
            left_child = 2 * node + 1
            right_child = 2 * node + 2
            self.build(arr, left_child, start, mid)
            self.build(arr, right_child, mid + 1, end)
            self.tree[node] = [self.tree[left_child][i] | self.tree[right_child][i] for i in range(self.n + 1)]
    
    def update(self, idx, value, node, start, end):
        if start == end:
            self.tree[node] = [0] * (self.n + 1)
            self.tree[node][value] = 1
        else:
            mid = (start + end) // 2
            left_child = 2 * node + 1
            right_child = 2 * node + 2
            if start <= idx <= mid:
                self.update(idx, value, left_child, start, mid)
            else:
                self.update(idx, value, right_child, mid + 1, end)
            self.tree[node] = [self.tree[left_child][i] | self.tree[right_child][i] for i in range(self.n + 1)]
    
    def query(self, L, R, node, start, end):
        if R < start or end < L:
            return [0] * (self.n + 1)
        if L <= start and end <= R:
            return self.tree[node]
        mid = (start + end) // 2
        left_child = 2 * node + 1
        right_child = 2 * node + 2
        left_result = self.query(L, R, left_child, start, mid)
        right_result = self.query(L, R, right_child, mid + 1, end)
        return [left_result[i] | right_result[i] for i in range(self.n + 1)]

def solve():
    N, Q = map(int, input().split())
    arr = list(map(int, input().split()))
    
    segment_tree = SegmentTree(N)
    segment_tree.build(arr, 0, 0, N - 1)
    
    for _ in range(Q):
        query = list(map(int, input().split()))
        if query[0] == 1:
            x, y = query[1] - 1, query[2]
            arr[x] = y
            segment_tree.update(x, y, 0, 0, N - 1)
        elif query[0] == 2:
            l, r = query[1] - 1, query[2] - 1
            present = segment_tree.query(l, r, 0, 0, N - 1)
            for i in range(1, N + 1):
                if present[i] == 0:
                    print(i)
                    break

solve()
