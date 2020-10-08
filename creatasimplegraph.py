import matplotlib.pyplot as plt
import networkx as nx
import scipy

G =nx.Graph()

node_pos=nx.get_node_attributes(G,'pos')

ed =[(1,5,1),(2,3,1),(2,4,1),(5,1,1),(2,5,1)]
G.add_weighted_edges_from(ed)
G.add_weighted_edges_from([(4,3,3),(4,1,2),(5,3,4)])
arc_weight=nx.get_edge_attributes(G,'weight')

pos=nx.spring_layout(G)
t= nx.draw(G,pos,with_labels=True,node_color="gray")
nx.draw_networkx_edge_labels(G,pos,edge_labels=arc_weight)

plt.show()

A = nx.adjacency_matrix(G)
print(A.todense())

A= nx.incidence_matrix(G)
print(A.todense())