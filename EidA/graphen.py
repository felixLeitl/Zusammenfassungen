import random
import networkx as nx
import matplotlib.pyplot as plt


def random_graph(size: int, numbers: int) -> list[list[int]]:
    graph = []
    for _ in range(size):
        graph.append([])
    for i in range(size):
        for j in range(size):
            if i != j:
                graph[i].append(random.randint(0, numbers))
            else:
                graph[i].append(0)
    return graph


def bfs(graph: list[list[int]], start: int) -> list[bool]:
    visited = []
    queue = []
    for i in range(len(graph)):
        visited.append(False)
    queue.append(start)
    while len(queue) > 0:
        u = queue.pop(0)
        visited[u] = True
        for i in range(len(graph)):
            if graph[u][i] > 0 and not visited[i]:
                queue.append(i)
            if graph[i][u] > 0 and not visited[i]:
                queue.append(i)
    return visited


def dfs(graph: list[list[int]], start: int) -> list[bool]:
    visited = []
    stack = []
    for i in range(len(graph)):
        visited.append(False)
    stack.append(start)
    while len(stack) > 0:
        u = stack.pop()
        visited[u] = True
        for i in range(len(graph)):
            if graph[u][i] > 0 and not visited[i]:
                stack.append(i)
            if graph[i][u] > 0 and not visited[i]:
                stack.append(i)
    return visited


# TODO: implement dijkstra
def dijkstra(graph: list[list[int]], start: int) -> list[int]:
    queue = []
    for i in range(len(graph)):
        queue.append(i)
    visited = []
    shortest_path = []
    for i in range(len(graph)):
        visited.append(False)
        shortest_path.append(0)
    while len(queue) > 0:
        u = queue.pop()
        visited[u] = True
        for i in range(len(graph)):
            if graph[u][i] > 0 and graph[u][i] and not visited[i]:
                print('fuck')
    pass







# TODO: implement floyd_warshall
def floyd_warshall(graph: list[list[int]]) -> list[list[int]]:
    pass


# TODO: implement ford_fulkerson
def ford_fulkerson(graph: list[list[int]], start: int, final: int) -> list[list[int]]:
    pass


def page_rank(graph: list[list[int]], probability: float, iterations: int) -> list[list[int]]:
    m = []
    # Calculate M from graph
    for i in range(len(graph)):
        row_count = 0
        row = []
        for j in range(len(graph)):
            if graph[i][j] == 1:
                row_count += 1
        for j in range(len(graph)):
            if graph[i][j] == 1:
                row.append(1 / row_count)
            else:
                row.append(0)
        m.append(row)

    # Calculate M' = probability * M + ...
    for i in range(len(m)):
        for j in range(len(m)):
            m[i][j] = probability * m[i][j] + (1 - probability) / len(m)

    M_transposed = []

    for i in range(len(m)):
        row = []
        for j in range(len(m)):
            row.append(m[j][i])
        M_transposed.append(row)

    # Initialize rank

    rank = list(1 / len(m) for i in range(len(m)))
    # Power Iteration

    for i in range(iterations):
        result = []
        for i in range(len(m)):
            row = 0
            for j in range(len(m)):
                row += M_transposed[i][j] * rank[j]
            result.append(row)
        sum = 0  # Norm result
        for i in range(len(result)):
            sum += result[i]
        if sum != 1:
            for i in range(len(result)):
                result[i] = result[i] / sum
        rank = result

    return rank


# TODO: implement kruskal
def kruskal(graph: list[list[int]]) -> list[list[int]]:
    pass


# TODO: implement prim
def prim(graph: list[list[int]]) -> list[list[int]]:
    pass


def plot_graph(adj_matrix):
    # create directed graph from adjacency matrix
    edges = []
    for i in range(len(adj_matrix)):
        for j in range(len(adj_matrix[i])):
            if adj_matrix[i][j] != 0:
                edges.append((i, j))
    g = nx.DiGraph(edges)
    for i in range(len(adj_matrix)):
        if not g.has_node(i):
            g.add_node(i)
    node_sizes, node_labels = [], {}
    for i in g.nodes:
        node_labels[i] = f'{i}'
        node_sizes.append(max(1000, int(10000 * 0.1)))
    node_colors = [(0.0 + 1, 0.0, 1.0 - 1, 1.0) for _ in g.nodes]
    # plot graph
    pos = nx.spring_layout(g, seed=42, k=1, iterations=10)
    nx.draw_networkx_nodes(g, pos, node_size=node_sizes, node_color=node_colors)
    nx.draw_networkx_labels(g, pos, labels=node_labels, font_size=10)
    nx.draw_networkx_edges(g, pos, connectionstyle='arc3,rad=.1', node_size=node_sizes)
    plt.axis('off')
    plt.show()


if __name__ == '__main__':
    null_graph = [[0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0, 0], [0, 0, 0, 0, 0], [0, 0, 0, 0, 0]]
    ran_graph = random_graph(size=5, numbers=1)

    plot_graph(ran_graph)
    # plot_graph(null_graph)

    print(ran_graph[:])
    print(bfs(ran_graph[:], 0))
    print(bfs(null_graph, 0))
    print(dfs(ran_graph[:], 0))
    print(dfs(null_graph, 0))
    print(page_rank(graph=ran_graph[:], probability=0.85, iterations=100))
