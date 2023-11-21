
    # 1. Copy/paste the problem definition. Read it out loud and understand what they want.
        Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sum to target.

        Each number in candidates may only be used once in the combination.

        Note: The solution set must not contain duplicate combinations.
    # 2. Look at the examples they give you for what the algorithm should do. "Solution(input) -> output". Come up with 1 or 2 examples on your own, and write them down.

        input
    # 3. Think out loud, and write down (!!) the possible high-level approaches to solving the problem. 
    #     Eg: "this two-sum problem can be brute-forced in O(n^2) time using two for-loops, or it can be solved in O(n) using a hashmap." 
    #     This doesn't have to be detailed, just a possible approach. Think about possible edge cases and how they could break the solution.

    #     Here, if you are completely blanking after 5 minutes, and can't even do a brute-force solution, then do what the OP said 
    #     - abort mission, and spend the next hour understanding the problem by looking at the solution. Once you understood the solution go to step 4.

        1. use a set

        2. dictionary to track freq, 

        3. use a similar mindset to subset sum 2, only one branch can have that duplicate number
    # 4. Pick one of the approaches, and write out the pseudo code for it, while taking out loud as to what your thought process is.

        andidates.sort()
        res = []

        def dfs(idx, lst):

            if sum(lst) > target:
                return
            
            if sum(lst) == target:
                res.append(lst)
                return
            
            for i in range(idx, len(candidates)):
                if i > idx and candidates[i] == candidates[i-1]:
                    continue
                dfs(i + 1, lst + [candidates[i]])
                
        
        dfs(0, [])

        return res
    # 5. CODE THE ACTUAL SOLUTION. If you actually followed steps 1-4, this part is going to be trivial. You will bang out the actual code often in under 5 minutes. 
    # Paste the code into leetcode (or whatever platform you are using) to ensure it works. You can even write your own test cases, and run locally.

    # 6. If you haven't addressed this in step 3 (when you were talking about approaches), think about how you would optimize the solution. Talk about big O here.

