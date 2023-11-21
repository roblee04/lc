
    # 1. Copy/paste the problem definition. Read it out loud and understand what they want.
        In this problem, there is an undirected graph with n nodes. There is also an edges array. Where edges[i] = [a, b] means that there is an edge between node a and node b in the graph.

        You need to return the number of connected components in that graph.
    # 2. Look at the examples they give you for what the algorithm should do. "Solution(input) -> output". Come up with 1 or 2 examples on your own, and write them down.

    # 3. Think out loud, and write down (!!) the possible high-level approaches to solving the problem. 
    #     Eg: "this two-sum problem can be brute-forced in O(n^2) time using two for-loops, or it can be solved in O(n) using a hashmap." 
    #     This doesn't have to be detailed, just a possible approach. Think about possible edge cases and how they could break the solution.

    #     Here, if you are completely blanking after 5 minutes, and can't even do a brute-force solution, then do what the OP said 
    #     - abort mission, and spend the next hour understanding the problem by looking at the solution. Once you understood the solution go to step 4.
        1. Idea, use the union find algorithm to create the ranking system, then take the len of the set of ranking system
    # 4. Pick one of the approaches, and write out the pseudo code for it, while taking out loud as to what your thought process is.
        # first, all unconnected
        par = [i for i in range(len(edges) + 1)]
        rank = [0] * (len(edges) + 1)

        def find(n):
            # want to find the root parent of the node
            p = par[n]

            while p != par[p]:
                par[n] = par[par[n]]
                p = par[n]

            return p

        def union(n1, n2):
            n1 = find(n1)
            n2 = find(n2)

            if n1 == n2:
                # if the same parent, already connected, no operation needed
                return 0 
            
            if rank[n1] > rank[n2]:
                par[n2] = par[n1]
                rank[n1] += rank[n2]
            else:
                par[n1] = par[n2]
                rank[n2] += rank[n1]

        res = n
        for n1, n2 in edges:
            res -= union(n1, n2)

        return res


    # 5. CODE THE ACTUAL SOLUTION. If you actually followed steps 1-4, this part is going to be trivial. You will bang out the actual code often in under 5 minutes. 
    # Paste the code into leetcode (or whatever platform you are using) to ensure it works. You can even write your own test cases, and run locally.

    # 6. If you haven't addressed this in step 3 (when you were talking about approaches), think about how you would optimize the solution. Talk about big O here.

