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


'--------------------------------------------------'

#PREGUNTA 2

#una matriz dispersa es una matriz en la que la mayoría de los elementos son cero. 
#No existe una definición estricta con respecto a la proporción de elementos de valor 
#cero para que una matriz califique como dispersa, pero un criterio común es que el 
#número de elementos distintos de cero es aproximadamente igual al número de filas o columnas. 
#Por el contrario, si la mayoría de los elementos son distintos de cero, la matriz se considera densa.

#Esta caracteristica se cumple en la matriz A, debido a que la mayoria de sus elemento son 0,
#y los valores no ceros son aproximadamente iguales al numero de filas o de columnas.

#Esta propiedad implica que todas las especies (a excepcion del phytoplancton) tienen al menos una presa,
#es decir, hay al menos un elemento distinto de 0 por columna, a excepcion de la columna 12 que es la que
#representa al phytoplancton

#Pregunta 3
""""Definicion 1 (opcion 1): Nivel Trofico El nivel trofico de una especie X es:
1, si X es un productor primario (una especie que no consume otra especie en la red alimentaria).
k + 1, si el camino mas corto desde el nivel 1 a la especie X tiene largo k.
Definicion 1 (opcion 2): Nivel Tr´ofico El nivel tr´ofico de una especie X es:
1, si X es un productor primario (una especie que no consume otra especie en la red alimentaria).
k + 1, si el camino mas largo desde el nivel 1 a la especie X tiene largo k. [1]"""

import networkx as nx
G=nx.DiGraph()
nodeslist=["phy","ZH","ZC","TA","CAP","FA","BAC","PA","FP","OP","FAN","BA"]
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
print('0=phy')
print('1=ZH')
print('2=ZC')
print('3=TA')
print('4=CAP')
print('5=FA')
print('6=BAC')
print('7=PA')
print('8=FP')
print('9=OP')
print('10=FAN')
print('11=BA')
