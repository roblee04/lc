
    # 1. Copy/paste the problem definition. Read it out loud and understand what they want.


        Given a string s, find the length of the longest substring without repeating characters.

    # 2. Look at the examples they give you for what the algorithm should do. "Solution(input) -> output". Come up with 1 or 2 examples on your own, and write them down.

        input: "aaa"        output: 1

        input " abcdddcd"   output: 4


    # 3. Think out loud, and write down (!!) the possible high-level approaches to solving the problem. 
    #     Eg: "this two-sum problem can be brute-forced in O(n^2) time using two for-loops, or it can be solved in O(n) using a hashmap." 
    #     This doesn't have to be detailed, just a possible approach. Think about possible edge cases and how they could break the solution.

    #     Here, if you are completely blanking after 5 minutes, and can't even do a brute-force solution, then do what the OP said 
    #     - abort mission, and spend the next hour understanding the problem by looking at the solution. Once you understood the solution go to step 4.

        1. The easiest way to solve this problem is to have a set to record each duplicate. 
        Then iterate through the entire string, preserving the largest length. 
        we will use a 2 pointer approach 

    # 4. Pick one of the approaches, and write out the pseudo code for it, while taking out loud as to what your thought process is.

        for char in string:

            left = 0
            right = 0
            # 2 ptrs
            if we add the right char, and it is in the set,
                while loop to increment the left pointer
            
            we add the right char successfully!
            calculate leng and max

        return max

    # 5. CODE THE ACTUAL SOLUTION. If you actually followed steps 1-4, this part is going to be trivial. You will bang out the actual code often in under 5 minutes. 
    # Paste the code into leetcode (or whatever platform you are using) to ensure it works. You can even write your own test cases, and run locally.

        l = 0
        maxl = 0
        cset = set()

        for r in range(len(s)):
            # try to add r into the set
            if s[r] in cset:
                while s[r] in cset:
                    cset.remove(s[l])
                    l += 1
            
            # lets try to add r into set
            cset.add(s[r])
            leng = r - l + 1
            maxl = max(maxl, leng)

        
        return maxl
            



    # 6. If you haven't addressed this in step 3 (when you were talking about approaches), think about how you would optimize the solution. Talk about big O here.

        good job robin