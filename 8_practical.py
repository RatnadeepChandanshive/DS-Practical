# Consider a particular area in your city. Note the popular locations A, B, C . . . in that area.
# Assume these locations represent nodes of a graph.
# If there is a route between two locations, it is represented as connections between nodes.
# Find out the sequence in which you will visit these locations, starting from (say A) using
# (i) BFS and (ii) DFS.
# Represent a given graph using an adjacency matrix to perform DFS and an adjacency list to perform BFS.

# Setup: locations a(0), b(1), c(2), d(3), e(4)
v = 5
node_map = {0: "a", 1: "b", 2: "c", 3: "d", 4: "e"}
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


def bfs(adj, start_node, mapping):
    visited = [False] * len(adj)
    result = []
    queue = []  # Using list as a queue (less efficient than deque)

    visited[start_node] = True
    queue.append(start_node)

    while queue:
        curr = queue.pop(0)  # Dequeue
        result.append(mapping[curr])

        for neighbor in adj[curr]:
            if not visited[neighbor]:
                visited[neighbor] = True
                queue.append(neighbor)  # Enqueue
    return result


def dfs(adj_matrix_ref, num_v, start_node, visited, result, mapping):
    result.append(mapping[start_node])
    visited[start_node] = True

    for i in range(num_v):
        if adj_matrix_ref[start_node][i] == 1 and (not visited[i]):
            dfs(adj_matrix_ref, num_v, i, visited, result, mapping)
    return result


def show_map_details():
    print("\n--- map details ---")
    print(f"locations: {', '.join(node_map.values())}, start: {node_map[start]}")
    print("adj list (bfs):", adj_list)
    print("adj matrix (dfs):")
    for row in adj_matrix:
        print(row)
    print("-------------------")


# Main Menu Loop
while True:
    print("\n| graph traversal menu |")
    print("1. run bfs | 2. run dfs | 3. show map | 4. exit")

    choice = input("enter choice (1-4): ")

    if choice == "1":
        seq = bfs(adj_list, start, node_map)
        print(f"bfs sequence: {', '.join(seq)}")

    elif choice == "2":
        seq = dfs(adj_matrix, v, start, [False] * v, [], node_map)
        print(f"dfs sequence: {', '.join(seq)}")

    elif choice == "3":
        show_map_details()

    elif choice == "4":
        print("exiting.")
        break

    else:
        print("invalid choice.")
