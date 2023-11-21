
    # 1. Copy/paste the problem definition. Read it out loud and understand what they want.
        You are climbing a staircase. It takes n steps to reach the top.

        Each time you can either climb 1 or 2 steps. In how many distinct ways can you climb to the top?
    # 2. Look at the examples they give you for what the algorithm should do. "Solution(input) -> output". Come up with 1 or 2 examples on your own, and write them down.

    # 3. Think out loud, and write down (!!) the possible high-level approaches to solving the problem. 
    #     Eg: "this two-sum problem can be brute-forced in O(n^2) time using two for-loops, or it can be solved in O(n) using a hashmap." 
    #     This doesn't have to be detailed, just a possible approach. Think about possible edge cases and how they could break the solution.

    #     Here, if you are completely blanking after 5 minutes, and can't even do a brute-force solution, then do what the OP said 
    #     - abort mission, and spend the next hour understanding the problem by looking at the solution. Once you understood the solution go to step 4.

        1. number of steps is limiting factor for ways to reach the top

        naive solution:
            global counter

            recursive function to iterate on n - 1 and n - 2
            - stop if n < 0

        to save time, use memoization to stop repeated work
        - store calculations in a hashmap

    # 4. Pick one of the approaches, and write out the pseudo code for it, while taking out loud as to what your thought process is.

        global counter

        recursive function + iterate on n-1 and n-2
        - also store the result of those functions in a hashmap

    # 5. CODE THE ACTUAL SOLUTION. If you actually followed steps 1-4, this part is going to be trivial. You will bang out the actual code often in under 5 minutes. 
    # Paste the code into leetcode (or whatever platform you are using) to ensure it works. You can even write your own test cases, and run locally.

        counter = 0

        d = {}

        def climb_stair(steps):

            if steps <= 0:
                return 0

            if steps in d:
                return d[steps]

            # calculations

            sum = 1 + climb_stair(steps - 1) + climb_stair(steps - 2)
            d[steps] = sum
            return sum

        return climb_stair(n) 

    # 6. If you haven't addressed this in step 3 (when you were talking about approaches), think about how you would optimize the solution. Talk about big O here.

