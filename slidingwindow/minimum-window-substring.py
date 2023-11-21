
    # 1. Copy/paste the problem definition. Read it out loud and understand what they want.

        Given two strings s and t of lengths m and n respectively, return the minimum window substring
        of s such that every character in t (including duplicates) is included in the window.
        If there is no such substring, return the empty string "".

        The testcases will be generated such that the answer is unique.

    # 2. Look at the examples they give you for what the algorithm should do. "Solution(input) -> output". Come up with 1 or 2 examples on your own, and write them down.

        input: s = "abracadabra"    t = "adar"      output = "adabr"

        input: s = "he"             t = "ok"        output = ""

    # 3. Think out loud, and write down (!!) the possible high-level approaches to solving the problem. 
    #     Eg: "this two-sum problem can be brute-forced in O(n^2) time using two for-loops, or it can be solved in O(n) using a hashmap." 
    #     This doesn't have to be detailed, just a possible approach. Think about possible edge cases and how they could break the solution.

    #     Here, if you are completely blanking after 5 minutes, and can't even do a brute-force solution, then do what the OP said 
    #     - abort mission, and spend the next hour understanding the problem by looking at the solution. Once you understood the solution go to step 4.

        1. brute force approach would be to iteratively increment string leng and record shortest for every char in s.

        very slow

        2. our window has to be at least len(t) long. 
        Thinking... expand this window until we find the substring is included

        hmmm idea: snail movement

        expand until subtring is included

        retract until substring is not included

        record min string leng and string



    # 4. Pick one of the approaches, and write out the pseudo code for it, while taking out loud as to what your thought process is.

        left = 0

        dt = {} # add all chars in t into a counter

        ds = {} # substring s

        for right in range(len(t) - 1, len(s)):

            # try to add right char in
            is always possible

            # check if all of t is included within the substring, ds
            if it is, lets first preserve length + string
            and then lets increment left
        
        return the string


    # 5. CODE THE ACTUAL SOLUTION. If you actually followed steps 1-4, this part is going to be trivial. You will bang out the actual code often in under 5 minutes. 
    # Paste the code into leetcode (or whatever platform you are using) to ensure it works. You can even write your own test cases, and run locally.

        l = 0

        minl = 0
        minw = ""

        ds = {}

        dt = {}

        for i in range(len(t)): 
            # init ds, dt
            if s[i] not in ds:
                ds[s[i]] = 1
            else:
                ds[s[i]] += 1
            
            if t[i] not in dt:
                dt[t[i]] = 1
            else:
                dt[t[i]] += 1


        for r in range(len(t) - 1, len(s)):
            # add right char to substring
            if s[r] not in ds:
                ds[s[r]] = 1
            else:
                ds[s[r]] += 1

            # check if dt is a subset of ds / if t is in the substring of ds
            issub = 1
            for val in dt:
                if not dt[val] == ds.get(ds[val], 0):
                    issub = 0
                    break
                    # if not substring, break

            if issub == 1:
                minw = 
            
        tried my best T.T
            
    # 6. If you haven't addressed this in step 3 (when you were talking about approaches), think about how you would optimize the solution. Talk about big O here.

        looking at NC solution

        The thinking is the same, the solution that he codes up is more succinct

        Use a Have / Need variable

        