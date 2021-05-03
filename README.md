# simple_graphs
testing graph decomposition 

Given graph2.txt as a graph we calculate the truss and core decomposition and then colouring nodes depending on the levels of 
decomposition. 

Known issue needs generalaization

possible fix: adding a pallet of colors as a list and the level is depicted as the index of that list

The k-core decomposition is based on the paper "An O(m) Algorithm for Cores Decomposition of Networks Vladimir Batagelj and Matjaz Zaversnik, 2003. https://arxiv.org/abs/cs.DS/0310049" and implemented by the networkx module. And the K truss decomposition is based on "Truss Decomposition in Massive Networks
" by Wang and Chen (ref: https://arxiv.org/pdf/1205.6693.pdf)


