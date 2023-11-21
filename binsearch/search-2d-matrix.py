    # 1. Copy/paste the problem definition. Read it out loud and understand what they want.


    You are given an m x n integer matrix matrix with the following two properties:

        Each row is sorted in non-decreasing order.
        The first integer of each row is greater than the last integer of the previous row.

    Given an integer target, return true if target is in matrix or false otherwise.

    You must write a solution in O(log(m * n)) time complexity.

    # 2. Look at the examples they give you for what the algorithm should do. "Solution(input) -> output". Come up with 1 or 2 examples on your own, and write them down.

    # 3. Think out loud, and write down (!!) the possible high-level approaches to solving the problem. 
    #     Eg: "this two-sum problem can be brute-forced in O(n^2) time using two for-loops, or it can be solved in O(n) using a hashmap." 
    #     This doesn't have to be detailed, just a possible approach. Think about possible edge cases and how they could break the solution.

    #     Here, if you are completely blanking after 5 minutes, and can't even do a brute-force solution, then do what the OP said 
    #     - abort mission, and spend the next hour understanding the problem by looking at the solution. Once you understood the solution go to step 4.

        1. convert matrix into array


    # 4. Pick one of the approaches, and write out the pseudo code for it, while taking out loud as to what your thought process is.

        cat = []
        for row in matrix:
            cat.extend(row)

        l = 0
        r = len(cat) - 1
        # print(cat)

        while l <= r:

            m = (l + r) / 2
            if cat[m] == target:
                return True
            elif cat[m] > target:
                r = m - 1
            else:
                l = m + 1

        return False
    # 5. CODE THE ACTUAL SOLUTION. If you actually followed steps 1-4, this part is going to be trivial. You will bang out the actual code often in under 5 minutes. 
    # Paste the code into leetcode (or whatever platform you are using) to ensure it works. You can even write your own test cases, and run locally.

        2. translate coordinates
        if not matrix or target is None:
            return False

        m = len(matrix)
        n = len(matrix[0])

        l = 0
        r = (m * n) - 1
        # print(cat)

        while l <= r:

            mid = (l + r) / 2
            # mid is the index
            # to find what row we are on, idx // n
            row = (mid / n)
            # to find what pos we are in, idx % m
            pos = (mid % n)
            num = matrix[row][pos]

            if num == target:
                return True
            elif num > target:
                r = mid - 1
            else:
                l = mid + 1

        return False

    # 6. If you haven't addressed this in step 3 (when you were talking about approaches), think about how you would optimize the solution. Talk about big O here.

