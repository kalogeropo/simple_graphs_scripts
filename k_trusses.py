# input a graph G = (V,E)
# Output a list [[lists_of_V_of_each_level_of_truss_decomposition]]
# output_list[-1] contains the max level
from collections import OrderedDict

import matplotlib.pyplot as plt

import networkx as nx
from networkx import core_number, k_core

import operator

# dummy graph to check the functionality


#debug test
#zero_deg_node = []
#for node in testgraph.nodes:
    #print(testgraph.degree[node])
#    if testgraph.degree[node] == 0:
#        zero_deg_node.append(node)
#print(zero_deg_node)

# K-TRUSS
# For each edge with vertices u and v  a score 'sup' is given as the intersection of nb(u) and nb(v)
# for each edge the sup must be greater than k-2
# the above will happen for k =3 until kmax, The kmax is the maximal truss which there are no more edges of the graph

def intersection(lst1, lst2):
    return list(set(lst1) & set(lst2))


def k_truss_support(g):
    dict_of_support = {}
    testcounter = 0
    for edge in g.edges():
        u = edge[0]
        v = edge[1]
        nb_u = list(g.neighbors(u))
        nb_v = list(g.neighbors(v))
        sup = len(intersection(nb_u, nb_v))
        testcounter += 1
        dict_of_support[edge] = sup
    return OrderedDict(sorted(dict_of_support.items(), key=operator.itemgetter(1)))


def k_truss(g):
    # init nodes so we can determine where they belongs
    num_of_trussnode = {}
    for node in g.nodes:
        num_of_trussnode[node] = 0

    k = 2
    rm_list = []
    edges_sort = k_truss_support(g)
    #print(edges_sort)
    boolean_no_edges = True
    while (boolean_no_edges):
        rm_list_of_level = []
        while (list(edges_sort.values())[0] <= k - 2):
            e = list(edges_sort.keys())[0]
            node1 = list(edges_sort.keys())[0][0]
            node2 = list(edges_sort.keys())[0][1]
            nb_u = g.neighbors(node1)
            nb_v = g.neighbors(node2)
            nbU = list(nb_v)
            u = node2
            v = node1
            if (len(list(nb_u)) < len(list(nb_v))):
                nbU = list(nb_u)
                u = node1
                v = node2
            # for each
            for w in nbU:
                if (g.has_edge(w, v)):
                    if (v, w) in edges_sort.keys():
                        edges_sort[(v, w)] -= 1
                    elif (w, v) in edges_sort.keys():
                        edges_sort[(w, v)] -= 1
                    if (u, w) in edges_sort.keys():
                        edges_sort[(u, w)] -= 1
                    elif (w, u) in edges_sort.keys():
                        edges_sort[(w, u)] -= 1
                    # resorting after the support change
                    edges_sort = OrderedDict(sorted(edges_sort.items(), key=operator.itemgetter(1)))

            del edges_sort[e]
            g.remove_edge(e[0], e[1])
            rm_list_of_level.append(e)
            if (len(g.edges) == 0):
                break
        rm_list.append(rm_list_of_level)
        if (len(list(edges_sort.keys())) == 0):
            boolean_no_edges = False
            k = k - 1
        else:
            k += 1
            #print(edges_sort)
            graph = max(nx.connected_component_subgraphs(g), key=len)
            for not_removed_node in graph.nodes:
                num_of_trussnode[not_removed_node] += 1
            #nx.draw(graph, with_labels=True, font_weight='bold')
            #plt.show()
    # print(num_of_trussnode)
    #print(rm_list)
    return graph, num_of_trussnode


def k_truss_decomp(g):
    testgraph1, node_dict = k_truss(g.copy())
    grouped_list = []
    for i in range(0, len(node_dict)): #worst case senario is when each edge
        temp = sorted([k for k, v in node_dict.items() if v == i])
        if temp:
            grouped_list.append(temp)
    return grouped_list








