
    # 1. Copy/paste the problem definition. Read it out loud and understand what they want.
        Given an m x n matrix board containing 'X' and 'O', capture all regions that are 4-directionally surrounded by 'X'.

        A region is captured by flipping all 'O's into 'X's in that surrounded region.
    # 2. Look at the examples they give you for what the algorithm should do. "Solution(input) -> output". Come up with 1 or 2 examples on your own, and write them down.

    # 3. Think out loud, and write down (!!) the possible high-level approaches to solving the problem. 
    #     Eg: "this two-sum problem can be brute-forced in O(n^2) time using two for-loops, or it can be solved in O(n) using a hashmap." 
    #     This doesn't have to be detailed, just a possible approach. Think about possible edge cases and how they could break the solution.

    #     Here, if you are completely blanking after 5 minutes, and can't even do a brute-force solution, then do what the OP said 
    #     - abort mission, and spend the next hour understanding the problem by looking at the solution. Once you understood the solution go to step 4.
        1. basically first, look for "islands", anything that is SURROUNDED by Xs

        if it is not an island, dont flip

        if it is, use another graph search algorithm to flip all Os


    # 4. Pick one of the approaches, and write out the pseudo code for it, while taking out loud as to what your thought process is.

        seen tiles = set()

        doubl for loop to traverse entire board

            if tile is not X, check if is island
                var = check if is island call

                if var = is island, flip
                    call other flip function
        
        return board

    # 5. CODE THE ACTUAL SOLUTION. If you actually followed steps 1-4, this part is going to be trivial. You will bang out the actual code often in under 5 minutes. 
    # Paste the code into leetcode (or whatever platform you are using) to ensure it works. You can even write your own test cases, and run locally.

        def checkIsland(i, j):

            if board[i][j] == 'X':
                return 0

            # bounds
            if i == 0 or i == (len(board) - 1) or j == 0 or j ==(len(board[0]) - 1):
                return 1

            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
                return 0

            sum = checkIsland(i + 1, j) + checkIsland(i - 1, j) + checkIsland(i, j + 1) + checkIsland(i, j - 1)

            return sum

        def flip(i, j):

            if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
                return

            if board[i][j] == 'O':
                board[i][j] == 'X'
            else:
                return
            
            flip(i + 1, j)
            flip(i - 1, j)
            flip(i, j + 1)
            flip(i, j - 1)


        seen = set()

        for i in range(len(board)):
            for j in range(len(board[0])):

                tile = board[i][j]

                if tile != 'X':
                    var = checkIsland(i, j)

                    if var == 0:
                        flip(i, j)
        


    # 6. If you haven't addressed this in step 3 (when you were talking about approaches), think about how you would optimize the solution. Talk about big O here.

    NEETCODE solution, thinking backwards

    # capture non-islands
    def mark(i, j):
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[0]):
            return

        if board[i][j] != 'O':
            return
        
        if board[i][j] == 'O':
            board[i][j] = 'T'

        mark(i + 1, j)
        mark(i - 1, j)
        mark(i, j + 1)
        mark(i, j - 1)

    # capture all edges
    for i in range(len(board)):
        # ROWS
        mark(i, 0)
        mark(i, len(board[0]) - 1)
    
    for j in range(len(board[0])):
        #COLS
        mark(0, j)
        mark(len(board) - 1, j)

    # flip all islands

    for i in range(len(board)):
        for j in range(len(board[0])):
            if board[i][j] == 'T':
                board[i][j] = 'O'
            elif board[i][j] == 'O':
                board[i][j] = 'X'
