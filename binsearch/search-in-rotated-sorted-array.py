
    # 1. Copy/paste the problem definition. Read it out loud and understand what they want.
        There is an integer array nums sorted in ascending order (with distinct values).

        Prior to being passed to your function, nums is possibly rotated at an unknown pivot index k (1 <= k < nums.length) such that the resulting array is [nums[k], nums[k+1], ..., nums[n-1], nums[0], nums[1], ..., nums[k-1]] (0-indexed). For example, [0,1,2,4,5,6,7] might be rotated at pivot index 3 and become [4,5,6,7,0,1,2].

        Given the array nums after the possible rotation and an integer target, return the index of target if it is in nums, or -1 if it is not in nums.

        You must write an algorithm with O(log n) runtime complexity.
    # 2. Look at the examples they give you for what the algorithm should do. "Solution(input) -> output". Come up with 1 or 2 examples on your own, and write them down.

    # 3. Think out loud, and write down (!!) the possible high-level approaches to solving the problem. 
    #     Eg: "this two-sum problem can be brute-forced in O(n^2) time using two for-loops, or it can be solved in O(n) using a hashmap." 
    #     This doesn't have to be detailed, just a possible approach. Think about possible edge cases and how they could break the solution.

    #     Here, if you are completely blanking after 5 minutes, and can't even do a brute-force solution, then do what the OP said 
    #     - abort mission, and spend the next hour understanding the problem by looking at the solution. Once you understood the solution go to step 4.
        1. thinking about finding min and max and maybe doing something with that? 

        2. ok found solution, essentially treat it as if we have 2 sorted arrays
        - we can choose which partition to sort in by checking if min <= target <= max

            1. check which side we are on

            2. do binary search
    # 4. Pick one of the approaches, and write out the pseudo code for it, while taking out loud as to what your thought process is.

        # 4 5 1 2 3, if mid < left we are on the right side
        # 3 4 5 1 2, if mid >= right we are on the left side

        init ptrs

        while l <= r:
            if we found val, ret

            check if left side:
                # 2 3 4 5 1, if tar > mid, l = mid + 1
                # if tar < left, l = mid + 1
                # else r = m

            check if right side:
                # 5 1 2 3 4, if tar < mid, r = mid - 1
                # if tar > right, r = mid  - 1
                # else l = m

    # 5. CODE THE ACTUAL SOLUTION. If you actually followed steps 1-4, this part is going to be trivial. You will bang out the actual code often in under 5 minutes. 
    # Paste the code into leetcode (or whatever platform you are using) to ensure it works. You can even write your own test cases, and run locally.

        l, r = 0, len(nums) - 1

        while l <= r:
            m = (l + r) // 2
            if nums[m] == target:
                return m 

            # check left
            if nums[m] >= nums[l]:
                if target > nums[m] or target < nums[l]:
                    l = m + 1
                else:
                    r = m - 1
            #check right
            else:
                if target < nums[m] or target > nums[r]:
                    r = m - 1
                else:
                    l = m + 1

        return -1
    # 6. If you haven't addressed this in step 3 (when you were talking about approaches), think about how you would optimize the solution. Talk about big O here.


        deconstructing the problem helps,
        the approach i had was not bad though.
