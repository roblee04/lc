
    # 1. Copy/paste the problem definition. Read it out loud and understand what they want.
        Given an array of integers nums containing n + 1 integers where each integer is in the range [1, n] inclusive.

        There is only one repeated number in nums, return this repeated number.

        You must solve the problem without modifying the array nums and uses only constant extra space.
    # 2. Look at the examples they give you for what the algorithm should do. "Solution(input) -> output". Come up with 1 or 2 examples on your own, and write them down.

    # 3. Think out loud, and write down (!!) the possible high-level approaches to solving the problem. 
    #     Eg: "this two-sum problem can be brute-forced in O(n^2) time using two for-loops, or it can be solved in O(n) using a hashmap." 
    #     This doesn't have to be detailed, just a possible approach. Think about possible edge cases and how they could break the solution.

    #     Here, if you are completely blanking after 5 minutes, and can't even do a brute-force solution, then do what the OP said 
    #     - abort mission, and spend the next hour understanding the problem by looking at the solution. Once you understood the solution go to step 4.
        1. this problem is displayed as some kind of array problem
            - my first approach would be a O(n^2) double for loop approach

            - a better approach would be an O(nlogn) sorting approach

        2. how to do in O(n) time without extra space?
            - To convert the problem into a linked list cycle problem
                - the values at each index can denote the next index to go to
                - because there will always be 2 values pointing to one index, there will always be a cycle
                - can use Floyds algorithm
                    - slow + fast pointer, stop when meet, preserve slow pointer as slow1
                    - slow2 = start of list, increment slow1 and slow2 til they meet, at the start of the cycle
    # 4. Pick one of the approaches, and write out the pseudo code for it, while taking out loud as to what your thought process is.

        # approach 2

        slow, fast = 0, 0

        while True:
            # this is how to increment, treat the problem as a linked list problem
            slow = nums[slow]
            fast = nums[nums[fast]] # increment 2x

            if slow == fast:
                break

        # now find the start of the cycle
        slow2 = 0
        while True:
            slow = nums[slow]
            slow2 = nums[slow2]
            if slow == slow2:
                return slow

    

    # 5. CODE THE ACTUAL SOLUTION. If you actually followed steps 1-4, this part is going to be trivial. You will bang out the actual code often in under 5 minutes. 
    # Paste the code into leetcode (or whatever platform you are using) to ensure it works. You can even write your own test cases, and run locally.

    # 6. If you haven't addressed this in step 3 (when you were talking about approaches), think about how you would optimize the solution. Talk about big O here.

