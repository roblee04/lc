
    # 1. Copy/paste the problem definition. Read it out loud and understand what they want.
        Given an array of integers temperatures represents the daily temperatures, return an array answer such that answer[i] is the number of days you have to wait after the ith day to get a warmer temperature. If there is no future day for which this is possible, keep answer[i] == 0 instead.
    # 2. Look at the examples they give you for what the algorithm should do. "Solution(input) -> output". Come up with 1 or 2 examples on your own, and write them down.

    # 3. Think out loud, and write down (!!) the possible high-level approaches to solving the problem. 
    #     Eg: "this two-sum problem can be brute-forced in O(n^2) time using two for-loops, or it can be solved in O(n) using a hashmap." 
    #     This doesn't have to be detailed, just a possible approach. Think about possible edge cases and how they could break the solution.

    #     Here, if you are completely blanking after 5 minutes, and can't even do a brute-force solution, then do what the OP said 
    #     - abort mission, and spend the next hour understanding the problem by looking at the solution. Once you understood the solution go to step 4.
        1. the key here is to use a stack
            - we will add each day AND idx to the stack

            - if the day we add is hotter than the previous, pop the day
                - continue to pop the days til no more
                - we want to add hot day idx - prev day idx

            - if the day we add is colder or the same, just add to the stack

    # 4. Pick one of the approaches, and write out the pseudo code for it, while taking out loud as to what your thought process is.

        res = []
        stack = []

        for i in range(len(temperatures)):

            if stack and temperatures[i] > temperatures(stack[-1]):
                # do while loop 
                    # pop stack and add to res

                # add temp to stack

            else:
                stack.append(i)

        return res
    # 5. CODE THE ACTUAL SOLUTION. If you actually followed steps 1-4, this part is going to be trivial. You will bang out the actual code often in under 5 minutes. 
    # Paste the code into leetcode (or whatever platform you are using) to ensure it works. You can even write your own test cases, and run locally.
        res = []
        stack = []

        for i in range(len(temperatures)):

            if stack and temperatures[i] > temperatures[stack[0]]:
                # do while loop 
                    # pop stack and add to res
                while stack and temperatures[i] > temperatures[stack[0]]:
                    prev = stack.pop(0)
                    res.append(i - prev)
                    

            stack.append(i)

        while stack:
            stack.pop()
            res.append(0)

        return res

        actually my approach was a bit flawed
    # 6. If you haven't addressed this in step 3 (when you were talking about approaches), think about how you would optimize the solution. Talk about big O here.

        res = [0] * len(temperatures)
        stack = []

        for i in range(len(temperatures)):

            if stack and temperatures[i] > temperatures[stack[-1]]:
                # do while loop 
                    # pop stack and add to res
                while stack and temperatures[i] > temperatures[stack[-1]]:
                    prev = stack.pop()
                    res[prev] = (i - prev)
                    

            stack.append(i)

        return res

        YAY tnx neetcode