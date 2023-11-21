
    # 1. Copy/paste the problem definition. Read it out loud and understand what they want.
        You are given a m x n 2D grid initialized with these three possible values.

        -1 - A wall or an obstacle.
        0 - A gate.
        INF - Infinity means an empty room. We use the value 2^31 - 1 = 2147483647 to represent INF as you may assume that the distance to a gate is less than 2147483647.
        Fill each empty room with the distance to its nearest gate. If it is impossible to reach a Gate, that room should remain filled with INF
    # 2. Look at the examples they give you for what the algorithm should do. "Solution(input) -> output". Come up with 1 or 2 examples on your own, and write them down.

    # 3. Think out loud, and write down (!!) the possible high-level approaches to solving the problem. 
    #     Eg: "this two-sum problem can be brute-forced in O(n^2) time using two for-loops, or it can be solved in O(n) using a hashmap." 
    #     This doesn't have to be detailed, just a possible approach. Think about possible edge cases and how they could break the solution.

    #     Here, if you are completely blanking after 5 minutes, and can't even do a brute-force solution, then do what the OP said 
    #     - abort mission, and spend the next hour understanding the problem by looking at the solution. Once you understood the solution go to step 4.

        1. was thinking of using a dfs solution again, but that will be very slow

        2. solution is very similar to the rotting oranges solution
        basically, make a a bfs and also populate the grid starting from the gates rather than an emptyroom


        practice thinking backwards
    # 4. Pick one of the approaches, and write out the pseudo code for it, while taking out loud as to what your thought process is.

        so first, populate a queue with gate coordinates

        next, use a while loop and execute a for loop on all the children

            update the grid coordinates with their distances
    # 5. CODE THE ACTUAL SOLUTION. If you actually followed steps 1-4, this part is going to be trivial. You will bang out the actual code often in under 5 minutes. 
    # Paste the code into leetcode (or whatever platform you are using) to ensure it works. You can even write your own test cases, and run locally.

        q = deque()

        # have a visited set, to not revisit things
        seen = set()

        def explore(r, c):
            if r < 0 or r >= len(rooms) or c < 0 or c >= len(rooms[0]) or rooms[r][c] == -1 or (r, c) in seen:
                return 
            
            seen.add((r, c))
            q.append((r, c))

        for i in range(len(rooms)):
            for j in range(len(rooms[0])):
                if rooms[i][j] == 0:
                    q.append((i, j))
                    seen.add((i, j))

        d = 0

        while q:
            for i in range(len(q)):
                r, c = q.popleft()
                rooms[r][c] = d

                #then try in different directions

                explore(i + 1, j)
                explore(i - 1, j)
                explore(i, j + 1)
                explore(i, j - 1)
            
            d += 1
    # 6. If you haven't addressed this in step 3 (when you were talking about approaches), think about how you would optimize the solution. Talk about big O here.

