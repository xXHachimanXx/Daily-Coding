def minimize_cost(costs, N, K):
    if N == 0 or K == 0:
        return 0
    
    dp = [[0 for i in range(N)] for j in range(K)]

    for i in range(K):
        dp[0][i] = costs[0][i]

    for i in range(1, N, 1):
       
        # If current house is colored
        # with red the take min cost of
        # previous houses colored with
        # (blue and green)
        for j in range(K):
            dp[i][j] = min(dp[i - 1][1], dp[i - 1][2]) + costs[i][j]
 
        # If current house is colored
        # with blue the take min cost of
        # previous houses colored with
        # (red and green)
        dp[i][1] = min(dp[i - 1][0], dp[i - 1][2]) + costs[i][1]
 
        # If current house is colored
        # with green the take min cost of
        # previous houses colored with
        # (red and blue)
        dp[i][2] = min(dp[i - 1][0], dp[i - 1][1]) + costs[i][2]
 
    # Print the min cost of the
    # last painted house
    return (min(dp[N - 1][0], min(dp[N - 1][1],dp[N - 1][2])))

costs = [[14, 2, 11],
             [11, 14, 5],
             [14, 3, 10]]
N = len(costs)
K = len(costs[0])
    
# Function Call
minCost(costs, N, K)
