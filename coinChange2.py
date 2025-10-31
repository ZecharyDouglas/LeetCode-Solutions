class Solution:
    def change(self, amount: int, coins: List[int]) -> int:
        # Step 1: Initialize table
        dp = [0] * (amount + 1)
        dp[0] = 1  # 1 way to make 0

# You start with a list of coin values.
# Underneath, you keep a running “count” of ways to make each amount.
# You create an expression to make the target with the smallest element and count 1.
# For the next element, you reset the expression, replace parts of the previous expression with the new coin if possible, and increment the count.
# When substitution isn’t possible, you reuse results from previous calculations for the remaining piece.
# Keep doing this until the coin is too large.
        
        # Step 2: Build up combinations layer by layer
        for coin in coins:
            for curr in range(coin, amount + 1):
                dp[curr] += dp[curr - coin]
        
        # Step 3: Return final count
        return dp[amount]
