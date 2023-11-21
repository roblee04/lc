
    # 1. Copy/paste the problem definition. Read it out loud and understand what they want.
        Given strings s1, s2, and s3, find whether s3 is formed by an interleaving of s1 and s2.

        An interleaving of two strings s and t is a configuration where s and t are divided into n and m
        substrings
        respectively, such that:

            s = s1 + s2 + ... + sn
            t = t1 + t2 + ... + tm
            |n - m| <= 1
            The interleaving is s1 + t1 + s2 + t2 + s3 + t3 + ... or t1 + s1 + t2 + s2 + t3 + s3 + ...

        Note: a + b is the concatenation of strings a and b.
    # 2. Look at the examples they give you for what the algorithm should do. "Solution(input) -> output". Come up with 1 or 2 examples on your own, and write them down.

    # 3. Think out loud, and write down (!!) the possible high-level approaches to solving the problem. 
    #     Eg: "this two-sum problem can be brute-forced in O(n^2) time using two for-loops, or it can be solved in O(n) using a hashmap." 
    #     This doesn't have to be detailed, just a possible approach. Think about possible edge cases and how they could break the solution.

    #     Here, if you are completely blanking after 5 minutes, and can't even do a brute-force solution, then do what the OP said 
    #     - abort mission, and spend the next hour understanding the problem by looking at the solution. Once you understood the solution go to step 4.
        1. the first solution that comes to mind is a pointer approach, where we track each letter n the strings
        - if one matches, then we increment both

        2. this approach fails if there is an ambiguity, so we will try both letters by using recursion

    # 4. Pick one of the approaches, and write out the pseudo code for it, while taking out loud as to what your thought process is.
        memo = {}

        def dfs(idx1, idx2, idx3):
            if idx1 + idx2 == idx3:
                return True

            if s1 s2 chars are same:
                check if char is same as s3
                    dfs on both

            else:
                if s1 char == s3 char:
                    dfs incr s1
                elif s2 char == s3 char:
                    dfs incr s2
                else:
                    return false

    # 5. CODE THE ACTUAL SOLUTION. If you actually followed steps 1-4, this part is going to be trivial. You will bang out the actual code often in under 5 minutes. 
    # Paste the code into leetcode (or whatever platform you are using) to ensure it works. You can even write your own test cases, and run locally.
        memo = {}

        def dfs(idx1, idx2, idx3):
            if idx1 + idx2 == idx3:
                return True

            # check bounds

            if (idx1 < len(s1) and idx2 < len(s2)) and (s1[idx1] == s2[idx2]):

                if s1[idx1] == s3[idx3]:
                    return dfs(idx1 + 1, idx2, idx3 + 1) or dfs(idx1, idx2 + 1, idx3 + 1)

            else:
                if (idx1 < len(s1)) and (s1[idx1] == s3[idx3]):
                    return dfs(idx1 + 1, idx2, idx3 + 1)
                elif (idx2 < len(s2)) and (s2[idx2] == s3[idx3]):
                    return dfs(idx1, idx2 + 1, idx3 + 1)
                else:
                    return False

        return dfs(0, 0, 0)

        ___ cleaner code

        if len(s1) + len(s2) != len(s3):
            return False

        memo = {}

        def dfs(idx1, idx2, idx3):
            if idx1 == len(s1) and idx2 == len(s2):
                return True

            if (idx1, idx2, idx3) in memo:
                return memo[(idx1, idx2, idx3)]

            c1 = False
            c2 = False
            if (idx1 < len(s1)) and (s1[idx1] == s3[idx3]):
                c1 = dfs(idx1 + 1, idx2, idx3 + 1)
            
            if (idx2 < len(s2)) and (s2[idx2] == s3[idx3]):
                c2 = dfs(idx1, idx2 + 1, idx3 + 1)

            memo[(idx1, idx2, idx3)] = c1 or c2

            return memo[(idx1, idx2, idx3)]

        
        return dfs(0, 0, 0)

    # 6. If you haven't addressed this in step 3 (when you were talking about approaches), think about how you would optimize the solution. Talk about big O here.

