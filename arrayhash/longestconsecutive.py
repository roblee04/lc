
    # 1. Copy/paste the problem definition. Read it out loud and understand what they want.

        Given an unsorted array of integers nums, return the length of the longest consecutive elements sequence.

        You must write an algorithm that runs in O(n) time.

    # 2. Look at the examples they give you for what the algorithm should do. "Solution(input) -> output". Come up with 1 or 2 examples on your own, and write them down.

        input: [ 0, 2, 6, 4, 5]         output: 3

        input: [ 0, 2, 6]               output: 1

    # 3. Think out loud, and write down (!!) the possible high-level approaches to solving the problem. 
    #     Eg: "this two-sum problem can be brute-forced in O(n^2) time using two for-loops, or it can be solved in O(n) using a hashmap." 
    #     This doesn't have to be detailed, just a possible approach. Think about possible edge cases and how they could break the solution.

    #     Here, if you are completely blanking after 5 minutes, and can't even do a brute-force solution, then do what the OP said 
    #     - abort mission, and spend the next hour understanding the problem by looking at the solution. Once you understood the solution go to step 4.

        1. the easiest way to solve this problem is by sorting the list logn

        2. something to notice is that we do not have to keep track of the numbers / consecutive sequence, only the longest one

        My solution is counting sort, i will make an array of max(a) long, and then try to count the longest seq

    # 4. Pick one of the approaches, and write out the pseudo code for it, while taking out loud as to what your thought process is.

        take the max of the arr, set the [0] array size to it

        iterate through the array, set [0] array to 1 by index

    # 5. CODE THE ACTUAL SOLUTION. If you actually followed steps 1-4, this part is going to be trivial. You will bang out the actual code often in under 5 minutes. 
    # Paste the code into leetcode (or whatever platform you are using) to ensure it works. You can even write your own test cases, and run locally.

        if not nums:    # for [] case
            return 0

        countp = [0] * (max(nums) + 1)
        
        for n in nums:
            count[n] = 1
        
        gc = 0
        lc = 0
        for n in count:

            if n == 0:
                lc = 0
            else:
                lc += 1
                gc = max(lc, gc)

        return gc


        # problem, does not work for negative numbers
        # solution? extend

        if not nums:    # for [] case
            return 0

        countp = [0] * (max(nums) + 1)
        countn = [0] * (abs(min(nums))) # no + 1, 0 is -1, -1 is -2 ...
        for n in nums:
            if n >= 0:
                countp[n] = 1
            if n < 0:
               
                countn[abs(n) - 1] = 1

        countn.reverse()
        countn.extend(countp)
        
        gc = 0
        lc = 0
        for n in countn:

            if n == 0:
                lc = 0
            else:
                lc += 1
                gc = max(lc, gc)

        return gc

    # memory limit exceeded


    # 6. If you haven't addressed this in step 3 (when you were talking about approaches), think about how you would optimize the solution. Talk about big O here.

        logic

        # iterate thru the array, check if the number is the start of a sequence, e.g. if the num -1 is not in the set
        # if it is the start, add one to counter and check if the next number is in the set
        # update the max leng
        # if it is not, then continue to interate

        check = set(nums)
        maxc = 0
        for n in nums:
            localc = 0
            if not n - 1 in check:
                # check if it is the start
                local = n
                while local in check:
                    localc += 1
                    local += 1
                
                maxc = max(maxc, localc)
            
            
            else:
                continue
        
        return maxc

        +++++
        heck = set(nums)
        maxc = 0
        for n in nums:
            if n - 1 not in check:
                # check if it is the start
                localc = 0
                while n + localc in check:
                    localc += 1
                
                maxc = max(maxc, localc)
            
        
        return maxc

        code cleaned up.

        I should have thought a bit more about this problem, and with what kind of data structures I could have used.

        finding if the sequence was the start is very smart, using the set for o1 lookup was also very smart. I will do more of these
