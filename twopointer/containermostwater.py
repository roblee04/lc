
    # 1. Copy/paste the problem definition. Read it out loud and understand what they want.

        You are given an integer array height of length n. 
        There are n vertical lines drawn such that the two endpoints of the ith line are (i, 0) and (i, height[i]).

        Find two lines that together with the x-axis form a container, such that the container contains the most water.

        Return the maximum amount of water a container can store.

        Notice that you may not slant the container.

    # 2. Look at the examples they give you for what the algorithm should do. "Solution(input) -> output". Come up with 1 or 2 examples on your own, and write them down.

        look at the problem

    # 3. Think out loud, and write down (!!) the possible high-level approaches to solving the problem. 
    #     Eg: "this two-sum problem can be brute-forced in O(n^2) time using two for-loops, or it can be solved in O(n) using a hashmap." 
    #     This doesn't have to be detailed, just a possible approach. Think about possible edge cases and how they could break the solution.

    #     Here, if you are completely blanking after 5 minutes, and can't even do a brute-force solution, then do what the OP said 
    #     - abort mission, and spend the next hour understanding the problem by looking at the solution. Once you understood the solution go to step 4.

        1. brute force solution, going to be double for loop basically
            n^2 / 2 runtime

            2 for loops, one nested within the other, calculate leng and also min(left, right)

            have a running max for area, preserve the max area

        2. thinking maybe something with 2 pointers and a greedy solution?

            The thinking was on the right mindset, but we should have shifted the one that was min, not the next

        3. correct solution is a 2 ptr and shift the min


            
    # 4. Pick one of the approaches, and write out the pseudo code for it, while taking out loud as to what your thought process is.

        init left and right ptr 

        while left < right:

            compute area, update max

            if left < right, update left

            else update right


    # 5. CODE THE ACTUAL SOLUTION. If you actually followed steps 1-4, this part is going to be trivial. You will bang out the actual code often in under 5 minutes. 
    # Paste the code into leetcode (or whatever platform you are using) to ensure it works. You can even write your own test cases, and run locally.

        a = 0
        l, r = 0, len(height) - 1

        while l < r:
            area = (r - l) * min(height[l], height[r])
            a = max(a, area)

            if height[l] < height[r]:
                l += 1
            else:
                r -= 1
        
        return a

    # 6. If you haven't addressed this in step 3 (when you were talking about approaches), think about how you would optimize the solution. Talk about big O here.

        i think i overthought about this again, i should have been a bit more careful in approaching this problem

        try solving it on paper >?

        even if i cannot find a solution, attempting it on paper will give me one
        