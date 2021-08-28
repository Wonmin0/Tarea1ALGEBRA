#Pregunta 1
import networkx as nx
G=nx.DiGraph()
#nodeslist=["phy","ZH","ZC","TA","CAP","FA","BAC","PA","FP","OP","FAN","BA"]
nodeslist=["BA","OP","FAN","FP","PA","FA","BAC","CAP","TA","ZC","ZH","phy"]
for node in nodeslist:
    G.add_node(node)
print("nodeslist:", G.nodes()) 

start= ["phy","ZH","ZH","ZC","ZC","TA","CAP","CAP","BAC","BAC","BAC","BAC","FP","FP","FAN","FAN"]
to=    ["ZH","ZC","BAC","TA","BAC","CAP","FA","FP","PA","FA","OP","FAN","OP","BA","OP","BA"]
value=[1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1,1] 
for j in range(0, len(start)):
    G.add_weighted_edges_from([(start[j], to[j], value[j])]) 
nx.draw(G, with_labels=True,pos=nx.circular_layout(G),
        width=[float(v['weight']) for (r, c, v) in G.edges(data=True)])
import matplotlib.pyplot as plt
plt.show()
a= nx.adjacency_matrix(G)
print(a)
A=a.todense()
print(A)
import numpy
numpy.savetxt('correlation_matrix.csv',A, delimiter = ',')

#una matriz dispersa es una matriz en la que la mayoría de los elementos son cero. 
#No existe una definición estricta con respecto a la proporción de elementos de valor 
#cero para que una matriz califique como dispersa, pero un criterio común es que el 
#número de elementos distintos de cero es aproximadamente igual al número de filas o columnas. 
#Por el contrario, si la mayoría de los elementos son distintos de cero, la matriz se considera densa.

