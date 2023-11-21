
    # 1. Copy/paste the problem definition. Read it out loud and understand what they want.

        Design an algorithm to encode a list of strings to a string. 
        The encoded string is then sent over the network and is decoded back to the original list of strings.

        Please implement encode and decode

    # 2. Look at the examples they give you for what the algorithm should do. "Solution(input) -> output". Come up with 1 or 2 examples on your own, and write them down.

        I am a bit confused at the problem statement. will watch intro video for clarification

        input: ["neet", "code"] --> some encoding --> decode --> ["neet", "code"]

                            possible encoding could be: neet%code%


    # 3. Think out loud, and write down (!!) the possible high-level approaches to solving the problem. 
    #     Eg: "this two-sum problem can be brute-forced in O(n^2) time using two for-loops, or it can be solved in O(n) using a hashmap." 
    #     This doesn't have to be detailed, just a possible approach. Think about possible edge cases and how they could break the solution.

    #     Here, if you are completely blanking after 5 minutes, and can't even do a brute-force solution, then do what the OP said 
    #     - abort mission, and spend the next hour understanding the problem by looking at the solution. Once you understood the solution go to step 4.

        The key solution is to count the number of characters for each word. 

        So for our example above, it could be encoded as "neet4code4", this can easily be decoded 

        a problem occurs if you try to add a numeric char to the list so like ["neet", "4", "code"]

        which would be encoded as "neet45code4"

        you can easily solve this by adding another delimiter like "!"

        so the end result would be "neet4!5code!4"

        in the case of ["neet", "!4", "code"] --> "neet!4!6code!4", you can peek for "!" delimiter after the 4

        Actually, it should be the reverse, where !4 is in front!!!

    # 4. Pick one of the approaches, and write out the pseudo code for it, while taking out loud as to what your thought process is.

        def encode(strs):

            s = ""

            for every string in strs:
                add the string to s
                add delimiter to s
                add str len to s
            
            return s
        
        def decode(s):

            count = 0
            iterate over the string
                count every char

                if i see a "!" delimiter, pause
                    check if next val is num

    # 5. CODE THE ACTUAL SOLUTION. If you actually followed steps 1-4, this part is going to be trivial. You will bang out the actual code often in under 5 minutes. 
    # Paste the code into leetcode (or whatever platform you are using) to ensure it works. You can even write your own test cases, and run locally.

        def encode(self, strs):

            s = ""

            for st in strs:
                s += str(len(st))
                s += !
                s += st
        
            return s

        def decode(self, str):

            r = []
            ptr = 0
            
            while ptr < len(str):

                j = i

                while(str[j] != "!"):
                    j += 1
                
                leng = int(str[i:j])
                r.append(str[j + 1: j + 1 + leng])
            
                i = j + 1 + leng

            


    # 6. If you haven't addressed this in step 3 (when you were talking about approaches), think about how you would optimize the solution. Talk about big O here.

        This problem was pretty tough. Finding patterns in strings and knowing to put it in front...
        Another complication was the string extraction in decode method. I will review python string manipulation techniques