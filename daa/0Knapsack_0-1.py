def knapsack(w, p, cap):
    n = len(w)
    dp = [[0] * (cap + 1) for _ in range(n + 1)]

    for i in range(1, n + 1):
        for c in range(cap + 1):
            dp[i][c] = dp[i-1][c]

            if w[i-1] <= c:
                dp[i][c] = max(
                    dp[i][c],
                    p[i-1] + dp[i-1][c-w[i-1]]
                )
    c = cap
    selected = []
    for i in range(n, 0, -1):
        if dp[i][c] != dp[i-1][c]:
            selected.append(i)
            c -= w[i-1]

    print("Selected items:", selected)
    print("Maximum profit:", dp[n][cap])


# Input
n = int(input("Enter number of items: "))

w = []
p = []

for i in range(n):
    weight = int(input(f"Enter weight of item {i+1}: "))
    
    w.append(weight)
    
for i in range(n):
    profit = int(input(f"Enter profit of item {i+1}: "))
    p.append(profit)

cap = int(input("Enter knapsack capacity: "))

knapsack(w, p, cap)