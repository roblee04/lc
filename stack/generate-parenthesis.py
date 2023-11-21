
    # 1. Copy/paste the problem definition. Read it out loud and understand what they want.
        Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.
    # 2. Look at the examples they give you for what the algorithm should do. "Solution(input) -> output". Come up with 1 or 2 examples on your own, and write them down.

    # 3. Think out loud, and write down (!!) the possible high-level approaches to solving the problem. 
    #     Eg: "this two-sum problem can be brute-forced in O(n^2) time using two for-loops, or it can be solved in O(n) using a hashmap." 
    #     This doesn't have to be detailed, just a possible approach. Think about possible edge cases and how they could break the solution.

    #     Here, if you are completely blanking after 5 minutes, and can't even do a brute-force solution, then do what the OP said 
    #     - abort mission, and spend the next hour understanding the problem by looking at the solution. Once you understood the solution go to step 4.
        1. this problem can be solved by combining a "valid parenthesis" and backtracking approach
            - i do want to avoid passing in stacks though, because they might be janky 

    # 4. Pick one of the approaches, and write out the pseudo code for it, while taking out loud as to what your thought process is.
        parenthesis dictionary here

        res = []

        def dfs(i, stack, r):
            # 'i' represents which decision we are on
            # stack shows previous parenthesis
            if i == n:
                res.append(r)
                return

            #choose betwen the two
            dfs(i + 1, stack + ['('], r + "(")
            
            if stack.peek() == '(':
                stack.pop()
                r += ")"
                dfs(i + 1, stack + ['('], r + "(")
            
            return

        this may be an over thinking solution

        nah this was the correct approach just not clean


    # 5. CODE THE ACTUAL SOLUTION. If you actually followed steps 1-4, this part is going to be trivial. You will bang out the actual code often in under 5 minutes. 
    # Paste the code into leetcode (or whatever platform you are using) to ensure it works. You can even write your own test cases, and run locally.

        # base case, open = close = n
        # if open < n, add paren
        # if close < n, add paren

        stack = []
        res = []

        def bt(open, close):

            if open == close == n:
                res.append("".join(stack))
                return

            if open < n:
                stack.append("(")
                bt(open + 1, close)
                stack.pop()

            if close < open:
                stack.append(")")
                bt(open, close + 1)
                stack.pop()

        bt(0,0)

        return res

        _
        stack = []
        res = []

        def backtrack(openN, closedN):
            if openN == closedN == n:
                res.append("".join(stack))
                return

            if openN < n:
                stack.append("(")
                backtrack(openN + 1, closedN)
                stack.pop()
            if closedN < openN:
                stack.append(")")
                backtrack(openN, closedN + 1)
                stack.pop()

        backtrack(0, 0)
        return res

            
    # 6. If you haven't addressed this in step 3 (when you were talking about approaches), think about how you would optimize the solution. Talk about big O here.

