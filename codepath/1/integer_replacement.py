# 1. Copy/paste the problem definition. Read it out loud and understand what they want.
Given a positive integer n, you can apply one of the following operations:

    If n is even, replace n with n / 2.
    If n is odd, replace n with either n + 1 or n - 1.

Return the minimum number of operations needed for n to become 1.

# 2. Look at the examples they give you for what the algorithm should do. "Solution(input) -> output". Come up with 1 or 2 examples on your own, and write them down.

# 3. Think out loud, and write down (!!) the possible high-level approaches to solving the problem. 
#     Eg: "this two-sum problem can be brute-forced in O(n^2) time using two for-loops, or it can be solved in O(n) using a hashmap." 
#     This doesn't have to be detailed, just a possible approach. Think about possible edge cases and how they could break the solution.

#     Here, if you are completely blanking after 5 minutes, and can't even do a brute-force solution, then do what the OP said 
#     - abort mission, and spend the next hour understanding the problem by looking at the solution. Once you understood the solution go to step 4.

brute force via recursion. previous solution can be memoized.
O(n) < x < O(logn)
O(logn) ? time complexity

# 4. Pick one of the approaches, and write out the pseudo code for it, while taking out loud as to what your thought process is.

def replace(n):

    check if n is odd or even, then do corresponding operations

    we want to return the number of steps

    do another function call until we reach 1

# 5. CODE THE ACTUAL SOLUTION. If you actually followed steps 1-4, this part is going to be trivial. You will bang out the actual code often in under 5 minutes. 
# Paste the code into leetcode (or whatever platform you are using) to ensure it works. You can even write your own test cases, and run locally.

def replace(n):
    
    if n == 1:
        return 0
    
    if n % 2 == 0:
        return replace(n / 2) + 1
    
    else:
        return min(replace(n + 1), replace(n - 1)) + 1

# 6. If you haven't addressed this in step 3 (when you were talking about approaches), think about how you would optimize the solution. Talk about big O here.

With memoization

def integerReplacement(self, n: int) -> int:
    memo = {}
    return self.helper(n, memo)
    
    
def helper(self, n, memo):
    if n in memo:
        return memo[n]
    if n == 1:
        return 0
    
    num = 0
    if n % 2 == 0:
        num = self.integerReplacement(n / 2) + 1
    
    else:
        num = min(self.integerReplacement(n + 1), self.integerReplacement(n - 1)) + 1

    memo[n] = num
    return num
