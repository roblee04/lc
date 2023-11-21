
    # 1. Copy/paste the problem definition. Read it out loud and understand what they want.
        There is a robot on an m x n grid. The robot is initially located at the top-left corner (i.e., grid[0][0]). The robot tries to move to the bottom-right corner (i.e., grid[m - 1][n - 1]). The robot can only move either down or right at any point in time.

        Given the two integers m and n, return the number of possible unique paths that the robot can take to reach the bottom-right corner.

        The test cases are generated so that the answer will be less than or equal to 2 * 109.

    # 2. Look at the examples they give you for what the algorithm should do. "Solution(input) -> output". Come up with 1 or 2 examples on your own, and write them down.

    # 3. Think out loud, and write down (!!) the possible high-level approaches to solving the problem. 
    #     Eg: "this two-sum problem can be brute-forced in O(n^2) time using two for-loops, or it can be solved in O(n) using a hashmap." 
    #     This doesn't have to be detailed, just a possible approach. Think about possible edge cases and how they could break the solution.

    #     Here, if you are completely blanking after 5 minutes, and can't even do a brute-force solution, then do what the OP said 
    #     - abort mission, and spend the next hour understanding the problem by looking at the solution. Once you understood the solution go to step 4.
        1. I think the easiest way to do this is to just call a recursive function with a counter
    # 4. Pick one of the approaches, and write out the pseudo code for it, while taking out loud as to what your thought process is.


        def dfs(i, j):
            if i >= m or j >= n:
                return 0

            if i == m - 1 and j == n - 1:
                return 1

            return dfs(i + 1, j) + dfs(i, j + 1)

        return dfs(0, 0)
    # 5. CODE THE ACTUAL SOLUTION. If you actually followed steps 1-4, this part is going to be trivial. You will bang out the actual code often in under 5 minutes. 
    # Paste the code into leetcode (or whatever platform you are using) to ensure it works. You can even write your own test cases, and run locally.
        
        #to save time, lets add memoization? or we can make use of the fact that it only will go right or down.
        # the number of unique paths per square is always going to be unique, so lets memoize that
        memo = {}

        def dfs(i, j):
            if i >= m or j >= n:
                return 0

            if i == m - 1 and j == n - 1:
                return 1

            if (i, j) in memo:
                return memo[tuple((i,j))]

            sum = dfs(i + 1, j) + dfs(i, j + 1)
            memo[tuple((i, j))] = sum

            return sum

        return dfs(0, 0)
    # 6. If you haven't addressed this in step 3 (when you were talking about approaches), think about how you would optimize the solution. Talk about big O here.

