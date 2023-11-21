
    # 1. Copy/paste the problem definition. Read it out loud and understand what they want.

        Given a 1-indexed array of integers numbers that is already sorted in non-decreasing order, find two numbers such that they add up to a specific target number. Let these two numbers be numbers[index1] and numbers[index2] where 1 <= index1 < index2 < numbers.length.

        Return the indices of the two numbers, index1 and index2, added by one as an integer array [index1, index2] of length 2.

        The tests are generated such that there is exactly one solution. You may not use the same element twice.

        Your solution must use only constant extra space.

    # 2. Look at the examples they give you for what the algorithm should do. "Solution(input) -> output". Come up with 1 or 2 examples on your own, and write them down.

        input:  [1, 3 , 4, 5]        target = 5     output: [1, 3]

        input: [-3, 7, 9, 10]        target = 6     output: [1, 3]

    # 3. Think out loud, and write down (!!) the possible high-level approaches to solving the problem. 
    #     Eg: "this two-sum problem can be brute-forced in O(n^2) time using two for-loops, or it can be solved in O(n) using a hashmap." 
    #     This doesn't have to be detailed, just a possible approach. Think about possible edge cases and how they could break the solution.

    #     Here, if you are completely blanking after 5 minutes, and can't even do a brute-force solution, then do what the OP said 
    #     - abort mission, and spend the next hour understanding the problem by looking at the solution. Once you understood the solution go to step 4.

        1. brute force solution. O(n^2)
        Iterate through the entire list to check if combinations of sums will reach the target. Preserve the idx to return the end result.

        2. 2 pointers solution. The array is in increasing order

        We can do this...
        1. init pointers at the start.
        [1, 3, 3, 4, 5]        target  = 5
        p1
            p2

        p1 + p2 = 4
        t - p2 = 2
        t - p1 = 4

        2. pointers move depending on target - p1 / target - p2

        if target - p1 > p2, move p2

        3. just put pointers on the ends and meet in the middle, there is no ambiguity when thinking of which pointer to move

        [1, 3, 3, 4, 5]        target  = 5
        p1
                     p2
    
        csum = 6

        [1, 3, 3, 4, 5]        target  = 5
        p1
                  p2
    
        csum = 5

    # 4. Pick one of the approaches, and write out the pseudo code for it, while taking out loud as to what your thought process is.

        approach 3

        make a pointer on the left and the right

        running sum towards the middle, increment and decrement accordingly

    # 5. CODE THE ACTUAL SOLUTION. If you actually followed steps 1-4, this part is going to be trivial. You will bang out the actual code often in under 5 minutes. 
    # Paste the code into leetcode (or whatever platform you are using) to ensure it works. You can even write your own test cases, and run locally.

        left, right = 0, len(numbers) - 1
        running_sum = 0
        while(left < right):

            running_sum = numbers[left] + numbers[right]

            if running_sum == target:
                return [left + 1, right  + 1]
            elif running_sum > target:
                right -= 1
            else:
                left += 1
        


    # 6. If you haven't addressed this in step 3 (when you were talking about approaches), think about how you would optimize the solution. Talk about big O here.


        I felt kinda dumb doing this problem. I way overcomplicated the issue of when to increment and decrement by trying to solve the 
        problem instantly without thinking about other approaches.

        In the future I will try to think about the solution very clearly before I solve the problem. I was a bit blind.