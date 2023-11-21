
    # 1. Copy/paste the problem definition. Read it out loud and understand what they want.
        Given an integer array nums, find a
        subarray
        that has the largest product, and return the product.

        The test cases are generated so that the answer will fit in a 32-bit integer.
    # 2. Look at the examples they give you for what the algorithm should do. "Solution(input) -> output". Come up with 1 or 2 examples on your own, and write them down.

    # 3. Think out loud, and write down (!!) the possible high-level approaches to solving the problem. 
    #     Eg: "this two-sum problem can be brute-forced in O(n^2) time using two for-loops, or it can be solved in O(n) using a hashmap." 
    #     This doesn't have to be detailed, just a possible approach. Think about possible edge cases and how they could break the solution.

    #     Here, if you are completely blanking after 5 minutes, and can't even do a brute-force solution, then do what the OP said 
    #     - abort mission, and spend the next hour understanding the problem by looking at the solution. Once you understood the solution go to step 4.
        1. brute force approach, keep creating subarrays and find the sum of eveyr one of them, keep the largest number found
            O(n^2)
        
        2. keep track of minimums and maximums

        they will keep swapping

    # 4. Pick one of the approaches, and write out the pseudo code for it, while taking out loud as to what your thought process is.

    # 5. CODE THE ACTUAL SOLUTION. If you actually followed steps 1-4, this part is going to be trivial. You will bang out the actual code often in under 5 minutes. 
    # Paste the code into leetcode (or whatever platform you are using) to ensure it works. You can even write your own test cases, and run locally.
        res = max(nums)
        lmin, lmax = 1, 1

        for n in nums:
            # if we ever hit 0
            if n == 0:
                lmin, lmax = 1, 1
                continue

            tmp = n * lmax
            lmax = max(n * lmax, n * lmin)
            lmin = min(tmp, n * lmin)
            res = max(res, lmax)

        return lmax
    # 6. If you haven't addressed this in step 3 (when you were talking about approaches), think about how you would optimize the solution. Talk about big O here.

