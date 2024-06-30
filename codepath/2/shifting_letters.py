# 1. Copy/paste the problem definition. Read it out loud and understand what they want.
You are given a string s of lowercase English letters and an integer array shifts of the same length.

Call the shift() of a letter, the next letter in the alphabet, (wrapping around so that 'z' becomes 'a').

    For example, shift('a') = 'b', shift('t') = 'u', and shift('z') = 'a'.

Now for each shifts[i] = x, we want to shift the first i + 1 letters of s, x times.

Return the final string after all such shifts to s are applied.
# 2. Look at the examples they give you for what the algorithm should do. "Solution(input) -> output". Come up with 1 or 2 examples on your own, and write them down.
Input: s = "abc", shifts = [3,5,9]
Output: "rpl"
Explanation: We start with "abc".
After shifting the first 1 letters of s by 3, we have "dbc".
After shifting the first 2 letters of s by 5, we have "igc".
After shifting the first 3 letters of s by 9, we have "rpl", the answer.

# 3. Think out loud, and write down (!!) the possible high-level approaches to solving the problem. 
#     Eg: "this two-sum problem can be brute-forced in O(n^2) time using two for-loops, or it can be solved in O(n) using a hashmap." 
#     This doesn't have to be detailed, just a possible approach. Think about possible edge cases and how they could break the solution.

#     Here, if you are completely blanking after 5 minutes, and can't even do a brute-force solution, then do what the OP said 
#     - abort mission, and spend the next hour understanding the problem by looking at the solution. Once you understood the solution go to step 4.

            a b c   0 0 0
shift 3     d b c   3 0 0
shift 5     i g c   8 5 0
shift 9     r p l   17 14 9

only lower case letters
range is a - z / ord(a) - ord(z)

# 4. Pick one of the approaches, and write out the pseudo code for it, while taking out loud as to what your thought process is.
letter matrix = [0, 0, 0]

for num in shifts
    for letters in mat
        increment

return matrix

# 5. CODE THE ACTUAL SOLUTION. If you actually followed steps 1-4, this part is going to be trivial. You will bang out the actual code often in under 5 minutes. 
# Paste the code into leetcode (or whatever platform you are using) to ensure it works. You can even write your own test cases, and run locally.

def shiftingLetters(self, s: str, shifts: List[int]) -> str:
    ret = ""
    sl = [0] * len(s)

    for i in range(len(shifts)):
        for j in range(i + 1):
            sl[j] += shifts[i]
    
    
    
    rangeA = 26
    

    for i in range(len(s)):
        val = ord(s[i]) + sl[i] - 97
        
        val = val % rangeA
        
        ret += chr(val + 97) 

    return ret
# 6. If you haven't addressed this in step 3 (when you were talking about approaches), think about how you would optimize the solution. Talk about big O here.
running sum solution

def shiftingLetters(self, s: str, shifts: List[int]) -> str:
    ret = ""
    shift = 0
    for i in range(len(s) - 1, -1, -1):
        shift += shifts[i]
        val = ord(s[i]) + shift - 97
        val = val % 26
        ret += chr(val + 97) 
        print(shift)

    return ret[::-1]