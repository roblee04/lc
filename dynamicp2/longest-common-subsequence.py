
    # 1. Copy/paste the problem definition. Read it out loud and understand what they want.
        Given two strings text1 and text2, return the length of their longest common subsequence. If there is no common subsequence, return 0.

        A subsequence of a string is a new string generated from the original string with some characters (can be none) deleted without changing the relative order of the remaining characters.

            For example, "ace" is a subsequence of "abcde".

        A common subsequence of two strings is a subsequence that is common to both strings.
    # 2. Look at the examples they give you for what the algorithm should do. "Solution(input) -> output". Come up with 1 or 2 examples on your own, and write them down.

    # 3. Think out loud, and write down (!!) the possible high-level approaches to solving the problem. 
    #     Eg: "this two-sum problem can be brute-forced in O(n^2) time using two for-loops, or it can be solved in O(n) using a hashmap." 
    #     This doesn't have to be detailed, just a possible approach. Think about possible edge cases and how they could break the solution.

    #     Here, if you are completely blanking after 5 minutes, and can't even do a brute-force solution, then do what the OP said 
    #     - abort mission, and spend the next hour understanding the problem by looking at the solution. Once you understood the solution go to step 4.
        1. generate all subsequences and then take the max of the overlapped subsequences
            -  can do this via counter

        2. maybe some chopping solution, short
            - given something like abcde, acet
            - core idea: we use one string as the reference string and the other as the "working" string
            the reference string will be something we refer to
            the working string we will iterate thru

            while iterating, we look at c
            if c is nevre found in the reference string, 

            problem is a string like
            "abqqqq"
            "qqqqabq", idx, pointer, leng

            maybe can work actually/ nah wrong approach

        3. NC 

    # 4. Pick one of the approaches, and write out the pseudo code for it, while taking out loud as to what your thought process is.

        m = 0

        def dfs(idx, ptr, leng):

            if idx > len(s1) - 1:
                return

            if s1[idx] in s2:
                # find s1 idx, check if its after pointer

                # check where it acutally lives

                # update the ptr

                leng += 1
                m = max(m, leng)

            dfs(idx + 1, ptr, leng)
        

            
    # 5. CODE THE ACTUAL SOLUTION. If you actually followed steps 1-4, this part is going to be trivial. You will bang out the actual code often in under 5 minutes. 
    # Paste the code into leetcode (or whatever platform you are using) to ensure it works. You can even write your own test cases, and run locally.
        m = 0

        def dfs(idx, ptr, leng):

            if idx > len(s1) - 1:
                return

            if s1[idx] in s2:
                for i in range(ptr, len(s2)):
                    if s1[idx] == s2[i]:
                        ptr = i
                        break

                if 
                # find s1 idx, check if its after pointer
                

                # check where it acutally lives

                # update the ptr

                leng += 1
                m = max(m, leng)

            dfs(idx + 1, ptr, leng)
    # 6. If you haven't addressed this in step 3 (when you were talking about approaches), think about how you would optimize the solution. Talk about big O here.

        The solution is to create a 2d grid essentially.follow NC's train of thought
        grid = [0 for i in range(len(text2)) + 1] for i in range(len(text1) + 1)

        # text 1 is y value, text 2 is x val

        def dfs(idx1, idx2):
            
            # check bounds
            if idx1 >= len(text1) or idx2 >= len(text2):
                return 0

            if grid[idx2][idx1] != 0:
                return grid[idx2][idx1]

            if text1[idx1] == text2[idx2]:
                # go diagonal
                sum = 1 + dfs(idx1 + 1, idx2 + 2)
                grid[idx2, idx1] = sum
                return sum

            
            return max(dfs(idx1 + 1, idx2), dfs(idx1, idx2 + 1))

        return dfs(0, 0)

            


