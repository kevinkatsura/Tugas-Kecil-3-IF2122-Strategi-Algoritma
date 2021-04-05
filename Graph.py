import networkx as nx
import matplotlib.pyplot as plt
import matplotlib.patches as mpatches

# Defining a Class
class GraphVisualization:
    # Inisialisasi atribut visual dengan array kosong
    def __init__(self):
        self.visual = []
        self.edgeLabel = []

    # Menambahkan edge
    def addEdge(self, a, b,edgeLabel):
        temp = [a, b]
        self.visual.append(temp)
        self.edgeLabel.append(edgeLabel)

    # Visualisasi
    def visualize(self,jalur):
        G = nx.Graph()
        G.add_edges_from(self.visual)

        # Mawarnai nodes jalur Astar
        for i in G.nodes():
            node_colors = ["pink" if i in jalur else "skyblue" for i in G.nodes()]

        # Menambahkan label jarak antar simpul
        formatted_edge_labels = {(self.visual[i][0],self.visual[i][1]):self.edgeLabel[i] for i in range(len(self.visual))}


        # Menambahkan warna pada edge yang dilalui

        # Draw nodes and edges
        pos = nx.spring_layout(G)
        nx.draw_networkx_nodes(G,pos=pos,node_color=node_colors,node_size=1000)
        nx.draw_networkx_edges(G,pos=pos)
        nx.draw_networkx_edge_labels(G,pos,edge_labels=formatted_edge_labels)

        # Labeling nodes
        labels = {}
        for i in G.nodes():
            labels[i] = i
        nx.draw_networkx_labels(G,pos,labels,font_size=16)

        # Menambahkan legenda
        pink_patches = mpatches.Patch(color='pink', label='Node yang dilalui')
        skyblue_patches = mpatches.Patch(color='skyblue', label='Node yang tidak dilalui')
        plt.legend(handles=[pink_patches,skyblue_patches])
        plt.show()