
    # 1. Copy/paste the problem definition. Read it out loud and understand what they want.
        Given the root of a binary search tree, and an integer k, return the kth smallest value (1-indexed) of all the values of the nodes in the tree.
    # 2. Look at the examples they give you for what the algorithm should do. "Solution(input) -> output". Come up with 1 or 2 examples on your own, and write them down.

    # 3. Think out loud, and write down (!!) the possible high-level approaches to solving the problem. 
    #     Eg: "this two-sum problem can be brute-forced in O(n^2) time using two for-loops, or it can be solved in O(n) using a hashmap." 
    #     This doesn't have to be detailed, just a possible approach. Think about possible edge cases and how they could break the solution.

    #     Here, if you are completely blanking after 5 minutes, and can't even do a brute-force solution, then do what the OP said 
    #     - abort mission, and spend the next hour understanding the problem by looking at the solution. Once you understood the solution go to step 4.
        1. the only solution I can think of is populating an array with nums from the tree
            - sort the array,return kth element
            - This solution would be O(n*logn), because sorting
            - not sure how to do better

        2. NC solution
            - do in order traversal
            - practice iterative solution



    # 4. Pick one of the approaches, and write out the pseudo code for it, while taking out loud as to what your thought process is.

    # 5. CODE THE ACTUAL SOLUTION. If you actually followed steps 1-4, this part is going to be trivial. You will bang out the actual code often in under 5 minutes. 
    # Paste the code into leetcode (or whatever platform you are using) to ensure it works. You can even write your own test cases, and run locally.
        1. recursive approach, to do in order traversal, we always add left first

        lst = []

        def dfs(node):
            nonlocal lst
            # inorder traversal, visit left, mid, right
            if not node:
                return

            dfs(node.left)
            lst.append(node.val)
            dfs(node.right)

            
        dfs(root)

        return lst[k - 1]

        2. iterative approach

        n = 0
        stack = []
        cur = root

        while cur and stack:
            while cur:
                stack.append(cur.val)
                cur = cur.left
            
            cur = stack.pop()
            n += 1
            if n == k:
                return cur.val
            
            cur = cur.right


    # 6. If you haven't addressed this in step 3 (when you were talking about approaches), think about how you would optimize the solution. Talk about big O here.

