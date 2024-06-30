# 1. Copy/paste the problem definition. Read it out loud and understand what they want.
Given a linked list, swap every two adjacent nodes and return its head. You must solve the problem without modifying the values in the list's nodes (i.e., only nodes themselves may be changed.)

# 2. Look at the examples they give you for what the algorithm should do. "Solution(input) -> output". Come up with 1 or 2 examples on your own, and write them down.
Input: head = [1,2,3,4]
Output: [2,1,4,3]

# 3. Think out loud, and write down (!!) the possible high-level approaches to solving the problem. 
#     Eg: "this two-sum problem can be brute-forced in O(n^2) time using two for-loops, or it can be solved in O(n) using a hashmap." 
#     This doesn't have to be detailed, just a possible approach. Think about possible edge cases and how they could break the solution.

#     Here, if you are completely blanking after 5 minutes, and can't even do a brute-force solution, then do what the OP said 
#     - abort mission, and spend the next hour understanding the problem by looking at the solution. Once you understood the solution go to step 4.
2 pass solution

1st pass, odd and even linked lists

2nd pass, join together


# 4. Pick one of the approaches, and write out the pseudo code for it, while taking out loud as to what your thought process is.

we want to iterate through the list
dummy.next = head

prev = dummy
curr = prev.next

while curr and curr.next:

    curr_node = curr
    next_node = curr.next

    prev.next = next_node
    curr_node.next = next_node.next
    prev.next.next = curr_node

    
    prev = curr
    curr = curr.next



# 5. CODE THE ACTUAL SOLUTION. If you actually followed steps 1-4, this part is going to be trivial. You will bang out the actual code often in under 5 minutes. 
# Paste the code into leetcode (or whatever platform you are using) to ensure it works. You can even write your own test cases, and run locally.

def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:

    dummy = ListNode(0, head)

    prev = dummy
    curr = prev.next

    while curr and curr.next:

        curr_node = curr
        next_node = curr.next

        prev.next = next_node
        curr_node.next = next_node.next
        prev.next.next = curr_node

        prev = curr
        curr = curr.next
    
    return dummy.next
                
# 6. If you haven't addressed this in step 3 (when you were talking about approaches), think about how you would optimize the solution. Talk about big O here.
