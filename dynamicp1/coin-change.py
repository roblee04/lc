
    # 1. Copy/paste the problem definition. Read it out loud and understand what they want.

    # 2. Look at the examples they give you for what the algorithm should do. "Solution(input) -> output". Come up with 1 or 2 examples on your own, and write them down.

    # 3. Think out loud, and write down (!!) the possible high-level approaches to solving the problem. 
    #     Eg: "this two-sum problem can be brute-forced in O(n^2) time using two for-loops, or it can be solved in O(n) using a hashmap." 
    #     This doesn't have to be detailed, just a possible approach. Think about possible edge cases and how they could break the solution.

    #     Here, if you are completely blanking after 5 minutes, and can't even do a brute-force solution, then do what the OP said 
    #     - abort mission, and spend the next hour understanding the problem by looking at the solution. Once you understood the solution go to step 4.

    # 4. Pick one of the approaches, and write out the pseudo code for it, while taking out loud as to what your thought process is.
        atoc = {}

        def dfs(amount): # returning no of coins we get back
            print(amount)

            if amount in set(coins):
                return 1

            if amount in atoc:
                return atoc[amount]

            # next take the min of what could it denominations be
            sum = 0
            temp = 0
            for c in coins:
                n = dfs(c)

                if sum == -1:
                    temp = n
                else:
                    temp = min(temp, n)

            # do memoization
            if amount not in atoc:
                atoc[amount] = 1 + temp

            print(sum, temp)

            return 1 + temp

        return dfs(amount)
    # 5. CODE THE ACTUAL SOLUTION. If you actually followed steps 1-4, this part is going to be trivial. You will bang out the actual code often in under 5 minutes. 
    # Paste the code into leetcode (or whatever platform you are using) to ensure it works. You can even write your own test cases, and run locally.

    # 6. If you haven't addressed this in step 3 (when you were talking about approaches), think about how you would optimize the solution. Talk about big O here.

        NC solution

        bottom up solution, 

        c = [amount + 1] * (amount + 1)
        c[0] = 0

        for mn in range(1, amount + 1):

            for c in coins:
                if mn - c >= 0 :
                    c[mn] = min(c[mn], 1 + c[mn - c])


        return c[amount] if c[amount] != amount + 1 else -1

        understand coin change