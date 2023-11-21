
    # 1. Copy/paste the problem definition. Read it out loud and understand what they want.
        Suppose an array of length n sorted in ascending order is rotated between 1 and n times. For example, the array nums = [0,1,2,4,5,6,7] might become:

            [4,5,6,7,0,1,2] if it was rotated 4 times.
            [0,1,2,4,5,6,7] if it was rotated 7 times.

        Notice that rotating an array [a[0], a[1], a[2], ..., a[n-1]] 1 time results in the array [a[n-1], a[0], a[1], a[2], ..., a[n-2]].

        Given the sorted rotated array nums of unique elements, return the minimum element of this array.

        You must write an algorithm that runs in O(log n) time.
    # 2. Look at the examples they give you for what the algorithm should do. "Solution(input) -> output". Come up with 1 or 2 examples on your own, and write them down.

    # 3. Think out loud, and write down (!!) the possible high-level approaches to solving the problem. 
    #     Eg: "this two-sum problem can be brute-forced in O(n^2) time using two for-loops, or it can be solved in O(n) using a hashmap." 
    #     This doesn't have to be detailed, just a possible approach. Think about possible edge cases and how they could break the solution.

    #     Here, if you are completely blanking after 5 minutes, and can't even do a brute-force solution, then do what the OP said 
    #     - abort mission, and spend the next hour understanding the problem by looking at the solution. Once you understood the solution go to step 4.

    # 4. Pick one of the approaches, and write out the pseudo code for it, while taking out loud as to what your thought process is.
        l = 0
        r = len(nums) - 1

        while l < r:
            m = (l + r) // 2

            if nums[m] < nums[r]:
                # its i the left
                r = m 
            else:
                l = m + 1

        return nums[l]
 
    # 5. CODE THE ACTUAL SOLUTION. If you actually followed steps 1-4, this part is going to be trivial. You will bang out the actual code often in under 5 minutes. 
    # Paste the code into leetcode (or whatever platform you are using) to ensure it works. You can even write your own test cases, and run locally.

    # 6. If you haven't addressed this in step 3 (when you were talking about approaches), think about how you would optimize the solution. Talk about big O here.

        key to solving this problem is being able to effectively determine what side the small num will be on

        i would have maybe gotten to this solution