
    # 1. Copy/paste the problem definition. Read it out loud and understand what they want.
        There are a total of numCourses courses you have to take, labeled from 0 to numCourses - 1. You are given an array prerequisites where prerequisites[i] = [ai, bi] indicates that you must take course bi first if you want to take course ai.

        For example, the pair [0, 1], indicates that to take course 0 you have to first take course 1.

        Return the ordering of courses you should take to finish all courses. If there are many valid answers, return any of them. If it is impossible to finish all courses, return an empty array.
    # 2. Look at the examples they give you for what the algorithm should do. "Solution(input) -> output". Come up with 1 or 2 examples on your own, and write them down.

    # 3. Think out loud, and write down (!!) the possible high-level approaches to solving the problem. 
    #     Eg: "this two-sum problem can be brute-forced in O(n^2) time using two for-loops, or it can be solved in O(n) using a hashmap." 
    #     This doesn't have to be detailed, just a possible approach. Think about possible edge cases and how they could break the solution.

    #     Here, if you are completely blanking after 5 minutes, and can't even do a brute-force solution, then do what the OP said 
    #     - abort mission, and spend the next hour understanding the problem by looking at the solution. Once you understood the solution go to step 4.
        1. this problem is exactly like course schedule 1
        , but instead we want to add to an each course to an array

        a. create an adjacency list

        b. dfs
            the point of this dfs is to make sure that some arbitrary class that we select will (at the end)
            - enter a cycle, thus fail
            - have some class that will not have a prereq, 
                - thus this class will have no prereq either

            # one thing to note is that we need to add all these classes to a list
            -edge case diamond could be a problem

            the way to solve this is to also include a seen set to prevent multiple additions
        
        c. potentially need to add every class

    # 4. Pick one of the approaches, and write out the pseudo code for it, while taking out loud as to what your thought process is.

    # 5. CODE THE ACTUAL SOLUTION. If you actually followed steps 1-4, this part is going to be trivial. You will bang out the actual code often in under 5 minutes. 
    # Paste the code into leetcode (or whatever platform you are using) to ensure it works. You can even write your own test cases, and run locally.
        adj_list = {}
        for i in range(numCourses):
            adj_list[i] = []
        
        for crs, pre in prerequisites:
            adj_list[crs].append(pre)

        cycle = set()
        seen = set()
        res = []

        def dfs(crs):
            if crs in cycle:
                return False
            
            if adj_list[crs] == []:
                if crs not in seen:
                    seen.add(crs)
                    res.append(crs)

                return True

            cycle.add(crs)
            # do it on children
            for c in adj_list[crs]:
                if dfs(c) == False:
                    return False

            cycle.remove(crs)
            
            if crs not in seen:
                seen.add(crs) 
                res.append(crs)

            adj_list[crs] = []

            return True
        
        for crs in range(numCourses):
            if not dfs(crs):
                return []
        
        return res

        #works, but too slow
            

    # 6. If you haven't addressed this in step 3 (when you were talking about approaches), think about how you would optimize the solution. Talk about big O here.

        adj_list = {}
        for i in range(numCourses):
            adj_list[i] = []
        
        for crs, pre in prerequisites:
            adj_list[crs].append(pre)

        cycle = set()
        seen = set()
        res = []

        def dfs(crs):
            if crs in cycle:
                return False
            
            if crs in seen:
                return True

            cycle.add(crs)
            # do it on children
            for c in adj_list[crs]:
                if dfs(c) == False:
                    return False

            cycle.remove(crs)
            
            
            seen.add(crs) 
            res.append(crs)

            return True
        
        for crs in range(numCourses):
            if not dfs(crs):
                return []
        
        return res
