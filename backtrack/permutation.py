
    # 1. Copy/paste the problem definition. Read it out loud and understand what they want.
        Given an array nums of distinct integers, return all the possible permutations. You can return the answer in any order.

    # 2. Look at the examples they give you for what the algorithm should do. "Solution(input) -> output". Come up with 1 or 2 examples on your own, and write them down.

    # 3. Think out loud, and write down (!!) the possible high-level approaches to solving the problem. 
    #     Eg: "this two-sum problem can be brute-forced in O(n^2) time using two for-loops, or it can be solved in O(n) using a hashmap." 
    #     This doesn't have to be detailed, just a possible approach. Think about possible edge cases and how they could break the solution.

    #     Here, if you are completely blanking after 5 minutes, and can't even do a brute-force solution, then do what the OP said 
    #     - abort mission, and spend the next hour understanding the problem by looking at the solution. Once you understood the solution go to step 4.

        1. essentially, we want to convert the decision tree that we made into code

        1. for loop, to iterate on the rest of the options
        2. something to prevent us from going on dupes

    # 4. Pick one of the approaches, and write out the pseudo code for it, while taking out loud as to what your thought process is.

        res = []

        def dfs(num, lst):

            if num in lst:
                res.append(lst)

            # else make the lst
            
            for n in nums:
                if n not in lst:
                    dfs(n, lst)

        return res
            
    # 5. CODE THE ACTUAL SOLUTION. If you actually followed steps 1-4, this part is going to be trivial. You will bang out the actual code often in under 5 minutes. 
    # Paste the code into leetcode (or whatever platform you are using) to ensure it works. You can even write your own test cases, and run locally.
        def permute(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """

        res = []
        self.dfs(nums,[], res)
        return res
    
    def dfs(self, nums, path, res):
        if not nums:
            res.append(path)

        for i in range(len(nums)):
            self.dfs(nums[:i]+nums[i+1:], path+[nums[i]], res)
            
    # 6. If you haven't addressed this in step 3 (when you were talking about approaches), think about how you would optimize the solution. Talk about big O here.

