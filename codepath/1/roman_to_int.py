# 1. Copy/paste the problem definition. Read it out loud and understand what they want.
Roman numerals are represented by seven different symbols: I, V, X, L, C, D and M.

Symbol       Value
I             1
V             5
X             10
L             50
C             100
D             500
M             1000

Given a roman numeral, convert it to an integer.

# 2. Look at the examples they give you for what the algorithm should do. "Solution(input) -> output". Come up with 1 or 2 examples on your own, and write them down.

Input: s = "MCMXCIV"
Output: 1994
Explanation: M = 1000, CM = 900, XC = 90 and IV = 4.

# 3. Think out loud, and write down (!!) the possible high-level approaches to solving the problem. 
#     Eg: "this two-sum problem can be brute-forced in O(n^2) time using two for-loops, or it can be solved in O(n) using a hashmap." 
#     This doesn't have to be detailed, just a possible approach. Think about possible edge cases and how they could break the solution.

#     Here, if you are completely blanking after 5 minutes, and can't even do a brute-force solution, then do what the OP said 
#     - abort mission, and spend the next hour understanding the problem by looking at the solution. Once you understood the solution go to step 4.
sum of numbers and correspondingly add sign or no sign

e.g. MCMXCIV

1000 + 100 + 1000 + 10 + 100 + 1 + 5

flip all the signs for values less than next neighbor

1000 - 100 + 1000 - 10 + 100 - 1 + 5

1000 + 900 + 90 + 4

e.g. XXVII

10 + 10 + 5 + 1 + 1

27
# 4. Pick one of the approaches, and write out the pseudo code for it, while taking out loud as to what your thought process is.

def rtoi(s):

    for c in s:
        convert each char to its corresponding int value

        store in array
    
    for val in array:
        check if val is < valnext

        if so, flip value

    sum up all values
# 5. CODE THE ACTUAL SOLUTION. If you actually followed steps 1-4, this part is going to be trivial. You will bang out the actual code often in under 5 minutes. 
# Paste the code into leetcode (or whatever platform you are using) to ensure it works. You can even write your own test cases, and run locally.

def romanToInt(self, s: str) -> int:

        d = {"I":1, "V":5,"X":10,"L":50,"C":100,"D":500,"M":1000}

        nums = []

        for c in s:
            nums.append(d[c])
        
        for i in range(len(nums) - 1):

            if nums[i] < nums[i + 1]:
                nums[i] = -nums[i]
            
        return sum(nums)

# 6. If you haven't addressed this in step 3 (when you were talking about approaches), think about how you would optimize the solution. Talk about big O here.
