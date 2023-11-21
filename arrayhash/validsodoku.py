
    # 1. Copy/paste the problem definition. Read it out loud and understand what they want.

        Determine if a 9 x 9 Sudoku board is valid. Only the filled cells need to be validated according to the following rules:

            Each row must contain the digits 1-9 without repetition.
            Each column must contain the digits 1-9 without repetition.
            Each of the nine 3 x 3 sub-boxes of the grid must contain the digits 1-9 without repetition.

        Note:

            A Sudoku board (partially filled) could be valid but is not necessarily solvable.
            Only the filled cells need to be validated according to the mentioned rules.

    # 2. Look at the examples they give you for what the algorithm should do. "Solution(input) -> output". Come up with 1 or 2 examples on your own, and write them down.

        must follow those 3 rules

    # 3. Think out loud, and write down (!!) the possible high-level approaches to solving the problem. 
    #     Eg: "this two-sum problem can be brute-forced in O(n^2) time using two for-loops, or it can be solved in O(n) using a hashmap." 
    #     This doesn't have to be detailed, just a possible approach. Think about possible edge cases and how they could break the solution.

    #     Here, if you are completely blanking after 5 minutes, and can't even do a brute-force solution, then do what the OP said 
    #     - abort mission, and spend the next hour understanding the problem by looking at the solution. Once you understood the solution go to step 4.

        1. Brute force solution
            iterate over all columns, check for duplicates in column
            iterate over all rows, check for duplicates in row

            iterate in every 3x3 square, check for duplicates, will be a very complicated loop

        2. similar to brute force, except we simplify the 3x3 search process

        we can use a hash set to store the set of nums in each 3x3 square, we can encode using floor div by 3


    # 4. Pick one of the approaches, and write out the pseudo code for it, while taking out loud as to what your thought process is.
        
        create dictionary of sets

        for idx in row:
            for idx in col:

                #iterate over every number
                if num is ".":
                    continue
                else if num in rowset or num in colset or num in squareset:
                    return False
                else:
                    add that num to the 3 sets
                
        return True


    # 5. CODE THE ACTUAL SOLUTION. If you actually followed steps 1-4, this part is going to be trivial. You will bang out the actual code often in under 5 minutes. 
    # Paste the code into leetcode (or whatever platform you are using) to ensure it works. You can even write your own test cases, and run locally.
        rowhash = {} #encoded by    ROW_NUM --> set()
        colhash = {} #encoded by    COL_NUM --> set()
        squarehash = {} #encoded by tuple(ROW_NUM, COL_NUM) --> set()

        for i in range(9):
            rowhash[i] = set()
            colhash[i] = set()

        for i in range(3):
            for j in range(3):
                squarehash[tuple((i, j))] = set()

        for i in range(9):  # i --> row
            for j in range(9): # j --> col

                n = board[i][j]
                if n == ".":
                    continue
                elif n in rowhash[i] or n in colhash[j] or n in squarehash[(i // 3, j // 3)]:
                    return False
                else:
                    #add
                    rowhash[i].add(n)

                    colhash[j].add(n)
                
                    squarehash[tuple((i // 3, j // 3))].add(n)

        return True

    # 6. If you haven't addressed this in step 3 (when you were talking about approaches), think about how you would optimize the solution. Talk about big O here.

        Maybe i can learn default dict so i do not need to initialize every dict. 
        Memory could be further improved by using just sets for rows and cols, but adds complexity to the code. especially for vertical
            - could use zip() or a transpose essentially, but that adds memory complication

        This solution is optimized, O(n^2)

        In the future, I will try to do a simpler solution first rather than trying to do a complex one at the beginning.