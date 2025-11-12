# Consider a particular area in your city. Note the popular locations A, B, C . . . in that area.
# Assume these locations represent nodes of a graph.
# If there is a route between two locations, it is represented as connections between nodes.
# Find out the sequence in which you will visit these locations, starting from (say A) using
# (i) BFS and (ii) DFS.
# Represent a given graph using an adjacency matrix to perform DFS and an adjacency list to perform BFS.

v = 5
start = 0

# Adjacency List for bfs (Required representation)
adj_list = [[1, 2], [0, 3, 4], [0, 3], [1, 2], [1]]

# Adjacency Matrix for dfs (Required representation)
adj_matrix = [
    [0, 1, 1, 0, 0],
    [1, 0, 0, 1, 1],
    [1, 0, 0, 1, 0],
    [0, 1, 1, 0, 0],
    [0, 1, 0, 0, 0],
]

def bfs(adj, start_node):
    visited = [False] * len(adj)
    result = []
    queue = []  

    visited[start_node] = True
    queue.append(start_node)

    while queue:
        curr = queue.pop(0)  
        result.append(curr)  

        for neighbor in adj[curr]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)  
    return result

def dfs(adj_matrix_ref, num_v, start_node, visited, result):

    result.append(start_node)  
    visited[start_node] = True

    for i in range(num_v):
        if adj_matrix_ref[start_node][i] == 1 and (not visited[i]):
            dfs(adj_matrix_ref, num_v, i, visited, result)
    return result


def show_map_details():
    print("\n--- map details ---")
    print(f"locations (nodes): 0, 1, 2, 3, 4, start: {start}")
    print("adj list (bfs):", adj_list)
    print("adj matrix (dfs):")
    for row in adj_matrix:
        print(row)
    print("-------------------")


while True:
    print("\n| graph traversal menu |")
    print("1. run bfs | 2. run dfs | 3. show map | 4. exit")

    choice = input("enter choice (1-4): ")

    if choice == "1":
        seq = bfs(adj_list, start)
        print(f"bfs sequence: {seq}")

    elif choice == "2":
        seq = dfs(adj_matrix, v, start, [False] * v, [])
        print(f"dfs sequence: {seq}")

    elif choice == "3":
        show_map_details()

    elif choice == "4":
        print("exiting.")
        break

    else:
        print("invalid choice.")