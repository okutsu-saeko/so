
# coding: utf-8

# In[2]:


from networkx import *

import matplotlib.pyplot as plt


# In[5]:


#元データ
data = [["A","B"],["A","C"],["C","B"],["D","C"],["D","E"],["C","E"],["E","F"]]

#ノードの構築
G = nx.Graph()

for p in list(set([r[0] for r in data] + [r[1] for r in data])):
    G.add_node(p)


# In[6]:


#エッジの構築
for d in data:
    G.add_edge(d[0],d[1])


# In[7]:


#描画
pos = nx.spring_layout(G)
nx.draw_networkx_nodes(G, pos, node_size=1200,node_color="white")
nx.draw_networkx_edges(G, pos)
nx.draw_networkx_labels(G, pos)
plt.show()

