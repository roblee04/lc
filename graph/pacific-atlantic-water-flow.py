
    # 1. Copy/paste the problem definition. Read it out loud and understand what they want.
        There is an m x n rectangular island that borders both the Pacific Ocean and Atlantic Ocean. The Pacific Ocean touches the island's left and top edges, and the Atlantic Ocean touches the island's right and bottom edges.

        The island is partitioned into a grid of square cells. You are given an m x n integer matrix heights where heights[r][c] represents the height above sea level of the cell at coordinate (r, c).

        The island receives a lot of rain, and the rain water can flow to neighboring cells directly north, south, east, and west if the neighboring cell's height is less than or equal to the current cell's height. Water can flow from any cell adjacent to an ocean into the ocean.

        Return a 2D list of grid coordinates result where result[i] = [ri, ci] denotes that rain water can flow from cell (ri, ci) to both the Pacific and Atlantic oceans.
    # 2. Look at the examples they give you for what the algorithm should do. "Solution(input) -> output". Come up with 1 or 2 examples on your own, and write them down.

    # 3. Think out loud, and write down (!!) the possible high-level approaches to solving the problem. 
    #     Eg: "this two-sum problem can be brute-forced in O(n^2) time using two for-loops, or it can be solved in O(n) using a hashmap." 
    #     This doesn't have to be detailed, just a possible approach. Think about possible edge cases and how they could break the solution.

    #     Here, if you are completely blanking after 5 minutes, and can't even do a brute-force solution, then do what the OP said 
    #     - abort mission, and spend the next hour understanding the problem by looking at the solution. Once you understood the solution go to step 4.
        1. break this down into two problems,

        try to find all squares reachable by edges that connect to pacific ocean

        try to do the same with atlantic

        any squares that overlap are able to reach both!

        for each ocean algo,
        - use some graph search algo to traverse vert + horiz
        - go there if you are able to, e.g. number is higher
        - b4 you leave the square, add it to the ocean's seen list

    # 4. Pick one of the approaches, and write out the pseudo code for it, while taking out loud as to what your thought process is.

    # 5. CODE THE ACTUAL SOLUTION. If you actually followed steps 1-4, this part is going to be trivial. You will bang out the actual code often in under 5 minutes. 
    # Paste the code into leetcode (or whatever platform you are using) to ensure it works. You can even write your own test cases, and run locally.

    # 6. If you haven't addressed this in step 3 (when you were talking about approaches), think about how you would optimize the solution. Talk about big O here.

