import numpy as np
import matplotlib.pyplot as plt
from dijkstar import Graph, find_path

nodesX = np.random.randint(1,101,100)
nodesY = np.random.randint(1,101,100)

#construir grafo y pintarlo
g = Graph()
plt.figure()
for origin in range(100):
    for destination in range(100):
        x1 = nodesX[origin]
        y1 = nodesY[origin]
        x2 = nodesX[destination]
        y2 = nodesY[destination]

        euclidean = np.sqrt((x1-x2)**2+(y1-y2)**2)
        if 0 < euclidean < 14:
            #edge --> node1,node2,cost
            g.add_edge(origin,destination,euclidean)

            plt.plot(x1,y1,"ok")
            plt.text(x1+1,y1,origin)
            plt.plot(x2,y2,"ok")
            plt.plot([x1,x2],[y1,y2],'--k')
            #print((nodesX[origin], nodesY[origin]), (nodesX[destination], nodesY[destination]), euclidean)

random = np.random.randint(0,100,2)
path=find_path(g,random[0],random[1])

#pintar ruta mas corta
for p in range(len(path.nodes)-2):
    x1 = nodesX[path.nodes[p]]
    y1 = nodesY[path.nodes[p]]
    x2 = nodesX[path.nodes[p+1]]
    y2 = nodesY[path.nodes[p+1]]
    plt.plot([x1,x2],[y1,y2],"-r")
plt.show()