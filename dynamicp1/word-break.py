
    # 1. Copy/paste the problem definition. Read it out loud and understand what they want.
        Given a string s and a dictionary of strings wordDict, return true if s can be segmented into a space-separated sequence of one or more dictionary words.

        Note that the same word in the dictionary may be reused multiple times in the segmentation.
    # 2. Look at the examples they give you for what the algorithm should do. "Solution(input) -> output". Come up with 1 or 2 examples on your own, and write them down.

        input: s = "bobburger" dict = ["bob", "burger"]     output: true

        input: s = "abab"       dict = ["ab"]               output: true

        input: s = "labomba"

    # 3. Think out loud, and write down (!!) the possible high-level approaches to solving the problem. 
    #     Eg: "this two-sum problem can be brute-forced in O(n^2) time using two for-loops, or it can be solved in O(n) using a hashmap." 
    #     This doesn't have to be detailed, just a possible approach. Think about possible edge cases and how they could break the solution.

    #     Here, if you are completely blanking after 5 minutes, and can't even do a brute-force solution, then do what the OP said 
    #     - abort mission, and spend the next hour understanding the problem by looking at the solution. Once you understood the solution go to step 4.

        1. A brute force solution would be to test every single combination of words created from the dictionary

        if any match the input string, you win

        2. create s from ground up using words in dictionary. instead of brute force, do sm with dp

        IVE GOT it

        so we try to make word s one char at a time, to populate a dp array.
        This dp array will tell us true or false as to if it is possible

        return dp[len(s)]

        problem is, how will this dp array help us?

        3. my dfs approach
    # 4. Pick one of the approaches, and write out the pseudo code for it, while taking out loud as to what your thought process is.
        dp = [-1] * (len(s) + 1)

        def dfs(substring):

            if no word in the dict can fit in the substring, false

            check if it is alr in dp, if so return that val

            else, recurse on all other valid words

        return  substr


    # 5. CODE THE ACTUAL SOLUTION. If you actually followed steps 1-4, this part is going to be trivial. You will bang out the actual code often in under 5 minutes. 
    # Paste the code into leetcode (or whatever platform you are using) to ensure it works. You can even write your own test cases, and run locally.

        dp = [-1] * (len(s) + 1)

        def dfs(idx):
            remLen = len(s) - 1 - idx 

            if dp[idx] != -1:  # 0 is false, 1 is true
                return dp[idx]
            
            c = 0
            for word in wordDict:   # or none of the words will fit
                if len(word) > remLen:
                    c += 1
                if word != s[idx, idx + len(word)]:
                    c += 1
            if c > 0:
                return 0

            for word in wordDict:
                dp[idx] = dfs(idx + len(word) - 1)

            return 1

    # 6. If you haven't addressed this in step 3 (when you were talking about approaches), think about how you would optimize the solution. Talk about big O here.

        dp = [False] * (len(s) + 1)
        dp[len(s)] = True

        for i in range(len(s) -1, -1, -1):

            for word in wordDict:
                if (i + len(word)) <= len(s) and word == s[i: i + len(word)]:
                    dp[i] = dp[i + len(word)]
                if dp[i]:
                    break
        
        return dp[0]
