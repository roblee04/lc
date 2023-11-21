
    # 1. Copy/paste the problem definition. Read it out loud and understand what they want.
        You are given the head of a singly linked-list. The list can be represented as:

        L0 → L1 → … → Ln - 1 → Ln

        Reorder the list to be on the following form:

        L0 → Ln → L1 → Ln - 1 → L2 → Ln - 2 → …

        You may not modify the values in the list's nodes. Only nodes themselves may be changed.
    # 2. Look at the examples they give you for what the algorithm should do. "Solution(input) -> output". Come up with 1 or 2 examples on your own, and write them down.

    # 3. Think out loud, and write down (!!) the possible high-level approaches to solving the problem. 
    #     Eg: "this two-sum problem can be brute-forced in O(n^2) time using two for-loops, or it can be solved in O(n) using a hashmap." 
    #     This doesn't have to be detailed, just a possible approach. Think about possible edge cases and how they could break the solution.

    #     Here, if you are completely blanking after 5 minutes, and can't even do a brute-force solution, then do what the OP said 
    #     - abort mission, and spend the next hour understanding the problem by looking at the solution. Once you understood the solution go to step 4.
        1. one approach is to store all the nodes into some array
            -  after that, we can add the left and right nodes one by one to our ending linked list

        2. another approach: split the linked list into 2, reverse the second array
            - to modify in place, we can keep adding to the first list
            - another thing you could do is to just make another linked list,
                -  this linked list can be allocated by alteranting adds between the left and right linked lists

    # 4. Pick one of the approaches, and write out the pseudo code for it, while taking out loud as to what your thought process is.
        
        # first, lets find the middle of the linked

        slow, fast = head, head.next

        while fast and fast.next:
            slow = slow.next
            fast = fast.next.next

        # now, slow is a ptr to the middle of the linked list

        second = slow.next
        slow.next = None # cut off the first linked list

        # now, lets reverse the second part of the list
        prev = None
        while second:
            nxt = second.next
            second.next = prev
            prev = second
            second = nxt
        
        # prev holds the head of the reversed linked list
        first = head
        second = prev

        while prev:
            tmp1, tmp2 = first.next, second.next
            first.next = second
            second.next = tmp1
            first = tmp1
            second = tmp2



    # 5. CODE THE ACTUAL SOLUTION. If you actually followed steps 1-4, this part is going to be trivial. You will bang out the actual code often in under 5 minutes. 
    # Paste the code into leetcode (or whatever platform you are using) to ensure it works. You can even write your own test cases, and run locally.

    # 6. If you haven't addressed this in step 3 (when you were talking about approaches), think about how you would optimize the solution. Talk about big O here.

