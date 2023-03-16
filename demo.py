import random
import networkx as nx
import matplotlib.pyplot as plt

def generate_graph(num_nodes):
    """Generates a random graph with the specified number of nodes."""
    # initialize an empty graph
    graph = {}

    # add nodes to the graph
    for node in range(num_nodes):
        graph[node] = set()

    # add random edges to the graph

    num_edges = random.randint(num_nodes, (num_nodes * (num_nodes - 1)) // 2)
    #num_edges = 125
    print(f"The number of edges used is {num_edges}.")
    edge_count = 0
    while edge_count < num_edges:
        node1 = random.randint(0, num_nodes - 1)
        node2 = random.randint(0, num_nodes - 1)
        if node2 not in graph[node1] and node1 != node2:
            graph[node1].add(node2)
            graph[node2].add(node1)
            edge_count += 1

    return graph

def greedy_coloring(graph):
    """Returns a dictionary where keys are vertices and values are the assigned colors."""
    # initialize all vertices with no color assigned
    colors = {}
    for vertex in graph:
        colors[vertex] = None

    # assign the first color to the first vertex
    first_vertex = list(graph.keys())[0]
    colors[first_vertex] = 0

    # assign colors to the rest of the vertices
    for vertex in graph:
        if colors[vertex] is None:
            # get the colors of the adjacent vertices
            adjacent_colors = [colors[adjacent] for adjacent in graph[vertex] if colors[adjacent] is not None]
            if adjacent_colors:
                adjacent_colors = sorted(set(adjacent_colors))
            else:
                adjacent_colors = []
            # find the lowest available color
            for color in range(len(graph)):
                if color not in adjacent_colors:
                    colors[vertex] = color
                    break

    return colors

def draw_graph(graph, colors):
    """Draws the graph with the vertices colored according to the colors dictionary."""
    node_colors = [colors[vertex] for vertex in graph]
    pos = nx.spring_layout(graph)
    nx.draw_networkx_nodes(graph, pos, node_color=node_colors, cmap=plt.cm.Set1)
    nx.draw_networkx_edges(graph, pos)
    plt.show()

# generate a random graph with 125 nodes
graph = generate_graph(125)

# color the graph
colors = greedy_coloring(graph)

# draw the graph
G = nx.Graph(graph)
draw_graph(G, colors)

# print the number of colors used
num_colors = len(set(colors.values()))
print(f"The number of colors used is {num_colors}.")
