
    # 1. Copy/paste the problem definition. Read it out loud and understand what they want.

        Given an m x n 2D binary grid grid which represents a map of '1's (land) and '0's (water),
         return the number of islands.

        An island is surrounded by water 
        and is formed by connecting adjacent lands horizontally or vertically.
        You may assume all four edges of the grid are all surrounded by water.
    # 2. Look at the examples they give you for what the algorithm should do. "Solution(input) -> output". Come up with 1 or 2 examples on your own, and write them down.

    # 3. Think out loud, and write down (!!) the possible high-level approaches to solving the problem. 
    #     Eg: "this two-sum problem can be brute-forced in O(n^2) time using two for-loops, or it can be solved in O(n) using a hashmap." 
    #     This doesn't have to be detailed, just a possible approach. Think about possible edge cases and how they could break the solution.

    #     Here, if you are completely blanking after 5 minutes, and can't even do a brute-force solution, then do what the OP said 
    #     - abort mission, and spend the next hour understanding the problem by looking at the solution. Once you understood the solution go to step 4.


        1. the idea is to first convert to a graph problem

        a. convert 2d to coordinate system. each node is a 0 / 1. each edge represents a path to land.

        b. finding islands
            find an entire island using a BFS approach. A helper function will search vertically and horizontally
            for island terrain. All coordinates will be added to the "seen" set.

        c. iterate throughout the entire thing

    # 4. Pick one of the approaches, and write out the pseudo code for it, while taking out loud as to what your thought process is.

        for row in graph:
            for element in row:
                if in seen, skip

                else:
                    call helper function
                    add one to islands counter

    # 5. CODE THE ACTUAL SOLUTION. If you actually followed steps 1-4, this part is going to be trivial. You will bang out the actual code often in under 5 minutes. 
    # Paste the code into leetcode (or whatever platform you are using) to ensure it works. You can even write your own test cases, and run locally.

        seen = set()
        islands = 0
        for row in range(len(grid)):
            for col in range(len(grid[0])):
                c = [col, row]
                if c not in seen and grid[r][c] == "1":
                    find_island(coordinate)
                    islands += 1

                else:
                    continue
            
        return islands

        def find_island(coordinate):
            row_b = len(grid[0])
            col_b = len(grid)

            seen.add(coordinate)

            if coordinate[0] < col_b:
                c = [coordinate[0], coordinate[1] + 1]
                find_island(c)
            
            if coordinate[1] < row_b:
                c = [coordinate[0] + 1, coordinate[1]]
                find_island(c)


    # 6. If you haven't addressed this in step 3 (when you were talking about approaches), think about how you would optimize the solution. Talk about big O here.

        need to practice bfs, dfs both recursive and iterative solutions

        lets redo find island

        def find_island(coordinate):

            # check bounds
            x = coordinate[0]
            y = coordinate[1]

            if x < 0 or x > len(grid[0]) or y < 0 or y > len(grid):
                return

            seen.add(coordinate)

            find_island((x + 1, y))
            find_island((x - 1, y))
            find_island((x, y + 1))
            find_island((x, y - 1))         

        
        runtime error?