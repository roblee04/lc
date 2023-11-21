
    # 1. Copy/paste the problem definition. Read it out loud and understand what they want.
        There are n cars going to the same destination along a one-lane road. The destination is target miles away.

    You are given two integer array position and speed, both of length n, where position[i] is the position of the ith car and speed[i] is the speed of the ith car (in miles per hour).

    A car can never pass another car ahead of it, but it can catch up to it and drive bumper to bumper at the same speed. The faster car will slow down to match the slower car's speed. The distance between these two cars is ignored (i.e., they are assumed to have the same position).

    A car fleet is some non-empty set of cars driving at the same position and same speed. Note that a single car is also a car fleet.

    If a car catches up to a car fleet right at the destination point, it will still be considered as one car fleet.

    Return the number of car fleets that will arrive at the destination.
    # 2. Look at the examples they give you for what the algorithm should do. "Solution(input) -> output". Come up with 1 or 2 examples on your own, and write them down.

    # 3. Think out loud, and write down (!!) the possible high-level approaches to solving the problem. 
    #     Eg: "this two-sum problem can be brute-forced in O(n^2) time using two for-loops, or it can be solved in O(n) using a hashmap." 
    #     This doesn't have to be detailed, just a possible approach. Think about possible edge cases and how they could break the solution.

    #     Here, if you are completely blanking after 5 minutes, and can't even do a brute-force solution, then do what the OP said 
    #     - abort mission, and spend the next hour understanding the problem by looking at the solution. Once you understood the solution go to step 4.
        1. solution is really smart
            - view the cars as a system of linear equations, from that you can calculate their intersection point
            - or if the cars meet between some interval

            - view in sorted order
            - the last car will always be the relative bottleneck, so start from the back

            - use a stack to check if cars will intersection

            - return len of stack

    # 4. Pick one of the approaches, and write out the pseudo code for it, while taking out loud as to what your thought process is.

        concatenate lists and put into reverse sorted order

        iterate thru this sorted list

            if stack:
                check if there is an intersection, if so, continue

                
            append

        return len
    # 5. CODE THE ACTUAL SOLUTION. If you actually followed steps 1-4, this part is going to be trivial. You will bang out the actual code often in under 5 minutes. 
    # Paste the code into leetcode (or whatever platform you are using) to ensure it works. You can even write your own test cases, and run locally.
        pair = []
        for i in range(len(position)):
            pair.append((position[i], speed[i]))

        pair.sort()
        stack = []

        for p, s in pair[::-1]:
            time = (target - p) / float(s)

            if stack:
                p2, s2 = stack[-1]
                time2 = (target - p2) / float(s2)
                # print(time, time2)
                if time2 >= time:
                    continue
            
            stack.append((p, s))

        
        return len(stack)
    # 6. If you haven't addressed this in step 3 (when you were talking about approaches), think about how you would optimize the solution. Talk about big O here.

        ty nc