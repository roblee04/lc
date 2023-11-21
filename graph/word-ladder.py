
    # 1. Copy/paste the problem definition. Read it out loud and understand what they want.
        A transformation sequence from word beginWord to word endWord using a dictionary wordList is a sequence of words beginWord -> s1 -> s2 -> ... -> sk such that:

        Every adjacent pair of words differs by a single letter.
        Every si for 1 <= i <= k is in wordList. Note that beginWord does not need to be in wordList.
        sk == endWord

    Given two words, beginWord and endWord, and a dictionary wordList, return the number of words in the shortest transformation sequence from beginWord to endWord, or 0 if no such sequence exists.
    # 2. Look at the examples they give you for what the algorithm should do. "Solution(input) -> output". Come up with 1 or 2 examples on your own, and write them down.

    # 3. Think out loud, and write down (!!) the possible high-level approaches to solving the problem. 
    #     Eg: "this two-sum problem can be brute-forced in O(n^2) time using two for-loops, or it can be solved in O(n) using a hashmap." 
    #     This doesn't have to be detailed, just a possible approach. Think about possible edge cases and how they could break the solution.

    #     Here, if you are completely blanking after 5 minutes, and can't even do a brute-force solution, then do what the OP said 
    #     - abort mission, and spend the next hour understanding the problem by looking at the solution. Once you understood the solution go to step 4.
        1. 
        a. first, create a dictionary that is word: [list of words 1 off]
        b. secondly, start from the start word and use BFS to find shortest path


    # 4. Pick one of the approaches, and write out the pseudo code for it, while taking out loud as to what your thought process is.

        # first map words
        d = {}

        wordList.append(beginWord)

        for word in wordList:
            for word2 in wordList:

                if word != word2:

                    c = 0
                    for i in range(len(word)):
                        if word[i] != word2[i]:
                            c += 1

                    if c == 1:
                        if word not in d:
                            d[word] = [word2]
                        else:
                            d[word].append(word2)

        # next, do bfs
        visited = set([beginWord])
        q = deque([beginWord])
        count = 1
        while q:
            for i in range(len(q)):
                word = q.popleft()
                
                if word == endWord:
                    return count

                firstList = d[word]
                for w in firstList:
                    if w not in visited:
                        q.append(w)
                        visited.add(w)

            count += 1

        return 0


        
    # 5. CODE THE ACTUAL SOLUTION. If you actually followed steps 1-4, this part is going to be trivial. You will bang out the actual code often in under 5 minutes. 
    # Paste the code into leetcode (or whatever platform you are using) to ensure it works. You can even write your own test cases, and run locally.

    # 6. If you haven't addressed this in step 3 (when you were talking about approaches), think about how you would optimize the solution. Talk about big O here.

