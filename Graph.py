# First networkx library is imported
# along with matplotlib
import networkx as nx
import matplotlib.pyplot as plt

x = [0,3]
# Defining a Class
class GraphVisualization:

    # Inisialisasi atribut visual dengan array kosong
    def __init__(self):
        self.visual = []

    # Menambahkan edge
    def addEdge(self, a, b):
        temp = [a, b]
        self.visual.append(temp)

    #Visualisasi
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