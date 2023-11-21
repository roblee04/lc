
    # 1. Copy/paste the problem definition. Read it out loud and understand what they want.
        Given the head of a linked list, remove the nth node from the end of the list and return its head.
    # 2. Look at the examples they give you for what the algorithm should do. "Solution(input) -> output". Come up with 1 or 2 examples on your own, and write them down.

    # 3. Think out loud, and write down (!!) the possible high-level approaches to solving the problem. 
    #     Eg: "this two-sum problem can be brute-forced in O(n^2) time using two for-loops, or it can be solved in O(n) using a hashmap." 
    #     This doesn't have to be detailed, just a possible approach. Think about possible edge cases and how they could break the solution.

    #     Here, if you are completely blanking after 5 minutes, and can't even do a brute-force solution, then do what the OP said 
    #     - abort mission, and spend the next hour understanding the problem by looking at the solution. Once you understood the solution go to step 4.
        1. initial way to solve this problem is to have a counter to find the leng of the linked list
            - after that, you can do leng - n to find which node you want to delete
            -  this is a 2 pass solution

        2. another smart solution is a thinking of this as a kind of 2 ptr problem. 
            - left ptr is slow, right ptr is offset by n. when right ptr runs into null, left ptr is at the node to be deleted
            - we will make a dummy node so left ptr starts at a correct place
            - or, we could just increase the offset by n + 1 instead, will try that

    # 4. Pick one of the approaches, and write out the pseudo code for it, while taking out loud as to what your thought process is.

        right = left = head

        while (n + 1) > 0:
            right = right.next
            n -= 1
        # move right ptr to the right

        while right:
            # iterate on the LL
            right = right.next
            left = left.next

        # deletion operation, what if node to delete is out of range?
        left.next = left.next.next

        return head

        # actually, dummy is needed to prevent some stupid things from happening
        # like, if node delete is out of range
        dummy = ListNode(0, head)
        left = dummy
        right = head

        while n > 0:
            right = right.next
            n -= 1
        # move right ptr to the right

        while right:
            # iterate on the LL
            right = right.next
            left = left.next

        # deletion operation, what if node to delete is out of range?
        left.next = left.next.next

        return dummy.next

    # 5. CODE THE ACTUAL SOLUTION. If you actually followed steps 1-4, this part is going to be trivial. You will bang out the actual code often in under 5 minutes. 
    # Paste the code into leetcode (or whatever platform you are using) to ensure it works. You can even write your own test cases, and run locally.

    # 6. If you haven't addressed this in step 3 (when you were talking about approaches), think about how you would optimize the solution. Talk about big O here.

        use dummy nodes
