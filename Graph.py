# First networkx library is imported
# along with matplotlib
import networkx as nx
import matplotlib.pyplot as plt

x = [0,3]
# Defining a Class
class GraphVisualization:

    def __init__(self):
        # visual is a list which stores all
        # the set of edges that constitutes a
        # graph
        self.visual = []

    # addEdge function inputs the vertices of an
    # edge and appends it to the visual list
    def addEdge(self, a, b):
        temp = [a, b]
        self.visual.append(temp)

    # In visualize function G is an object of
    # class Graph given by networkx G.add_edges_from(visual)
    # creates a graph with a given list
    # nx.draw_networkx(G) - plots the graph
    # plt.show() - displays the graph
    def visualize(self):
        G = nx.Graph()
        G.add_edges_from(self.visual)
        for i in range (len(x)):
            node_colors = ["red" if i in x else "green" for i in G.nodes()]
        pos = nx.spring_layout(G)
        nx.draw_networkx_nodes(G,pos=pos,node_color=node_colors)
        nx.draw_networkx_edges(G,pos=pos)
        labels = {}
        for i in G.nodes():
            labels[i] = i
        nx.draw_networkx_labels(G,pos,labels,font_size=16)
        plt.show()


# Driver code
G = GraphVisualization()
G.addEdge(0, 2)
G.addEdge(1, 2)
G.addEdge(1, 3)
G.addEdge(5, 3)
G.addEdge(3, 4)
G.addEdge(1, 0)
G.visualize()