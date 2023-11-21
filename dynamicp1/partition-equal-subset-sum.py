
    # 1. Copy/paste the problem definition. Read it out loud and understand what they want.
        Given an integer array nums, return true if you can partition the array into two subsets such that the sum of the elements in both subsets is equal or false otherwise.
    # 2. Look at the examples they give you for what the algorithm should do. "Solution(input) -> output". Come up with 1 or 2 examples on your own, and write them down.

    # 3. Think out loud, and write down (!!) the possible high-level approaches to solving the problem. 
    #     Eg: "this two-sum problem can be brute-forced in O(n^2) time using two for-loops, or it can be solved in O(n) using a hashmap." 
    #     This doesn't have to be detailed, just a possible approach. Think about possible edge cases and how they could break the solution.

    #     Here, if you are completely blanking after 5 minutes, and can't even do a brute-force solution, then do what the OP said 
    #     - abort mission, and spend the next hour understanding the problem by looking at the solution. Once you understood the solution go to step 4.
        1. brute force

        2. sorting, nlogn

        3. prob some n solution

        So we want to break it up into decision trees, and then we want to convert that into a solution
        - first, the calculation of the decision tree can be done via dfs
            - for dfs to work, we need some base cases
            - we want to populate some cache with true false values
            - if the sum > target, terminate

        - second, to stop repeated work, we can have a memoized table
            - for this problem, this table will check if some value can be created from the givne numbers
            - True if yes
    # 4. Pick one of the approaches, and write out the pseudo code for it, while taking out loud as to what your thought process is.
        if sum(nums) % 2 == 1:
            return False
        target = sum(nums) // 2


        cache = set()

        def dfs(idx, s):

            # check cache
            if s > target or idx > len(nums) - 1:
                return False

            lsum = nums[idx] + s
            if lsum == target:
                return True

            cache.add((idx, s))
            v1, v2 = False, False
            if (idx + 1, s) in cache:
                v1 = True
            else:
                v1 = dfs(idx + 1, s) 
            
            if (idx + 1, s + nums[idx]) in cache:
                v2 = True
            else:
                v1 = dfs(idx + 1, s + nums[idx]) 

            return v1 or v2

        print(cache)
        return dfs(0, 0)

        without cache addition, soltion works, 
        unable to add caching
    # 5. CODE THE ACTUAL SOLUTION. If you actually followed steps 1-4, this part is going to be trivial. You will bang out the actual code often in under 5 minutes. 
    # Paste the code into leetcode (or whatever platform you are using) to ensure it works. You can even write your own test cases, and run locally.
        f (sum(nums) % 2) == 1:
            return False

        cache = {}

        target = sum(nums) // 2

        
        def dfs(idx, s):
            if (idx, s) in cache:
                return cache[(idx, s)]

            if s > target or idx >= len(nums):
                return False

            if s == target:
                return True

            # check curr or not curr
            v1, v2 = False, False

            v1 = dfs(idx + 1, s)
            v2 = dfs(idx + 1, s + nums[idx])

            cache[(idx, s)] = v1 or v2

            return cache[(idx, s)]


        a = dfs(0, 0)
        
        return a
    # 6. If you haven't addressed this in step 3 (when you were talking about approaches), think about how you would optimize the solution. Talk about big O here.

        back tracking needs practice
        still a 
