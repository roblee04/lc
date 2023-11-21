
    # 1. Copy/paste the problem definition. Read it out loud and understand what they want.

        You are a professional robber planning to rob houses along a street. 
        Each house has a certain amount of money stashed. 
        All houses at this place are arranged in a circle. 
        That means the first house is the neighbor of the last one. 
        Meanwhile, adjacent houses have a security system connected, and it will automatically contact the police if two adjacent houses were broken into on the same night.

        Given an integer array nums representing the amount of money of each house,
        return the maximum amount of money you can rob tonight without alerting the police.
    # 2. Look at the examples they give you for what the algorithm should do. "Solution(input) -> output". Come up with 1 or 2 examples on your own, and write them down.

    # 3. Think out loud, and write down (!!) the possible high-level approaches to solving the problem. 
    #     Eg: "this two-sum problem can be brute-forced in O(n^2) time using two for-loops, or it can be solved in O(n) using a hashmap." 
    #     This doesn't have to be detailed, just a possible approach. Think about possible edge cases and how they could break the solution.

    #     Here, if you are completely blanking after 5 minutes, and can't even do a brute-force solution, then do what the OP said 
    #     - abort mission, and spend the next hour understanding the problem by looking at the solution. Once you understood the solution go to step 4.
        1. house robber solution without circle is basically:

            a. f(n) = max(f(n - 1), f(n - 2) + currMoney)

            essentially, you find your current value by taking the max between last house and last last house + curr square

            and the houses are in a circle, the only thing that this changes is the base case for the dfs

            - instead of you hitting the base case at when index < 1, we should change the condition


    # 4. Pick one of the approaches, and write out the pseudo code for it, while taking out loud as to what your thought process is.

    # 5. CODE THE ACTUAL SOLUTION. If you actually followed steps 1-4, this part is going to be trivial. You will bang out the actual code often in under 5 minutes. 
    # Paste the code into leetcode (or whatever platform you are using) to ensure it works. You can even write your own test cases, and run locally.

    # 6. If you haven't addressed this in step 3 (when you were talking about approaches), think about how you would optimize the solution. Talk about big O here.


        the solution is actually just to use house robber 1, but take the max of nums[1:] and nums[:-1]