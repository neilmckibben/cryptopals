

def longestOnes(A, K):
    def expand(i, dp):
        count = dp[i]
        remaining = K
        # expand left
        j = i - 1
        while j >= 0 and remaining >= 0:
            print("Left", remaining, j, count)
            if dp[j] > 0:
                count += dp[j]
            elif dp[j] < 0 <= (remaining + dp[j]):
                count -= dp[j]
                remaining += dp[j]
            else:
                count += remaining
                remaining += dp[j]
            j -= 1

        j = i + 1
        while j < len(dp) and remaining >= 0:
            if dp[j] > 0:
                count += dp[j]
            elif dp[j] < 0 <= (remaining + dp[j]):
                count -= dp[j]
                remaining += dp[j]
            else:
                count += remaining
                remaining += dp[j]
            j += 1

        return count

    dp = []
    i = 0
    while i < len(A):
        count = 0
        value = A[i]
        while i < len(A) and A[i] == value:
            count += 1
            i += 1
        encoded = count
        if value == 0:
            encoded *= -1
        dp.append(encoded)

    ans = 0
    print(dp)
    for i in range(0, len(dp)):
        if dp[i] > 0:
            ans = max(ans, expand(i, dp))
        i += 1
    return ans


A = [1,1,1,0,0,0,1,1,1,1,0]
print(longestOnes(A, 2))