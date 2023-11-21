
    # 1. Copy/paste the problem definition. Read it out loud and understand what they want.

        Given an integer array nums, return all the triplets 
        [nums[i], nums[j], nums[k]] such that i != j, i != k, and j != k, 
        and nums[i] + nums[j] + nums[k] == 0.

        Notice that the solution set must not contain duplicate triplets.

    # 2. Look at the examples they give you for what the algorithm should do. "Solution(input) -> output". Come up with 1 or 2 examples on your own, and write them down.

        input: nums = [1 , 2, -1, 4, -6]        output: [[1, 2, -1], [2, 4, -6]]

        input: nums = [0, 1, 2, 3]              output: []

    # 3. Think out loud, and write down (!!) the possible high-level approaches to solving the problem. 
    #     Eg: "this two-sum problem can be brute-forced in O(n^2) time using two for-loops, or it can be solved in O(n) using a hashmap." 
    #     This doesn't have to be detailed, just a possible approach. Think about possible edge cases and how they could break the solution.

    #     Here, if you are completely blanking after 5 minutes, and can't even do a brute-force solution, then do what the OP said 
    #     - abort mission, and spend the next hour understanding the problem by looking at the solution. Once you understood the solution go to step 4.

        1. the approach is to combine both the solution of 2sum and 2sum2

        first we want to order the list, to make it easier to manipulate

        then we want to put pointers on both ends of the list and find the sum and put that sum in a dictionary

        if the negative verison of that sum is ever equal to a value we are looking at, then that means we found a 3 sum

        iterate thru the entire list

    # 4. Pick one of the approaches, and write out the pseudo code for it, while taking out loud as to what your thought process is.

        left, right = 0, len(nums)

        mydict = {}

        while left < right:
            sum = add left and right

            check if the the negative version is in dict, if so, we found a 3sum

            add that 2ple into the dictionary

            move pointers

        return :)

    # 5. CODE THE ACTUAL SOLUTION. If you actually followed steps 1-4, this part is going to be trivial. You will bang out the actual code often in under 5 minutes. 
    # Paste the code into leetcode (or whatever platform you are using) to ensure it works. You can even write your own test cases, and run locally.

        nums.sort()
        left, right = 0, len(nums) - 1
        two_sum = {}

        res = []

        c = -1

        while left < right:
            sum = nums[left] + nums[right]
            val = 0

            if c == 1:
                val = nums[right]
            elif c == 0:
                val = nums[left]
            
            if -val in two_sum:
                res.append(two_sum[-val].extend(val))

            two_sum[sum] = [nums[left], nums[right]]

            if sum > 0:
                right -= 1
                c = 1
            
            else:
                left += 1
                c = 0

        return res

        maybe like hafl test cases passed

            

    # 6. If you haven't addressed this in step 3 (when you were talking about approaches), think about how you would optimize the solution. Talk about big O here.

    did not pass all the test cases, looked at neetcode solution
    still am perplexed at how you can find this kind of solution, passing all test cases
    maybe just need more time

    # 7. we try again!! for loop over the list and then do 2 sum 2 over the entire thing

    nums.sort()
    res = []

    for i in range(len(nums)):
        # iterate over the list

        # curr 'a'
        a = nums[i]

        if a > 0:
            break 

        if i > 0 and a == nums[i - 1]:
            # also duplicate protection
            continue

        left = i + 1
        right = len(nums) - 1

        while left < right:
            b = nums[left]
            c = nums[right]


            if (a + b + c) < 0:
                left += 1
                
            elif (a + b + c) > 0:
                right -= 1

            else:
                res.append([a, b, c])
                left += 1
                right -= 1

                while nums[left - 1] == b and left < right:
                # protect against duplicates
                    left += 1

    return res

