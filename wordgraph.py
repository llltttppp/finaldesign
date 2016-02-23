import networkx as nx
import matplotlib.pyplot as plt
from createnodeinfo import *
G=nx.DiGraph()
G.add_node('Start')
G.add_node('End')
for v in nodeinfo(i=2):
    edge_pair = [('Start',v[0])] + [(v[i],v[i+1]) for i in range(0,len(v)-1)]+[(v[len(v)-1],'End')]
    G.add_edges_from(edge_pair)
p =nx.spring_layout(G)
nx.draw(G,pos = p,with_labels=True,node_size = 300)
T= nx.all_simple_paths(G,'Start','End')
plt.show()