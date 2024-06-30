# 1. Copy/paste the problem definition. Read it out loud and understand what they want.
Given the head of a linked list, rotate the list to the right by k places.

# 2. Look at the examples they give you for what the algorithm should do. "Solution(input) -> output". Come up with 1 or 2 examples on your own, and write them down.

# 3. Think out loud, and write down (!!) the possible high-level approaches to solving the problem. 
#     Eg: "this two-sum problem can be brute-forced in O(n^2) time using two for-loops, or it can be solved in O(n) using a hashmap." 
#     This doesn't have to be detailed, just a possible approach. Think about possible edge cases and how they could break the solution.

#     Here, if you are completely blanking after 5 minutes, and can't even do a brute-force solution, then do what the OP said 
#     - abort mission, and spend the next hour understanding the problem by looking at the solution. Once you understood the solution go to step 4.

2 pointer approach with one pointer to be idx + k
# 4. Pick one of the approaches, and write out the pseudo code for it, while taking out loud as to what your thought process is.

# 5. CODE THE ACTUAL SOLUTION. If you actually followed steps 1-4, this part is going to be trivial. You will bang out the actual code often in under 5 minutes. 
# Paste the code into leetcode (or whatever platform you are using) to ensure it works. You can even write your own test cases, and run locally.

    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        
        if not head or not head.next:
            return head

        tail = head
        l = 1
        while tail.next != None:
            tail = tail.next
            l += 1

        # found length
        k = k % l

        if k == 0:
            return head

        # increment ptr by l - k - 1 times
        ptr = head
        c = l - k - 1
        while c > 0:
            ptr = ptr.next
            c -= 1

        newhead = ptr.next 
        ptr.next = None
        tail.next = head
    
        return newhead
# 6. If you haven't addressed this in step 3 (when you were talking about approaches), think about how you would optimize the solution. Talk about big O here.
