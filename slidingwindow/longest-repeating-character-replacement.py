    # 1. Copy/paste the problem definition. Read it out loud and understand what they want.
        You are given a string s and an integer k. 
        You can choose any character of the string and change it to any other uppercase English character.
         You can perform this operation at most k times.

    Return the length of the longest substring containing the same letter you can get after performing the above operations.

    # 2. Look at the examples they give you for what the algorithm should do. "Solution(input) -> output". Come up with 1 or 2 examples on your own, and write them down.

        input: "aabaa" k = 1    output: 5

        input: "aabbcc" k = 1   output: 3


    # 3. Think out loud, and write down (!!) the possible high-level approaches to solving the problem. 
    #     Eg: "this two-sum problem can be brute-forced in O(n^2) time using two for-loops, or it can be solved in O(n) using a hashmap." 
    #     This doesn't have to be detailed, just a possible approach. Think about possible edge cases and how they could break the solution.

    #     Here, if you are completely blanking after 5 minutes, and can't even do a brute-force solution, then do what the OP said 
    #     - abort mission, and spend the next hour understanding the problem by looking at the solution. Once you understood the solution go to step 4.

        1. Using 2 pointers. one ptr to keep track of beginning

            make a dictionary that'll hold values

            one "primary value?" how to find this?
                - maybe primary value is the left ptr, edge case "ABBB" k = 1
                - find primary value by taking max of the dic O(26)

        

    # 4. Pick one of the approaches, and write out the pseudo code for it, while taking out loud as to what your thought process is.

        left = 0

        d = {} # store the counts

        #condition is k >= len(s) - max(d) , if condition ever not true, remove vals until it is

        for right in range(len(s)):

            d[r] += 1

            find max in d, 
            check condition
                if not true, increment left and remove values from dictionary
            
            update maxl




        
    # 5. CODE THE ACTUAL SOLUTION. If you actually followed steps 1-4, this part is going to be trivial. You will bang out the actual code often in under 5 minutes. 
    # Paste the code into leetcode (or whatever platform you are using) to ensure it works. You can even write your own test cases, and run locally.

        l = 0
        maxl = 0
        d = {}

        for r in range(len(s)):

            maxf = 0
            for n in d: # 26
                maxf = max(maxf, n)
            
            if k < (l - r + 1 - maxf):
                while(k < (len(s) - maxf)):
                    d[s[l]] -= 1
                    l += 1
            
            # condition cleared

            if s[r] not in d:
                d[s[r]] = 1
            else:
                d[s[r]] += 1

            leng = r - l + 1

            maxl = max(maxl, leng)

        return maxl
    # 6. If you haven't addressed this in step 3 (when you were talking about approaches), think about how you would optimize the solution. Talk about big O here.


        count = {}
        res = 0
        l = 0

        for r in range(len(s)):
            count[s[r]] = 1 + count.get(s[r], 0)

            while (r - l + 1) - max(count.values()) > k:
                count[s[l]] -= 1
                l += 1
            
            res = max(res, r - l + 1)
        
        return res