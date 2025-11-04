from collections import defaultdict, deque
 
def alienOrder(words):
    # Step 1: Create a graph and indegree array
    graph = defaultdict(set)
    indegree = {char: 0 for word in words for char in word}
 
    # Step 2: Build the graph
    for i in range(len(words) - 1):
        word1, word2 = words[i], words[i + 1]
        min_len = min(len(word1), len(word2))
 
        # Check for invalid order like ["abc", "ab"]
        if len(word1) > len(word2) and word1[:min_len] == word2[:min_len]:
            return ""
 
        for j in range(min_len):
            if word1[j] != word2[j]:
                if word2[j] not in graph[word1[j]]:
                    graph[word1[j]].add(word2[j])
                    indegree[word2[j]] += 1
                break
 
    # Step 3: Topological sort using BFS (Kahn's Algorithm)
    queue = deque([char for char in indegree if indegree[char] == 0])
    result = []
 
    while queue:
        char = queue.popleft()
        result.append(char)
 
        for neighbor in graph[char]:
            indegree[neighbor] -= 1
            if indegree[neighbor] == 0:
                queue.append(neighbor)
 
    # Step 4: If result contains all characters, return as string, else return ""
    if len(result) == len(indegree):
        return "".join(result)
    else:
        return ""
