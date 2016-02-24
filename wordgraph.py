import networkx as nx
def find_all_paths(graph, start, end):
    '''find all paths between the source and the target '''
    path  = []
    paths = []
    queue = [(start, end, path)]
    while queue:
        start, end, path = queue.pop()
        path = path + [start]
        if start == end:
            paths.append(path)
        x = [path[i] for i in range(1,len(path)) if path[i-1]==start]
        for node in set(graph[start]).difference(x):
            queue.append((node, end, path))
    return paths
def caculater_weight(graph,path):
    '''caculate a path's weight'''
    edge_p =  [(path[i],path[i+1]) for i in range(0,len(path)-1)]
    w=nx.get_edge_attributes(G =graph, name = 'weight')
    return sum([w[v] for v in edge_p])
    
import matplotlib.pyplot as plt
from createnodeinfo import *
G=nx.DiGraph()
G.add_node('Start')
G.add_node('End')
for v in nodeinfo(i=20):
    edge_pair = [('Start',v[0])] + [(v[i],v[i+1]) for i in range(0,len(v)-1)]+[(v[len(v)-1],'End')]
    for n in edge_pair:
        if(n in G.edges()):G.edge[n[0]][n[1]]['weight'] = 1.0*G.edge[n[0]][n[1]]['weight'] / (G.edge[n[0]][n[1]]['weight'] +1)
        else:G.add_edge(u=n[0],v=n[1],weight = 1)
for v in nodeinfo(i=20):
    for u in v:
        if('times' in G.node[u].keys()):G.node[u]['times'] =1 +  G.node[u]['times'] 
        else:G.node[u]['times'] =1
p =nx.spring_layout(G)
nx.draw(G,pos = p,with_labels=True,node_size = 300)
T= nx.all_simple_paths(G,'Start','End')
from itertools import islice
k_sp = find_all_paths(graph=G, start='Start', end='End')
#k_sp = list(nx.shortest_simple_paths(G, source='Start', target='End', weight='weight'))
k_sp.sort(key=lambda x:caculater_weight(G,x))

for v in k_sp[1:30]:
    print ' '.join([u[0] for u in v[1:-1]])
plt.show()