
    # 1. Copy/paste the problem definition. Read it out loud and understand what they want.
        You are a professional robber planning to rob houses along a street. Each house has a certain amount of money stashed, the only constraint stopping you from robbing each of them is that adjacent houses have security systems connected and it will automatically contact the police if two adjacent houses were broken into on the same night.

Given an integer array nums representing the amount of money of each house, return the maximum amount of money you can rob tonight without alerting the police.
    # 2. Look at the examples they give you for what the algorithm should do. "Solution(input) -> output". Come up with 1 or 2 examples on your own, and write them down.

    # 3. Think out loud, and write down (!!) the possible high-level approaches to solving the problem. 
    #     Eg: "this two-sum problem can be brute-forced in O(n^2) time using two for-loops, or it can be solved in O(n) using a hashmap." 
    #     This doesn't have to be detailed, just a possible approach. Think about possible edge cases and how they could break the solution.

    #     Here, if you are completely blanking after 5 minutes, and can't even do a brute-force solution, then do what the OP said 
    #     - abort mission, and spend the next hour understanding the problem by looking at the solution. Once you understood the solution go to step 4.
        1. f(n) = max(f(n - 1), f(n - 2))

    # 4. Pick one of the approaches, and write out the pseudo code for it, while taking out loud as to what your thought process is.

    # 5. CODE THE ACTUAL SOLUTION. If you actually followed steps 1-4, this part is going to be trivial. You will bang out the actual code often in under 5 minutes. 
    # Paste the code into leetcode (or whatever platform you are using) to ensure it works. You can even write your own test cases, and run locally.

        memo = [0] * len(nums) 

        def r(idx):

            # base cases
            if idx < 0:
                return 0

            if memo[idx - 1] != 0:
                return memo[idx - 1]


            sum = max(r(idx - 1), r(idx - 2) + nums[idx])
            memo[idx - 1] = sum

            return sum

        return r(len(nums) - 1)
    # 6. If you haven't addressed this in step 3 (when you were talking about approaches), think about how you would optimize the solution. Talk about big O here.

        can be improved by doing iterative?

        memo = [0] * (len(nums) + 1)

        memo[0] = nums[0]
        memo[1] = nums[1]

        for i in range(1, len(nums)):
            sum = max(memo[i - 1], memo[i - 2] + nums[i])
            memo[i] = sum

        return memo[len(nums) - 1]