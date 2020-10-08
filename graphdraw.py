import matplotlib.pyplot as plt
import networkx as nx
from k_trusses import k_truss_decomp
import numpy
# import scipy
from networkx import core_number, k_core

def graphToPng(graph, *args, **kwargs):
    options = {
        'node_size': 300,
        'line_color': 'grey',
        'linewidths': 0,
        'width': 0.3,
        'font_size': 8,
    }
    filename = kwargs.get('filename', None)
    if not filename:
        filename = 'graph'
    plt.figure(filename, figsize=(17, 8))
    plt.suptitle(filename)
    pos_nodes = nx.circular_layout(graph)

    colors = [node[1]['color'] for node in graph.nodes(data=True)]
    print(colors)

    nx.draw(graph, pos_nodes, with_labels=True,node_color=colors, **options)
    pos_atrs = {}
    for node, coords in pos_nodes.items():
        pos_atrs[node] = (coords[0], coords[1] + 0.01)

    node_attrs = nx.get_node_attributes(graph, 'term')
    cus_node_att = {}
    for node, attr in node_attrs.items():
        cus_node_att[node] = attr

    nx.draw_networkx_labels(graph, pos_atrs, labels=cus_node_att, node_color=colors, font_size=8)

    #labels = nx.get_edge_attributes(graph, 'weight')
    #nx.draw_networkx_edge_labels(graph, pos_nodes, edge_labels=labels)
    plt.show()

with open('graph_2.txt') as f:
    lines = f.readlines()

edges = [line.strip().split() for line in lines]
# [['a', 'b'], ['a', 'c'], ['b', 'd'], ['c', 'e']]

testgraph = nx.Graph()
testgraph.add_edges_from(edges)
corno= nx.core_number(testgraph)
trussno = k_truss_decomp(testgraph)
print(k_truss_decomp(testgraph))
print(corno)

# colour depending on core num
test1 = []
test2 = []
test3 = []
test4 = []
for key,value in corno.items():
    if value ==1:
        test1.append(key)
        testgraph.nodes[key]['color'] = '#e2e2e2'
    if value == 2:
        test2.append(key)
        testgraph.nodes[key]['color'] = '#767676'
    if value == 3:
        test3.append(key)
        testgraph.nodes[key]['color'] = '#bbbbbb'
    if value == 4:
        test4.append(key)
        testgraph.nodes[key]['color'] = '#b54b4b'

graphToPng(testgraph,filename="K Core Decomposition")
for i in range(1,5):
    Kcore = k_core(testgraph,i,corno)
    graphToPng(Kcore, filename=i)

for node in testgraph.nodes():
    if node in trussno[0]:
        testgraph.nodes[node]['color'] = '#e2e2e2'
    if node in trussno[1]:
        testgraph.nodes[node]['color'] = '#808080'
    if node in trussno[2]:
        testgraph.nodes[node]['color'] = '#b54b4b'
    #if node in trussno[3]:
    #    testgraph.nodes[node]['color'] = 'black'
graphToPng(testgraph,filename="K truss Decomposition")


print(test1)
print(test2)
print(test3)
print(test4)


