
    # 1. Copy/paste the problem definition. Read it out loud and understand what they want.
        Given an array of strings strs, group the anagrams together. You can return the answer in any order.

        An Anagram is a word or phrase formed by rearranging the letters of a different word or phrase, 
        typically using all the original letters exactly once.
    # 2. Look at the examples they give you for what the algorithm should do. "Solution(input) -> output". Come up with 1 or 2 examples on your own, and write them down.

        input: strs = ["bob", "obb", "bbo", "cob", "job"]       output = [["bob", "obb", "bbo"], ["cob"], ["job"]]

        input: strs = ["j"]     output = [["j"]]
    # 3. Think out loud, and write down (!!) the possible high-level approaches to solving the problem. 
    #     Eg: "this two-sum problem can be brute-forced in O(n^2) time using two for-loops, or it can be solved in O(n) using a hashmap." 
    #     This doesn't have to be detailed, just a possible approach. Think about possible edge cases and how they could break the solution.

    #     Here, if you are completely blanking after 5 minutes, and can't even do a brute-force solution, then do what the OP said 
    #     - abort mission, and spend the next hour understanding the problem by looking at the solution. Once you understood the solution go to step 4.

        1. brute force approach: iterate over every string. Everytime we iterate, check if the given string is already in the anagrams-list.
        if not, make a list for every unique anagram. This approach would be O(n^2).

        2. using dictionaries. where key-value = [tuple(letter freq list), list of words]

        another way to make this simpler would be creating an array of size 26 to track frequency of letters and using that as the key.



    # 4. Pick one of the approaches, and write out the pseudo code for it, while taking out loud as to what your thought process is.

        Using approach 2.

        list of strs dict
        
        for string in strings:

            make a list and track letter frequency

            chekc if it is in list of strs dict
                if it is, append
            if it is not, create a new entry

        return list of strs dict

    # 5. CODE THE ACTUAL SOLUTION. If you actually followed steps 1-4, this part is going to be trivial. You will bang out the actual code often in under 5 minutes. 
    # Paste the code into leetcode (or whatever platform you are using) to ensure it works. You can even write your own test cases, and run locally.

    stringsdict = {}

    ret = []

    for s in strs:

        letterfreq = [0] * 26

        for letter in s:
            letterfreq[ord(letter) - 97] += 1
        
        freq = tuple(letterfreq)

        if freq in stringsdict:
            stringsdict[freq].append(s)
        else:
            stringsdict[freq] = [s]
    
    for s in stringsdict:
        ret.append(stringsdict[s])
    
    return ret

    # 6. If you haven't addressed this in step 3 (when you were talking about approaches), think about how you would optimize the solution. Talk about big O here.

    This is the optimized approach. I am glad that I have many ways to find anagram (dictionary + letter freq list). 

