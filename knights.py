


def solution(n, start_col, start_row, end_col, end_row):

    dir = [...]

    memo = {} # position : # steps

    def dfs(row, col):

        # if out of bounds
        # return 100000

        # if in memo, return memo

        # if == end
        # return 0


        min_steps = 10000
        for i, j in direction:

            min_steps = min(min_steps, 1 + dfs(row + i, col + j))

        memo[(row, col)] = min_steps

    
    return memo[(end_row, end_col)]

