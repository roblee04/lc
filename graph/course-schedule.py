
    # 1. Copy/paste the problem definition. Read it out loud and understand what they want.
        There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

        For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.

        Return true if you can finish all courses. Otherwise, return false.
    # 2. Look at the examples they give you for what the algorithm should do. "Solution(input) -> output". Come up with 1 or 2 examples on your own, and write them down.

    # 3. Think out loud, and write down (!!) the possible high-level approaches to solving the problem. 
    #     Eg: "this two-sum problem can be brute-forced in O(n^2) time using two for-loops, or it can be solved in O(n) using a hashmap." 
    #     This doesn't have to be detailed, just a possible approach. Think about possible edge cases and how they could break the solution.

    #     Here, if you are completely blanking after 5 minutes, and can't even do a brute-force solution, then do what the OP said 
    #     - abort mission, and spend the next hour understanding the problem by looking at the solution. Once you understood the solution go to step 4.
        1. first, represent each course as a node and each edge as a "requires" link

        represent the entire thing as an adjacency list

        have a seen array to prevent cycles

        do dfs on potentially every node
    # 4. Pick one of the approaches, and write out the pseudo code for it, while taking out loud as to what your thought process is.

        populate adjacency list

        create a seen array

        dfs function:
        - conditions, check if we are in cycle --> return false if yes
                    check if there is no prerequisite for the course --> return true

        - add the node to the seen array
        - iterate dfs on children

        - remove the node from visited (to let main for loop to false flag a loop)
        - set the prereq of the course to none

        loop over all nodes



    # 5. CODE THE ACTUAL SOLUTION. If you actually followed steps 1-4, this part is going to be trivial. You will bang out the actual code often in under 5 minutes. 
    # Paste the code into leetcode (or whatever platform you are using) to ensure it works. You can even write your own test cases, and run locally.

        adj_list = {}
        seen = set()
        for i in range(numCourses):
            adj_list[i] = []
        
        for crs, pre in prerequisities:
            adj_list[crs].append(pre)
        
        def dfs(course):
            if course in seen:
                return False
            if adj_list[course] == []:
                return True
            
            seen.add(course)

            for pre in adj_list(course):
                if dfs(pre) == False:
                    # loop
                    return False
                
            # so it is a valid course and has prereq

            # remove from seen, to let other iterations work
            seen.remove(course)
            # reset prereq
            adj_list(course) = []
            return True
        
        for crs in range(numCourses):
            if not dfs(crs) return False else True

    # 6. If you haven't addressed this in step 3 (when you were talking about approaches), think about how you would optimize the solution. Talk about big O here.

        practice turning non graph problems into graphs
        1. adj list
        2. edge maps

        practice more of these problems
        practice bfs