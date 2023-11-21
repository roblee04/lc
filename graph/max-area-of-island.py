
    # 1. Copy/paste the problem definition. Read it out loud and understand what they want.
        You are given an m x n binary matrix grid. An island is a group of 1's (representing land) connected 4-directionally (horizontal or vertical.) You may assume all four edges of the grid are surrounded by water.

        The area of an island is the number of cells with a value 1 in the island.

        Return the maximum area of an island in grid. If there is no island, return 0.
    # 2. Look at the examples they give you for what the algorithm should do. "Solution(input) -> output". Come up with 1 or 2 examples on your own, and write them down.

    # 3. Think out loud, and write down (!!) the possible high-level approaches to solving the problem. 
    #     Eg: "this two-sum problem can be brute-forced in O(n^2) time using two for-loops, or it can be solved in O(n) using a hashmap." 
    #     This doesn't have to be detailed, just a possible approach. Think about possible edge cases and how they could break the solution.

    #     Here, if you are completely blanking after 5 minutes, and can't even do a brute-force solution, then do what the OP said 
    #     - abort mission, and spend the next hour understanding the problem by looking at the solution. Once you understood the solution go to step 4.
        1. feel like this is just an extension of "number of islands" problem

        use number of islands solutions, but in dfs return the count if there is island or no

    # 4. Pick one of the approaches, and write out the pseudo code for it, while taking out loud as to what your thought process is.

        seen = set()

        def islandArea(r, c):
            

            # condition for in seen
            if (r, c) in seen:
                return 0

            seen.add((r, c))
            # condition for out of bounds
            if r < 0 or r > len(grid) or c < 0 or c > len(grid[0]):
                return 0
            # condition for 0
            if grid[r][c] == '0':
                return 0

            # recurse in 4 cardinal directions

            sum = islandArea(r - 1, c) + islandArea(r + 1, c) + islandArea(r, c - 1) + islandArea(r, c + 1)

            return 1 + sum

        res = 0
        for r in len(grid):
            for c in len(grid[0]):
                if grid[r][c] == "1":
                    area = islandArea(r, c)
                    res = max(res, area)
        
        return res
    # 5. CODE THE ACTUAL SOLUTION. If you actually followed steps 1-4, this part is going to be trivial. You will bang out the actual code often in under 5 minutes. 
    # Paste the code into leetcode (or whatever platform you are using) to ensure it works. You can even write your own test cases, and run locally.

    # 6. If you haven't addressed this in step 3 (when you were talking about approaches), think about how you would optimize the solution. Talk about big O here.

    fixed solution

    seen = set()

        def islandArea(r, c):
            

            # condition for in seen
            if (r, c) in seen:
                return 0

            seen.add((r, c))
            # condition for out of bounds
            if r < 0 or r >= len(grid) or c < 0 or c >= len(grid[0]): # need to include >=
                return 0
            # condition for 0
            print(r, c)
            if grid[r][c] == 0:
                return 0
            

            # recurse in 4 cardinal directions

            sum = islandArea(r - 1, c) + islandArea(r + 1, c) + islandArea(r, c - 1) + islandArea(r, c + 1)

            return 1 + sum

        res = 0
        for r in range(len(grid)):
            for c in range(len(grid[0])):
                if grid[r][c] == 1:
                    area = islandArea(r, c)
                    res = max(res, area)
        
        return res