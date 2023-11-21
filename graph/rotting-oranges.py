
    # 1. Copy/paste the problem definition. Read it out loud and understand what they want.
        You are given an m x n grid where each cell can have one of three values:

            0 representing an empty cell,
            1 representing a fresh orange, or
            2 representing a rotten orange.

        Every minute, any fresh orange that is 4-directionally adjacent to a rotten orange becomes rotten.

        Return the minimum number of minutes that must elapse until no cell has a fresh orange. If this is impossible, return -1.
    # 2. Look at the examples they give you for what the algorithm should do. "Solution(input) -> output". Come up with 1 or 2 examples on your own, and write them down.

    # 3. Think out loud, and write down (!!) the possible high-level approaches to solving the problem. 
    #     Eg: "this two-sum problem can be brute-forced in O(n^2) time using two for-loops, or it can be solved in O(n) using a hashmap." 
    #     This doesn't have to be detailed, just a possible approach. Think about possible edge cases and how they could break the solution.

    #     Here, if you are completely blanking after 5 minutes, and can't even do a brute-force solution, then do what the OP said 
    #     - abort mission, and spend the next hour understanding the problem by looking at the solution. Once you understood the solution go to step 4.
        1. thinking of using some sort of bfs algorithm

            the tricky part is if there are multiple rotting oranges, how do you sync up each recursive call?

            thinking of using a while loop with an outside counter?

            i have a solution!
                we create another n*m board to store the maximum time an orange can be fresh for according to the rules of the game

                iterate over each rotting orange in order to populate and update this board, have a running max to keep track of highest value seen

        2. implement bfs with queue, neetcode
        - first find no. of fresh oranges + coordinates of rotting oranges
        - add rotting to queue

    

    # 4. Pick one of the approaches, and write out the pseudo code for it, while taking out loud as to what your thought process is.

        first find no. of fresh oranges + coordinates of rotting oranges to queue

        while loop to pop thru the queue

            for all 4 directions, check if in bounds and if it is a fresh orange
                if so, add it to the queue
            else, continue

            on each iteration add to time

    # 5. CODE THE ACTUAL SOLUTION. If you actually followed steps 1-4, this part is going to be trivial. You will bang out the actual code often in under 5 minutes. 
    # Paste the code into leetcode (or whatever platform you are using) to ensure it works. You can even write your own test cases, and run locally.

        q = collections.deque()
        fresh, time = 0, 0

        for i in range(len(grid)):
            for j in range(len(grid[0])):
                if grid[i][j] == 1:
                    fresh += 1
                if grid[i][j] == 2:
                    q.append((i, j))

        directions = [(1, 0), (-1, 0), (0, 1), (0, -1)]
        while q and fresh > 0:

            for i in range(len(q)):

                r, c = q.popleft()

                for dr, dc in directions:
                    row = r + dr
                    col = c + dc

                    if row < 0 or row >= len(grid) or col < 0 or col >= len(grid[0]) or grid[row][col] != 1:
                        continue

                    q.append((row, col))
                    grid[row][col] = 2
                    fresh -= 1

            time += 1 

        return time if fresh == 0 else -1

            
        
    # 6. If you haven't addressed this in step 3 (when you were talking about approaches), think about how you would optimize the solution. Talk about big O here.

