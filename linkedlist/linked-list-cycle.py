
    # 1. Copy/paste the problem definition. Read it out loud and understand what they want.
        Given head, the head of a linked list, determine if the linked list has a cycle in it.

        There is a cycle in a linked list if there is some node in the list that can be reached again by continuously following the next pointer. Internally, pos is used to denote the index of the node that tail's next pointer is connected to. Note that pos is not passed as a parameter.

        Return true if there is a cycle in the linked list. Otherwise, return false.
    # 2. Look at the examples they give you for what the algorithm should do. "Solution(input) -> output". Come up with 1 or 2 examples on your own, and write them down.

    # 3. Think out loud, and write down (!!) the possible high-level approaches to solving the problem. 
    #     Eg: "this two-sum problem can be brute-forced in O(n^2) time using two for-loops, or it can be solved in O(n) using a hashmap." 
    #     This doesn't have to be detailed, just a possible approach. Think about possible edge cases and how they could break the solution.

    #     Here, if you are completely blanking after 5 minutes, and can't even do a brute-force solution, then do what the OP said 
    #     - abort mission, and spend the next hour understanding the problem by looking at the solution. Once you understood the solution go to step 4.
        1. One way to solve this problem is to store every single node in a set. (either val if unique or actual object)
            - if we ever find it again, we are in a cycle

        2. Another way to solve this problem is with slow and fast pointers. 
            - slow will move at 1, fast will move at 2. Because of this, they will always meet if in a cycle
            -  one thing to keep in mind is how to find the beginning node for the graph starting the cycle
                - find this again later

    # 4. Pick one of the approaches, and write out the pseudo code for it, while taking out loud as to what your thought process is.

        slow, fast = head, head 

        while fast and fast.next:
            # need to make sure fast.next also exists,
            # so fast.next.next exists
            slow = slow.next
            fast = fast.next.next

            if slow == fast:
                return True
            

        return False    

    # 5. CODE THE ACTUAL SOLUTION. If you actually followed steps 1-4, this part is going to be trivial. You will bang out the actual code often in under 5 minutes. 
    # Paste the code into leetcode (or whatever platform you are using) to ensure it works. You can even write your own test cases, and run locally.

    # 6. If you haven't addressed this in step 3 (when you were talking about approaches), think about how you would optimize the solution. Talk about big O here.

