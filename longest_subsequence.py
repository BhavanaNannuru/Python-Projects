# This function computes the Longest Common Subsequence (LCS) between two strings X and Y.
# It uses dynamic programming to build a 2D dp table that stores LCS lengths for all subproblems.
# After building the table, it performs a backtracking step to reconstruct one valid LCS string.
# The function returns both the LCS string and its length.


def longest(X,Y):
    m = len(X)
    n = len(Y)
    dp = [[0 for i in range(n+1)] for i in range(m+1)]
    for i in range(1,m+1):
        for j in range(1,n+1):
            if X[i-1]==Y[j-1]:
                dp[i][j] = dp[i-1][j-1]+1
            else:
                dp[i][j] = max(dp[i-1][j], dp[i][j-1])
    # return dp[m][n],dp

    i=m
    j = n
    lcs = []
    while i>0 and j>0:
        if X[i-1]==Y[j-1]:
            lcs.append(X[i-1])
            i-=1
            j-=1
        elif dp[i-1][j]>dp[i][j-1]:
            i-=1
        else:
            j-=1
    lcs.reverse()
    lcs = ''.join(lcs)
    return lcs,dp[m][n]


X = "XMJYAUZ"
Y = "MZJAWXU"
print(longest(X,Y))

print(longest("ABCBDAB","BDCABA"))
