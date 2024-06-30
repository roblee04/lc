
    # 1. Copy/paste the problem definition. Read it out loud and understand what they want.
        Given an m x n integers matrix, return the length of the longest increasing path in matrix.

        From each cell, you can either move in four directions: left, right, up, or down. You may not move diagonally or move outside the boundary (i.e., wrap-around is not allowed).
    # 2. Look at the examples they give you for what the algorithm should do. "Solution(input) -> output". Come up with 1 or 2 examples on your own, and write them down.

        def dfs(i, j, prevMax):
            #check bounds
            if i < 0 or i >= n or j < 0 or j >= m:
                return 0
            
            if board[i][j] <= prevMax:
                return 0

            # try a direction
            left = dfs(i, j - 1, board[i][j])
            right = dfs(i, j + 1, board[i][j])
            up = dfs(i - 1, j, board[i][j])
            down = dfs(i, j + 1, board[i][j])

            return 1 + max(left, right, up, down)

    # 3. Think out loud, and write down (!!) the possible high-level approaches to solving the problem. 
    #     Eg: "this two-sum problem can be brute-forced in O(n^2) time using two for-loops, or it can be solved in O(n) using a hashmap." 
    #     This doesn't have to be detailed, just a possible approach. Think about possible edge cases and how they could break the solution.

    #     Here, if you are completely blanking after 5 minutes, and can't even do a brute-force solution, then do what the OP said 
    #     - abort mission, and spend the next hour understanding the problem by looking at the solution. Once you understood the solution go to step 4.

        1. i think i am going to do a dfs with memoization approach
            - memoize: key = tile, val = longest path

    # 4. Pick one of the approaches, and write out the pseudo code for it, while taking out loud as to what your thought process is.


        def dfs(i, j, prev):

            check bounds, if out of bounds, return 0
            # dfs condition
            if curr <= prev, return 0

            take the max 1 + of dfs in 4 directions

            # need to check if ascending

    # 5. CODE THE ACTUAL SOLUTION. If you actually followed steps 1-4, this part is going to be trivial. You will bang out the actual code often in under 5 minutes. 
    # Paste the code into leetcode (or whatever platform you are using) to ensure it works. You can even write your own test cases, and run locally.

        # barebones dfs, going to add cache and double for loop
        cache = {}

        def dfs(i, j, prev):

            if i < 0 or i >= len(matrix) or j < 0 or j >= len(matrix[0]):
                return 0
            
            if matrix[i][j] <= prev:
                return 0

            cur = matrix[i][j]

            right = dfs(i + 1, j, cur)
            left = dfs(i - 1, j, cur)
            up = dfs(i, j + 1, cur)
            down = dfs(i, j - 1, cur)

            return 1 + max(right, left, up, down)

        # 2
        cache = {}

        def dfs(i, j, prev):

            if i < 0 or i >= len(matrix) or j < 0 or j >= len(matrix[0]):
                return 0

            if (i, j) in cache:
                return cache[(i, j)]
            
            if matrix[i][j] <= prev:
                return 0

            cur = matrix[i][j]

            right = dfs(i + 1, j, cur)
            left = dfs(i - 1, j, cur)
            up = dfs(i, j + 1, cur)
            down = dfs(i, j - 1, cur)

            cache[(i, j)] = 1 + max(right, left, up, down)
            return cache[(i, j)]

        # 3 done

        cache = {}

        def dfs(i, j, prev):

            if i < 0 or i >= len(matrix) or j < 0 or j >= len(matrix[0]):
                return 0
            
            if matrix[i][j] <= prev:
                return 0

            if (i, j) in cache:
                return cache[(i, j)]

            cur = matrix[i][j]

            right = dfs(i + 1, j, cur)
            left = dfs(i - 1, j, cur)
            up = dfs(i, j + 1, cur)
            down = dfs(i, j - 1, cur)
            # print((i, j), matrix[i][j])

            cache[(i, j)] = 1 + max(right, left, up, down)
            return cache[(i, j)]


        mval = 1

        for i in range(len(matrix)):
            for j in range(len(matrix[0])):
                mval = max(mval, dfs(i, j, -1))

        return mval


    # 6. If you haven't addressed this in step 3 (when you were talking about approaches), think about how you would optimize the solution. Talk about big O here.

