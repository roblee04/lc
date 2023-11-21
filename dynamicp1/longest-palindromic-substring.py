
    # 1. Copy/paste the problem definition. Read it out loud and understand what they want.
        Given a string s, return the longest
        palindromic
        substring
        in s.
    # 2. Look at the examples they give you for what the algorithm should do. "Solution(input) -> output". Come up with 1 or 2 examples on your own, and write them down.

    # 3. Think out loud, and write down (!!) the possible high-level approaches to solving the problem. 
    #     Eg: "this two-sum problem can be brute-forced in O(n^2) time using two for-loops, or it can be solved in O(n) using a hashmap." 
    #     This doesn't have to be detailed, just a possible approach. Think about possible edge cases and how they could break the solution.

    #     Here, if you are completely blanking after 5 minutes, and can't even do a brute-force solution, then do what the OP said 
    #     - abort mission, and spend the next hour understanding the problem by looking at the solution. Once you understood the solution go to step 4.
        1. brute force approach would be to compare the given string with a reversed version of itself
        - try to find the same substring in both

        2. nah brute force would be trying to create every substring and trying to find if it is a palindrome

        3. best solution is to find a palindrome via the inside out method
            Use 2 pointers to do this,
            iterate a loop on this 

    # 4. Pick one of the approaches, and write out the pseudo code for it, while taking out loud as to what your thought process is.

    # 5. CODE THE ACTUAL SOLUTION. If you actually followed steps 1-4, this part is going to be trivial. You will bang out the actual code often in under 5 minutes. 
    # Paste the code into leetcode (or whatever platform you are using) to ensure it works. You can even write your own test cases, and run locally.
        res = ""
        maxl = 0

        for i in range(len(s)):

            #odds
            r, l = i, i

            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > maxl:
                    res = s[l:r + 1]
                    maxl = r - l + 1
                
                l += 1
                r -= 1
            
            # evens
            r, l = i + 1, i

            while l >= 0 and r < len(s) and s[l] == s[r]:
                if (r - l + 1) > maxl:
                    res = s[l: r + 1]
                    maxl = r - 1 + 1
                
                l += 1
                r -= 1
            
        return res

    # 6. If you haven't addressed this in step 3 (when you were talking about approaches), think about how you would optimize the solution. Talk about big O here.

