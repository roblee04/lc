# 1. Copy/paste the problem definition. Read it out loud and understand what they want.
Given an m x n integer matrix matrix, if an element is 0, set its entire row and column to 0's.

You must do it in place.
# 2. Look at the examples they give you for what the algorithm should do. "Solution(input) -> output". Come up with 1 or 2 examples on your own, and write them down.

# 3. Think out loud, and write down (!!) the possible high-level approaches to solving the problem. 
#     Eg: "this two-sum problem can be brute-forced in O(n^2) time using two for-loops, or it can be solved in O(n) using a hashmap." 
#     This doesn't have to be detailed, just a possible approach. Think about possible edge cases and how they could break the solution.

#     Here, if you are completely blanking after 5 minutes, and can't even do a brute-force solution, then do what the OP said 
#     - abort mission, and spend the next hour understanding the problem by looking at the solution. Once you understood the solution go to step 4.

iterate through entire matrix and track rows and columns in sets

# 4. Pick one of the approaches, and write out the pseudo code for it, while taking out loud as to what your thought process is.

# 5. CODE THE ACTUAL SOLUTION. If you actually followed steps 1-4, this part is going to be trivial. You will bang out the actual code often in under 5 minutes. 
# Paste the code into leetcode (or whatever platform you are using) to ensure it works. You can even write your own test cases, and run locally.
def setZeroes(self, matrix: List[List[int]]) -> None:
    """
    Do not return anything, modify matrix in-place instead.
    """
    zRow = set()
    zCol = set()


    for col in range(len(matrix)):
        for row in range(len(matrix[0])):
            element = matrix[col][row]

            if element == 0:
                zRow.add(row)
                zCol.add(col)
    
    # augment matrix
    for col in range(len(matrix)):
        if col in zCol:
            for i in range(len(matrix[0])):
                matrix[col][i] = 0
    
    for row in range(len(matrix[0])):
        if row in zRow:
            for i in range(len(matrix)):
                matrix[i][row] = 0
    
    return matrix

# 6. If you haven't addressed this in step 3 (when you were talking about approaches), think about how you would optimize the solution. Talk about big O here.
