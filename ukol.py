import networkx as nx

Gd = nx.Graph()


def readdimacs(filename):

    file = open(filename, 'r')
    lines = file.readlines()
    
    Gd = nx.Graph()

    for line in lines:
        if line[0] == "e":
            vs = [int(s) for s in line.split() if s.isdigit()]
            Gd.add_edge(vs[0]-1, vs[1]-1)
    return Gd

Gd = readdimacs('graf')  
print("# vrcholu: ", Gd.number_of_nodes(), "# hran:", Gd.number_of_edges()) 