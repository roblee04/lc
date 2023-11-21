
    # 1. Copy/paste the problem definition. Read it out loud and understand what they want.

    Given an integer array nums, return an array answer such that answer[i] is equal to the product of all the elements of nums except nums[i].

    The product of any prefix or suffix of nums is guaranteed to fit in a 32-bit integer.

    You must write an algorithm that runs in O(n) time and without using the division operation.

    # 2. Look at the examples they give you for what the algorithm should do. "Solution(input) -> output". Come up with 1 or 2 examples on your own, and write them down.

    input: nums = [1, 5, 2, 7]      output: [70, 14, 35, 10]
    
    input: nums = [-2, 3, 0]        output: [0, 0, -6]

    # 3. Think out loud, and write down (!!) the possible high-level approaches to solving the problem. 
    #     Eg: "this two-sum problem can be brute-forced in O(n^2) time using two for-loops, or it can be solved in O(n) using a hashmap." 
    #     This doesn't have to be detailed, just a possible approach. Think about possible edge cases and how they could break the solution.

    #     Here, if you are completely blanking after 5 minutes, and can't even do a brute-force solution, then do what the OP said 
    #     - abort mission, and spend the next hour understanding the problem by looking at the solution. Once you understood the solution go to step 4.

    1. brute force approach (no division) O(n^2)
        iterate over the entire list, and calculate the product between the previous and next intervals
        most likely using a for loop with 2 nested for loops to calculate product

    2. running sum approach O(n^2) 
        As we iterate through the list, keep a running product of nums up until the given idx
        This running product will preserve the state of the previous product intervals

        As for products that are being calculated, they can be updated by just multiplying the next index value

        finished when we reach the end of the array

    3. running product in both directions and multiply 
        do solution 2, but iterate in forward and backwards direction, preserve the list



    # 4. Pick one of the approaches, and write out the pseudo code for it, while taking out loud as to what your thought process is.

        running_product = 1

        ret = []* len(nums)

        for n in nums:

            fill in our array idx for that n

            update the running product

            multiply all of the products in the array by the number


    # 5. CODE THE ACTUAL SOLUTION. If you actually followed steps 1-4, this part is going to be trivial. You will bang out the actual code often in under 5 minutes. 
    # Paste the code into leetcode (or whatever platform you are using) to ensure it works. You can even write your own test cases, and run locally.

        run = 1
        ret = [0] * len(nums)
        
        for i in range(len(nums)):
            ret[i] = run

            for j in range(i):
                ret[j] *= nums[i]
            print(ret)
            run *= nums[i]


        return ret

    # 6. If you haven't addressed this in step 3 (when you were talking about approaches), think about how you would optimize the solution. Talk about big O here.

        run1 = 1
        run2 = 1
        list1 = [1] * len(nums)
        list2 = [1] * len(nums)

        for i in range(len(nums)):
            list1[i] = run1
            run1 *= nums[i]

        for i in range(len(nums) - 1, -1, -1):
            list2[i] = run2
            run2 *= nums[i]

        
        for i in range(len(list1)):
            list1[i] *= list2[i]
        
        return list1

        