import networkx as nx
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
###################################################################
G = nx.Graph()
G.add_edges_from(
    [('A', 'B'),('A', 'C'),('A','I'),
     ('B', 'H'),('B', 'G'),('B', 'F'),('B', 'C'),
     ('C', 'G'),('D', 'B'),('E', 'C'),('E', 'F'),
     ('F','A'),('F','L')])

###################################################################
print(50*'#')
grafo=G.nodes(data=False)
len_grafo=len(grafo)
print('Total nodes:'+str(len_grafo))
print(grafo)
###################################################################
print(50*'#')

u=0
for line in nx.generate_edgelist(G, data=False):
    u=u+1
    print(line)

print('Total edge:'+str(u))
###################################################################
print(50*'#')
print('Paths matrix')
mat=np.zeros((len(grafo),len(grafo)))

m=[]
for u in grafo:
    for i in grafo:
        r=nx.shortest_path_length(G, source=u, target=i)
        m.append(r)
m=np.reshape(m,(len_grafo,len_grafo))
#print(m)
dataframe=pd.DataFrame(m,columns=grafo,index=grafo)
print(dataframe)
###################################################################
#plot do grafo
print(50*'#')
nx.draw(G, with_labels=True)
plt.show()

print(50*'#')
###################################################################
print('End!')
###################################################################