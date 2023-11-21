
    # 1. Copy/paste the problem definition. Read it out loud and understand what they want.
        In this problem, a tree is an undirected graph that is connected and has no cycles.

        You are given a graph that started as a tree with n nodes labeled from 1 to n, with one additional edge added. The added edge has two different vertices chosen from 1 to n, and was not an edge that already existed. The graph is represented as an array edges of length n where edges[i] = [ai, bi] indicates that there is an edge between nodes ai and bi in the graph.

        Return an edge that can be removed so that the resulting graph is a tree of n nodes. If there are multiple answers, return the answer that occurs last in the input.
    # 2. Look at the examples they give you for what the algorithm should do. "Solution(input) -> output". Come up with 1 or 2 examples on your own, and write them down.

        1. without nc solution i would p think of some complex sol idk

        2. repeatly add connections to a set, if there is a repeat, return

        3. union find
    # 3. Think out loud, and write down (!!) the possible high-level approaches to solving the problem. 
    #     Eg: "this two-sum problem can be brute-forced in O(n^2) time using two for-loops, or it can be solved in O(n) using a hashmap." 
    #     This doesn't have to be detailed, just a possible approach. Think about possible edge cases and how they could break the solution.

    #     Here, if you are completely blanking after 5 minutes, and can't even do a brute-force solution, then do what the OP said 
    #     - abort mission, and spend the next hour understanding the problem by looking at the solution. Once you understood the solution go to step 4.

        par = [i for i in range(len(edges) + 1)]
        rank = [1] * (len(edges) + 1)

        def find(n):
            # curr parent
            p = par[n]

            # we want to find the root parent
            while p != par[p]:
                # list reduction
                par[p] = par[par[p]]
                p = par[p]
            
            # return root
            return p

        def union(n1, n2):
            p1 = find(n1)
            p2 = find(n2)

            # if same root parent, then it is already connected
            if p1 == p2:
                return False

            # otherwise, union the things
            if rank[p1] > rank[p2]:
                rank[p1] += rank[p2]
                par[p2] = p1
            else:
                rank[p2] += rank[p1]
                par[p1] = p2
            
            return True

        for n1, n2 in range(len(edges)):
            if not union(n1, n2):
                return [n1, n2]
            
    

    # 4. Pick one of the approaches, and write out the pseudo code for it, while taking out loud as to what your thought process is.

    # 5. CODE THE ACTUAL SOLUTION. If you actually followed steps 1-4, this part is going to be trivial. You will bang out the actual code often in under 5 minutes. 
    # Paste the code into leetcode (or whatever platform you are using) to ensure it works. You can even write your own test cases, and run locally.
        learning union find
        
    # 6. If you haven't addressed this in step 3 (when you were talking about approaches), think about how you would optimize the solution. Talk about big O here.

