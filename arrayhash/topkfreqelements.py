
    # 1. Copy/paste the problem definition. Read it out loud and understand what they want.

        Given an integer array nums and an integer k, return the k most frequent elements. You may return the answer in any order.

    # 2. Look at the examples they give you for what the algorithm should do. "Solution(input) -> output". Come up with 1 or 2 examples on your own, and write them down.

        input: nums = [3, 5, 5, 6, 6, 6, 7]     k = 2       output = [6, 5]
        input: nums = [1, 2, 2]     k = 1                   output = [2]
    # 3. Think out loud, and write down (!!) the possible high-level approaches to solving the problem. 
    #     Eg: "this two-sum problem can be brute-forced in O(n^2) time using two for-loops, or it can be solved in O(n) using a hashmap." 
    #     This doesn't have to be detailed, just a possible approach. Think about possible edge cases and how they could break the solution.

    #     Here, if you are completely blanking after 5 minutes, and can't even do a brute-force solution, then do what the OP said 
    #     - abort mission, and spend the next hour understanding the problem by looking at the solution. Once you understood the solution go to step 4.

        1. solution 1, store frequencies into an array, remember the values. Order it and then take the top k elements.
        O(logn)

        2. solution 2, make dict to create [element, freq] mapping. set a zeroes array of len(array size) where idx represents frequency and element represeents element.
        Then return top k elements.

        this works only because the answer is unique

    # 4. Pick one of the approaches, and write out the pseudo code for it, while taking out loud as to what your thought process is.

        buckets = [0] * len(array)

        count freq dict

        for elements over array

            make counter

        for element in dict, update mapping
        
        check buckets, and return top values k times

        
    # 5. CODE THE ACTUAL SOLUTION. If you actually followed steps 1-4, this part is going to be trivial. You will bang out the actual code often in under 5 minutes. 
    # Paste the code into leetcode (or whatever platform you are using) to ensure it works. You can even write your own test cases, and run locally.

    buckets = [[] for i in range(len(nums) + 1) ]

    dic = {}

    for element in nums:

        if element in dic:
            dic[element] += 1
        else:
            dic[element] = 1
    
    for element in dic:
        buckets[dic[element]].append(element)
    
    ret = []

    idx = len(buckets) - 1
    while len(ret) != k:
        ret.extend(buckets[idx])
        idx -= 1
    
    return ret


    # 6. If you haven't addressed this in step 3 (when you were talking about approaches), think about how you would optimize the solution. Talk about big O here.

    This is the optimized solution. For the future, I will review more on list comprehension and also review backwards list iteration.

    I am happy that I was able to remember counting sort solution.