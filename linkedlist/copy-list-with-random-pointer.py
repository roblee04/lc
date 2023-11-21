
    # 1. Copy/paste the problem definition. Read it out loud and understand what they want.
        A linked list of length n is given such that each node contains an additional random pointer, which could point to any node in the list, or null.

        Construct a deep copy of the list. The deep copy should consist of exactly n brand new nodes, where each new node has its value set to the value of its corresponding original node. Both the next and random pointer of the new nodes should point to new nodes in the copied list such that the pointers in the original list and copied list represent the same list state. None of the pointers in the new list should point to nodes in the original list.

        For example, if there are two nodes X and Y in the original list, where X.random --> Y, then for the corresponding two nodes x and y in the copied list, x.random --> y.

        Return the head of the copied linked list.

        The linked list is represented in the input/output as a list of n nodes. Each node is represented as a pair of [val, random_index] where:

            val: an integer representing Node.val
            random_index: the index of the node (range from 0 to n-1) that the random pointer points to, or null if it does not point to any node.

        Your code will only be given the head of the original linked list.
    # 2. Look at the examples they give you for what the algorithm should do. "Solution(input) -> output". Come up with 1 or 2 examples on your own, and write them down.

    # 3. Think out loud, and write down (!!) the possible high-level approaches to solving the problem. 
    #     Eg: "this two-sum problem can be brute-forced in O(n^2) time using two for-loops, or it can be solved in O(n) using a hashmap." 
    #     This doesn't have to be detailed, just a possible approach. Think about possible edge cases and how they could break the solution.

    #     Here, if you are completely blanking after 5 minutes, and can't even do a brute-force solution, then do what the OP said 
    #     - abort mission, and spend the next hour understanding the problem by looking at the solution. Once you understood the solution go to step 4.
        1. the easiest way to solve this problem is thru a 2 pass solution
            - first, iterate thru the entire linked list
                - make a ListNode(next, random) and map the original node to the new node
            - second pass, create the links between everything
                - use the hashmap earlier to lookup the new nodes
    # 4. Pick one of the approaches, and write out the pseudo code for it, while taking out loud as to what your thought process is.

        ptr = head
        oldToNew = {None:None} # init, null maps to null
        while ptr:
            newNode = Node(ptr.val)
            oldToNew[ptr] = newNode # dont need to create the links yet
            ptr = ptr.next

        ptr = head # reset ptr for second pass, to create links

        while ptr:
            nxt = oldToNew[ptr.next]
            rand = oldToNew[ptr.random]
            newNode = oldToNew[ptr]
            newNode.next = nxt
            newNode.random = rand
            ptr = ptr.next
        
        return oldToNew[head]
        

    # 5. CODE THE ACTUAL SOLUTION. If you actually followed steps 1-4, this part is going to be trivial. You will bang out the actual code often in under 5 minutes. 
    # Paste the code into leetcode (or whatever platform you are using) to ensure it works. You can even write your own test cases, and run locally.

    # 6. If you haven't addressed this in step 3 (when you were talking about approaches), think about how you would optimize the solution. Talk about big O here.

