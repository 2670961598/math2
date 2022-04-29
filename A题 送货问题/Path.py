def tsp(matrix):
    m, n = len(matrix) * len(matrix), len(matrix)
    # 状态压缩DP,5表示0101,dp[i][j]表示从0出发,经过i中的几个到达j,要求i中有j
    dp = [[float('inf')] * n for _ in range(m)]
    dp[1][0] = 0
    for i in range(1, m):
        if not (i & 1):  # i中不能包括0,不能从0出发
            continue
        for j in range(1, n):  # j是要加入的
            if i & (1 << j):  # 如果i中包括j就重复了
                continue
            for k in range(n):
                if i & (1 << k):  # 如果i中包括k
                    # i中加上j,0到j的最短距离可能为原来i中任何一个k到j的距离与剩余最短距离之和
                    dp[(1 << j) | i][j] = min(
                        dp[(1 << j) | i][j], dp[i][k] + matrix[k][j])
    res = float('inf')
    # 最后还要回到0
    for i in range(n):
        res = min(res, dp[m - 1][i] + matrix[i][0])
    return res


n = int(input())
martix = []
for i in range(n):
    arr = list(map(int, input().split()))
    martix.append(arr)
print(tsp(martix))