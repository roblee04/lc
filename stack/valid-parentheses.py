
    # 1. Copy/paste the problem definition. Read it out loud and understand what they want.

        Given a string s containing just the characters '(', ')', '{', '}', '[' and ']', determine if the input string is valid.

        An input string is valid if:

            Open brackets must be closed by the same type of brackets.
            Open brackets must be closed in the correct order.
            Every close bracket has a corresponding open bracket of the same type.


    # 2. Look at the examples they give you for what the algorithm should do. "Solution(input) -> output". Come up with 1 or 2 examples on your own, and write them down.

        input: {()}     output: true

        input: {(})     output: false


    # 3. Think out loud, and write down (!!) the possible high-level approaches to solving the problem. 
    #     Eg: "this two-sum problem can be brute-forced in O(n^2) time using two for-loops, or it can be solved in O(n) using a hashmap." 
    #     This doesn't have to be detailed, just a possible approach. Think about possible edge cases and how they could break the solution.

    #     Here, if you are completely blanking after 5 minutes, and can't even do a brute-force solution, then do what the OP said 
    #     - abort mission, and spend the next hour understanding the problem by looking at the solution. Once you understood the solution go to step 4.

        1. use a stack!

        - this stack will hold all left parenthesis
        - it will be filled up by iterating through the string
        - if a right parenthesis is ever encountered, try to pop the opposite parenthesis
            - if it is not right, return error
    # 4. Pick one of the approaches, and write out the pseudo code for it, while taking out loud as to what your thought process is.

        make stack

        for p in string:

            if left, add to stack

            if right, check if opp exists on stack

                if not, return false

    # 5. CODE THE ACTUAL SOLUTION. If you actually followed steps 1-4, this part is going to be trivial. You will bang out the actual code often in under 5 minutes. 
    # Paste the code into leetcode (or whatever platform you are using) to ensure it works. You can even write your own test cases, and run locally.

        st = []
        opening = set(["(", "{", "["])
        closing = { "}":"{", "]":"[", ")":"(" }

        for p in s:

            if p in opening:
                st.append(p)
                continue
            
            if p in closing:

                if not st or closing[p] != st[-1]:
                    return False
                
                st.pop()
        
        return not st


    # 6. If you haven't addressed this in step 3 (when you were talking about approaches), think about how you would optimize the solution. Talk about big O here.

    yay