
    # 1. Copy/paste the problem definition. Read it out loud and understand what they want.
        A message containing letters from A-Z can be encoded into numbers using the following mapping:

        'A' -> "1"
        'B' -> "2"
        ...
        'Z' -> "26"

        To decode an encoded message, all the digits must be grouped then mapped back into letters using the reverse of the mapping above (there may be multiple ways). For example, "11106" can be mapped into:

            "AAJF" with the grouping (1 1 10 6)
            "KJF" with the grouping (11 10 6)

        Note that the grouping (1 11 06) is invalid because "06" cannot be mapped into 'F' since "6" is different from "06".

        Given a string s containing only digits, return the number of ways to decode it.

        The test cases are generated so that the answer fits in a 32-bit integer.
    # 2. Look at the examples they give you for what the algorithm should do. "Solution(input) -> output". Come up with 1 or 2 examples on your own, and write them down.

    # 3. Think out loud, and write down (!!) the possible high-level approaches to solving the problem. 
    #     Eg: "this two-sum problem can be brute-forced in O(n^2) time using two for-loops, or it can be solved in O(n) using a hashmap." 
    #     This doesn't have to be detailed, just a possible approach. Think about possible edge cases and how they could break the solution.

    #     Here, if you are completely blanking after 5 minutes, and can't even do a brute-force solution, then do what the OP said 
    #     - abort mission, and spend the next hour understanding the problem by looking at the solution. Once you understood the solution go to step 4.

        the only thing we should note is the 0, 0 will always follow a number, never starting one

        1. The brute force approach would be to create every combination of string and then decode every one of them
            - remove invalid approaches

        2. dfs approach dfs(string) always pass in a string segment

        what does dfs do?
        - choose 1 or 2 to iterate on
        - if we choose 1, the next digit cannot be 0
        - if we choose 2, the next next digit cannot be 0

        to prevent duplicat matching, maybe add a seen

        
        return 1 + both

    # 4. Pick one of the approaches, and write out the pseudo code for it, while taking out loud as to what your thought process is.
        seen = {} # dont do over duplicate segments

        def dfs(segment):
            print(segment, seen)
            if not segment:
                return 0
            if segment[0] == "0":
                return 0
            elif len(segment) == 1:
                return 1
            elif len(segment) == 2 and segment[1] == "0" or (len(segment) == 2 and int(segment) > 26):
                return 1
            elif len(segment) == 2 and segment[1] != "0":
                return 2
            

            # prevent 0 decodings
            if segment in seen:
                return 0

            if segment[1] != "0" and segment[2] != "0":
                sum = dfs(segment[1:]) + dfs(segment[2:])
            elif segment[1] != "0":
                sum = dfs(segment[1:])
            else:
                sum = dfs(segment[2:])

            seen[segment] = sum

            return sum

        return dfs(s)

        about half test cases passed

        lets look at NC solution
        
    # 5. CODE THE ACTUAL SOLUTION. If you actually followed steps 1-4, this part is going to be trivial. You will bang out the actual code often in under 5 minutes. 
    # Paste the code into leetcode (or whatever platform you are using) to ensure it works. You can even write your own test cases, and run locally.

    # 6. If you haven't addressed this in step 3 (when you were talking about approaches), think about how you would optimize the solution. Talk about big O here.

        The idea should be more formalized, but high level idea is te same

        c = {len(s): 1} # edge case

        def dfs(i):
            if i in c:
                return c[i]
            if s[i] == "0": # basically dealing with 0
                return 0

            res = dfs(i + 1)

            if (i + 1) < len(s) and (s[i] == "1" or (s[i] == "2" and int(s[i+1]) < 7)):
                res += dfs(i + 2)
            
            c[i] = res
            return res

        return dfs(0)
            