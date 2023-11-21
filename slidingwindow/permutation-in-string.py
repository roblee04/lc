
    # 1. Copy/paste the problem definition. Read it out loud and understand what they want.

        Given two strings s1 and s2, return true if s2 contains a permutation of s1, or false otherwise.

        In other words, return true if one of s1's permutations is the substring of s2.

    # 2. Look at the examples they give you for what the algorithm should do. "Solution(input) -> output". Come up with 1 or 2 examples on your own, and write them down.

        input:   s1 = "abc"     s2 = "abnfcbajg"    output: "true"

        input:   s1 = "pop"     s2 = "cornppo"      output: "true"

    # 3. Think out loud, and write down (!!) the possible high-level approaches to solving the problem. 
    #     Eg: "this two-sum problem can be brute-forced in O(n^2) time using two for-loops, or it can be solved in O(n) using a hashmap." 
    #     This doesn't have to be detailed, just a possible approach. Think about possible edge cases and how they could break the solution.

    #     Here, if you are completely blanking after 5 minutes, and can't even do a brute-force solution, then do what the OP said 
    #     - abort mission, and spend the next hour understanding the problem by looking at the solution. Once you understood the solution go to step 4.

        1. brute force method, iterate over every char in s2, iterate to see if it matches a char 
        (no dupes) in s1

        2. method 2,
        sliding window and two dictionaries, fill d1 to be counter for s1

        for each char in s2, check if it is a val in the set, fill a dictionary and check if equal

    # 4. Pick one of the approaches, and write out the pseudo code for it, while taking out loud as to what your thought process is.

        counter for s1

        abc = set()

        iterate over s2, if we find a char in abc, make a dic and compare

    # 5. CODE THE ACTUAL SOLUTION. If you actually followed steps 1-4, this part is going to be trivial. You will bang out the actual code often in under 5 minutes. 
    # Paste the code into leetcode (or whatever platform you are using) to ensure it works. You can even write your own test cases, and run locally.
        d1= {}

        s1_words = set(s1)

        for c in s1:
            if c not in d1:
                d1[c] = 1
            else:
                d1[c] += 1
            
        
        for i in range(len(s2) - len(s1) + 1):

            if s2[i] not in d1:
                continue
            else:
                d2 = {}
                for j in range(len(s1)):
                    
                    idx = i + j
                    if s2[idx] not in d2:
                        d2[s2[idx]] = 1
                    else:
                        d2[s2[idx]] += 1
                    
                if d1 == d2:
                    return True
        
        return False
                    


    # 6. If you haven't addressed this in step 3 (when you were talking about approaches), think about how you would optimize the solution. Talk about big O here.

    leetcode solution, 26
