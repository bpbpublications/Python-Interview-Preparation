def alienOrder(words):
    graph = defaultdict(set)
    visited = {}  # 'visiting' (True) or 'visited' (False)
    result = []
 
    # Step 1: Build the graph
    for i in range(len(words) - 1):
        word1, word2 = words[i], words[i + 1]
        min_len = min(len(word1), len(word2))
 
        if len(word1) > len(word2) and word1[:min_len] == word2[:min_len]:
            return ""
 
        for j in range(min_len):
            if word1[j] != word2[j]:
                graph[word1[j]].add(word2[j])
                break
 
    # Step 2: DFS for topological sort
    def dfs(char):
        if char in visited:
            return visited[char]
 
        visited[char] = True  # Mark as visiting
 
        for neighbor in graph[char]:
            if dfs(neighbor):  # Cycle detected
                return True
 
        visited[char] = False  # Mark as visited
        result.append(char)
        return False
 
    # Visit all characters in the graph
    for char in {char for word in words for char in word}:
        if dfs(char):
            return ""  # Return empty string if cycle detected
 
    return "".join(result[::-1])
