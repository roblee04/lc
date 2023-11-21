
    # 1. Copy/paste the problem definition. Read it out loud and understand what they want.

        Given an array of integers nums and an integer target, return indices of the two numbers such that they add up to target.

        You may assume that each input would have exactly one solution, and you may not use the same element twice.

        You can return the answer in any order.

    # 2. Look at the examples they give you for what the algorithm should do. "Solution(input) -> output". Come up with 1 or 2 examples on your own, and write them down.

        input: nums = [ 1, 3 , 6]   target = 9      output = [1, 2]

        [8, 6, 3] --> [0, 1, 2]

        input: nums = [ 2, 1, 2 ]   target = 4      output = [0, 2]

    # 3. Think out loud, and write down (!!) the possible high-level approaches to solving the problem. 
    #     Eg: "this two-sum problem can be brute-forced in O(n^2) time using two for-loops, or it can be solved in O(n) using a hashmap." 
    #     This doesn't have to be detailed, just a possible approach. Think about possible edge cases and how they could break the solution.

        This problem can be solved by checking every combination of numbers for every element in the list. would be n^2

        Something to note is that are returning he indices.

        Another way to solve is to create a dict. the keys would be [target - element] and the value would be [index].

        So, for nums = [ 2, 1, 2 ]   target = 4,

        the dict would look like: [2] --> 0
                                  [3] --> 1
                                  [2] --> 2

        We will iterate over the list to populate the dict and also compare values to see if it works.

    #     Here, if you are completely blanking after 5 minutes, and can't even do a brute-force solution, then do what the OP said 
    #     - abort mission, and spend the next hour understanding the problem by looking at the solution. Once you understood the solution go to step 4.

    # 4. Pick one of the approaches, and write out the pseudo code for it, while taking out loud as to what your thought process is.

        #first we want to iterate
        for( every element in the list) {

            check if target - element is in dict
                if so, return both indices
            if not, add the key value pair into the dict

        }


    # 5. CODE THE ACTUAL SOLUTION. If you actually followed steps 1-4, this part is going to be trivial. You will bang out the actual code often in under 5 minutes. 
    # Paste the code into leetcode (or whatever platform you are using) to ensure it works. You can even write your own test cases, and run locally.

        dict = {}

        for i in range(len(nums)):
            if nums[i] in dict:
                return [dict[nums[i]], i]
            else:
                dict[target - nums[i]] = i

    # 6. If you haven't addressed this in step 3 (when you were talking about approaches), think about how you would optimize the solution. Talk about big O here.

        This is the most optimal solution. In the future, I will need to focus on using dictionaries in smart ways.  
        I am not sure how the intuition behind target - value comes from though.
